def wordCount(wordlist):
    d = {}
    for item in wordlist:
        if item in d:
            d[item] = d[item] + 1
        else:
            d[item] = 1
    sort = d.items()
    sort = list(sort)
    sort.sort()
    for item in range(len(sort)):
        pop = sort.pop(item)
        print(pop[0],pop[1])
        sort.insert(item,pop)

def main():
    sentence = input("Input a Sentence Here:")
    sentence = sentence.split()
    wordCount(sentence)

main()
        
    
         
