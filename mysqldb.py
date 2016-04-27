# coding: utf-8
'''
some method about MySQL-python(MySQLdb)
'''
import MySQLdb
from DBUtils.PooledDB import PooledDB


def select_from_db(conn, sql, values):
    '''
    select from database
    '''
    c = conn.cursor()
    c.execute(sql, values)
    result = c.fetchall()
    c.close()
    conn.close()
    return result


def insert_into_db(conn, sql, values):
    '''
    insert into database
    '''
    c = conn.cursor()
    c.execute(sql, values)
    conn.commit()
    c.close()
    conn.close()

if __name__ == '__main__':
    # db = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='zjyTest')
    pool = PooledDB(MySQLdb, 5, user='root', passwd='123456',
                    host='localhost', port=3306, db='zjyTest')
    sql_insert = 'insert into animals values (%s, %s)'
    insert_values = (1, 'dog')
    insert_into_db(pool.connection(), sql_insert, insert_values)
    sql_select = 'select * from animals where id = %s'
    select_values = (1, )
    print select_from_db(pool.connection(), sql_select, select_values)
