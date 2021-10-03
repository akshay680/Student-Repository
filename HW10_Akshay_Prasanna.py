""" Creating a Repository for University """

import os
from collections import defaultdict
from prettytable import PrettyTable
from HW08_Akshay_Prasanna import file_reader


class University:
    " Student and Instructor repository"

    def __init__(self, path: str, tables=True)-> None:
        self.path = path
        self.student = dict()
        self.instructor = dict()
        self.major = dict()

        try:
            self.major_details(os.path.join(path, 'majors.txt'))
            self.student_details(os.path.join(path, 'students.txt'))
            self.instructor_details(os.path.join(path, 'instructors.txt'))
            self.grade_details(os.path.join(path, 'grades.txt'))

        except FileNotFoundError:
            raise FileNotFoundError(f"the path {path} do not exist")
        else:
            if tables:
                print(" Student Table ")
                self.student_table()
                print(" Instructor Table ")
                self.instructor_table()
                print(" Majors Table")
                self.majors_table()

    def major_details(self, path: str)-> None:
        """Major detail are put in dictionary with file reader"""
        for major, flag, course in file_reader(path, 3, sep='\t', header=True):
            if major not in self.major:
                self.major[major] = Major(major)
            self.major[major].add_course(course, flag)

    def student_details(self, path: str)-> None:
        """ Student detail are put in dictionary with file reader """
        for cwid, name, major in file_reader(path, 3, sep=';', header=True):
            if major not in self.major:
                print(f"Student {cwid} '{name}' has unknown major '{major}'")
            else:
                self.student[cwid] = Student(cwid, name, self.major[major])

    def instructor_details(self, path):
        """ Instructor detail are put in dictionary with file reader """
        for cwid, name, dept in file_reader(path, 3, sep='|', header=True):
            self.instructor[cwid] = Instructor(cwid, name, dept)

    def grade_details(self, path):
        """Grades are put in dictionary with file reader """
        for std_cwid, course, grade, instructor_cwid in file_reader(path, 4, sep='|', header=True):
            if std_cwid in self.student:
                self.student[std_cwid].add_course(course, grade)
            else:
                print(f'Student Grade is {std_cwid}')

            if instructor_cwid in self.instructor:
                self.instructor[instructor_cwid].add_student(course)
            else:
                print(f'Instructor Grade is {instructor_cwid}')

    def student_table(self) -> None:
        """ printing student details """
        tab = PrettyTable(field_names=Student.tab_header)
        a = list()
        for student in self.student.values():
            tab.add_row(student.tab_row())
            a.append(student.tab_row())
        print(tab)
        print(a)

    def instructor_table(self):
        """ printing instructor details """
        tab = PrettyTable(field_names=Instructor.tab_header)
        for instructor in self.instructor.values():
            for row in instructor.tab_row():
                tab.add_row(row)
        print(tab)

    def majors_table(self):
        """ printing major details """
        tab = PrettyTable(field_names=Major.tab_header)
        for major in self.major.values():
            tab.add_row(major.tab_row())
        print(tab)


class Major:
    """ Class for Major """
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
        """addition of pending and elective courses"""
        passed = {course for course, grade in completed.items() if grade in Major.min_grades}
        rem_required = self._required - passed

        if self._electives.intersection(passed):
            rem_electives = None
        else:
            rem_electives = self._electives

        return self._dept, passed, rem_required, rem_electives

    def tab_row(self):
        """ To return a row from table """
        return [self._dept, sorted(self._required), sorted(self._electives)]


class Student:
    """ Class for student details """
    tab_header = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives']

    def __init__(self, cwid, name, major):
        self._cwid = cwid
        self._name = name
        self._major = major
        self._courses = dict()

    def add_course(self, course, grade):
        """ To add a course along with a grade """
        self._courses[course] = grade

    def tab_row(self):
        """ Returning a row in table """
        major, passed, rem_required, rem_electives = self._major.remaining(self._courses)
        return [self._cwid, self._name, major, sorted(passed), rem_required, rem_electives]


class Instructor:
    """ Class for instructor details """
    tab_header = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, cwid, name, dept):
        self._cwid = cwid
        self._name = name
        self._dept = dept
        self._courses = defaultdict(int)

    def add_student(self, course):
        """ No of students handled by instructor """
        self._courses[course] += 1

    def tab_row(self):
        """ Yielding the row """
        for course, count in self._courses.items():
            yield [self._cwid, self._name, self._dept, course, count]


def main():
    direct = 'E:\Python Practice'
    University(direct)


if __name__ == '__main__':
    main()

