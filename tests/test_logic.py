"""
Тестування алгоритму розрахунку назви групи
Це найбільш критичний модуль бізнес-логіки
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Student


class TestGroupNameCalculation:
    """Тести для функції розрахунку назви групи"""
    
    def test_group_name_2024_group1(self):
        """Тест: 2024, група 1 -> ТВ-41"""
        student = Student(
            full_name="Тест Студент 1",
            entrance_code="TEST2024_1",
            year_of_entrance=2024,
            group_number=1
        )
        assert student.get_group_name() == "ТВ-41"
    
    def test_group_name_2024_group2(self):
        """Тест: 2024, група 2 -> ТВ-42"""
        student = Student(
            full_name="Тест Студент 2",
            entrance_code="TEST2024_2",
            year_of_entrance=2024,
            group_number=2
        )
        assert student.get_group_name() == "ТВ-42"
    
    def test_group_name_2023_group1(self):
        """Тест: 2023, група 1 -> ТВ-31"""
        student = Student(
            full_name="Тест Студент 3",
            entrance_code="TEST2023_1",
            year_of_entrance=2023,
            group_number=1
        )
        assert student.get_group_name() == "ТВ-31"
    
    def test_group_name_2025_group3(self):
        """Тест: 2025, група 3 -> ТВ-53"""
        student = Student(
            full_name="Тест Студент 4",
            entrance_code="TEST2025_3",
            year_of_entrance=2025,
            group_number=3
        )
        assert student.get_group_name() == "ТВ-53"
    
    def test_group_name_2020_group1(self):
        """Тест: 2020, група 1 -> ТВ-01"""
        student = Student(
            full_name="Тест Студент 5",
            entrance_code="TEST2020_1",
            year_of_entrance=2020,
            group_number=1
        )
        assert student.get_group_name() == "ТВ-01"
    
    def test_group_name_2019_group2(self):
        """Тест: 2019, група 2 -> ТВ-92"""
        student = Student(
            full_name="Тест Студент 6",
            entrance_code="TEST2019_2",
            year_of_entrance=2019,
            group_number=2
        )
        assert student.get_group_name() == "ТВ-92"
    
    def test_group_name_edge_cases(self):
        """Тест граничних випадків"""
        # Рік з нулем в кінці
        student1 = Student(
            full_name="Test",
            entrance_code="TEST1",
            year_of_entrance=2030,
            group_number=5
        )
        assert student1.get_group_name() == "ТВ-05"
        
        # Великий номер групи
        student2 = Student(
            full_name="Test",
            entrance_code="TEST2",
            year_of_entrance=2024,
            group_number=10
        )
        assert student2.get_group_name() == "ТВ-410"


