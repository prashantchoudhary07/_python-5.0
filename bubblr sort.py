def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr=[11,2,3,8,5,6,7,3,9,10]
sorted_arr = bubble_sort(arr)
print(sorted_arr)
