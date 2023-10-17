def bubble_sort(a: list, n: int) -> None :
    totalSwaps = 0
    for _ in range(n):
        noOfSwaps = 0
        for j in range(n-1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                noOfSwaps += 1
        totalSwaps+=noOfSwaps
        if (noOfSwaps == 0):
            break
    
    print(f'Array is sorted in {totalSwaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[n-1]}')

def rotLeft(a: list, d: int) -> list:
    for _ in range(d):
        tmp = a.pop(0)
        a.append(tmp)
    return a    

def minimumSwaps(arr: list) -> int:
    noOfSwaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            arr[arr.index(i+1)] = arr[i]
            arr[i] = i+1
            noOfSwaps+=1
    return noOfSwaps        

# Optimal solution
def minimum_swaps(arr: list) -> int:
    nswaps = 0
    for i in range(len(arr)):
        while arr[i] != i+1:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            nswaps+=1            
    return nswaps  