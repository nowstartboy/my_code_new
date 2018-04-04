s=input()
s1=int(s)
result=[]
for i in range(s1):
  ss=input()
  si=[int(j) for j in ss.split(' ')]
  if sum(si)-max(si)>0.5*max(si):
    min_s=min(si)
    num=0
    num += min_s
    sii=[k-min_s for k in si if k !=min_s]
    print (sii)
    a,b=sii[0],sii[1]
    while a+b>=3 and a>0 and b>0:
      if a>b:
          a -=2
          b -=1
      else:
          b-=2
          a-=1
      num +=1
      print (num)
    result.append(num)
  else:
    result.append(max(si)//2)
for u in result:
  print (u)