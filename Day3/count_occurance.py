def count_elements(arr):
    occurance = {}
    for i in arr:
        if i in occurance:
            occurance[i] = occurance[i]+1
        else:
            occurance[i] = 1
    return occurance
print(count_elements([1,8,4,5,3,2,1,5, 2, 2, 3, 3, 3]))