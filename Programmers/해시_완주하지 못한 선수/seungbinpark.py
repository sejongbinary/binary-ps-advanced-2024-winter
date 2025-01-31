from collections import Counter
def solution(participant, completion):
    ans=[]
    
    c = Counter(completion)
    
    for name in participant:
        if c[name]>0:
            c[name] -= 1
        else:
            ans.append(name)
            
    return ans[0]
