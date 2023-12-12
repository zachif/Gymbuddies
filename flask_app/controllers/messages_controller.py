from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.messages_model import Messages

@app.route('/GymBuddies/message/host/<int:plan_id>', methods=["POST"])
def hostMessage(plan_id):
    data = {
        "content":request.form['content'],
        "sender":"host",
        "plan_id":plan_id
    }
    result=Messages.create_messages(data)
    print(result)
    return redirect('/GymBuddies/display/' + str(plan_id))

@app.route('/GymBuddies/message/buddy/<int:plan_id>', methods=["POST"])
def buddyMessage(plan_id):
    data = {
        "content":request.form['content'],
        "sender":"buddy",
        "plan_id":plan_id
    }
    result=Messages.create_messages(data)
    print(result)
    return redirect('/GymBuddies/display/' + str(plan_id))