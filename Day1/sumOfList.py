def sumOfList(l1,l2):
    number1 = ""
    number2 = ""
    result = []
    if len(l1) == 0 and len(l2) == 0:
        return []
    for i in l1:
        number1 += str(i)
    for j in l2:
        number2 += str(j)
    total = str(int(number1) + int(number2))
    for k in total:
        result.append(k)
    return result


l1 = [0,0,4]
l2 = [9,9,6]

answer = sumOfList(l1,l2)
print(answer)

