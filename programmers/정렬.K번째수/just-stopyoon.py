def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        i = commands[a][0] - 1 # i번째 숫자
        j = commands[a][1] # j번째 숫자 (슬라이싱 고려해서 -1 안함)
        k = commands[a][2] - 1 # 배열은 0부터 시작하므로 1 빼기

        sorted_array = sorted(array[i:j])  # 정렬된 리스트 생성
        answer.append(sorted_array[k])  # k번째 요소 추가

    return answer
