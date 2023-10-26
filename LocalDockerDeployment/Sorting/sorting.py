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

    if len(sys.argv) > 2:
        print("Too many parameters: You must specify array size to sort in digit e.g: 10.")
        sys.exit(1)       
    if len(sys.argv) < 2:
        print("You did not specify array size. Default size of 100 is assumed",end='\n')
        arr = 100
    else:
        arr = int(sys.argv[1])
    size = roundom_generator(arr)
    print(size)

    size = insertionSort(size)
    #for i in range(size):
    #    print ("% d" % size[i])
    print(size)
    print("--- %s seconds ---" % (time.time() - start_time))