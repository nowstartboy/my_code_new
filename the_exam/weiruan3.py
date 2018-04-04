def maxStipend2(numOfDays,taskList,state):
    if not taskList or not numOfDays:
        return 0
    if state==1: #前一天工作了
        max1=taskList[0][0]+maxStipend2(numOfDays-1,taskList[1:],1)
    else:
        max1=taskList[0][1]+maxStipend2(numOfDays-1,taskList[1:],1)
    max2 = maxStipend2(numOfDays - 1, taskList[1:], 0)
    return max(max1,max2)

def maxStipend(numOfDays,taskList):
    max0=0
    max1=maxStipend2(numOfDays-1,taskList[1:],1)+taskList[0][1]
    max2=maxStipend2(numOfDays-1,taskList[1:],0)
    return max(max1,max2)

print (maxStipend(4,[[7,10],[6,7],[4,6],[6,7]]))