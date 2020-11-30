#Yusuf Can Kan - 161044007
#part 3



# Quick sort partititon function. It sets the last element as a pivot.
def rearrange(a,low,high):
	pivot = a[high]
	left = low
	for i in range(low,high):
		if a[i]<pivot:
			a[i], a[left]=a[left], a[i] #swap
			left+=1
	a[left], a[high]= a[high], a[left] #swap
	return left #return current left.


# insertion sort
# a=first index
# b=last index
def insertionSort(array,a,b):
	for i in range(a+1,b+1):
		c=array[i]
		p=i-1
		while p>=0 and c < array[p]: # basic operation for insertion sort
			array[p+1] = array[p]
			p=p-1
		array[p+1]=c


#combination of quicksort and insertion sort.
def quick_insertion_sort(arr,low,high):
	while low<high: # we changed this part from (quicksort). It was if but, we put while here 
					#because of insertion sort is not recursive.

		if high-low+1<7: #if size is smaller than given number then insertion sort will be more efficient.
			insertionSort(arr,low,high)
			return

		else: #do normal quicksort
			p = rearrange(arr, low, high)
			if high-p>p-low:
				quick_insertion_sort(arr, low, p-1)
				low=p+1
			else:
				quick_insertion_sort(arr, p + 1, high)
				high=p-1
				


if __name__ == "__main__":
	arr=[20,10,21,3234,41,532,2,1,80,30,67,88,233,12,89,4325,765,1387,1,2,865,90,37,50]
	
	quick_insertion_sort(arr,0,len(arr)-1)
	print(arr)
