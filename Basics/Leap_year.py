#Check if a year is a leap year
y = int(input("Enter any year: "))
if (y % 4 ==0 and y % 100 != 0) or y % 400 == 0:
    print(y, " is leap year")
else:
    print(y, " is not leap year")