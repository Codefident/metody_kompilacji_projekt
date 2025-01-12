T = [0.12, 0.77, 0.45, 0.66, 0.28, 0.97, 0.22, 0.32, 0.01, 0.69]


def insertionSort(arr):
    for i in range(1, len(arr)):
        up = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > up:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = up
    return arr


def bucketSort(T):

    n = len(T)
    BUCKETS = 10
    B = []
    for _ in range(BUCKETS):
        B.append([])

    for x in T:
        index = int(x * BUCKETS)
        B[index].append(x)
    
    for i in range(BUCKETS):
        B[i] = insertionSort(B[i])

    k = 0
    for i in range(BUCKETS):
        for j in range(len(B[i])):
            T[k] = B[i][j]
            k += 1


bucketSort(T)
print(T)