def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [2,11,4,7,6,8,9,12,10]
sorted_arr = insertion_sort(arr)
print(sorted_arr)
