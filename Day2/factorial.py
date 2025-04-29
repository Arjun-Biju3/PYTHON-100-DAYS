def factorial(num):
    fact= 1
    if num == 0 or num == 1:
        return 1
    for i in range(1,num+1):
        fact = fact*i
    return fact

result = factorial(6)
print("Factorial is :",result)