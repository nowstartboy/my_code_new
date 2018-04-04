def numberOfDays(numOfPlants,plantHeight):
    if numOfPlants==1:
        return 1
    cutPlants=[]
    for i in range(numOfPlants-1):
        if plantHeight[i]>plantHeight[i+1]:
            cutPlants.append(plantHeight[i+1])
    if len(cutPlants)==0:
        return 1
    cutedPlants=[i for i in plantHeight if i not in cutPlants]
    print (cutedPlants)
    return 1+numberOfDays(len(cutedPlants),cutedPlants)

print (numberOfDays(4,[3,6,9,8]))
