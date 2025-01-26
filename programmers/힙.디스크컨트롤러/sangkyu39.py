def solution(jobs):     
    jobs.sort(key=lambda x:-x[0]) #작업을 요청 시간 역순으로 정렬
    time = jobs[-1][0] # 요청 시간이 가장 빠른 것 시간 선택
    buffer = []
    turnTime = 0
    jobCnt = len(jobs)
    while buffer or jobs:
        while jobs and jobs[-1][0] <= time: # 뒤에서 부터 요청시간이 지난 것까지만 힙에 넣기 
            start, duration = jobs.pop() 
            hq.heappush(buffer, (duration, start)) # 힙 정렬을 위해 소요시간과 요청 시간 반대로 넣기 
        if not buffer: # 대기하는 작업이 없는데 시간이 안 흐를 때 
            time = jobs[-1][0]
            continue
        job = hq.heappop(buffer) # 가장 소요시간이 적은 것 POP
        time += job[0] # 소요시간 더하기
        turnTime += time - job[1]

    return turnTime // jobCnt