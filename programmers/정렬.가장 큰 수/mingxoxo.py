from functools import cmp_to_key

def custom_compare(a:str, b:str):
    return -1 if a + b > b + a else 1
    

def solution(numbers):
    answer = ''.join(sorted(map(str, numbers), key=cmp_to_key(custom_compare)))
    return str(int(answer))
