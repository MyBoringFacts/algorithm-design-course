def merge_and_count(arr, temp_arr, left, right):
    if left == right:
        return 0
    
    mid = (left + right) // 2
    inv_count = 0

    inv_count += merge_and_count(arr, temp_arr, left, mid)
    inv_count += merge_and_count(arr, temp_arr, mid + 1, right)
    inv_count += merge_and_merge(arr, temp_arr, left, mid, right)
    
    return inv_count

def merge_and_merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def count_inversions(arr):
    temp_arr = [0] * len(arr)
    return merge_and_count(arr, temp_arr, 0, len(arr) - 1)

# Input handling for multiple test cases
t = int(input().strip())  # number of test cases
ans=[]
input()
for _ in range(t):
    n = int(input().strip())  # size of array
    arr = []
    for _ in range(n):
        arr.append(int(input().strip()))  # input array elements
    input()  # blank line

    # Count inversions
    result = count_inversions(arr)
    
    ans.append(result)


for x in ans:
    print(x)


# note to self:
# How it works:
# merge_and_count: Recursively divides the array into two halves and counts inversions in each half.
# merge_and_merge: Merges the two halves and counts inversions that occur across them (when elements from the right half are smaller than elements from the left).
# count_inversions: This function initiates the merge sort and returns the total inversion count.

