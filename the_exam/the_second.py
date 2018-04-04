def the_first(m,s):
    m=s
    s=s+s
    return [m,s]

def the_second(m,s):
    s = s+m
    return [m,s]

def count_all(n,m,s):
    if len(s)==n:
        return 0
    if len(the_first(m,s)[1])== n or len(the_second(m,s)[1])==n:
        return 1
    if len(s)>n:
        return float('inf')
    else:
        max1=count_all(n,the_first(m,s)[0],the_first(m,s)[1])+1
        print (max1)
        max2=count_all(n,the_second(m,s)[0],the_second(m,s)[1])+1
        return min(max1,max2)

if __name__=="__main__":
    a=input()
    n=int(a)
    print (count_all(n,'a','a'))