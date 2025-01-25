def solution(nums):  
    if len(set(nums)) < len(nums) / 2: #N/2 마리보다 적은 경우
        return len(set(nums))    
    return len(nums)/2 # 종류가 N/2보다 많으면 N/2가 답 