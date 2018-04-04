a=input()
b=input()
nk=[int(i) for i in a.split(' ')]
nums=[int(i) for i in b.split(' ')]
collect={}
for num in nums:
    if num not in collect:
        collect[num] = 1
    else:
        collect[num] += 1

if nk[1]==0:
    count=0
    for value in collect.values():
        if value>1:
            count += 1
    print (count)
else:
    already={}
    count=0
    for num in nums:
        tuple1=(num,num+nk[1])
        if num+nk[1] in collect and tuple1 not in already:
            already[tuple1] = 'Y'
            count +=1
        tuple2=(num-nk[1],num)
        if num-nk[1] in collect and tuple2 not in already:
            already[tuple2] = 'Y'
            count +=1
    print (count)