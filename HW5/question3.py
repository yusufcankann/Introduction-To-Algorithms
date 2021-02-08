
# i current index,
# W capacity
def knapsackProblem(i,W,weights,values,memory):
    if memory[i][W] != 0:
        return memory[i][W]
    if i==-1 or W==0: #if capacity is full or there is no element left
        returnValue=[0,[]]
    elif weights[i]>W: #if weight of single element is bigger than current
                    # capacity, ignore it 
        returnValue=knapsackProblem(i-1,W,weights,values,memory)
    else:
        withoutCurrent=knapsackProblem(i-1,W,weights,values,memory)
        
        withCurrent=knapsackProblem(i-1,W-weight[i],weights,values,memory)
        withCurrent[1].append([weights[i],values[i],i])
        withCurrent[0]=withCurrent[0]+values[i]
        if withoutCurrent[0] > withCurrent[0]:
            returnValue=withoutCurrent
        else:
            returnValue=withCurrent
    
    memory[i][W]=returnValue
    return returnValue




# main
if __name__ == "__main__":
    values = [ 10, 4, 3 ]
    weight = [ 5, 4, 2 ]
    W = 9
    
    print("The input is:")
    print("Values:",values)
    print("Weights:",weight)
    print("Capacity:",W)
    print("")
    print("The output is:")

    zero = [0] * (W + 1)
    memory = [zero.copy() for i in range(len(values))]

    result=knapsackProblem(len(values)-1, W, weight, values,memory)

    print("Total value:",result[0])
    for i in result[1]:
        print("Element",i[2],"Value is:",i[1],"weight is:",i[0])






