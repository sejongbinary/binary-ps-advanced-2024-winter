def solution(participant, completion):
    participant.sort() # 참가자 리스트 정렬
    completion.sort() # 완주자 리스트 정렬
    
    for p, c in zip(participant, completion): # 인덱스 값을 통해 비교
        if p != c: # 만약 완주하지 못한 참가자가 있다면,
            return p # 해당 값 반환 
    return participant[-1]  # 끝까지 차이가 없다면 마지막 사람이 미완주자
