import random
import time
import matplotlib.pyplot as plt
import numpy as np

# compare the time of bubble sort and quick sort
numpy = []
for i in range(1000):
    number = random.randint(1, 1000000)
    numpy.append(number)

# สร้างตัวแปรสำหรับเก็บเวลาที่ใช้ในการเรียงลำดับข้อมูล น้อยไปมาก ด้วย bubble sort
# เก็บในตัวแปรที่ชื่อ bubble_sort_asc_time_compare
time_bubble_sort_asc = np.sort(numpy)
# Bubble Sort
start = time.time()
bubble_sort_asc = np.sort(numpy)
end = time.time()
print("Time: ", end - start, "s")
# End of Bubble Sort

start = time.time()
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


quick_sort_asc = quick_sort_asc_func(numpy)
print("Quick Sort น้อยไปมาก")
print(quick_sort_asc[0:100])
end = time.time()
time_quick_sort_asc = end - start
# End of Quick Sort

# นำเวลาที่ใช้ในการเรียงลำดับข้อมูล น้อยไปมาก ของ bubble sort และ quick sort มาเปรียบเทียบกัน
# โดยใช้กราฟแท่ง
# และเก็บไว้ในไฟล์ชื่อ time_compare.png
# โดยใช้คำสั่ง plt.bar
plt.bar("Bubble Sort", time_bubble_sort_asc)
plt.bar("Quick Sort", time_quick_sort_asc)
# plt.savefig('time_compare.png')
plt.show()

# ตรวจสอบว่าเรียงลำดับข้อมูล น้อยไปมาก ของ bubble sort และ quick sort ถูกต้องหรือไม่
# โดยใช้คำสั่ง np.array_equal
print(np.array_equal(bubble_sort_asc, quick_sort_asc))


