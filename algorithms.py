def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False;
        for j in range(0, n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n): # i = insert index
        currentElement = arr[i] # element to insert
        j = i - 1
        while j >= 0 and (currentElement < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = currentElement
    return arr

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while(i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot] # all values smaller than pivot
    middle = [x for x in arr if x == pivot] # all values equal to pivot
    right = [x for x in arr if x > pivot] # all values greater than pivot
    return quicksort(left) + middle + quicksort(right)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    target = 25

    print(f"Input:         {arr}")
    print(f"Bubble sort:   {bubble_sort(arr[:])}")
    print(f"Insertion sort:{insertion_sort(arr[:])}")
    print(f"Merge sort:    {merge_sort(arr)}")
    print(f"Quick sort:    {quicksort(arr)}")
    print(f"Linear search: index {linear_search(arr, target)} for target {target}")
    print(f"Binary search: index {binary_search(quicksort(arr), target)} for target {target}")