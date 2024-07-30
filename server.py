from flask import Flask , render_template

app = Flask(__name__,template_folder="./Templates")

about = ''' I am programmer with a master's degree in the physics. I learn the programming 
about the four years ago as an hobby because i am so free and i can learn it using free sources
like youtube and its documentations. I learn multiple languages and frameworks by myself just as an 
hobby. But i fall into the ocean of programming and it become 
my passion. Now I wanted to turn my passion into my job.'''

eduction = [{'website':"https://www.gjust.ac.in",'university':'Guru Jambheshwar University of Science and Technology, Hisar','course':'  M.Sc. Physics','session':'2022-2024'},{'website':"https://www.crsu.ac.in",'university':'Chaudary Ranbir Singh University, Jind','course':'  B.Sc. Physics Chemistry Mathematic','session':'2019-2022'}]

from generate_html import make_html_highlight , list_2_html_str

skills = [["Programming language",['Python','C/C++','JavaScript','SQLite','MySQL','Fortran']],["Technologies and Tools",['HTML','CSS','Nginx','JSON','LaTeX','Microcontrollers','Sensors','Origin']],["OS",['Ubuntu','Windows','macOs']],["Frameworks and Python Libraries",['Django','Flask','WebSockets','NumPy','SciPy','RESTful API']],["Version Controls",['Git']],['other','Good understanding of computer hardware and networking hardware',['computer','hardware','networking']],["other",'Good understanding of Physics and Mathematics . And working knowledge of Electronics and Chemistry',['Physics','Mathematics','Electronics','Chemistry']]]

projects = [{'name':'WebRoot','desc':'It is deployable server for file across the network with efficiently and securely and it uses flask for web app and nginx as the server','link':'https//github.com/sourabh945/WebRoot','skills':['Python','Flask','WebSockets','HTML','Nginx']}]

@app.route("/")
def home():
    return render_template("home/index.html",name='Sourabh Sheokand',about=about,eduction=eduction,skills=skills)


if __name__ == "__main__":
    app.run(debug=True)