year = int(input("Enter a year: "))
leap = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
result = "Leap year" if leap else "Not a leap year"
print(result)
