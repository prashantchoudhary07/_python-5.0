def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            print("element found at index:", i)
            return i
        else:
            print("element not found at index:", i)

arr = [11,3,4,5,6,7,19,10,16]
target = 5
linear_search(arr, target)
