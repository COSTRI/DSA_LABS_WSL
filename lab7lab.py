#Graph
#class Node:
 #   def __init__(self, key):
  #      self.key = key
   #     #initializing key to 0

    #def __init__(self, n):
     #   self.capacity = n
      #  self. population = 0
       # self.arr = [None] #ghelping us keep track of the data
        #self. amatrix =[[0]*n]*5

    #def addNode(self):#to help us add data
     #   self.arr[self.population] = Node(self.pop)

 #we need a funtion that would A and B, that woud help us match the matrix,  amatrix[A.key][B.key] = 1

    #def Relate(self, A, B):
     #   self.amatrix[A.key][B.key] = 1
        #using the relate and line 19 would 


#BINARY SEARCH TREE
#left=[0], m= (l + R)/2,, R=[n], is arr[m] > what youre trying to find? if true set the R = m-1, if lesser
#integer division ignores any decimal, it gives you  the lower bound of the num

  #def bSearch(arr, element):
   #right = len (arr)
    #left = 0
    #while (left < right):
     # m =(left + right) // 2
      #if arr[m] is element:
       # return m
    #def arr[m] > element:
     #       right = m -1


#class TrieNode:
 #   def __init__(self):
  #      children = {}
   #     is_end = False

#class Trie:

 #def __init__(self):
  #      self.root = Trie.Node()

   # def insert(self, word):
    #    for char in word:
     #       if char not in


# def unordered_linear_search(A, n, data):
    #for i in range(n):
        #if A[i] == data:
            #return i
#return -1


# def ordered_linear_search(A, n, data):
    #for i in range(n):
        #if A[i] == data:
            #return i
    #elif A[i] > data:
            #return -1
#return -1

#def binary_search_iterative(A, n, data):
 #   low = 0
  #  high = n - 1
#
 #   while low <= high:
  #      mid = low + (high - low) // 2 
#
 #       if A[mid] == data:
  #          return mid
   #     
    #    elif A[mid] < data:
     #       low = mid + 1
#
 #       else:
  #          high = mid -1

   # return -1

#def binary_search_recursive(A, n, data):
 #   if low > high:
  #      return -1
    
   # mid = low + (high - low) // 2

    #if A[mid] == data:
     #   return mid
    #elif A[mid] < data:
     #   return binary_search_recursive(A, mid + 1, high, data)
    #else:
     #   return binary_search_recursive(A, low, mid - 1, data)


#def brute_force_string_match(T, n, P, m):
    #for i in range(n - m + 1):
     #   j = 0
      #  while j < m and P[j] == T[i + j]:
       #     j += 1
        #if j == m: #if we match all chracters successfully
         #   return i
    #return -1

#class TrieNode:
 #   def __init__(self,data):
  #      self.data = data #character storedin the node
   #     self.is_end_of_string = False #idicates this node marks the end of striing
    #    self.child = [None]*26 #array of 26 pointers;alphabets
#
 #   def search_in_trie(root, word):
  #      if root is None:
   #         return -1
    #    
     #   if not word:
      #      if root.is_end_of_string:
       #         return 1
        #    else:
         #       return -1
            
        #if root.data == word[0]:
         #   return search_in_trie(root.children[ord(word[0])], word[1:])
        #else:
         #   return -1



#class TSTNode:
    #def __init__(self, data):
        #self.data = data
        #self.is_end_of_string = False
       # self.left = None
      #  self.eq = None
     #   self.right = None

    #def insert_in_tst(root, word):
        #if root is None:
            #root = TSTNode(word[0])
            #if len(word) == 1:
           #     root.is_end_of_string = True

        ##if word[0] < root.data:
          #  root.left = insert_in_tst(root.left, word) # type: ignore
       # elif word[0] > root.data:
      #      root.right = insert_in_tst(root.right, word) # type: ignore
     #   else:
    #        if len(word) > 1:
   #             root.eq = insert_in_tst(root.eq, word[1:]) # type: ignore # type : ignore
  #          else:
 #               root.is_end_of_string = True
#
      #  return root
    ##
    #def search_in_tst_recursive(root, word):
        #if root is None:
        #    return -1
       # if word[0] < root.data:
      #      return search_in_tst_recursive(root.left, word)
     #   elif word[0] > root.data:
    #     return search_in_tst_recursive(root.right, word)
   #     else:
  #          if root.is_end_of_string and len(word) == 1:
 #return 1
 #elif len(word) > 1:
 #return search_in_tst_recursive(root.eq, word[1:])
 #else:
 #return -1