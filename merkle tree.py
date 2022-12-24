#  To design a Merkel tree, you will need to decide on the following elements:

#  The data blocks to be stored in the tree. These can be any type of data, such as files, blocks of a blockchain, or key-value pairs.
#  The hash function to be used to generate the hashes of the data blocks. The hash function should be a cryptographic hash function that is collision-resistant and has a fixed output size.
#  The structure of the tree. A Merkel tree is typically a binary tree, with each node in the tree representing the hash of its two children. However, you could also use a different tree structure, such as a trie or a Patricia trie.
#  The algorithm for building the tree. To build the tree, you will need to compute the hashes of the data blocks and then insert them into the tree according to the chosen tree structure



import hashlib

class MerkelNode:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

    def hash(self):
        if self.data:
            return self.data
        elif self.left and self.right:
            return hashlib.sha256(self.left.hash() + self.right.hash()).hexdigest()
        else:
            return None

# Example usage
root = MerkelNode(
    left=MerkelNode(data='hello'),
