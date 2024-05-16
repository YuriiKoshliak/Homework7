import random
import logging
from faker import Faker
from sqlalchemy import select
from src.models import Teacher, Student, Grade, Group, Subject
from src.connections import session

group_list = [21, 22, 23, 24]
subject_list = ["Python", "Java", "C++", "C#", "Go"]

fake = Faker('uk_UA')
TEACHERS_COUNT = 5
STUDENTS_COUNT = 30
GRADES_COUNT = 20

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_all_ids(model):
    return session.scalars(select(model.id)).all()

def seed_groups():
    try:
        for g in group_list:
            group = Group(name=g)
            session.add(group)
        session.commit()
        logger.info("Groups seeded successfully.")
    except Exception as e:
        session.rollback()
        logger.error(f"Error seeding groups: {e}")
    
def seed_teachers():
    try:
        for _ in range(TEACHERS_COUNT):
            teacher = Teacher(firstname=fake.first_name())
            session.add(teacher)
        session.commit()
        logger.info("Teachers seeded successfully.")
    except Exception as e:
        session.rollback()
        logger.error(f"Error seeding teachers: {e}")

def seed_subjects():
    try:
        teachers_ids = get_all_ids(Teacher)
        for s in subject_list:
            subject = Subject(name=s, teacher_id=random.choice(teachers_ids))
            session.add(subject)
        session.commit()
        logger.info("Subjects seeded successfully.")
    except Exception as e:
        session.rollback()
        logger.error(f"Error seeding subjects: {e}")

def seed_students():
    try:
        for _ in range(STUDENTS_COUNT):
            groups_ids = get_all_ids(Group)
            student = Student(firstname=fake.first_name(),
                            lastname=fake.last_name(),
                            group_id=random.choice(groups_ids)
            )
            session.add(student)
        session.commit()
        logger.info("Students seeded successfully.")
    except Exception as e:
        session.rollback()
        logger.error(f"Error seeding students: {e}")

def seed_grades():
    try:
        students_ids = get_all_ids(Student)
        subjects_ids = get_all_ids(Subject)
        for s in students_ids:
            for _ in range(GRADES_COUNT):
                grade = Grade(
                    grade=random.randint(1, 5),
                    date_of=fake.date_object(),
                    student_id=s,
                    subject_id=random.choice(subjects_ids)
                )
                session.add(grade)
        session.commit()
        logger.info("Grades seeded successfully.")
    except Exception as e:
        session.rollback()
        logger.error(f"Error seeding grades: {e}")
        

    

if __name__ == "__main__":
    logger.info("Starting seeding process...")
    try:
        seed_groups()
        seed_teachers()
        seed_subjects()
        seed_students()
        seed_grades()
    except Exception as e:
        logger.error(f"Error running seed script: {e}")
    finally:
        session.close()
        logger.info("Database session closed.")