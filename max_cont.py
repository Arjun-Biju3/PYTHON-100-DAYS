def maximumSubarray(num):
    current_max = num[0]
    max_soo_far = num[0]
    for i in range(1,len(num)):
        current_max = max(num[i],current_max+num[i])
        max_soo_far = max(max_soo_far,current_max)
    return max_soo_far

print(maximumSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))