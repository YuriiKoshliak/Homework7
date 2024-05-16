from sqlalchemy import func, desc
from src.models import Student, Teacher, Grade, Group, Subject
from src.connections import session


def select_1():
    result = session.query(
        Student.firstname, 
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade, Grade.student_id == Student.id)\
     .group_by(Student.id)\
     .order_by(desc('avg_grade'))\
     .limit(5)\
     .all()
    return result

def select_2(subject_id):
    result = session.query(
        Student.firstname,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade, Grade.student_id == Student.id)\
     .filter(Grade.subject_id == subject_id)\
     .group_by(Student.id)\
     .order_by(desc('avg_grade'))\
     .first()
    return result

def select_3(subject_id):
    result = session.query(
        Group.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Student, Student.group_id == Group.id)\
     .join(Grade, Grade.student_id == Student.id)\
     .filter(Grade.subject_id == subject_id)\
     .group_by(Group.id)\
     .all()
    return result

def select_4():
    result = session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).all()
    return result

def select_5(teacher_id):
    result = session.query(
        Subject.name
    ).filter(Subject.teacher_id == teacher_id)\
     .all()
    return result

def select_6(group_id):
    result = session.query(
        Student.firstname, Student.lastname
    ).filter(Student.group_id == group_id)\
     .all()
    return result

def select_7(group_id, subject_id):
    result = session.query(
        Student.firstname,
        Grade.grade
    ).join(Grade, Grade.student_id == Student.id)\
     .filter(Student.group_id == group_id)\
     .filter(Grade.subject_id == subject_id)\
     .all()
    return result

def select_8(teacher_id):
    result = session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Subject, Subject.id == Grade.subject_id)\
     .filter(Subject.teacher_id == teacher_id)\
     .all()
    return result

def select_9(student_id):
    result = session.query(
        func.distinct(Subject.name)
    ).join(Grade, Grade.subject_id == Subject.id)\
     .filter(Grade.student_id == student_id)\
     .all()
    return result


def select_10(student_id, teacher_id):
    result = session.query(
        func.distinct(Subject.name)
    ).join(Grade, Grade.subject_id == Subject.id)\
     .filter(Grade.student_id == student_id)\
     .filter(Subject.teacher_id == teacher_id)\
     .all()
    return result
