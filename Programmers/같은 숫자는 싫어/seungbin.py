def solution(arr):
    ans = []
    ans.append(arr[0]) #처음은 중복X
    x=arr[0] #비교 위해 저장
    
    for i in arr:
        #앞과 다르면 추가
        if i != x:
            ans.append(i)
            print(i)
        else:
            continue
        x=i #x값 초기화
    
    return ans
