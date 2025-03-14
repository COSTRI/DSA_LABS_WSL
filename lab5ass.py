#1815522
#2nd March,2025


#Task 1: Check if a Binary Tree is a Valid BST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize the tree node with a value and optional left/right children
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(node, low=float('-inf'), high=float('inf')):
    """
    Recursively checks if the binary tree is a valid BST.
    
    Args:
    - node: The current tree node.
    - low: The lower bound for the current node's value.
    - high: The upper bound for the current node's value.
    
    Returns:
    - True if the subtree is a valid BST, False otherwise.
    """
    if not node:
        return True  # An empty node is a valid BST
    if not (low < node.val < high):
        return False  # Current node's value must be within the bounds
    # Recursively check left and right subtrees with updated bounds
    return (is_valid_bst(node.left, low, node.val) and
            is_valid_bst(node.right, node.val, high))

def inorder_traversal(node, result):
    """
    Performs an in-order traversal of the tree to collect values in sorted order.
    
    Args:
    - node: The current tree node.
    - result: A list to store the in-order traversal result.
    """
    if node:
        inorder_traversal(node.left, result)  # Traverse left subtree
        result.append(node.val)                # Visit current node
        inorder_traversal(node.right, result) # Traverse right subtree

def check_bst_and_sorted(node):
    """
    Checks if the binary tree is a valid BST and returns its elements in sorted order.
    
    Args:
    - node: The root of the binary tree.
    
    Returns:
    - A tuple (is_valid, sorted_elements). 
      - is_valid: Boolean indicating if the tree is a valid BST.
      - sorted_elements: List of elements in sorted order if valid, else empty.
    """
    if is_valid_bst(node):
        sorted_elements = []
        inorder_traversal(node, sorted_elements)  # Collect sorted elements
        return True, sorted_elements
    return False, []  # Return false and empty list if not a valid BST

# Example usage:
root = TreeNode(2, TreeNode(1), TreeNode(3))  # Create a valid BST
is_bst, sorted_elements = check_bst_and_sorted(root)
print("Is valid BST:", is_bst)  # Output: True
print("Sorted elements:", sorted_elements)  # Output: [1, 2, 3]


#Task 2: Build a Max-Heap and Return Top-K Elements
import heapq  # Import heapq for heap operations

def build_max_heap(arr):
    """
    Builds a max-heap from an unsorted array.
    
    Args:
    - arr: The input unsorted array.
    
    Returns:
    - A list representing the max-heap.
    """
    # Negate the values to use Python's min-heap as a max-heap
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)  # Transform the list into a heap in-place
    return max_heap

def get_top_k_elements(arr, k):
    """
    Retrieves the top-K elements from the unsorted array using a max-heap.
    
    Args:
    - arr: The input unsorted array.
    - k: The number of top elements to return.
    
    Returns:
    - A list of the top-K elements in descending order.
    """
    # Check for valid k value
    if k <= 0 or k > len(arr):
        return []  # Return an empty list for invalid k
    
    max_heap = build_max_heap(arr)  # Build the max-heap from the array
    top_k = []  # List to store the top-K elements
    
    for _ in range(k):
        # Pop the largest element (negated back to original value) and add to top_k
        top_k.append(-heapq.heappop(max_heap))
    
    return top_k

# Example usage:
unsorted_array = [3, 1, 5, 12, 2]  # Input unsorted array
k = 3  # Number of top elements to retrieve
top_k_elements = get_top_k_elements(unsorted_array, k)
print("Top-K elements:", top_k_elements)  # Output: [12, 5, 3]