def reverse(alist):
    if len(alist) == 0:
        return []
    else:
        return [alist[-1]] + reverse(alist[:-1])

def main():
    L = [1,3,5,7,9,2,4,6,8]
    print(reverse(L))

main()

