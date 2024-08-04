from flask import Flask , render_template, request

from modules.load_data import load

data = load()

app = Flask(__name__,template_folder="./templates")

@app.template_filter('list')
def change_to_list(object) -> list:
    return list(object)

@app.template_filter('str')
def change_to_list(object) -> str:
    return str(object)

@app.template_filter('type')
def typeof(object)-> str:
    return str(type(object)).split("'")[1]

@app.route("/")
def home():
    return render_template("home.html",data=data,source_code="https://github.com/sourabh945/Portfolio")

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
                return render_template('projects/project.html',data=data,project=i,source_code="https://github.com/sourabh945/Portfolio")
    return render_template('projects/index.html',data=data,source_code="https://github.com/sourabh945/Portfolio")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)