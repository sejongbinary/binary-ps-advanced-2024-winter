from collections import Counter
p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]

ans=[]
    
com = Counter(c)
    
for name in p:
    if c[name]>0:
        c[name] -= 1
    else:
        ans.append(name)
print(ans)
