import os
from collections import defaultdict
from prettytable import PrettyTable
from HW08_Akshay_Prasanna import file_reader

class University:
    """Student, instructor and grade repository"""
    def __init__(self, path: str, data = True):
        self.path = path
        self.student = {}
        self.instructor = {}

        try:
            self.student_details(os.path.join(path, 'students.txt'))
            self.instructor_details(os.path.join(path, 'instructors.txt'))
            self.grade_details(os.path.join(path, 'grades.txt'))
        except FileNotFoundError:
            raise FileNotFoundError(f"the path {path} do not exist")
        else:
            if data:
                print(" Student Table ")
                self.student_table()
                print(" Instructor Table ")
                self.instructor_table()

    def instructor_details(self, path: str)-> None:
        """ Instructor detail are put in dictionary with file reader """
        for cwid, name, dept in file_reader(path, 3, sep='|', header=False):
            self.instructor[cwid] = Instructor(cwid, name, dept)

    def student_details(self, path: str)-> None:
        """ Student detail are put in dictionary with file reader """
        for cwid, name, major in file_reader(path,3,sep=';',header=False):
            self.student[cwid] = Student(cwid, name, major)

    def grade_details(self, path: str)-> None:
        """Grades are added using file reader """
        for std_cwid, course, grade, instructor_cwid in file_reader(path, 4, sep='|', header=False):
            if std_cwid in self.student:
                self.student[std_cwid].add_course(course, grade)
            else:
                print(f'Student grade is {std_cwid}')

            if instructor_cwid in self.instructor:
                self.instructor[instructor_cwid].add_student(course)
            else:
                print(f'Instructor grade is {instructor_cwid}')

    def student_table(self) -> None:
        """ printing student details """
        line = PrettyTable(field_names=Student.header)
        for student in self.student.values():
            line.add_row(student.row())
        print(line)

    def instructor_table(self) -> None:
        """ printing Instructor details """
        line = PrettyTable(field_names=Instructor.header)
        for instructor in self.instructor.values():
            for row in instructor.row():
                line.add_row(row)
        print(line)

class Student:
    """ Class for student details """
    header = ['CWID', 'Name', 'Completed Courses']

    def __init__(self, cwid: int, name: str, major: str)-> None:
        self._cwid = cwid
        self._name = name
        self._major = major
        self._courses = dict()

    def add_course(self, course: str, grade: str)-> None:
        """ To add a course along with a grade """
        self._courses[course] = grade

    def row(self):
        """ Returning a row in table """
        return [self._cwid, self._name, sorted(self._courses.keys())]


class Instructor:
    """ Class for instructor details """
    header = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, cwid: int, name: str, dept: str)-> None:
        self._cwid = cwid
        self._name = name
        self._dept = dept
        self._courses = defaultdict(int)

    def add_student(self, course: str)-> None:
        """ No of Students handled by instructor """
        self._courses[course] += 1

    def row(self):
        """ Yielding the row """
        for course, count in self._courses.items():
            yield [self._cwid, self._name, self._dept, course, count]


def main():
    direct = 'Users\dell\PycharmProjects\untitled1\grades.txt'
    University(direct)

if __name__ == '__main__':
    main()
