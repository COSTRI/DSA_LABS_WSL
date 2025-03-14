#Array implementation of python

class Array:
    def __init__(self):
        self.array = [] 
        #initializes the array class
        #init sets up an empty list for self.array to store


    def insert(self, element) :
        self.array.append(element)
        #insert adds an element to the end of an array using the append method


    def remove(self,element):
        if element in self.array:
            self.array.remove(element)
            #removes an element if it exists


    def get(self, index):
        if index < len (self.array):
            return self.array[index]
        else:
            return None
        #returns a specific element within bounds, if not present it returns None
        

    def size(self):
        return len(self.array)
    #returns number of elements
    

    def display(self):
        print(self.array)
        #prints current elements present in array


 #Example Usage
arr = Array()
arr.insert(1)
arr.insert(2)
arr.insert(4)
arr.display() #output[1,2,4]
arr.remove(4)
arr.display() #output[1,2]
print(arr.get(1)) #2
print(arr.size()) #2


#Implentation of Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None


    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
#insert method, creates a new node with given data,sets its pointer to the cureent head of the list

    def remove(self, data):
        current = self.head
        prev = None

        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
            #removes the first node with specified data.
            #iterates through the list,keeping track of the current node and the previous
            #if wanted node is found,it is updates

    def display(self):
        current = self.head
        while current:
            print(current.data, end="-> ")
            current = current.next
        print("None")
        #prints the data of each node in the list followwed by anarrow
        #ends with None to indicate the end
       
    def size(self):
         count = 0
         current = self.head
         while current:
            count += 1
            current = current.next
         return count
    #counts number of nodes in the list bu iterating through the list, increment by one

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        current = self.head
        prev = None

        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    
    # Inserting elements into the linked list
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    
    # Display the linked list
    print("Linked List after inserting elements:")
    linked_list.display()  # Output: 30 -> 20 -> 10 -> None
    
    # Removing an element from the linked list
    linked_list.remove(20)
    
    # Display the linked list after removal
    print("Linked List after removing 20:")
    linked_list.display()  # Output: 30 -> 10 -> None

    # Size of the linked list
    print("Size of linked list:", linked_list.size())  # Output: 2

    # Removing another element
    linked_list.remove(30)

    # Display the linked list after removing another element
    print("Linked List after removing 30:")
    linked_list.display()  # Output: 10 -> None

    # Final size of the linked list
    print("Final size of linked list:", linked_list.size())  # Output: 1

