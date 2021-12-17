# 크레인 인형뽑기 게임
# 문제 설명
# 게임개발자인 "죠르디"는 크레인 인형뽑기 기계를 모바일 게임으로 만들려고 합니다.
# "죠르디"는 게임의 재미를 높이기 위해 화면 구성과 규칙을 다음과 같이 게임 로직에 반영하려고 합니다.

# crane_game_101.png

# 게임 화면은 "1 x 1" 크기의 칸들로 이루어진 "N x N" 크기의 정사각 격자이며
# 위쪽에는 크레인이 있고 오른쪽에는 바구니가 있습니다. (위 그림은 "5 x 5" 크기의 예시입니다).
# 각 격자 칸에는 다양한 인형이 들어 있으며 인형이 없는 칸은 빈칸입니다.
# 모든 인형은 "1 x 1" 크기의 격자 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓여 있습니다.
# 게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있습니다.
# 집어 올린 인형은 바구니에 쌓이게 되는 데, 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됩니다.
# 다음 그림은 [1번, 5번, 3번] 위치에서 순서대로 인형을 집어 올려 바구니에 담은 모습입니다.


# 만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다.
# 위 상태에서 이어서 [5번] 위치에서 인형을 집어 바구니에 쌓으면 같은 모양 인형 두 개가 없어집니다.


# 크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는
# 아무런 일도 일어나지 않습니다.
# 또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다.
# (그림에서는 화면표시 제약으로 5칸만으로 표현하였음)

# 게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해
# 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때,
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
# board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
# 0은 빈 칸을 나타냅니다.
# 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
# moves 배열의 크기는 1 이상 1,000 이하입니다.
# moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.
# 입출력 예
# board
# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves                 result
# [1,5,3,5,1,2,1,4]	    4

# board = [[0, 0, 0, 0, 0],
#          [0, 0, 1, 0, 3],
#          [0, 2, 5, 0, 1],
#          [4, 2, 4, 4, 2],
#          [3, 5, 1, 3, 1]]
# moves = [1, 5, 3, 5, 1, 2, 1, 4]

# board = [[0, 0, 1, 0, 0],
#          [0, 0, 1, 0, 0],
#          [0, 2, 1, 0, 0],
#          [0, 2, 1, 0, 0],
#          [0, 2, 1, 0, 0]]
# 1
# moves = [1, 2, 3, 3, 2, 3, 1]


# def solution(board, moves):
#     result = 0
#     basket = []
#     for i in moves:
#         for j in board:
#             if j[i-1] != 0:
#                 basket.append(j[i-1])
#                 j[i-1] = 0
#                 break
#         if len(basket) > 1:
#             if basket[-1:] == basket[-2:-1]:
#                 basket.pop(-2)
#                 basket.pop(-1)
#                 result += 2
#     return result


# print(solution(board, moves))


# == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 문제 설명
# 어떤 정수들이 있습니다.
# 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은
# 불리언 배열 signs가 매개변수로 주어집니다.
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# absolutes의 길이는 1 이상 1,000 이하입니다.
# absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
# signs의 길이는 absolutes의 길이와 같습니다.
# signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.
# 입출력 예
# absolutes	signs	            result
# [4,7,12]	[true,false,true]	9
# [1,2,3]	[false,false,true]	0


# absolutes = [4, 7, 12]
# signs = [True, False, True]


# def solution(absolutes, signs):
#     return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))


# print(solution(absolutes, signs))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 내적
# 문제 설명
# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다.
# a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

# 이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

# 제한사항
# a, b의 길이는 1 이상 1,000 이하입니다.
# a, b의 모든 수는 -1,000 이상 1,000 이하입니다.
# 입출력 예
# a	        b	            result
# [1,2,3,4]	[-3,-1,0,2]	    3
# [-1,0,1]	[1,0,-1]	    -2

# a = [1, 2, 3, 4]
# b = [-3, -1, 0, 2]


# def solution(a, b):
#     return sum(x*y for x, y in zip(a, b))

# print(solution(a, b))
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 완주하지 못한 선수
# 문제 설명
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다.
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.
# 입출력 예
# participant
# ["leo", "kiki", "eden"]
# ["marina", "josipa", "nikola", "vinko", "filipa"]
# ["mislav", "stanko", "mislav", "ana"]
# completion	                                return
# ["eden", "kiki"]	                            "leo"
# ["josipa", "filipa", "marina", "nikola"]	    "vinko"
# ["stanko", "ana", "mislav"]	                "mislav"

import collections
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(part, comp):
    result = collections.Counter(part) - collections.Counter(comp)
    return ''.join(result)


print(solution(participant, completion))
