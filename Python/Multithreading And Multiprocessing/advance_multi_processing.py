# multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"Square : {number*number}"

numbers = [i for i in range(6)]
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number,numbers)

    t = time.time()
    for i in results:
        print(i)
    finished_time = time.time() - t
    print(finished_time)