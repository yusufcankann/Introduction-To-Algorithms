
#mergesort.
def merge(my_arr):
    if len(my_arr)<=1:
        return 0

    middle=len(my_arr)//2
    left=my_arr[:middle] #left part
    right=my_arr[middle:] #right part

    merge(left) #recursive calls
    merge(right)

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

# It looks in array if there is a pair 
#    that is povides the condition which is
#    multiplication of that pair is equal to given number.
def find_pairs(my_arr,number):
    i=0
    j=len(my_arr)-1
    merge(my_arr)

    while i<j:
        result=my_arr[i]*my_arr[j]

        if result < number:#increases 1 index. So in this way result is increases.
            i=i+1
        elif result > number: #decreases 1 index. So in this way result is decrease.
            j=j-1
        else:
            print("numbers are: "+str(my_arr[i])+" "+str(my_arr[j]))
            return 0
    return -1


if __name__ == "__main__":
    arr=[1,2,6,0,7,5,4,7,2,3,6]
    find_pairs(arr,14)
