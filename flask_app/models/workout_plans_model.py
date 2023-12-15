from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models.users_model import Users

db = 'users_login'

class Workout_Plans:
    def __init__(self, data):
        self.id=data['id']
        self.host_id=data['host_id']
        self.gym_name=data['gym_name']
        self.workout_plan=data['workout_plan']
        self.address=data['address']
        self.city=data['city']
        self.state=data['state']
        self.zip_code=data['zip_code']
        self.schedule=data['schedule']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.buddy_id=data['buddy_id']

    @classmethod
    def create_workout_plan(cls, data):
        valid=True
        if len(data['gym_name']) < 3:
            flash("Gym name must be atleast 3 characters.")
            valid=False
        if len(data['workout_plan']) < 20 and len(data['workout_plan']) > 500:
            flash("Workout plan must be between 20 and 500 characters.")
            valid=False
        if not (data['address']):
            flash("Address required.")
            valid=False
        if not (data['city']):
            flash("City required.")
            valid=False
        if not (data['state']):
            flash("State required.")
            valid=False
        if not (data['zip_code']):
            flash("Zip code required.")
            valid=False
        if len(data['schedule']) < 20 and len(data['workout_plan']) > 500:
            flash("Schedule must be between 20 and 500 characters.")
            valid=False
        if valid:
            result=connectToMySQL(db).query_db("INSERT INTO workout_plan (host_id, gym_name, workout_plan, address, city, state, zip_code, schedule) VALUES (%(host_id)s, %(gym_name)s, %(workout_plan)s, %(address)s, %(city)s, %(state)s, %(zip_code)s, %(schedule)s)", data)
            print('_____________________________________________________')
            print(result)
            return valid

    @classmethod
    def get_workouts_by_host(cls, data):
        return connectToMySQL(db).query_db("SELECT * FROM workout_plan WHERE host_id=%(id)s", data)
    
    @classmethod
    def get_workouts_by_buddy(cls, data):
        return connectToMySQL(db).query_db("SELECT * FROM workout_plan WHERE buddy_id=%(id)s", data)
    
    @classmethod
    def get_workouts_without_buddy(cls, data):
        return connectToMySQL(db).query_db("SELECT * FROM workout_plan WHERE (buddy_id is null) AND (host_id != %(id)s)", data)
    
    @classmethod
    def add_buddy(cls, data):
        return connectToMySQL(db).query_db("UPDATE workout_plan SET buddy_id=%(id)s WHERE id=%(plan_id)s", data)
    
    @classmethod
    def get_workout_by_id(cls, data):
        return connectToMySQL(db).query_db("SELECT * FROM workout_plan WHERE id = %(id)s", data)
    
    @classmethod
    def get_workout_host(cls, data):
        host= connectToMySQL(db).query_db("SELECT * FROM users WHERE id = %(host_id)s",(connectToMySQL(db).query_db("SELECT host_id FROM workout_plan WHERE id = %(id)s", data)[0]))
        print(host)
        return host
    
    @classmethod
    def get_workout_buddy(cls, data):
        buddy = connectToMySQL(db).query_db("SELECT * FROM users WHERE id = %(buddy_id)s",(connectToMySQL(db).query_db("SELECT buddy_id FROM workout_plan WHERE id = %(id)s", data)[0]))
        print(buddy)
        return buddy

    @classmethod
    def remove_buddy(cls, data):
        return connectToMySQL(db).query_db("UPDATE workout_plan SET buddy_id = NULL WHERE id=%(plan_id)s", data)
    
    @classmethod
    def update_plan(cls, data):
        valid=True
        if len(data['gym_name']) < 3:
            flash("Gym name must be atleast 3 characters.")
            valid=False
        if len(data['workout_plan']) < 20 and len(data['workout_plan']) > 500:
            flash("Workout plan must be between 20 and 500 characters.")
            valid=False
        if not (data['address']):
            flash("Address required.")
            valid=False
        if not (data['city']):
            flash("City required.")
            valid=False
        if not (data['state']):
            flash("State required.")
            valid=False
        if not (data['zip_code']):
            flash("Zip code required.")
            valid=False
        if len(data['schedule']) < 20 and len(data['workout_plan']) > 500:
            flash("Schedule must be between 20 and 500 characters.")
            valid=False
        if valid:
            connectToMySQL(db).query_db("UPDATE workout_plan SET gym_name = %(gym_name)s, address = %(address)s, city = %(city)s, state = %(state)s, zip_code = %(zip_code)s, workout_plan = %(workout_plan)s, schedule = %(schedule)s WHERE id=%(id)s",data)
            return valid
