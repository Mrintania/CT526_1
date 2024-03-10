import random
import time
import matplotlib.pyplot as plt
import numpy as np

numpy_quick = []
numpy_bubble = []
for i in range(1000):
    number = random.randint(1, 100000)
    numpy_quick.append(number)
    numpy_bubble.append(number)
print(numpy_quick[0:100])
print(numpy_bubble[0:100])

print(np.array_equal(numpy_quick, numpy_bubble))

start_time_bubble_sort_asc = time.time()

bubble_sort_asc = []
for i in range(len(numpy_bubble)):
    for j in range(len(numpy_bubble) - 1):
        if numpy_bubble[j] > numpy_bubble[j + 1]:
            numpy_bubble[j], numpy_bubble[j + 1] = numpy_bubble[j + 1], numpy_bubble[j]
    bubble_sort_asc.append(numpy_bubble.copy())

end_time_bubble_sort_asc = time.time()

time_bubble_sort_asc = end_time_bubble_sort_asc - start_time_bubble_sort_asc

print("Time: ", time_bubble_sort_asc, "s")

start_time_quick_sort_asc = time.time()


def quick_sort_asc_func(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort_asc_func(less) + [pivot] + quick_sort_asc_func(greater)


quick_sort_asc = quick_sort_asc_func(numpy_quick)

end_time_quick_sort_asc = time.time()

time_quick_sort_asc = end_time_quick_sort_asc - start_time_quick_sort_asc
print("Time: ", time_quick_sort_asc, "s")

print(np.array_equal(sorted(numpy_bubble), quick_sort_asc))

