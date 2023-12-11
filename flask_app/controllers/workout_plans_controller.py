from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.workout_plans_model import Workout_Plans

@app.route('/GymBuddies/create')
def createform():
    return render_template('create.html')

@app.route('/create', methods=["POST"])
def create():
    data ={
        "host_id":session['id'],
        "gym_name":request.form['gym_name'],
        "address":request.form['address'],
        "city":request.form['city'],
        "state":request.form['state'],
        "zip_code":request.form['zip_code'],
        "workout_plan":request.form['workout_plan'],
        "schedule":request.form['schedule'],
    }
    valid=Workout_Plans.create_workout_plan(data)
    print('_________________________________________________________')
    print (valid)
    return redirect("/GymBuddies/dashboard")