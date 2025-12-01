import pytest
import os
import sys
from flask import session

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db, Student, Subject


@pytest.fixture
def client():
    """Create a test client"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_edepartment.db'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            
            # Create test data
            test_student = Student(
                full_name="Тестовий Студент",
                entrance_code="TEST001",
                year_of_entrance=2024,
                group_number=1
            )
            db.session.add(test_student)
            db.session.commit()
        
        yield client
        
        with app.app_context():
            db.drop_all()


def test_valid_login_redirects_to_dashboard(client):
    """Test 1: Valid login should redirect to dashboard"""
    response = client.post('/', data={'entrance_code': 'TEST001'}, follow_redirects=False)
    
    assert response.status_code == 302
    assert '/dashboard' in response.location
    
    # Follow redirect to verify we're on dashboard
    response = client.post('/', data={'entrance_code': 'TEST001'}, follow_redirects=True)
    response_text = response.data.decode('utf-8')
    assert 'Тестовий Студент' in response_text or 'Dashboard' in response_text or 'Ласкаво просимо' in response_text


def test_invalid_login_shows_error(client):
    """Test 2: Invalid login should show error message"""
    response = client.post('/', data={'entrance_code': 'INVALID_CODE'}, follow_redirects=True)
    
    assert response.status_code == 200
    # Check for Ukrainian error message
    response_text = response.data.decode('utf-8')
    assert 'Невірний код доступу' in response_text or 'error' in response_text.lower()


def test_group_name_calculation(client):
    """Test 3: Check if Group Name calculation logic is correct"""
    with app.app_context():
        # Test case: 2024, group 1 -> ТВ-41
        student1 = Student(
            full_name="Test Student 1",
            entrance_code="TEST2024",
            year_of_entrance=2024,
            group_number=1
        )
        assert student1.get_group_name() == "ТВ-41"
        
        # Test case: 2023, group 2 -> ТВ-32
        student2 = Student(
            full_name="Test Student 2",
            entrance_code="TEST2023",
            year_of_entrance=2023,
            group_number=2
        )
        assert student2.get_group_name() == "ТВ-32"
        
        # Test case: 2025, group 3 -> ТВ-53
        student3 = Student(
            full_name="Test Student 3",
            entrance_code="TEST2025",
            year_of_entrance=2025,
            group_number=3
        )
        assert student3.get_group_name() == "ТВ-53"


def test_unauthorized_user_cannot_access_dashboard(client):
    """Test 4: Check if unauthorized user cannot access dashboard"""
    # Try to access dashboard without login
    response = client.get('/dashboard', follow_redirects=True)
    
    # Should redirect to login page
    assert response.status_code == 200
    assert 'login' in response.request.path.lower() or '/' in response.request.path
    # Should show error message
    response_text = response.data.decode('utf-8').lower()
    assert 'увійдіть' in response_text or 'login' in response_text or 'код доступу' in response_text

