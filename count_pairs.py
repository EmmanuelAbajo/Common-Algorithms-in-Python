def count_pairs(num, k):
    if k == 0:
        return len(num)
    count = 0
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] + num[j] == k:
                count+=1
    return count if count != 0 else -1


