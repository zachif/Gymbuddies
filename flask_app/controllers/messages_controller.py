from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.messages_model import Messages

@app.rout('/GymBuddies/message/host/<int:plan_id>')
def hostMessage(plan_id):
    data = {
        "content":request.form['content'],
        "sender":"host",
        "plan_id":plan_id
    }
    result=Messages.create_messages(data)
    print(result)
    return redirect('/GymBuddies/display/' + str(plan_id))

@app.rout('/GymBuddies/message/buddy/<int:plan_id>')
def hostMessage(plan_id):
    data = {
        "content":request.form['content'],
        "sender":"buddy",
        "plan_id":plan_id
    }
    result=Messages.create_messages(data)
    print(result)
    return redirect('/GymBuddies/display/' + str(plan_id))