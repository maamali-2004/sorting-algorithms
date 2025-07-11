def insertion_sort(arr):
    l = len(arr)
    for i in range(1, l):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
    for i in arr:
        print(i, end=' ')
arr = list(map(int, input().split()))
insertion_sort(arr)