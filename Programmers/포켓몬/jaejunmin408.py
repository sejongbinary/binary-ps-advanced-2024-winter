def solution(nums):
    nums_len = len(nums) / 2
    
    set_nums_len = len(set(nums))
    
    if (nums_len) < set_nums_len:
        answer = nums_len
    else :
        answer = set_nums_len
    return answer
