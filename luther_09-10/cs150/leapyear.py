def findLeapYear(year):
    if year%100==0:
        if year%400!=0:
            result = "false"
        else:
            result = "true"
    else:
        if year%4==0:
            result = "true"
        else:
            result = "false"

    return result

print(findLeapYear(1996))
print(findLeapYear(2000))
print(findLeapYear(1600))
print(findLeapYear(1700))
print(findLeapYear(1350))
print(findLeapYear(1433))
print(findLeapYear(2563))

