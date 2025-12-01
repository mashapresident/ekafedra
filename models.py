from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Student(db.Model):
    """Student model with entrance code authentication"""
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    entrance_code = db.Column(db.String(50), unique=True, nullable=False)
    year_of_entrance = db.Column(db.Integer, nullable=False)
    group_number = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Student {self.full_name} - {self.entrance_code}>'
    
    def get_group_name(self):
        """Generate group name in format ТВ-xy where x is last digit of year, y is group_number"""
        last_digit = str(self.year_of_entrance)[-1]
        return f"ТВ-{last_digit}{self.group_number}"


class Subject(db.Model):
    """Subject model for freshmen subjects"""
    __tablename__ = 'subjects'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Subject {self.name}>'


