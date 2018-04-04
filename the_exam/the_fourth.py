def high_max(arr,k,H,h):
    arr_pre=[i for i in arr if 0<i-h<=H]
    if k==0 or len(arr_pre)==0:
        return h
    arr_all=[]
    for pre in arr_pre:
        arr_new=[i for i in arr if i>2*pre-h]
        arr_all.append(arr_new)
    print (h)
    print (arr_pre)
    print (arr_all)
    max_h=max([high_max(arr_all[i],k-1,H,2*arr_pre[i]-h) for i in range(len(arr_pre))])
    return max_h

a=input()
nkh=[int(i) for i in a.split(' ')]
print (nkh)
plat_h=[]
for i in range(nkh[0]):
    h1=input()
    plat_h.append(int(h1))
print (plat_h)
max_h=high_max(plat_h,nkh[1],nkh[2],0)
print (max_h)