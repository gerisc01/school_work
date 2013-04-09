def replaceFunction(astring, achar, replacestring):
     for index in range(len(astring)):
          if astring[index] == achar:
               beg = astring[0:index]
               end = astring[index+1:len(astring)+1]
               mid = replacestring
               print(beg+mid+end)
               
               

def main():
    astring = input("Type a word:")
    achar = input("What do you want to replace in this word:")
    replacestring = input("What do you want to replace this with:")
    replaceFunction(astring, achar, replacestring)

main()

    
     
