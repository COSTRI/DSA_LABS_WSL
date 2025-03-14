#ASSIGNMENT 1815522
#Question: Solve and analyze the time complexity of each solution using O_notation.

#1.Finding the Maximum Element in array

def find_max(arr):
    if not arr:
        return None #Handle the case of an empty array
    max_element = arr[0] #assume the first element is the maximum
    for num in arr:
        if num > max_element:
            max_element = num #update max_element if a larger number is found
    return max_element

#Time complexity is O(n). The function performs a single travesal of the array, examining each element exactly once.
#Thus, the time taken grows linearly with sixe of the array(n).




#2.Counting the Occurrences of a Target Element in an array.
def count_occurrences(arr, target):
    count = 0 #initial count of 0
    for num in arr:
        if num == target:
            count += 1 #Increment count when the target is found
            return count

#Time complexity is O(n). The function performs a single pass through the array.
#The time taken increases directly with the number of elements(n).



#3.Checking if an array is Sorted.
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]: #compare each element with the next
         return False #If any element is greater than the next, it's not sorted
    return True # if no such element is found, the array is sorted

#Time complexity is O(n).
#The function makes a single pass through the array until it finds an unsorted pair or reaches the end.