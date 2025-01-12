from collections import defaultdict

def solution(participant, completion):
    completion_dict = defaultdict(int)

    for player in completion:
        completion_dict[player] += 1

    for player in participant:
        completion_dict[player] -= 1
        if completion_dict[player] < 0:
            answer = player
            break

    return answer
