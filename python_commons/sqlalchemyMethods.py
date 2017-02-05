# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import text
from contextlib import contextmanager
from logger import get_logger

sql_logger = get_logger('sql')

Base = declarative_base()
engine = create_engine('mysql://root:123456@localhost/testdb?charset=utf8', echo=False)
Session = sessionmaker(bind=engine)
# Session = sessionmaker()
# Session.configure(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    try:
        session = Session()
        Session.remove() # 这边已经可以remove
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close() # 也可以用Session.remove()，不过目的都是为了调用close()
        # Session.remove()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    password = Column(String(20))

    def __repr__(self):
        return '<User(name="%s", password="%s")>' % (self.name, self.password)


class Class(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    def __repr__(self):
        return '<Class(name="%s")>' % self.name


class Score(Base):
    __tablename__ = 'scores'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    class_id = Column(Integer, ForeignKey('classes.id'), primary_key=True)
    score = Column(Integer)
    user = relationship('User', backref='classes')
    _class = relationship('Class', backref='users')

    def __repr__(self):
        return '<Score(user_id="%s", class_id="%s", score="%s")>' % (self.user_id, self.class_id, self.score)


class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship(
        'User', backref=backref('cards', cascade='all, delete-orphan'))

    def __repr__(self):
        return '<Card(name="%s")>' % self.name


def drop_tables():
    Base.metadata.drop_all(engine)

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

def test_many_to_many():
    with session_scope() as session:
        user_a = User(name='zhujiongyao', password='123456')
        user_b = User(name='tongcc', password='123456')
        class_a = Class(name='AAA')
        class_b = Class(name='BBB')
        score_a = Score(score=99)
        score_b = Score(score=88)
        user_a.classes.append(score_a)
        class_a.users.append(score_a)
        user_b.classes.append(score_b)
        class_b.users.append(score_b)
        session.add_all([user_a, user_b, class_a, class_b, score_a, score_b])

if __name__ == '__main__':
    drop_tables()
    create_tables()
    test_many_to_many()
    # add_user(session)
    # delete_user('zhujiongyao')
    # delete_user('tongchenchen')
    # update_user('tongchenchen', 'tcc@2016')
    # print select_user('tongchenchen')
    # print select_user_cards('zhujyddd')
    # print select_user_cards('zhujy')
    # print select_all_from_user('zhujy')
