#Scott Gerike
#CS150
#10/22/09
#Uses the Caesar cypher to encrypt words by rotating them to the letter 13 away

def rotate13(astring):
    result = ""
    for index in astring:
        rotate = ord(index)
        if rotate<109:
            rotate = rotate + 13
        else:
            rotate = rotate - 13
        crypt = chr(rotate)
        result = result + crypt
    return result

def main():
    print(rotate13(input("Type in a word:")))
    
           
    
main()

    
    
        
            
