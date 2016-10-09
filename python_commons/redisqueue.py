# coding: utf-8
import redis


class RedisQueue(object):

    """Queue with Redis Backend"""

    def __init__(self, queue_name, **redis_kwargs):
        self.__db = redis.StrictRedis(**redis_kwargs)
        self.key = queue_name

    def qsize(self):
        """Return the size of the queue."""
        return self.__db.llen(self.key)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.qsize() == 0

    def put(self, item):
        """Put item into the queue."""
        self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue.
        If block is True and tiemout is None, block 
        if necessary until an item is available.
        """
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
            item = item[1] if item else None
        else:
            item = self.__db.lpop(self.key)
        return item

    def get_nowait(self):
        """Equivalent to get(False)."""
        return self.get(False)

if __name__ == '__main__':
    q = RedisQueue('test:queue', host='localhost', port=6379, db=0)
    print q.qsize()
    print q.empty()
    q.put('first')
    q.put('second')
    q.put('third')
    print q.qsize()
    print q.empty()
    print q.get_nowait()
    print q.get()
    print q.get()
    print q.qsize()
    print q.get(timeout=5)
