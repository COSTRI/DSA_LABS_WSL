#lab 4
#1815522
#11/02/2025

class TreeNode:
    def __init__(self, value):
        # Initialize a tree node with a value and no children
        self.value = value
        self.left = None  # Left child
        self.right = None  # Right child

class BinaryTree:
    def __init__(self):
        # Initialize the binary tree with no root
        self.root = None

    def insert(self, value):
        # Insert a new value into the binary tree
        if not self.root:
            self.root = TreeNode(value)  # If tree is empty, set root
        else:
            self._insert_recursive(self.root, value)  # Otherwise, insert recursively

    def _insert_recursive(self, node, value):
        # Helper method to insert a value recursively
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)  # Insert as left child
            else:
                self._insert_recursive(node.left, value)  # Continue left
        else:
            if node.right is None:
                node.right = TreeNode(value)  # Insert as right child
            else:
                self._insert_recursive(node.right, value)  # Continue right

    def in_order(self, node):
        # Perform in-order traversal (left, root, right)
        if node:
            self.in_order(node.left)  # Visit left subtree
            print(node.value, end=' ')  # Visit node
            self.in_order(node.right)  # Visit right subtree

    def pre_order(self, node):
        # Perform pre-order traversal (root, left, right)
        if node:
            print(node.value, end=' ')  # Visit node
            self.pre_order(node.left)  # Visit left subtree
            self.pre_order(node.right)  # Visit right subtree

    def post_order(self, node):
        # Perform post-order traversal (left, right, root)
        if node:
            self.post_order(node.left)  # Visit left subtree
            self.post_order(node.right)  # Visit right subtree
            print(node.value, end=' ')  # Visit node

    def count_nodes(self, node):
        # Count the number of nodes in the binary tree
        if not node:
            return 0  # Base case: no node
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)  # Count current node + left + right

    def compute_depth(self, node):
        # Compute the maximum depth of the binary tree
        if not node:
            return 0  # Base case: no node
        left_depth = self.compute_depth(node.left)  # Depth of left subtree
        right_depth = self.compute_depth(node.right)  # Depth of right subtree
        return max(left_depth, right_depth) + 1  # Max depth + 1 for current node

# Example usage
if __name__ == "__main__":
    bt = BinaryTree()  # Create a binary tree
    values = [5, 3, 7, 2, 4, 6, 8]  # Values to insert into the tree
    for v in values:
        bt.insert(v)  # Insert each value into the tree

    print("In-order traversal:")
    bt.in_order(bt.root)  # Display in-order traversal
    print("\nPre-order traversal:")
    bt.pre_order(bt.root)  # Display pre-order traversal
    print("\nPost-order traversal:")
    bt.post_order(bt.root)  # Display post-order traversal

    print("\nNumber of nodes:", bt.count_nodes(bt.root))  # Count and display number of nodes
    print("Depth of the tree:", bt.compute_depth(bt.root))  # Calculate and display depth of the tree