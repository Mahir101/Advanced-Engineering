import hashlib

class Node:
    def __init__(self, id, address):
        self.id = id
        self.address = address

class HashRing:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.sorted_nodes = []
        self.hash_ring = {}
        self.build_ring()

    def build_ring(self):
        for node in self.nodes:
            self.add_node(node)

    def add_node(self, node):
        self.hash_ring[node.id] = node
        self.sorted_nodes = sorted(self.hash_ring.keys())

    def remove_node(self, node_id):
        del self.hash_ring[node_id]
        self.sorted_nodes = sorted(self.hash_ring.keys())

    def get_node(self, key):
        if not self.hash_ring:
            return None

        key_hash = int(hashlib.md5(key.encode()).hexdigest(), 16)
        node_idx = bisect_left(self.sorted_nodes, key_hash) % len(self.sorted_nodes)
        return self.hash_ring[self.sorted_nodes[node_idx]]

# Example usage
ring = HashRing([Node(1, '192.0.2.1:8080'), Node(2, '192.0.2.2:8080')])
node = ring.get_node('key1')
print(node.address)

ring.add_node(Node(3, '192.0.2.3:8080'))
node = ring.get_node('key2')
print(node.address)

ring.remove_node(2)
node = ring.get_node('key3')
print(node.address)
