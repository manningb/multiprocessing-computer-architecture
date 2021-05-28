import math
import multiprocessing

def my_func(x):  
    s = math.sqrt(x)  
    return s

def my_func_verbose(x):
    s = math.sqrt(x)
    print("Task", multiprocessing.current_process(), x, s)
    return s


import time
import math
import multiprocess
from multiprocess import Pool
import random
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from timeit import default_timer as timer
import matplotlib.pyplot as plt

from functions import check_prime

# A function for timing a job that uses a pool of processes.
#  f is a function that takes a single argument
#  data is an array of arguments on which f will be mapped
#  pool_size is the number of processes in the pool. 
def pool_process(f, data, pool_size = multiprocess.cpu_count()):
    if __name__ == '__main__':
        with multiprocess.get_context('spawn').Pool(processes=pool_size) as pool:
            tp1 = time.time()
            print(data, pool_size)
#             pool = Pool(processes=pool_size) # initialize the Pool.
#             pool.set_context('spawn')
            result = pool.map(f, data)       # map f to the data using the Pool of processes to do the work 
            pool.close() # No more processes
            pool.join()  # Wait for the pool processing to complete. 
            print("Results", result)
            print("Overall Time:", int(time.time()-tp1))
            
            
dataRange = range(10)
pool_process(my_func_verbose, dataRange, 1)
