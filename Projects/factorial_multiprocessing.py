# find larger factorial

import multiprocessing
import sys
import math
import time

# Increase maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorial of number

def compute_factorial(number):
    print(f"Coumputing factorial of a {number}")
    factorial = math.factorial(number)
    print(f"Factorial of a {number} is {factorial}")
    return factorial

if __name__ == "__main__":
    numbers=[5000,6000,7000,8000]
    start_time = time.time()

    #create pool of work processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial,numbers)
    
    end_time = time.time()

    print(f"Results : {results}")
    print(f"Taken Time : {end_time-start_time} seconds")