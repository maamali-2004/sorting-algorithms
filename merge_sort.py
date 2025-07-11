def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right -  mid
    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2
    # Copy data to temporary arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[left + i]
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]
    i, j = 0 , 0
    k = left
    # Merge the temporary arrays back into arr[l..r]
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # Copy the remaining elements of L[] if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    # Copy the remaining elements of R[] if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
arr = list(map(int, input().split()))
merge_sort(arr, 0, len(arr)-1)
for i in arr:
    print(i, end= ' ')