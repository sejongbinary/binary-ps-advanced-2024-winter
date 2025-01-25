def solution(arr):
    answer = []
    answer.append(arr[0])
    for num in arr : # 어차피 첫 번째 숫자는 같은 숫자이므로 push가 안되니 처음부터 진행
        if num == answer[-1] : # 같은 숫자라면
            continue # 넘어감
        else : # 다른 숫자라면
            answer.append(num) # 추가
    return answer
