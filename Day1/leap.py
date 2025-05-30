def check(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False  

year = int(input("Enter year to search:"))
print(check(year))
if check(year):
    check(f"{year} is leap")
else:
    print(f"{year} is not leap")

