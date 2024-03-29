""" Creating a Repository for University """

import os
import sqlite3
from collections import defaultdict
from prettytable import PrettyTable
from HW08_Akshay_Prasanna import file_reader


class University:
    " Student and Instructor repository"

    def __init__(self, direct, tables=True):
        self._direct = direct
        self._students = dict()
        self._instructors = dict()
        self._majors = dict()


        try:
            self._get_majors(os.path.join(direct, 'majors.txt'))
            self._get_students(os.path.join(direct, 'students.txt'))
            self._get_instructors(os.path.join(direct, 'instructors.txt'))
            self._get_grades(os.path.join(direct, 'grades.txt'))

        except FileNotFoundError:
            raise FileNotFoundError
        else:
            if tables:
                print(" Student Table ")
                self.student_table()
                print(" Instructor Table ")
                self.instructor_table()
                print(" Majors Table")
                self.majors_table()



    def _get_majors(self, path):
        """Major details are read using file reading gen and added to dictionary"""
        for major, flag, course in file_reader(path, 3, sep='\t', header=True):
            if major not in self._majors:
                self._majors[major] = Major(major)
            self._majors[major].add_course(course, flag)

    def _get_students(self, path):
        """ Student detail are read using file reading gen and added to dictionary """
        for cwid, name, major in file_reader(path, 3, sep='\t', header=True):
            if major not in self._majors:
                print(f"Student {cwid} '{name}' has unknown major '{major}'")
            else:
                self._students[cwid] = Student(cwid, name, self._majors[major])

    def _get_instructors(self, path):
        """ Instructor detail are read using file reading gen and added to dictionary """
        for cwid, name, dept in file_reader(path, 3, sep='\t', header=True):
            self._instructors[cwid] = Instructor(cwid, name, dept)

    def _get_grades(self, path):
        """Grades are read using file reading gen and assigned to student and instructor """
        for std_cwid, course, grade, instructor_cwid in file_reader(path, 4, sep='\t', header=True):
            if std_cwid in self._students:
                self._students[std_cwid].add_course(course, grade)
            else:
                print(f'Grades for student is {std_cwid}')

            if instructor_cwid in self._instructors:
                self._instructors[instructor_cwid].add_student(course)
            else:
                print(f'Grades for instructor is {instructor_cwid}')



    def student_table(self):
        """ Student table """
        tab = PrettyTable(field_names=Student.tab_header)
        a = list()
        for student in self._students.values():
            tab.add_row(student.tab_row())
            a.append(student.tab_row())
        print(tab)

    def new_student_table_db(self, db_path=r"C:\Users\dell\Desktop\Student-Repository-HW11\810_startup.db"):
        """Database Table"""
        db = sqlite3.connect(db_path)
        tab = PrettyTable(field_names=['CWID', 'Name', 'Major', 'Remaining Required', 'Remaining Electives', 'GPA'])
        for row in db.execute(
                "select s.name,s.cwid,g.Course,g.Grade,i.Name  from students s,grades g,instructors i where s.CWID=g.Student CWID and i.CWID=g.Instructor CWID ORDER BY s.Name"):
            tab.add_row(row)
        print(tab)

    def instructor_table(self):
        """ Instructor table """
        tab = PrettyTable(field_names=Instructor.tab_header)
        for instructor in self._instructors.values():
            for row in instructor.tab_row():
                tab.add_row(row)
        print(tab)

    def majors_table(self):
        """ Majors Table """
        tab = PrettyTable(field_names=Major.tab_header)
        for major in self._majors.values():
            tab.add_row(major.tab_row())
        print(tab)



class Major:
    """ Major Class """
    tab_header = ['Major', 'Required Courses', 'Electives']
    min_grades = {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}

    def __init__(self, dept):
        self._dept = dept
        self._required = set()
        self._electives = set()

    def add_course(self, course, req):
        if req == 'R':
            self._required.add(course)
        elif req == 'E':
            self._electives.add(course)
        else:
            raise ValueError("Course not found")

    def remaining(self, completed):
        """Adding remaining courses as well as electives"""
        passed = {course for course, grade in completed.items() if grade in Major.min_grades}
        rem_required = self._required - passed

        if self._electives.intersection(passed):
            rem_electives = None
        else:
            rem_electives = self._electives

        return self._dept, passed, rem_required, rem_electives

    def tab_row(self):
        """ Returning a row in table """
        return [self._dept, sorted(self._required), sorted(self._electives)]


class Student:
    """ Student class """
    tab_header = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives']

    def __init__(self, cwid, name, major):
        self._cwid = cwid
        self._name = name
        self._major = major
        self._courses = dict()


    def add_course(self, course, grade):
        """ Adding course with grade """
        self._courses[course] = grade

    def tab_row(self):
        """ Returning a row in table """
        major, passed, rem_required, rem_electives = self._major.remaining(self._courses)
        return [self._cwid, self._name, major, sorted(passed), rem_required, rem_electives]


class Instructor:
    """ Instructor class """
    tab_header = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, cwid, name, dept):
        self._cwid = cwid
        self._name = name
        self._dept = dept
        self._courses = defaultdict(int)

    def add_student(self, course):
        """ NUmber of students taking course with Instructor """
        self._courses[course] += 1

    def tab_row(self):
        """ Yield the row """
        for course, count in self._courses.items():
            yield [self._cwid, self._name, self._dept, course, count]


def main():
    direct = r'C:\Users\dell\Desktop'
    University(direct)


if __name__ == '__main__':
    main()
