from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = "postgres"
password = "1234"
domain = "localhost"
db_name = "HW7"

url = f'postgresql+psycopg2://{username}:{password}@{domain}:5432/{db_name}'
engine = create_engine(url, echo=False) #echo - детальне логування всіх SQL-запитів
DBSession = sessionmaker(bind=engine)
session = DBSession()
