# єКафедра (eDepartment)

Веб-довідник для абітурієнтів університету

## Опис

єКафедра - це веб-додаток для студентів першого курсу, який надає інформацію про групу, куратора та предмети.

## Технології

- **Backend**: Python + Flask
- **Database**: SQLite (SQLAlchemy)
- **Frontend**: HTML/CSS (Jinja2 templates)
- **Testing**: PyTest

## Встановлення

1. Клонуйте репозиторій:
```bash
git clone https://github.com/mashapresident/ekafedra.git
cd ekafedra
```

2. Встановіть залежності:
```bash
pip install -r requirements.txt
```

3. Ініціалізуйте базу даних:
```bash
python init_db.py
```

4. Запустіть додаток:
```bash
python app.py
```

5. Відкрийте браузер і перейдіть на http://127.0.0.1:5000

## Тестові коди доступу

- `STU001` - Олександр Іванович Коваленко (група ТВ-41)
- `STU002` - Марія Петрівна Шевченко (група ТВ-42)
- `STU003` - Дмитро Олександрович Мельник (група ТВ-31)

## Запуск тестів

```bash
pytest -v
```

## Структура проекту

```
ekafedra/
├── app.py              # Головний Flask додаток
├── models.py           # Моделі бази даних
├── init_db.py          # Скрипт ініціалізації БД
├── requirements.txt    # Залежності Python
├── tests/              # Тести
│   ├── test_app.py    # Тести контролерів
│   └── test_logic.py  # Тести бізнес-логіки
├── templates/          # HTML шаблони
└── static/            # CSS стилі
```

## Автор

Розроблено для курсової роботи

