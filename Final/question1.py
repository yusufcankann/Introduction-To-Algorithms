
def findSubArr (arr):
    size=len(arr)
    result=[0,0]
    subArrTable= [[0 for x in range(size)] for x in range(size)]

    #fill 1 letter gap
    for i in range(size): 
        subArrTable[i][i] = 1
        if i<(size-1):
            if(arr[i]==arr[i+1]):
                subArrTable[i][i+1] = 1
                result[0]=i
                result[1]=2
            else:
                subArrTable[i][i+1] = 0 
 
    #fill the rest
    for i in range (2,size):
        x=0
        y=x+i
        while(y!=size):
            if arr[x]==arr[y] and subArrTable[x+1][y-1]==1: #if substring are true and
                                                            #current indexes are same
                subArrTable[x][y]=1 #set given index is true
                if(i>result[1]):
                    result[0]=i #update result values
                    result[1]=x
            else:
                subArrTable[x][y]=0
            x+=1
            y+=1
    
    result[0]=result[0]+1
    return result


def printResult(input,result):
    print("The Input is:",input)
    print("The Subset is: ",input[(result[1]):(result[0]+result[1])])
    print("The length is: ",result[0])
    print("")

#TEST1
input1=["t","e","n","e","t"]
result1=findSubArr(input1)
printResult(input1,result1)

#TEST2
input2=["t","e","n","e","t","y","u","s","u","f","f","u","s","u","y","a"]
result2=findSubArr(input2)
printResult(input2,result2)

#TEST3
input3=["x","b","a","a","b","x"]
result3=findSubArr(input3)
printResult(input3,result3)

#TEST4
input4=["x","b","a","a","b","a","a","a","a","a","a","a","x","h","k","k","h"]
result4=findSubArr(input4)
printResult(input4,result4)

