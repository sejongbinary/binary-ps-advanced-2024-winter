import math
def solution(progresses, speeds):
    answer = []

    # 남은 일을 효율로 나눈 배열(소요 시간)
    day=[math.ceil((100-progresses[i])/speeds[i]) for i in range(len(speeds))]
    
    while day:    
        x=day.pop(0)
        cnt=1 # 같이 배포할 수 있는 기능 수
        
        while day and day[0]<=x: # 다 돌았거나, 앞 기능 소요 시간이 더 많거나 같을 때
            day.pop(0) #같이 배포할 수 있는 기능 pop
            cnt+=1
        
        answer.append(cnt)

    return answer
