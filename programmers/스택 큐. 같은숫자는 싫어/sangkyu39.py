def solution(arr):
    arr.append(10)
    return [arr[i] for i in range(len(arr) - 1 ) if arr[i] != arr[i+1]]