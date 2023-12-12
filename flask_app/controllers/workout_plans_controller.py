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
        "schedule":request.form['schedule']
    }
    valid=Workout_Plans.create_workout_plan(data)
    print('_________________________________________________________')
    print (valid)
    return redirect("/GymBuddies/dashboard")

@app.route('/GymBuddies/display/<int:plan_id>')
def display(plan_id):
    data={'id':plan_id}
    result=Workout_Plans.get_workout_by_id(data)
    print (result)
    result=Workout_Plans.get_workout_host(data)
    print (result)
    result=Workout_Plans.get_workout_buddy(data)
    print (result)
    return render_template("display.html", user_id=session["id"],plan=(Workout_Plans.get_workout_by_id(data))[0], host=(Workout_Plans.get_workout_host(data))[0], buddy=(Workout_Plans.get_workout_buddy(data)))

@app.route('/GymBuddies/add/<int:plan_id>')
def addBuddy(plan_id):
    data={
        "id":session['id'],
        "plan_id":plan_id
    }
    result=Workout_Plans.add_buddy(data)
    return redirect('/GymBuddies/display/' + str(plan_id))

@app.route('/GymBuddies/remove/<int:plan_id>')
def removeBuddy(plan_id):
    data={
        "plan_id":plan_id
    }
    result=Workout_Plans.remove_buddy(data)
    return redirect('/GymBuddies/display/' + str(plan_id))

@app.route('/GymBuddies/edit/<int:plan_id>')
def editPlan(plan_id):
    data={
        "id":plan_id
    }
    return render_template("edit.html", plan=Workout_Plans.get_workout_by_id(data)[0])

@app.route('/update/<int:plan_id>', methods=["POST"])
def updatePlan(plan_id):
    data={
        "id":plan_id,
        "gym_name":request.form['gym_name'],
        "address":request.form['address'],
        "city":request.form['city'],
        "state":request.form['state'],
        "zip_code":request.form['zip_code'],
        "workout_plan":request.form['workout_plan'],
        "schedule":request.form['schedule']
    }
    result=Workout_Plans.update_plan(data)
    print(result)
    return redirect('/GymBuddies/display/' + str(plan_id))