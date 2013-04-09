def listtoString(alist):
    string = ""
    for item in alist:
        string = string + " " + str(item)
    return string
    

def wordOccurence(file):
    words = open(file, "r")
    d = {}
    line = 0
    for aline in words:
        line = line + 1
        values = aline.split()
        for item in values:
            if item not in d:
                d[item] = [line]
            if line not in d[item]:
                old = d[item]
                old.append(line)
                
    sort = d.items()
    sort = list(sort)
    sort.sort()
    for item in range(len(sort)):
        pop = sort.pop(item)
        print(pop[0],"is in line(s)",listtoString(pop[1]))
        sort.insert(item,pop)
    



def main():
    words = input("Input a file location:")
    wordOccurence(words)
        
main()
