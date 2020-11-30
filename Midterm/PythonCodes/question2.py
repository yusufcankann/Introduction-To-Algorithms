#Yusuf Can Kan - 161044007
#part 2

import math

def which_number(array,current_result):
    if len(array)==0 or len(array[0])==0:
         return int(current_result,2)
       
    array1=[]
    array2=[]
    for i in array:
        if i[-1]=='0':
            array1.append(i[:-1]) #stores the elements that finishes with 0
        else:
            array2.append(i[:-1]) #stores the elements that finishes with 1

    if len(array1)>len(array2): #if count(0)>count(1)
        current_result='1'+current_result
        return which_number(array2,current_result)
    else:
        current_result='0'+current_result
        return which_number(array1,current_result)



if __name__ == "__main__":
	arr=[0,1,2,3,4,5,6,7,8,9,10,11,26,12,27,13,14,15,16,17,18,19,20,21,22,23,24,25]
	str_arr=[]

	size=math.ceil(math.log(len(arr)+1,2)) #calculates the maximum size for representing array in binary.

	binary_size='0'+str(size)+'b' #sets the size of the binary int represantation string.

	for i in arr: #converts numbers to binary string.
		str_arr.append(format(i, binary_size))


    #calls the function.
	result=which_number(str_arr,"")
	print(result)
