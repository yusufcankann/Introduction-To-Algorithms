
#l is the memory of subsets
# this memory list contains subsets and sum of this subset elements
# fist element of all memry list a sum if this subsets.
# memory example;
# [
# 	[3,2,1],     subset1    2+1=3
#	[7,1,2,3,1], subset2    1+2+3+1=7
#   [0,5,-5]     subset3    5+(-5)=0
# ]
#
#
def findZero(elem,l): #memory of subsets
	for i in range(0,len(l)):
		subset=[(l[i][0])+elem]
		subset.extend(l[i][1:])
		subset.extend([elem])
		if subset[0] == 0:
			print(subset[1:])
		l.extend([subset])
	if(elem==0):
		print([elem])
	l.extend([[elem,elem]])

def printsubsets(l):
	subset_memory=[] #stores previous calculated subsets
	print("Input List;")
	print(l)
	print("The subsets that has 0 sum are;")
	for i in l:
		findZero(i,subset_memory)

if __name__ == "__main__":
	l=[2,3,-5,-8,6,-1]
	printsubsets(l)

	# l2=[1,2,3,-1,-2,-3]
	# printsubsets(l2)
