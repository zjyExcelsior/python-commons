# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import text
from contextlib import contextmanager
from logger import get_logger

sql_logger = get_logger('sql')

engine = create_engine('mysql://root:123456@localhost/testdb', echo=False)
Base = declarative_base()
#Session = sessionmaker()
# Session.configure(bind=engine)
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


class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship(
        'User', backref=backref('cards', cascade='all, delete-orphan'))

    def __repr__(self):
        return '<Card(name="%s")>' % self.name


def create_tables():
    Base.metadata.create_all(engine)


def add_user():
    with session_scope() as session:
        user_zjy = User(name='zhujiongyao', password='Zjy@2016')
        user_tcc = User(name='tongchenchen', password='Tcc@2016')
        session.add(user_zjy)
        session.add(user_tcc)
        session.add_all([
            User(name='zhujy', password='Zjy@2016'),
            User(name='tongcc', password='Tcc@2016')
        ])
        session.flush()
        card_zjy = Card(name='icbc', owner_id=user_zjy.id)
        card_tcc = Card(name='abc', owner_id=user_tcc.id)
        session.add_all([card_zjy, card_tcc])


def delete_user(name):
    with session_scope() as session:
        results = session.query(User).filter(User.name == name).all()
        for result in results:
            session.delete(result)


def update_user(name, new_password):
    with session_scope() as session:
        results = session.query(User).filter(User.name == name).all()
        for result in results:
            result.password = new_password


def select_user_cards(user_name):
    with session_scope() as session:
        users = session.query(User).filter(User.name == user_name).all()
        # session.expunge_all()
    if not users:
        sql_logger.info('No row was found for %s', user_name)
        return users
    users = map(session.merge, users)
    ret = []
    for user in users:
        cards = user.cards
        ret.append('user: %s, id: %s, cards: %s' % (user, user.id, cards))
    return ret

def select_all_from_user(user_name):
    with session_scope() as session:
        sql_expression = text('select * from users where users.name = :name')
        args = {
            'name': 'zhujy'
        }
        conn = engine.connect()
        results = conn.execute(sql_expression, args).fetchall()
        return results

if __name__ == '__main__':
    create_tables()
    # add_user(session)
    # delete_user('zhujiongyao')
    # delete_user('tongchenchen')
    # update_user('tongchenchen', 'tcc@2016')
    # print select_user('tongchenchen')
    # print select_user_cards('zhujyddd')
    print select_user_cards('zhujy')
    print select_all_from_user('zhujy')