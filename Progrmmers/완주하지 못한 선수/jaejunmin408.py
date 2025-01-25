def solution(participant, completion):
    temp = dict()
    
    for name in participant:
        if name in temp:
            temp[name] += 1
        else:
            temp[name] = 0
    
    for name in completion:
        if temp[name] == 0:
            del temp[name]
        else:
            temp[name] -= 1
        
    final = list(temp.keys())
    answer = final[0]
    return answer
