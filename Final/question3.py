
#elem is location with its income
#l is memory list
def placeAd(elem,l,max): #memory of subsets
    for i in range(0,len(l)):
        #if distance is bigger than 4km
        if abs(elem[0]-l[i][-1][0])>4:
            subset=[(l[i][0])+elem[1]]
            subset.extend(l[i][1:])
            subset.extend([elem])
            l.extend([subset])
            #updates the max element if new one
            if max[0] < subset[0]:
                max[0]=subset[0]
                max[1]=subset[1:]

    l.extend([[elem[1],elem]])
    if max[0] < elem[1]:
                max[0]=elem[1]
                max[1]=[elem]

def placeAds(locations,income):
    n=len(locations)
    
    #put locations and income in the same array
    inputs=[]
    for i in range(n):
        inputs.append([locations[i],income[i]])
    inputs.sort()
    print(inputs)
    memory=[]
    max=[0,[]]
    for i in inputs:
        placeAd(i,memory,max)
  
    print("Total Income:",max[0])
    print("Location-Income pairs:")
    for i in max[1:][0]:
        print(i)



if __name__ == "__main__": 
    locations=[3,4,8,11,2,7,5,6,1]
    income=[10,2,6,18,7,2,3,15,30]
    
    placeAds(locations,income)


