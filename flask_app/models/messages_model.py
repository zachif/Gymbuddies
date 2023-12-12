from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

db = 'users_login'

class Messages:
    def __init__(self, data):
        self.id=data['id']
        self.content=data['content']
        self.sender=data['sender']
        self.created_at=data['created_at']
        self.updated_at=data['update_at']
        self.plan_id=data['plan_id']

    @classmethod
    def create_messages(cls, data):
        result=connectToMySQL(db).query_db("INSERT INTO messages (content, sender, plan_id) VALUES (%(content)s, %(sender)s, %(plan_id)s)", data)
        print(result)
        return result
    
    @classmethod
    def delete_messages_by_plan(cls, data):
        result=connectToMySQL(db).query_db("DELETE FROM messages WHERE plan_id=%(plan_id)s", data)
        print(result)
        return result

    @classmethod
    def get_messages_by_plan(cls, data):
        result=connectToMySQL(db).query_db("SELECT * FROM messages WHERE plan_id=%(id)s", data)
        print(result)
        return result