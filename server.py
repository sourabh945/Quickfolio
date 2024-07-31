from flask import Flask , render_template

app = Flask(__name__,template_folder="./Templates")

about = ''' I am programmer with a master's degree in the physics. I learn the programming 
about the four years ago as an hobby because i am so free and i can learn it using free sources
like youtube and its documentations. I learn multiple languages and frameworks by myself just as an 
hobby. But i fall into the ocean of programming and it become 
my passion. Now I wanted to turn my passion into my job.'''

eduction = [{'website':"https://www.gjust.ac.in",'university':'Guru Jambheshwar University of Science and Technology, Hisar','course':'  M.Sc. Physics','session':'2022-2024'},{'website':"https://www.crsu.ac.in",'university':'Chaudary Ranbir Singh University, Jind','course':'  B.Sc. Physics Chemistry Mathematic','session':'2019-2022'}]


skills = [["Programming language",['Python','C/C++','JavaScript','SQLite','MySQL','Fortran']],["Technologies and Tools",['HTML','CSS','Nginx','JSON','LaTeX','Micro controllers','Sensors','Origin']],["OS",['Ubuntu','Windows','macOs']],["Frameworks and Python Libraries",['Django','Flask','WebSockets','NumPy','SciPy','RESTful API']],["Version Controls",['Git']],['other','Good understanding of computer hardware and networking hardware',['computer','hardware','networking']],["other",'Good understanding of Physics and Mathematics . And working knowledge of Electronics and Chemistry',['Physics','Mathematics','Electronics','Chemistry']]]

projects = [{'name':'WebRoot','desc':'It is deployable server for file across the network with efficiently and securely and it uses flask for web app and nginx as the server','link':'https://github.com/sourabh945/WebRoot','skills':['Python','Flask','WebSockets','HTML','Nginx']},{'name':'Xanalyser','desc':'It is a XRD Data analyzing software like Origin which utilize the scipy and written in python.','link':'https://github.com/sourabh945/xanalyser','skills':['Python','SciPy','NumPy','Matplotlib']}]

contact = [{'name':'Email','source':'sheokand.sourabh.anil@gmail.com','type':'email'},{'name':'Github','source':'https://github.com/sourabh945','type':'website'},{'name':'Phone','source':'+91-9306490337','type':'call'},{'name':'WhatsApp','source':'https://wa.me/+919306490337','type':'message'}]

@app.route("/")
def home():
    return render_template("home/index.html",name='Sourabh Sheokand',about=about,eduction=eduction,skills=skills,projects=projects,contacts=contact,source_code="https://github.com/sourabh945/Portfolio")

@app.route("/projects")
def projects_page():
    return render_template('projects/index.html',projects=projects)

if __name__ == "__main__":
    app.run(debug=True)