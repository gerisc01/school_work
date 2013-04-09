def isPal(s):
    first = 0
    last = len(s)-1
    stillPal = True
    while stillPal and first <= (len(s)/2):
        if s[int(first)] != s[int(last)]:
            stillPal = False
        else:
            first = first + 1
            last = last - 1
            stillPal = True
    return stillPal

def main():
    s = input("Please enter a word(DONE to quit):")
    while s!="DONE":
        print(isPal(s))
        s = input("Please enter a word(DONE to quit):")

main()
        
