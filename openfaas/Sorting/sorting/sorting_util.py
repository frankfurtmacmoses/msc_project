import random 
import sys
import time

def roundom_generator(size ):
    arr = [random.randrange(1, size) for i in range(1,size)]
    return arr

 
# Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr
    

 
# Driver code to test above

if __name__ == '__main__':
    start_time = time.time()
    size = roundom_generator(arr)
    sorted = insertionSort(size)
    print(json.size)
    print("Completed in seconds: " + (time.time() - start_time))