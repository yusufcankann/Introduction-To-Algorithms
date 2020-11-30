#Yusuf Can Kan - 161044007
#part 5

##################################################
# the input of the program is 2d array which every 
# row represents different person and every column
# represents different job. 
#
# Every value in the array is represents the cost.
# for that person and job.
#
#
# for example:
# 1 4 3
# 5 6 7
# 0 5 2
#
# in this array 6 is represents the cost for 1th person, 1th job.
#
#
# You must provide nxn array to the program.
#
##################################################


import copy


#finds maximum element from given array
#and returns its coordinates
def find_max(arr):
    i1,j1=-1,-1
    max=-1
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            if arr[i][j]>max:
                max=arr[i][j]
                i1=i
                j1=j
    
    return i1,j1

#finds minimum element from given column and row
#and returns its coordinates.
def find_min(arr,i1,j1):
    i2,j2=i1,j1

    min=arr[i1][j1]
    for i in range(0,len(arr)): #for column
      if arr[i1][i]<min and arr[i1][i]!=-1:
          min=arr[i1][i]
          i2=i1
          j2=i

    for i in range(0,len(arr)): #for row
      if arr[i][j1]<min and arr[i][j1]!=-1:
          min=arr[i][j1]
          i2=i
          j2=j1

    return i2,j2


#sets given colum and row to -1
def clear_row_column(arr,i1,j1): 
    for i in range(0,len(arr)): #for column
        arr[i1][i]=-1

    for i in range(0,len(arr)): #for row
      arr[i][j1]=-1


#prints the result.
def print_result(input_array,result):
    for i in result:
        print("Person "+str(i[0])+" assigned to job "+str(i[1])+". The cost is:",str(input_array[i[0]][i[1]]))


#the main funciton. This function does the all work.
#first it finds the max element.
#second it finds the min element that same is in the column and row with max.
#it stores that value to the result array
#it clears the min elements row and column (assignes -1)
#repeats same process
def assignment(arr):
    result=[]
    for i in range(0,len(arr)):
        maxi,maxj=find_max(arr)
        mini,minj=find_min(arr,maxi,maxj)
        result.append([mini,minj])
        clear_row_column(arr,mini,minj)
    return result


if __name__ == "__main__":

    #first we created the array. 
    #Row of the array represents the different peoples
    #Column of the array represents different jobs.
    #Every value of the array represents cost of different person-job assignments.
    input_array=[[47, 52, 25, 22, 39, 53],
    [90, 42, 88, 67, 19, 36],
    [16, 49, 21, 64, 86, 59],
    [45, 15, 69, 61, 81, 48],
    [27, 58, 62,  5, 24, 33],
    [65, 63, 38, 75, 54, 23]]
 

    #copies array for printing result.
    input_array_temp=copy.deepcopy(input_array) #takes the copy of the array for result

    result=assignment(input_array)

    #for printing result.
    print_result(input_array_temp,result)


