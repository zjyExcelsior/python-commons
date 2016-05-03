# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine('mysql://root:123456@localhost/testdb', echo=False)
Base = declarative_base()
#Session = sessionmaker()
#Session.configure(bind=engine)
Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    '''Provide a transactional scope around a series of operations.'''
    session = Session()
    try:
        # session.expire_on_commit = False
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

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
    with session_scope() as session:
        user_zjy = User(name='zhujiongyao', password='Zjy@2016')
        user_tcc = User(name='tongchenchen', password='Tcc@2016')
        session.add(user_zjy)
        session.add(user_tcc)
        session.add_all([
            User(name='zhujy', password='Zjy@2016'),
            User(name='tongcc', password='Tcc@2016')
            ])

def delete_user(session, name):
    with session_scope() as session:
        result = session.query(User).filter(User.name == name).one()
        session.delete(result)

def update_user(session, name, new_password):
    with session_scope() as session:
        result = session.query(User).filter(User.name == name).one()
        result.password = new_password

def select_user(session, name):
    with session_scope() as session:
        results = session.query(User).filter(User.name == name).all()
        # session.expunge_all()
    return map(session.merge, results)

if __name__ == '__main__':
    create_tables()
    session = Session()
    # add_user(session)
    # delete_user(session, 'zhujiongyao')
    # update_user(session, 'tongchenchen', 'tcc@2016')
    print select_user(session, 'tongchenchen')
