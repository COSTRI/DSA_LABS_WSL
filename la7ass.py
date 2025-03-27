#1815522
# A Ternary Search Tree (TST) is a data structure used to store a set of strings. It is similar to a binary search tree, but with three children for each node instead of two. The middle child contains the next character of the string being stored, while the left and right children contain characters that are less than and greater than the current character, respectively.
class TSTNode:
    def __init__(self, char):
        """
        Initialize a node in the Ternary Search Tree.

        :param char: The character stored in this node.
        """
        self.char = char  # Character at this node
        self.left = None  # Pointer to the left child
        self.middle = None  # Pointer to the middle child
        self.right = None  # Pointer to the right child
        self.is_end_of_word = False  # Indicates if this node marks the end of a word


class TernarySearchTree:
    def __init__(self):
        """
        Initialize the Ternary Search Tree.
        """
        self.root = None  # The root of the TST

    def insert(self, word):
        """
        Insert a word into the Ternary Search Tree.

        :param word: The word to be inserted.
        """
        if word:  # Ensure the word is not empty
            self.root = self._insert_recursive(self.root, word, 0)

    def _insert_recursive(self, node, word, index):
        """
        Recursive helper function to insert a word into the TST.

        :param node: The current node in the TST.
        :param word: The word being inserted.
        :param index: The current character index in the word.
        :return: The updated node.
        """
        char = word[index]  # Get the current character of the word

        # If the current node is None, create a new node for the character
        if node is None:
            node = TSTNode(char)

        # Compare the character with the current node's character
        if char < node.char:
            # Go to the left subtree if the character is smaller
            node.left = self._insert_recursive(node.left, word, index)
        elif char > node.char:
            # Go to the right subtree if the character is larger
            node.right = self._insert_recursive(node.right, word, index)
        else:
            # Move to the middle subtree if the character matches
            if index + 1 < len(word):
                # If there are more characters in the word, continue down the middle
                node.middle = self._insert_recursive(node.middle, word, index + 1)
            else:
                # Mark the end of the word if this is the last character
                node.is_end_of_word = True

        return node  # Return the updated node

    def search(self, word):
        """
        Search for a word in the Ternary Search Tree.

        :param word: The word to be searched.
        :return: True if the word exists, False otherwise.
        """
        if word:  # Ensure the word is not empty
            return self._search_recursive(self.root, word, 0)
        return False  # Return False for empty words

    def _search_recursive(self, node, word, index):
        """
        Recursive helper function to search for a word in the TST.

        :param node: The current node in the TST.
        :param word: The word being searched.
        :param index: The current character index in the word.
        :return: True if the word exists, False otherwise.
        """
        if node is None:
            return False  # Base case: reached a null node

        char = word[index]  # Get the current character of the word

        # Compare the character with the current node's character
        if char < node.char:
            # Go to the left subtree if the character is smaller
            return self._search_recursive(node.left, word, index)
        elif char > node.char:
            # Go to the right subtree if the character is larger
            return self._search_recursive(node.right, word, index)
        else:
            # Move to the middle subtree if the character matches
            if index + 1 == len(word):
                # If this is the last character, check if it's the end of a word
                return node.is_end_of_word
            # Continue searching for the next character in the middle subtree
            return self._search_recursive(node.middle, word, index + 1)


# Example usage
if __name__ == "__main__":
    tst = TernarySearchTree()

    # List of words to insert into the TST
    words_to_add = ["cat", "bat", "batman", "bats", "dog"]
    for word in words_to_add:
        tst.insert(word)

    # Search for words in the TST
    search_words = ["bat", "batman", "bats", "cat", "cattle", "dog"]
    for word in search_words:
        result = tst.search(word)
        print(f"Is '{word}' in TST? {result}")