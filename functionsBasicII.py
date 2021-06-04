def countdown(startNum):
    li=[]
    for i in range(startNum, -1, -1):
        li.append(i)
    return li

print(countdown(25))

def printAndReturn(numLi):
    print(numLi[0])
    return(numLi[1])

print(printAndReturn([1,2]))

def firstPlusLength(numLi):
    sum = numLi[0]+len(numLi)
    return sum

print(firstPlusLength([1,1,2,2,3,4,5,6]))

def valuesGreaterThanSecond(numLi):
    newLi=[]
    if len(numLi)<2:
        return False
    else:
        for i in range(len(numLi)):
            if numLi[i]>numLi[1]:
                newLi.append(numLi[i])
        return newLi

print(valuesGreaterThanSecond([1,1,1,1,2,2,2,5,5,5,6,8]))

def thisLengthThatValue(size,value):
    li=[]
    for i in range(size):
        li.append(value)
    return li

print(thisLengthThatValue(7,27))