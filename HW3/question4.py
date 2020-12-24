import random


#stores swap count for quicksort
swap_quicksort=0

#stores swap count for insertion sort
swap_insertion=0

def quick_sort(arr, low, high):
    if low<high:
        p=rearrange(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p + 1, high)

def rearrange(a,low,high):
    global swap_quicksort
    p = a[high]
    left = low-1
    for i in range(low,high):
        if a[i]<p:
            left+=1
            a[i], a[left]=a[left], a[i] #swap
            swap_quicksort+=1
    a[left+1], a[high]= a[high], a[left+1] #swap
    swap_quicksort+=1
    return left+1 #return current left.




def insertionSort(arr):
    global swap_insertion
    for i in range(2,len(arr)):
        current=arr[i]
        position=i-1
        while position>=1 and current < arr[position]: # basic operation for insertion sort
            swap_insertion+=1
            arr[position+1] = arr[position]
            position=position-1
        arr[position+1]=current




if __name__ == "__main__":
    arr1=[]

    #Sort with 100 items and 100 times
    for i in range(0,100):
        arr1=[]
        for i in range(0,100):
            arr1.append(random.randint(0,10000))
        arr2=arr1[:]

        quick_sort(arr1,0,len(arr1)-1)
        insertionSort(arr2)
        
    print("Average count for quicksort (size=100,100 times sort):"+str(swap_quicksort/100))
    print("Average count for insertionsort (size=100,100 times sort):"+str(swap_insertion/100))





