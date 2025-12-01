from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, Student, Subject
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edepartment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Static data
CURATOR_NAME = "Іван Петрович Сидоренко"
DEPARTMENT_NEWS = [
    "Запуск нового курсу з робототехніки",
    "Відкриття лабораторії штучного інтелекту",
    "Співпраця з провідними IT-компаніями"
]
ROBOTICS_CLUB_INFO = "Клуб робототехніки - це місце, де студенти можуть розвивати свої навички у створенні роботів та автоматизації. Регулярні зустрічі щопонеділка о 18:00."


def init_db():
    """Initialize database with sample data"""
    with app.app_context():
        db.create_all()
        
        # Check if data already exists
        if Student.query.first() is None:
            # Create sample students
            students = [
                Student(full_name="Олександр Іванович Коваленко", entrance_code="STU001", year_of_entrance=2024, group_number=1),
                Student(full_name="Марія Петрівна Шевченко", entrance_code="STU002", year_of_entrance=2024, group_number=2),
                Student(full_name="Дмитро Олександрович Мельник", entrance_code="STU003", year_of_entrance=2023, group_number=1),
            ]
            for student in students:
                db.session.add(student)
            
            # Create subjects for freshmen
            subjects = [
                "Основи програмування",
                "Математичний аналіз",
                "Лінійна алгебра",
                "Дискретна математика",
                "Основи веб-розробки",
                "Архітектура комп'ютерів",
                "Англійська мова",
                "Українська мова"
            ]
            for subject_name in subjects:
                subject = Subject(name=subject_name)
                db.session.add(subject)
            
            db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def login():
    """Login page with entrance code authentication"""
    if request.method == 'POST':
        entrance_code = request.form.get('entrance_code', '').strip()
        
        if not entrance_code:
            flash('Будь ласка, введіть код доступу', 'error')
            return render_template('login.html')
        
        student = Student.query.filter_by(entrance_code=entrance_code).first()
        
        if student:
            session['student_id'] = student.id
            session['student_name'] = student.full_name
            return redirect(url_for('dashboard'))
        else:
            flash('Невірний код доступу', 'error')
            return render_template('login.html')
    
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    """Main dashboard with student info"""
    if 'student_id' not in session:
        flash('Будь ласка, увійдіть у систему', 'error')
        return redirect(url_for('login'))
    
    student = Student.query.get(session['student_id'])
    if not student:
        session.clear()
        flash('Студента не знайдено', 'error')
        return redirect(url_for('login'))
    
    group_name = student.get_group_name()
    
    return render_template('dashboard.html', 
                         student=student, 
                         group_name=group_name,
                         curator_name=CURATOR_NAME)


@app.route('/subjects')
def subjects():
    """List of subjects page"""
    if 'student_id' not in session:
        flash('Будь ласка, увійдіть у систему', 'error')
        return redirect(url_for('login'))
    
    all_subjects = Subject.query.order_by(Subject.name).all()
    return render_template('subjects.html', subjects=all_subjects)


@app.route('/info')
def info():
    """Static information about the department"""
    if 'student_id' not in session:
        flash('Будь ласка, увійдіть у систему', 'error')
        return redirect(url_for('login'))
    
    return render_template('info.html', 
                         news=DEPARTMENT_NEWS,
                         robotics_info=ROBOTICS_CLUB_INFO)


@app.route('/logout')
def logout():
    """Logout and clear session"""
    session.clear()
    flash('Ви вийшли з системи', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    # Initialize database on startup
    with app.app_context():
        # Check if database exists, if not create it
        try:
            # Try to query to check if tables exist
            Student.query.first()
        except Exception:
            # Tables don't exist, create them
            init_db()
    app.run(debug=True)

