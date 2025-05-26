import heapq
import timeit

# метод черги пріритетів для злиття та сортування списків
def merge_k_lists(lists):
    min_heap = []
    
    # Ініціалізуємо heap з перших елементів кожного списку
    for i, lst in enumerate(lists):
        if lst:  # Якщо список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента у списку)

    result = []

    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)

        # Якщо є наступний елемент у цьому списку — додати до heap
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))

    return result

def merge_two_lists(l1, l2):
    result = []
    i = j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result.extend(l1[i:])
    result.extend(l2[j:])
    return result

# Метод рекурсивним злиттям парами
def merge_k_lists_sort(lists):
    if not lists:
        return []

    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i + 1 < len(lists) else []
            merged.append(merge_two_lists(l1, l2))
        lists = merged

    return lists[0]

def use_sum_and_sort(lists):
    merged = sum(lists, [])  # об'єднує всі підсписки в один
    merged.sort()
    print("Відсортований список:", merged)

def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    time_taken_merge_k_list = timeit.timeit(lambda: merge_k_lists(lists), number=1)
    print(f"Час виконання сортування злиттям з чергою пріоритетів: {time_taken_merge_k_list:.4f} секунд")

    time_taken_merge_two_lists = timeit.timeit(lambda: merge_k_lists_sort(lists), number=1)
    print(f"Час виконання сортування рекурсивним злиттям парами: {time_taken_merge_two_lists:.4f} секунд")

    time_taken_use_sum_and_sort = timeit.timeit(lambda: use_sum_and_sort(lists), number=1)
    print(f"Час виконання стандартними методами: {time_taken_use_sum_and_sort:.4f} секунд")


if __name__ == "__main__":
    main()

# Час виконання сортування злиттям з чергою пріоритетів: 0.0000 секунд
# Час виконання сортування рекурсивним злиттям парами: 0.0000 секунд
# Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
# Час виконання стандартними методами: 0.0006 секунд