def longest(arr):
    maximum = 0
    stack = [-1]
    for i in range(len(arr)):
        if arr[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                maximum = max(maximum,i-stack[-1])
    return maximum

a = "(()((())()))"
print(longest(a))