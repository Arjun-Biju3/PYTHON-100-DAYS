def checkLeap(year):
    if year % 4 == 0:
        if year % 400 != 0:
            return True
    return False    

year = int(input("Enter year to search:"))
print(checkLeap(year))
if checkLeap(year):
    print(f"{year} is leap")
else:
    print(f"{year} is not leap")

