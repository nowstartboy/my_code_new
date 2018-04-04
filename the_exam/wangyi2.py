def getDi(Di,num,DiL):
    if DiL==1:
        if num>Di:
            return Di[0]
    else:
        i,j=0,DiL
        while i<j:
            mid=(i+j)//2
            if Di[mid]>num:
                j=mid-1
            elif Di[mid]<num:
                i=mid+1
            else:
                return Di[mid]
        return Di[i]

def getDi2(Di,num,DiL):
    result=0
    for D in Di:
        if D<=num:
            result=D
    return result

s1=input()
inp=[int(i) for i in s1.split(' ')]
work={}
for i in range(inp[0]):
    ss=input()
    inp1=[int(j) for j in ss.split(' ')]
    work[inp1[0]]=inp1[1]
print (work)
sss=input()
inp2=[int(i) for i in sss.split(' ')]
Di=sorted(list(work.keys()))
print (Di)
DiL=len(Di)
work_select=[]
for num in inp2:
    Di_up=getDi2(Di,num,DiL)
    if Di_up==0:
        work_select.append(Di_up)
    else:
        work_select.append(work[Di_up])
for select in work_select:
    print (select)