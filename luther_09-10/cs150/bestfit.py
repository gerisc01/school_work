import cTurtle

t = cTurtle.Turtle()

def toIntX(alist):
    result = []
    for item in range(len(alist)):
        pop = alist.pop(item)
        integer = pop[0]
        result = result + [integer]
        alist.insert(item,pop)
    return result

def toIntY(alist):
    result = []
    for item in range(len(alist)):
        pop = alist.pop(item)
        integer = pop[1]
        result = result + [integer]
        alist.insert(item,pop)
    return result

def xmax(alist):
    maxSoFar = alist[0]
    for pos in range(1,len(alist)):
        if alist[pos] > maxSoFar:
            maxSoFar = alist[pos]
    return maxSoFar

def xmin(alist):
    minSoFar = alist[0]
    for pos in range(1,len(alist)):
        if alist[pos] < minSoFar:
            minSoFar = alist[pos]
    return minSoFar

def mean(alist):
    mean = int(sum(alist)/len(alist))
    return mean

def m(alist,howmany):
    answer = (((sum(toIntX(alist))*sum(toIntY(alist)))-(howmany*(mean(toIntX(alist)))*(mean(toIntY(alist)))))/((sum(toIntX(alist))**2)-(howmany*(mean(toIntX(alist))**2))))
    return answer
    

def getData(howmany):
    result = []
    for item in range(howmany):
        x = int(input("input x value:"))
        y = int(input("input y value:"))
        ordPair = [x,y]
        result = result + [ordPair]
    return result

def plotRegression(alist,howmany):
    t.setWorldCoordinates((xmin(toIntX(alist))-5),(xmin(toIntY(alist))-5),(xmax(toIntX(alist))+5),(xmax(toIntX(alist))+5))
    t.up()
    for item in range(len(alist)):
        ordPair = alist.pop(item)
        t.goto(float(ordPair[0]),float(ordPair[1]))
        t.dot(5)
        alist.insert(item,ordPair)
    y1 = (mean(toIntY(alist))+(m(alist,howmany))-(howmany*(mean(toIntX(alist)))**2))*(xmin(toIntX(alist))-mean(toIntX(alist)))
    y2 = (mean(toIntY(alist))+(m(alist,howmany))-(howmany*(mean(toIntX(alist)))**2))*(xmax(toIntX(alist))-mean(toIntX(alist)))
    t.color("green")
    print(float(xmin(toIntX(alist))),y1)
    t.down()
    t.goto(float(xmax(toIntX(alist))),y2)
    
    
def main():
    howmany = int(input("How many points do you want:"))
    plotRegression(getData(howmany),howmany)
        

main()


t.exitOnClick()
    
    
    
    

    


