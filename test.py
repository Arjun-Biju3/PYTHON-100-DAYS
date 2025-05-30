def armstrong(num):
    power = len(str(num))
    sum = 0
    for i in str(num):
        sum +=  int(i)**power
    return num == sum

print(armstrong(9474))