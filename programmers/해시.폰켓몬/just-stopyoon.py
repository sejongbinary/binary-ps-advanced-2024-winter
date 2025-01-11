def solution(nums):
    answer = 0
    N = len(nums) # 총 폰켓몬 수
    
    seen = [] # 폰켓몬 종류를 담을 리스트
    
    for num in nums :
        if num in seen : # 만약 중복된 폰켓몬일 경우
            continue # 넘어감
        else : # 새로운 폰켓몬일 경우
            seen.append(num) # 리스트에 추가
    
    if len(seen) >= N/2 : # 폰켓몬 종류가 가지고 갈 폰켓몬보다 클 때
        answer = N/2 # 최대값은 가지고 갈 폰켓몬 수
    else : # 폰켓몬 종류가 가지고 갈 폰켓몬보다 적을 때
        answer = len(seen) # 최대값은 폰켓몬 종류
        
    return answer
