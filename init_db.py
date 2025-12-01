"""
Скрипт для ініціалізації бази даних
Запустіть цей файл один раз для створення таблиць та заповнення тестовими даними
"""
from app import app, db, Student, Subject

def init_database():
    """Ініціалізує базу даних та створює тестові дані"""
    with app.app_context():
        # Видаляємо всі таблиці (якщо існують)
        db.drop_all()
        
        # Створюємо всі таблиці
        db.create_all()
        
        # Створюємо тестових студентів
        students = [
            Student(
                full_name="Олександр Іванович Коваленко",
                entrance_code="STU001",
                year_of_entrance=2024,
                group_number=1
            ),
            Student(
                full_name="Марія Петрівна Шевченко",
                entrance_code="STU002",
                year_of_entrance=2024,
                group_number=2
            ),
            Student(
                full_name="Дмитро Олександрович Мельник",
                entrance_code="STU003",
                year_of_entrance=2023,
                group_number=1
            ),
        ]
        
        for student in students:
            db.session.add(student)
        
        # Створюємо предмети для першокурсників
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
        
        # Зберігаємо зміни
        db.session.commit()
        
        print("База даних успішно ініціалізована!")
        print(f"Створено {len(students)} студентів та {len(subjects)} предметів")
        print("\nТестові коди доступу:")
        for student in students:
            print(f"  - {student.entrance_code}: {student.full_name} (група {student.get_group_name()})")

if __name__ == '__main__':
    init_database()


