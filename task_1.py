import timeit
from numpy import random

# Генерація масиву
arr = random.randint(10000, size=10000)  # NumPy-масив

# Сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Сортування вставками
def insertion_sort(lst):
    lst = lst.copy()
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

def main():
    list_for_merge = arr.tolist()
    list_for_insertion = arr.tolist()
    list_for_sorted = arr.tolist()

    time_taken_merge_sort = timeit.timeit(lambda: merge_sort(list_for_merge), number=1)
    print(f"Час виконання сортування злиттям: {time_taken_merge_sort:.4f} секунд")

    time_taken_insertion_sort = timeit.timeit(lambda: insertion_sort(list_for_insertion), number=1)
    print(f"Час виконання вставками: {time_taken_insertion_sort:.4f} секунд")

    time_taken_numpy_sort = timeit.timeit(lambda: arr.copy().sort(), number=1)
    print(f"Час виконання NumPy sort(): {time_taken_numpy_sort:.4f} секунд")

    time_taken_builtin_sorted = timeit.timeit(lambda: sorted(list_for_sorted), number=1)
    print(f"Час виконання built-in sorted(): {time_taken_builtin_sorted:.4f} секунд")

if __name__ == "__main__":
    main()

# Результат виконання 1
# Час виконання сортування злиттям: 0.0023 секунд
# Час виконання вставками: 0.0265 секунд
# Час виконання NumPy sort(): 0.0031 секунд
# Час виконання built-in sorted(): 0.0001 секунд

# Результат виконання 2
# Час виконання сортування злиттям: 0.0297 секунд
# Час виконання вставками: 2.6829 секунд
# Час виконання NumPy sort(): 0.0001 секунд
# Час виконання built-in sorted(): 0.0014 секунд

# Результат виконання 3
# Час виконання сортування злиттям: 0.0349 секунд
# Час виконання вставками: 2.8901 секунд
# Час виконання NumPy sort(): 0.0001 секунд
# Час виконання built-in sorted(): 0.0014 секунд