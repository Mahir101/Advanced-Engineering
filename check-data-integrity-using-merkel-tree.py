import hashlib

class MerkelTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hash = None

    def calculate_hash(self):
        if self.left is None and self.right is None:
            # Leaf node, return the hash of the data
            return hashlib.sha256(self.data).hexdigest()
        else:
            # Non-leaf node, return the hash of the concatenation of the left and right hashes
            left_hash = self.left.calculate_hash()
            right_hash = self.right.calculate_hash()
            return hashlib.sha256(left_hash + right_hash).hexdigest()

def contains_value(node, value):
    if node is None:
        return False

    if node.data == value:
        return True
    elif node.left is not None and contains_value(node.left, value):
        return True
    elif node.right is not None and contains_value(node.right, value):
        return True
    else:
        return False

# Example usage
tree = MerkelTree("root")
tree.left = MerkelTree("left")
tree.right = MerkelTree("right")

assert contains_value(tree, "root") == True
assert contains_value(tree, "left") == True
assert contains_value(tree, "right") == True
assert contains_value(tree, "wrong") == False
