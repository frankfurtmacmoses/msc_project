from .sorting_util import roundom_generator
from .sorting_util import insertionSort
import sys
import time
import json

def handle(req):
    start_time = time.time()
    """handle a request to the function
    Args:
        req (str): request body
    """
    req = {}
    unsortedarray = roundom_generator(10000)
    sortedarray = insertionSort(unsortedarray)
    req = {"sortedarray": sortedarray , "Completed in seconds ": (time.time() - start_time)}
    print(req)