def selection_sort(arr):
    l = len(arr)
    for i in range(l-1):
        min_idx = i
        for j in range(i+1, l):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    for i in arr:
        print(i, end=' ')
arr = list(map(int, input().split()))
selection_sort(arr)