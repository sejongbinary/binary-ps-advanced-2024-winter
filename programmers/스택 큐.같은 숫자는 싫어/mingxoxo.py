def solution(arr):
    answer = [arr[0]]
  
    for element in arr:
        if answer[-1] != element:
            answer.append(element)
    
    return answer
