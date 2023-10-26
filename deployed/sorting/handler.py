import random 
import sys
import time
from .factory import roundom_generator, insertionSort


def handle(req):
    
    #if __name__ == '__main__':
    start_time = time.time()
   
    if not req:
        req = 100

     
    else:
        arr = int(req)
        size = roundom_generator(arr)
        print(size, end="\n")
        print("------------------------------------Sorting------------------------------------",end="\n")
        size = insertionSort(size)
        #for i in range(size):
        #    print ("% d" % size[i])
        print(size)
        print("--- %s total seconds ---" % (time.time() - start_time))
        return req
        
