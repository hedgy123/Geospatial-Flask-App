from flask import Flask
from flask import render_template
from models import *

app = Flask(__name__)

@app.route('/')
def index():
    school_count = School.select().count()
    print("School count = ",school_count)
    schools = School.select().order_by(School.school_name.asc())
    print("schools are ",schools)
    return render_template('index.html',count = school_count,schools = schools)


@app.route('/school/<dbn>')
def show_details(dbn):


    #the_school = School.select().where(School.dbn == dbn)
    the_school = School.get(School.dbn == dbn)
    print("the school is ",the_school)
    return render_template('show.html',school = the_school)


if __name__ == '__main__':
    app.run(debug=True)
