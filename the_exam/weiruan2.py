def maxDegreeAnnoyance(numOfFriends,height):
    max_annoy=0
    for i in range(1,numOfFriends):
        u =0
        j=i
        key=height[i]
        while j>0 and key<height[j-1]:
            height[j]=height[j-1]
            u +=1
            j -=1
        height[j]=key
        max_annoy=max(max_annoy,u)
    return max_annoy

print (maxDegreeAnnoyance(9,[19,17,14,15,16,15,13,12,11]))