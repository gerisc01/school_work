#Scott Gerike
#CS150
#10/16/09
#Computing the Initials of a String of Words

def computeInitials(aname):
    result = aname[0]
    for index in range(len(aname)):
        if aname[index] == " ":
            name = index + 1
            name = aname[name]
            result = result + name
    return result

def main():
    aname = input("Please enter a name: ")
    print(computeInitials(aname))
    

main()

