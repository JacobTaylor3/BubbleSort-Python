
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




if __name__ =="__main__":  #Tests 
                        
    list1 = [2,9,12,15]#Even and Odd
    list2 = [3,4]
    newList = merge(list1,list2)
    #print(newList)

    list1 = [2,9]#Both even
    list2 = [3,4]
    newList = merge(list1,list2)
    #print(newList)
    list1 = [2,5,9]#Both Odd
    list2 = [4,5,90]
    newList = merge(list1,list2)
    #print(newList) 

    list1 = [9] #One element in each 
    list2 = [4]
    newList = merge(list1,list2)
    #print(newList)




    











    





