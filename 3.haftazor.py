import time
import csv
import random

def timer_decorator(func):
    def wrapper(arr):
        start_time = time.time()
        sorted_arr = func(arr)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} süresi: {elapsed_time:.5f} saniye")
        return sorted_arr
    return wrapper

@timer_decorator
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

@timer_decorator
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

@timer_decorator
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

@timer_decorator
def bogosort(arr):
    while not all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        random.shuffle(arr)
    return arr

def read_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return [float(row[0]) for row in reader]

def write_data(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for value in data:
            writer.writerow([value])

def main():
    data = read_data('data.csv')
    
    for sort_func in [bubble_sort, insertion_sort, selection_sort, bogosort]:
        sorted_data = sort_func(data[:])
        write_data(f'sorted_{sort_func.__name__}.csv', sorted_data)

if __name__ == "__main__":
    main()
