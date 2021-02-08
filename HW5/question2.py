# Starts from bottom of the triange and goes to the up
# while summing minimum paths.
# Output Format: [CostPath, [Path Values]]
def findPath(A):

	# this list stores the array such a way that first element of every subelement represents
	#	the sub of the way and second element is stores the elements in the path.
	paths = [] # this will store the paths

	for i in range(len(A[(len(A)-1)])): #put the last row elements in a list.
		paths.append([A[(len(A)-1)][i],[A[(len(A)-1)][i]]])
	for i in range(len(A)-2,-1,-1): # iterate every element in the memory list								# for finding next step of the ways.
		for j in range(len(A[i])):
			if paths[j][0]<paths[j+1][0]:# selects the smaller path.
				paths[j][0]=A[i][j]+paths[j][0]
				paths[j][1].append(A[i][j])
			else:
				paths[j][0]=A[i][j]+paths[j+1][0]
				paths[j][1]=[]
				paths[j][1].extend(paths[j+1][1])
				paths[j][1].append(A[i][j])
	paths[0][1].reverse()
	return paths[0]


def printResult(arr):
	if(arr != None):
		print("Sum Path:"+str(arr[0]))
		print("The Path is:"+str(arr[1]))




if __name__ == "__main__":
#	TEST CASES
	# B = [
	# [    1 ],
	# [  5, 1 ],
	# [ 5, 3, 4 ],
	# [5, 4 ,1, 8],
	# [1, 4, 7, 1, 11 ],
	# [12, 8, 6, 9, 1, 5]]
	# printResult(findPath(B))


	A = [
		[ 2 ],
		[5, 4],
	[1, 4, 7 ],
	[8, 6, 9 ,6]]

	printResult(findPath(A))
