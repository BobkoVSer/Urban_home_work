
import unittest
from main import Student
class TestStudent(unittest.TestCase):
    def setUp(self):
        self.name1 = '1 студент'
        self.student1 = Student(self.name1)

        self.name2 = '2 студент'
        self.student2 = Student(self.name2)

    def test_walk(self):
        for _ in range(10):
            self.student1.walk()
            self.assertEqual(self.student1.distance, 500, f"Дистанции не равны {self.name1} != 500")
    def test_run(self):
        for _ in range(10):
            self.student2.run()
            self.assertEqual(self.student2.distance, 1000, f"Дистанции не равны {self.name2} != 1000")
    def test_walk_run(self):
        self.student1.walk()
        self.student2.run()
        self.assertEqual(self.student1.distance, 500, f'Дистанция меньше чем у бегущего {self.name1} !')
        self.assertEqual(self.student2.distance, 1000, f'Дистанция бодьше  чем у идущего {self.name2} !')





