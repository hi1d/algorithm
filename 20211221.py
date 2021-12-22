# 체육복
# 문제 설명
# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다.
# 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
# 학생들의 번호는 체격 순으로 매겨져 있어,
# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
# 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
# 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
# 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
# 입출력 예
# n	lost	reserve	    return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	        4
# 3	[3]	    [1]	        2

# n = 5
# lost = [2, 4]
# reserve = [3]


# def solution(n, lost, reserve):
#     lost.sort()
#     reserve.sort()
#     for i in reserve[:]:
#         if i in lost:
#             lost.remove(i)
#             reserve.remove(i)
#     for i in lost[:]:
#         if i-1 in reserve[:]:
#             lost.remove(i)
#             reserve.remove(i-1)
#         elif i+1 in reserve[:]:
#             lost.remove(i)
#             reserve.remove(i+1)

#     return n-len(lost)


# print(solution(n, lost, reserve))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 최소직사각형
# 문제 설명
# 명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다. 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서,
# 작아서 들고 다니기 편한 지갑을 만들어야 합니다.
# 이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.

# 아래 표는 4가지 명함의 가로 길이와 세로 길이를 나타냅니다.

# 명함 번호	가로 길이	세로 길이
# 1	60	50
# 2	30	70
# 3	60	30
# 4	80	40
# 가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑을 만들면 모든 명함들을 수납할 수 있습니다.
# 하지만 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다.
# 이때의 지갑 크기는 4000(=80 x 50)입니다.

# 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다.
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# sizes의 길이는 1 이상 10,000 이하입니다.
# sizes의 원소는 [w, h] 형식입니다.
# w는 명함의 가로 길이를 나타냅니다.
# h는 명함의 세로 길이를 나타냅니다.
# w와 h는 1 이상 1,000 이하인 자연수입니다.
# 입출력 예
# sizes	                                            result
# [[60, 50], [30, 70], [60, 30], [80, 40]]	        4000
# [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	    120
# [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	    133

# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]


# def solution(sizes):
#     max_w = 0
#     max_h = 0
#     for i, j in sizes:
#         if i < j:
#             i, j = j, i
#         max_w = max(max_w, i)
#         max_h = max(max_h, j)

#     return max_w * max_h


# print(solution(sizes))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 문자열 내림차순으로 배치하기
# 문제 설명
# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

# 제한 사항
# str은 길이 1 이상인 문자열입니다.
# 입출력 예
# s	        return
# "Zbcdefg"	"gfedcbZ"

s = "Zbcadefg"


# def solution(s):
#     list = []
#     for i in s:
#         list.append(ord(i))
#     list.sort(reverse=True)
#     for i in range(len(list)):
#         list[i] = chr(list[i])

#     return ''.join(list)

def solution(s):
    return ''.join(sorted(s, reverse=True))


print(solution(s))