import random 
import sys
import time
from .factory import roundom_generator, insertionSort

import random 
import sys
import time


# Driver code to test above

#if __name__ == '__main__':
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    start_time = time.time()

    """if len(sys.argv) > 2:
        print("Too many parameters: You must specify array size to sort in digit e.g: 10.")
        sys.exit(1)       
    if len(sys.argv) < 2:
        print("You did not specify array size. Default size of 100 is assumed",end='\n')
        arr = 100
    else:
        arr = int(sys.argv[1])"""
    if not req:
       arr =100
    else:
        arr = int(req)
    
    size = roundom_generator(arr)
    print(size)

    size = insertionSort(size)
    #for i in range(size):
    #    print ("% d" % size[i])
    print(size)
    print("--- %s seconds ---" % (time.time() - start_time))