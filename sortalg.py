def bubble_sort(a: list, n: int) -> None :
    totalSwaps = 0
    for _ in range(n):
        noOfSwaps = 0
        for j in range(n-1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                noOfSwaps = noOfSwaps + 1
        totalSwaps = totalSwaps + noOfSwaps
        if (noOfSwaps == 0):
            break
    
    print(f'Array is sorted in {totalSwaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[n-1]}')

