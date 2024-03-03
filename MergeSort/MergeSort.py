
def mergeSort(aList):  # splits up the lists 
    if (len(aList) < 2):
        return(aList)
    else:
        a = aList[0:len(aList)//2]
        b = aList[len(aList)//2: len(aList)]
        aButSorted = mergeSort(a)
        bButSorted = mergeSort(b)
        return(merge(aButSorted, bButSorted))
        
def merge(listA, listB): #sorts the list 
    newList = []
    lookHereNextInA = 0
    lookHereNextInB = 0

    while(len(listA)> lookHereNextInA and len(listB)> lookHereNextInB):
        if(listA[lookHereNextInA]<listB[lookHereNextInB]):
            newList.append(listA[lookHereNextInA])
            lookHereNextInA = lookHereNextInA +1 #incrimenting the pointer for A
            
        else:
            newList.append(listB[lookHereNextInB])
            lookHereNextInB = lookHereNextInB +1  #incriminting the pointer for B 
    newList.extend(listA[lookHereNextInA:])
    newList.extend(listB[lookHereNextInB:])
    return(newList)




