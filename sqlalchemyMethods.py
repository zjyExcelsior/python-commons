# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:123456@localhost/testdb', echo=False)
Base = declarative_base()
#Session = sessionmaker()
#Session.configure(bind=engine)
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    password = Column(String(20))

    def __repr__(self):
        return '<User(name="%s", password="%s")>' % (self.name, self.password)

def create_tables():
    Base.metadata.create_all(engine)

def add_user(session):
    user_zjy = User(name='zhujiongyao', password='Zjy@2016')
    user_tcc = User(name='tongchenchen', password='Tcc@2016')
    session.add(user_zjy)
    session.add(user_tcc)
    session.commit()

def select_user(session, name):
    result = session.query(User).filter(User.name==name).all()
    return result

if __name__ == '__main__':
    create_tables()
    session = Session()
    # add_user(session)
    print select_user(session, 'zhujiongyao')
