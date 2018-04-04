'''
def indegree(nodes,table):
    if table==[]:
        return None
    tmp=nodes[:]
    for i in table:
        if i[1] in tmp:
            tmp.remove(i[1])
    if tmp==[]:
        return -1
    for t in tmp:
        for i in range(len(table)):
            if t in table[i]:
                table[i]='on'
    if table:
        eset=set(table)
        eset.remove('on')
        table[:]=list(eset)
    if nodes:
        for t in tmp:
            nodes.remove(t)
    return tmp



s=input()
ss=[int(i) for i in s.split(' ')]
n,m=ss[0],ss[1]
nodes=set([])
table=[]
for i in range(n):
    user=input()
    user1=user.split(',')
    nodes.add(user1[0])
    table.append((user1[0],user1[1]))
nodes=sorted(list(nodes))
print (nodes,table)
safe=[]
while True:
    node=indegree(nodes,table)
    if node==None:
        break
    if node==-1:
        break
    safe.append(node)
    print (safe)
print (' '.join(safe))
'''
s = input()
ss = [int(i) for i in s.split(' ')]
n, m = ss[0], ss[1]
nodes = set([])
table = []
tables = {}
for i in range(n):
    user = input()
    user1 = user.split(',')
    nodes.add(user1[0])
    table.append((user1[0], user1[1]))
    if user1[0] not in tables:
        tables[user1[0]] = [user1[1]]
    else:
        tables[user1[0]].append(user1[1])

safe = []
state = True
state_collect = {}
while state:
    state = False
    for item in tables.keys():
        for j in tables[item]:
            if j not in tables:
                if item not in state_collect:
                    state_collect[item] = [j]
                else:
                    state_collect[item].append(j)
                safe.append(j)
                state = True
            elif len(tables[j]) == 0:
                if item not in state_collect:
                    state_collect[item] = [j]
                else:
                    state_collect[item].append(j)
                safe.append(j)
                state = True
    for safe_state in state_collect.keys():
        safe_value = state_collect[safe_state]
        for u in safe_value:
            tables[safe_state].remove(u)
        if len(tables[safe_state])==0:
            safe.append(safe_state)
            tables.pop(safe_value)

    state_collect = {}
print (safe)
print(' '.join(safe))