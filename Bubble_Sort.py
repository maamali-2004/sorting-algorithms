def bubble_sort(arr):
    l = len(arr)
    for i in range(l):
        swap = False
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if swap == False :
            break
    for i in arr:
        print(i, end=' ')
arr = list(map(int, input().split()))
bubble_sort(arr)