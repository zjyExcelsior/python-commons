# coding=utf-8
"""一致性hash算法的实现"""
import hashlib


class HashRing(object):

    def __init__(self, nodes=None, replicas=3):
        """Manage a hash ring.

        `nodes` is a list of objects that have a proper __str__ representation.
        `replicas` indicates how many virtual points should used per node,
        replicas are required to improve the distribution.
        """
        self.replicas = replicas

        self.ring = dict()
        self._sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        """Add a `node` to the hash ring(including a number of replicas)"""
        for i in xrange(self.replicas):
            key = self.gen_key('%s:%s' % (node, i))
            self.ring[key] = node
            self._sorted_keys.append(key)

        self._sorted_keys.sort()

    def remove_node(self, node):
        """Remove `node` from """
        for i in xrange(self.replicas):
            key = self.gen_key('%s:%s' % (node, i))
            del self.ring[key]
            self._sorted_keys.remove(key)

    def get_node(self, string_key):
        """Given a string key a corresponding node in the hash ring is returned.

        If the hash ring is empty, `None` is returned.
        """
        return self.get_node_pos(string_key)[0]

    def get_node_pos(self, string_key):
        """Given a string key a corresponding node in the hash ring is returned
        along with its position in the ring.

        If the hash ring is empty, (`None`, `None`) is returned.
        """
        if not self.ring:
            return None, None
        key = self.gen_key(string_key)
        nodes = self._sorted_keys
        for i, node in enumerate(nodes):
            if key <= node:
                return self.ring[node], i
        return self.ring[nodes[0]], 0

    def get_nodes(self, string_key):
        """Given a string key it returns the nodes as a generator that
        can hold the key.

        The generator is never ending and iterates through the ring
        starting at the correct position.
        """
        if not self.ring:
            yield None, None
        node, pos = self.get_node_pos(string_key)
        for key in self._sorted_keys[pos:]:
            yield self.ring[key]
        while True:
            for key in self._sorted_keys:
                yield self.ring[key]

    def gen_key(self, key):
        """Given a string key it returns a long value,
        this long value represents a place on the hash ring.

        md5 is currently used because it mixes well.
        """
        m = hashlib.md5()
        m.update(key)
        return long(m.hexdigest(), 16)


if __name__ == '__main__':
    memcache_servers = [
        '192.168.0.246:11212', '192.168.0.247:11212', '192.168.0.249:11212'
    ]

    ring = HashRing(memcache_servers)
    server = ring.get_node('my_key')
    print(server)
