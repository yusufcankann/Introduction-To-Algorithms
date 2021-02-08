#Yusuf Can Kan

#for map function.
#this doubles the ight part of the array
def double(n): 
    return n*2

#mergesort.
def countInverseWithMergeSort(my_arr):
    inversionCount=0
    if len(my_arr)<=1:
        return 0

    middle=len(my_arr)//2
    left=my_arr[:middle] #left part
    right=my_arr[middle:] #right part

    inversionCount+=countInverseWithMergeSort(left) #recursive calls
    inversionCount+=countInverseWithMergeSort(right)

    #THIS PART MEGES THE LEFT AND RIGHT PART
    s1=len(left)    #size of left and right sub arrays.
    s2=len(right)

    i=0
    j=0
    x=0
    while i<s1 and j<s2:
        if left[i]<right[j]:
            my_arr[x]=left[i]
            i=i+1
        else:
            my_arr[x]=right[j]
            j=j+1
        x=x+1

    while i<s1:
        my_arr[x]=left[i]
        i=i+1
        x=x+1

    while j<s2:
        my_arr[x]=right[j]
        j=j+1
        x=x+1
    
    # this part takes the double of second array and calculates the 
    # incersion count for this subarray.
    i=0
    j=0
    x=0
    doubleRight= list(map(double, right))
    while i<s1 and j<s2:
        if left[i]<=doubleRight[j]:
            i=i+1
        else:
            inversionCount+=(len(left[i:]))
            j=j+1
        x=x+1
    
    return inversionCount


def printResult(input,result):
    print("")
    print("The input is:",input)
    print("The inverse count is:",result)
    print("")

def calculateInverse(input):
    inputCopy=input[:]
    result=countInverseWithMergeSort(input)
    printResult(inputCopy,result)

if __name__ == '__main__':
    
    arr1 = [12, 11, 13, 5, 6, 7]
    calculateInverse(arr1)

    arr2 = [16,17,14,16,12,2]
    calculateInverse(arr2)
 
    arr3 = [100,49,25,6,5,1]
    calculateInverse(arr3)

    arr4 = [10,5,2,8,100,2,50,60,20,30,1]
    calculateInverse(arr4)

    
   


  