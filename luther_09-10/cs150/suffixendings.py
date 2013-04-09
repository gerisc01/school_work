#Scott Gerike
#CS150
#10/19/09
#Print all the suffix endings

def suffixEndings(astring):
    for i in range((len(astring)),-1,-1):
        suffix = astring[i:len(astring)]
        print(suffix)

def main():
    astring = input("please enter a word:")
    suffixEndings(astring)

main()

