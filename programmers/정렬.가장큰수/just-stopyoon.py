from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:  # x를 앞에 두는 경우가 더 큰 수가 되는 경우
        return -1
    elif x + y < y + x:  # y를 앞에 두는 경우가 더 큰 수가 되는 경우
        return 1
    else:
        return 0

def solution(numbers):
    numbers = list(map(str, numbers)) # 숫자를 문자열로 변환    
    numbers.sort(key=cmp_to_key(compare)) # 정렬 (커스텀 비교 함수 사용)
    result = ''.join(numbers) # 정렬된 리스트를 합쳐서 결과 반환
    return '0' if result[0] == '0'else result # "0000" 같은 경우를 방지
