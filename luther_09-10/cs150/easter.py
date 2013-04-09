#Scott Gerike
#CS150
#10/12/09
#Computes the date for easter for any year from 1900 to 2099

def computeEaster(year):
    a = year%19
    b = year%4
    c = year%7
    d = (19*a+24)%30
    e = (2*b+4*c+6*d+5)%7

    easter = (22+d+e)

    if year>1900 and year<2099:
        if year==1954 or year==1981 or year==2049 or year==2076:
            easter = easter - 7
        if easter>31:
            easter = easter - 31
            print("Easter is on April",easter)
        else:
            print("Easter is on March",easter)
    else:
        print("The year is out of the range ... input another year")

def main():
    year = int(input("Enter a year(between 1900 and 2099): "))
    computeEaster(year)


main()
