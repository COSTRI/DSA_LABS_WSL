def bubble_sort(arr): #the function takes arr as input
    n = len(arr)#n = length of the list
    for i in range(n):#outer loop runs n times, i is the pass through the list
        for j in range(0, n-i-1):#inner loop iterates through the unsorted list.
            #j goes from 0 to n-i-1, as the last i elements are already sorted
            if arr[j] > arr[j+1]:
                #this compares adjacent elements and swaps them if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)
# Output: Sorted array is: [11, 12, 22, 25, 34, 64, 90]



#INSERTION SORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        #outer loop starts from the second element, i=1, and iterates through the list
        key = arr[i] #current element being inserted
        j = i-1 #index of last element in the sorted part of the list
        while j >=0 and key < arr[j] :
                #inner loop compares the key with elements in the sorted part of the list
                #shifts elements to the right to make space for the key
                arr[j + 1] = arr[j]
                j -= 1
                #loop continues until j = -1 or key is greater than the element being compared
        arr[j + 1] = key
        #inserts the key in the correct position

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sorted array is:", arr)
# Output: Sorted array is: [11, 12, 22, 25, 34, 64, 90]


#MERGE SORT
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid] #divides the list into two halves
        R = arr[mid:]
        #splits the list into two halves
        merge_sort(L) 
        merge_sort(R)
        #recursively sorts the two halves
        i = j = k = 0
        #initializes variables for the loop
        #i = index of the left half, j = index of the right half, k = index of the original list
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                #compares the first elements of the two halves
                #merges the two halves by comparing elements
                arr[k] = L[i]
                #copies the smaller element to the original list
                i += 1 #increments the index of the left half
            else:
                arr[k] = R[j]
                j += 1
            k += 1 #increments the index of the original list
            #copies the smaller element to the original list
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            #copies the remaining elements of the left half
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            #copies the remaining elements of the right half


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print("Sorted array is:", arr)
# Output: Sorted array is: [11, 12, 22, 25, 34, 64, 90]