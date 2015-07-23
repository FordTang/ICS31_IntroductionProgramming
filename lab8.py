# Ryan Carter 90751339 and Ford Tang 46564602. Lab 8 sec 8.

#-----Part C-----
from collections import namedtuple

Course = namedtuple('Course', 'dept num title instr units')
# Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)

Student = namedtuple('Student', 'ID name level major studylist')
# All are strings except studylist, which is a list of Courses.
sT = Student('31223344', 'Programmer, Ken', 'SR', 'SE', [ics32, wr39a, bio97])
sU = Student('12345678', 'Programmer, Bob', 'FR', 'CGS', [ics31, wr39a, bio97])
sV = Student('12223544', 'Anteater, Steve', 'FR', 'INFX', [ics31, wr39a, bio97, mgt1])
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1])

StudentBody = [sW, sX, sY, sZ]

#-----c.1-----
print('-----c.1-----')
def Students_at_level(students:list, s:str) -> list:
    result = []
    for student in students:
        if student.level == s:
            result.append(student)
    return result

assert Students_at_level(StudentBody, 'JR') == []
assert Students_at_level(StudentBody, 'FR') == [sW, sY]

#-----c.2-----
print()
print('-----c.2-----')
def Students_in_majors(students:list, majors:list) -> list:
    result = []
    for student in students:
        if student.major in majors:
            result.append(student)
    return result

assert Students_in_majors(StudentBody, ['PSB', 'CS']) == [sW, sX, sZ]
assert Students_in_majors(StudentBody, ['ICS']) == []

#-----c.3-----
print()
print('-----c.3-----')

def Course_equals(c1: Course, c2: Course) -> bool:
    ''' Return True if the department and number of c1 match the department and
	     number of c2 (and False otherwise)
    '''
    return c1.dept == c2.dept and c1.num == c2.num

assert not Course_equals(ics31, ics32)


def Course_on_studylist(c: Course, SL: 'list of Course') -> bool:
    ''' Return True if the course c equals any course on the list SL (where equality
	     means matching department name and course number) and False otherwise.
    '''
    return c in SL

assert Course_on_studylist(wr39a, sY.studylist)

def Student_is_enrolled(S: Student, department: str, coursenum: str) -> bool:
    ''' Return True if the course (department and course number) is on the student's
	     studylist (and False otherwise)
    '''
    for course in S.studylist:
        if course.dept == department and course.num == coursenum:
            return True
    return False

assert Student_is_enrolled(sZ, 'Management', '1')

def Students_in_class(students:list, department:str, num:str) -> list:
    ''' Return a list of students who are enrolled in the course
    '''
    result = []
    for student in students:
        if Student_is_enrolled(student, department, num):
            result.append(student)
    return result

assert Students_in_class(StudentBody, 'ICS', '31') == [sW, sX]

#-----c.4-----
print()
print('-----c.4-----')
def Student_names(students:list) -> list:
    result = []
    for student in students:
        result.append(student.name)
    return result

assert Student_names([sW, sX]) == [sW.name, sX.name]

#-----c.5-----
print()
print('-----c.5-----')

StudentBody = [sT, sU, sV, sW, sX, sY, sZ]
ICS_Majors = ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']
students_in_ICS = Students_in_majors(StudentBody, ICS_Majors)

print(students_in_ICS)
print()
print(Student_names(students_in_ICS))
print()
print(len(students_in_ICS))
print()
print(Students_at_level(students_in_ICS, 'SR'))
print()
print(len(Students_at_level(students_in_ICS, 'SR')))
print()
print(len(Students_at_level(students_in_ICS, 'SR')) / len(students_in_ICS))
print()
print(len(Students_in_class(Students_at_level(students_in_ICS, 'FR'), 'ICS', '31')))
print()
total_units = 0
for student in Students_in_class(Students_at_level(students_in_ICS, 'FR'), 'ICS', '31'):
    student_units = 0
    for course in student.studylist:
        student_units += course.units
    total_units += student_units / len(student.studylist)
print(total_units / len(Students_in_class(Students_at_level(students_in_ICS, 'FR'), 'ICS', '31')))
