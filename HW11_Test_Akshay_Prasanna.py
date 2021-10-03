"""" Test for Repository """

import unittest
import os
from HW11_Akshay_Prasanna import University, Student, Instructor, file_reader, Major


class TestRepository(unittest.TestCase):
    """ Test for repository """

    def setUp(self):
        self.test_path = "C:\Users\dell\Desktop"
        self.repo = University(self.test_path, False)

    def test_majors(self):
        """ Testing majors table"""
        expected = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
                    ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]

        calculated = [majors.tab_row() for majors in self.repo._majors.values()]
        self.assertEqual(expected, calculated)

    def test_Student_attributes(self):
        """ Testing student table """
        expected = [
            ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, None]]

        calculated = [student.tab_row() for cwid, student in self.repo._students.items()]
        self.assertEqual(expected, calculated)

    def test_Instructor_attributes(self):
        """ Testing instructors table """
        expected = {('98764', 'Cohen, R', 'SFEN', 'SSW 567', 4)}

        calculated = {tuple(detail) for instructor in self.repo._instructors.values() for detail in
                      instructor.tab_row()}
        self.assertEqual(expected, calculated)


if __name__ == "__main__":
    """ Run test cases on startup """
    unittest.main(exit=False, verbosity=2)