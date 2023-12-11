from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

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
            result=connectToMySQL(db).query_db("INSERT INTO workout_plan (id, host_id, gym_name, workout_plan, address, city, state, zip_code, schedule, created_at, updated_at, buddy_id) VALUES (%(id)s, %(host_id)s, %(gym_name)s, %(workout_plan)s, %(address)s, %(city)s, %(state)s, %(zip_code)s, %(schedule)s, %(created_at)s, %(updated_at)s, %(buddy_id)s)", data)
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
    def get_workouts_without_buddy(cls):
        return connectToMySQL(db).query_db("SELECT * FROM workout_plan WHERE buddy_id = Null")
    
    @classmethod
    def add_buddy(cls, data):
        return connectToMySQL(db).query_db("UPDATE workout_plan SET buddy_id=%(id)s WHERE id=%(plan_id)s", data)
