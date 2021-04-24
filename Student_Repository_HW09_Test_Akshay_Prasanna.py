import unittest
import os
from HW13_Akshay_Prasanna import Student, University, Instructor



class InstructorTest(unittest.TestCase):
    """Testing Instructor class"""


    def test_instructor_details(self):
        """testing instructor_details() method"""
        instructor = Instructor('98763', 'Newton, I', 'SYEN')
        instructor.add_student('SYS 660')
        self.assertNotEqual(instructor.add_student("SYS 660"), ['98763', 'Newton, I', 'SYEN', 'SYS 660', 1])

class StudentsTest(unittest.TestCase):
    """Testing Student class"""


    def test_student_details(self):
        """testing student_details() method"""
        student = Student('10103', 'Baldwin, C', 'SFEN')
        student.add_course('SSW 567', 'A')
        self.assertNotEqual(student.add_course('SSW 567', 'A'),['10103', 'Baldwin, C', ['SSW 567']])



class UniversityTest(unittest.TestCase):
    """Testing Repository class methods"""


    def test_University(self):
        """test cases for Repository class methods"""
        cwd = '/Users/akshay/Documents/SSW810/test_repo'
        repo = University(cwd)  # Instance of instructor used for testing
        self.assertEqual(repo.student(os.path.join(cwd, 'students.txt')), None)
        self.assertEqual(repo.instructor(os.path.join(cwd, 'instructors.txt')), None)





if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)










