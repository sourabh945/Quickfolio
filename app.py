from flask import Flask, redirect, render_template, request, send_from_directory

###########################################################################################

__author__ = "https://github.com/sourabh945/"

###########################################################################################

from modules.load_data import load

data = load()  # this function is for read the json file

##########################################################################################

app = Flask(__name__, template_folder="./templates")

env = app.jinja_env

env.cache_size = 500
env.auto_reload = False

###########################################################################################

### error pages


@app.errorhandler(404)
def not_found_error(error):
    return render_template("error_pages/404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("error_pages/500.html"), 500


@app.errorhandler(400)
def bad_request(error):
    return render_template("error_pages/400.html"), 400


#######################################################################################################

# seo settings

# --- SYSTEM FILES (Robots & Favicon) ---


@app.route("/robots.txt")
def robots():
    # Serves the robots.txt file directly from the static folder
    return send_from_directory(app.static_folder, "robots.txt")


@app.route("/favicon.ico")
def favicon():
    # Serves the favicon. Adjust the filename if yours is a .png
    return send_from_directory(
        app.static_folder,
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",  # Use 'image/png' if it is a PNG
    )


@app.route("/sitemap.xml")
def sitemap():
    # Serves the sitemap.xml file directly from the static folder
    return send_from_directory(
        app.static_folder, "sitemap.xml", mimetype="application/xml"
    )


###################################################################################################

# pages for the portfolio


@app.before_request
def before_request():
    if request.url.startswith("http://"):
        return redirect(request.url.replace("http://", "https://", 1)), 301


@app.route("/")
def home():
    return render_template(
        "index.html",
        data_file_location=data["data_file_location"],
        title=data["title"],
        description=data["description"],
    )


@app.route("/resume")
def resume():
    return redirect("/static/media/resume.pdf")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
