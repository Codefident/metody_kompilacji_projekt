T = [5, 1, 2, 8, 7, 6, 3, 9, 1, 1, 8, 7, 7, 1, 3, 3, 2]


def countingSort(T, k):

    n = len(T)

    # tablica do zliczania
    C = []
    for _ in range(k):
        C.append(0)

    # przepisujemy tam posortowane dane
    B = []
    for _ in range(n):
        B.append(0)


    # zliczamy liczbę wystąpień
    for x in T:
        C[x] += 1

    # robimy tak aby kolejne liczby zawierały
    # swoją liczbę wystąpień +
    # liczbę wystąpień poprzedników
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    
    for i in range(n-1, -1, -1):
        B[ C[ T[i] ] - 1 ] = T[i]
        C[ T[i] ] -= 1
    
    # dodatkowo - przepisanie do T[]
    for i in range(n):
        T[i] = B[i]


countingSort(T, 10)
print(T)