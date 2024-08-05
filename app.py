
from flask import Flask , render_template, request , redirect

###########################################################################################

__author__ = "https://github.com/sourabh945/"

###########################################################################################

from modules.load_data import load


data = load() # this function is for read the json file

##########################################################################################

app = Flask(__name__,template_folder="./templates")

env = app.jinja_env

env.cache_size = 500
env.auto_reload = False

###########################################################################################

# custom filters for the jinja code 

@app.template_filter('list')
def change_to_list(object) -> list:
    return list(object)

@app.template_filter('lower')
def change_to_list(object:str) -> str:
    return object.lower()

@app.template_filter('str')
def change_to_list(object) -> str:
    return str(object)

@app.template_filter('type')
def typeof(object)-> str:
    return str(type(object)).split("'")[1]

@app.template_filter('try')
def try_to_fetch(master,object) -> any:
    try:
        return master[object]
    except:
        return None
    
########################################################################################

### error pages


@app.errorhandler(404)
def not_found_error(error):
    return render_template("error page/404.html"), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("error page/500.html"), 500

@app.errorhandler(400)
def bad_request(error):
    return render_template("error page/400.html"), 400

#######################################################################################################
    
###################################################################################################
    
# pages for the portfolio

@app.before_request
def before_request():
    if request.url.startswith("http://"):
        return redirect(request.url.replace('http://','https://',1)) , 304

@app.route("/")
def home():
    return render_template('home.html',data=data,source_code="https://github.com/sourabh945/Quickfolio")


@app.route("/projects",methods=["GET"])
def projects_page():
    try:
        project_name = request.args.get('repo')
    except:
        project_name = None
    if project_name is not None:
        for i in data['projects']:
            if i['name'] == project_name:
                print(i['content'])
                return render_template('project.html',data=data,project=i,source_code="https://github.com/sourabh945/Quickfolio")
    return render_template('index.html',data=data,source_code="https://github.com/sourabh945/Quickfolio")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)