from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def createSession():
    engine = create_engine('sqlite:///Assets/baza.db')
    DBsession = sessionmaker(bind=engine)
    return DBsession()