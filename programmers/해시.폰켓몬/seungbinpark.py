def solution(nums):
    n = set(nums) # 중복 제외 종류 번호의 집합
    N = len(nums)/2 # 이론상의 최댓값
    # 종류 번호의 종류가 N/2개보다 적을 때
    if N>=len(n): return len(n) 
    # 종류 번호의 종류가 N/2개보다 많을 때
    elif N<len(n): return N
