import math
# constructs a sengment tree which hols 3 item
# [min value in the interval,[interval indexes]]
def construct_segment_tree(seg_tree,arr,node,start,end):
    if start == end:
        seg_tree[node] = [arr[start],[start,end]]
    else:
        
        mid = (start+end)//2
        #Contruct left part of tree
        construct_segment_tree(seg_tree,arr,2*node+1, start, mid)
        #Contruct right part of tree
        construct_segment_tree(seg_tree,arr,(2*node)+2,mid+1,end)
        #The node will store the min of 2 child as a min value
        seg_tree[node] = [min(seg_tree[2*node+1][0],seg_tree[2*node+2][0]),[start,end]]

#find the min of given interval
def find_min(segtree,node,l,r):
    if r<segtree[node][1][0] or l>segtree[node][1][1]:
        return [math.inf,[0,0]]
    if l<=segtree[node][1][0] and r>=segtree[node][1][1]:
        return segtree[node]
    
    r1 = find_min(segtree,2*node+1, l, r)
    r2 = find_min(segtree,2*node+2, l, r)

    if(r1[0]<r2[0]):
        return r1
    else:
        return r2

def printResult(arr,interval):
    print("Min element of interval",interval,"is","element:",arr[0])


def find(arr,intervals):
    n = len(arr)-1
    segtree=[[0,[0,0]] for i in range(4*n)]
    construct_segment_tree(segtree,arr,0,0,n)
    
    print("Input array:",arr)
    for i in intervals:
        printResult(find_min(segtree,0,i[0]-1,i[1]-1),i)
    print("")

if __name__ == "__main__": 
    test1=[0,1,2,12,9,0]
    intervals=[[1,2],[3,5],[2,6],[4,5],[4,4]]

    find(test1,intervals)


    test2=[132, 139, 280, 252, 138, 6, 225, 144, 18, 206, 42, 104, 19, 193, 259, 127, 183, 133, 228, 1]
    intervals_2=[[1,20],[2,15],[2,3],[10,12],[5,9],[7,12]]

    find(test2,intervals_2)
