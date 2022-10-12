#!/usr/bin/python3
#
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

Base = declarative_base()

class Language(Base):

    __tablename__ = 'languages'

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://root:root@localhost/demo_db', pool_pre_ping=True)
    Base.metadata.create_all(engine)

#Create/Insert Data
    session = Session(engine)
    lang1 = Language(name = 'Python')
    lang2 = Language(name = 'JavaScript')
    lang3 = Language(name = 'C')

#    session.add(lang1)
#    session.add(lang2)
#    session.add(lang3)
#    session.commit()

# Read Data
    languages = session.query(Language).order_by(Language.id.asc()).all()
#    print(session.query(Language).all())
    for language in languages:
        print("{}: {}".format(language.id, language.name))

#    item_del = session.query(Language).filter(Language.name == 'C').one()
#    session.delete(item_del)
#    session.commit()
#    for language in languages:
#    print("{}: {}".format(language.id, language.name))
#Update data
    new_update = session.query(Language).filter_by(id=2).first()
    new_update.name = "JavaScript JS"
    session.add(new_update)
    session.commit()
    
    languages = session.query(Language).order_by(Language.id.asc()).all()
    for language in languages:
        print("{}: {}".format(language.id, language.name))
    session.close()
