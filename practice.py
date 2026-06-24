arr = [10, 25, 7, 89, 45]
print("Maximum element:", max(arr))

arr = [10, 20, 4, 45, 99]

arr = sorted(arr)

print("Second largest element:", arr[-2])
print("third largest element:", arr[-3])

arr=[2,3,4,5,6,7,89]

left=0
right=len(arr)-1

while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1

print(arr)

def longest_contiguous(arr):
    if not arr:
        return 0

    max_len = 1
    curr_len = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            curr_len += 1
        else:
            curr_len = 1

        max_len = max(max_len, curr_len)

    return max_len

# Example
arr = [1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
print(longest_contiguous(arr))

def pushZerosToEnd(arr):

    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1


if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num, end=" ")



def remove_duplicates(arr):
    n = len(arr)

    if n == 0:
        return 0

    j = 0  # Index for distinct elements

    for i in range(1, n):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]

    return j + 1  # Length of distinct sorted subarray


# Example
arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
length = remove_duplicates(arr)

print("Length:", length)
print("Distinct sorted subarray:", arr[:length])       





def find_duplicate_missing(arr):
    n = len(arr)
    seen = set()

    duplicate = -1

    for num in arr:
        if num in seen:
            duplicate = num
        else:
            seen.add(num)

    for i in range(1, n + 1):
        if i not in seen:
            missing = i
            break

    return duplicate, missing


# Example
arr = [1, 3, 4, 5,6, 6, 2]

duplicate, missing = find_duplicate_missing(arr)

print("Duplicate Number:", duplicate)
print("Missing Number:", missing)
