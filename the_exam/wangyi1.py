s=input()
inp=[int(i) for i in s.split(' ')]
l=inp[0]
r=inp[1]
sum_i=0
for i in range(l):
    sum_i = sum_i + i
result=0
for j in range(l,r+1):
    sum_i += j
    if sum_i%3==0:
        result += 1
print (result)