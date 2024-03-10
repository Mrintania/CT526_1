import random
import time
import matplotlib.pyplot as plt
import numpy as np

# numpy = []
# for i in range(1000):
#     number = random.randint(1, 100000)
#     numpy.append(number)
# print(numpy[0:100])
# print("Before")
#
# plt.plot(numpy[0:100])
# plt.show()
#
# start = time.time()
# bubble_sort_asc = []
# for i in range(len(numpy)):
#     for j in range(len(numpy) - 1):
#         if numpy[j] > numpy[j + 1]:
#             numpy[j], numpy[j + 1] = numpy[j + 1], numpy[j]
#     bubble_sort_asc.append(numpy.copy())
# print("Bubble Sort น้อยไปมาก")
# print(numpy[0:100])
#
# end = time.time()
# print("Time: ", end - start, "s")
# print("After")
#
# plt.plot(numpy[0:100])
# plt.show()

# sort the list น้อยไปมาก ด้วย quick sort เก็บในตัวแปรที่ชื่อ quick_sort_asc
numpy_quick = []
numpy_bubble = []
for i in range(1000):
    number = random.randint(1, 100000)
    numpy_quick.append(number)
    numpy_bubble.append(number)
print(numpy_quick[0:100])
print(numpy_bubble[0:100])

start_time_quick_sort_asc = time.time()
# Quick Sort น้อยไปมาก ไม่ใช้ Library
quick_sort_asc = []


def quick_sort_asc_func(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort_asc_func(less) + [pivot] + quick_sort_asc_func(greater)


quick_sort_asc = quick_sort_asc_func(numpy_quick)
print("Quick Sort น้อยไปมาก")
print(quick_sort_asc[0:100])
end_time_quick_sort_asc = time.time()
time_quick_sort_asc = end_time_quick_sort_asc - start_time_quick_sort_asc
print("Time: ", time_quick_sort_asc, "s")
# End of Quick Sort

plt.plot(quick_sort_asc[0:100])
plt.show()
# End of Quick Sort

start_time_bubble_sort_asc = time.time()
# Bubble Sort น้อยไปมาก
bubble_sort_asc = []
for i in range(len(numpy_bubble)):
    for j in range(len(numpy_bubble) - 1):
        if numpy_bubble[j] > numpy_bubble[j + 1]:
            numpy_bubble[j], numpy_bubble[j + 1] = numpy_bubble[j + 1], numpy_bubble[j]
    bubble_sort_asc.append(numpy_bubble.copy())
print("Bubble Sort น้อยไปมาก")
print(numpy_bubble[0:100])
end_time_bubble_sort_asc = time.time()
time_bubble_sort_asc = end_time_bubble_sort_asc - start_time_bubble_sort_asc
print("Time: ", time_bubble_sort_asc, "s")
# End of Bubble Sort

plt.plot(numpy_bubble[0:100])
plt.show()

