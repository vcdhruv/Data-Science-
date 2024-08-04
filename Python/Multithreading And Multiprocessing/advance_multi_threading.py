# multithreading with thread pool executor
from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number : {number}"

numbers = [i for i in range(20)]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number,numbers)

t = time.time()
for i in results:
    print(i)
finished_time = time.time() - t
print(finished_time)