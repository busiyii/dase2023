import random
import time
import copy

# 选择排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

# 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [_ for _ in arr[1:] if _ <= pivot]
        right = [_ for _ in arr[1:] if _ > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

def random_array(length):
    return [random.randint(1, 1000) for _ in range(length)]


def test_sorting(length, n):
    selection_time = 0
    quick_time = 0

    for _ in range(n):
        arr = random_array(length)
        
        # 选择排序
        selection_arr = copy.deepcopy(arr)
        start_time = time.time()
        selection_sort(selection_arr)
        selection_time = time.time() - start_time

        # 快速排序
        quick_arr = copy.deepcopy(arr)
        start_time = time.time()
        quick_sort(quick_arr)
        quick_time = time.time() - start_time

    selection_time = selection_time / n
    quick_time = quick_time / n

    print(f"length: {length}")
    print(f"selection sort: {selection_time:.6f} s")
    print(f"quick sort: {quick_time:.6f} s")
    print()

if __name__ == "__main__":
    lengths = [1000, 5000, 10000]
    n = 10

    for length in lengths:
        test_sorting(length, n)

'''
快排远远快于选择排序
'''

