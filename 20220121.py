# H-Index
# 문제 설명
# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
# 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
# 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

# 어떤 과학자가 발표한 논문 n편 중,
# h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,
# 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
# 입출력 예
# citations	        return
# [3, 0, 6, 1, 5]	3

# citations = [3, 0, 6, 1, 5]
# citations = [41, 24]
# citations = [0, 0, 0, 0, 0]
# citations = [9, 9, 9, 12]
# citations = [1, 1, 5, 7, 6]


# def solution(citations):
#     citations.sort(reverse=True)
#     for i, j in enumerate(citations):
#         if i == j:
#             return j
#         elif i > j:
#             return i

#     return len(citations)


# print(solution(citations))

# == == == == == == == == == == == == == == == == == == == == == == == == =
# 기능개발
# 문제 설명
# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다.
# 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
# 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와
# 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때
# 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

# 제한 사항
# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다.
# 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
# 입출력 예
# progresses	            speeds	            return
# [93, 30, 55]	            [1, 30, 5]	        [2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]


progresses = [93, 30, 55, 60, 40, 65]
speeds = [1, 30, 5, 10, 60, 7]


# def solution(progresses, speeds):
#     result = []
#     while len(progresses) != 0:
#         if progresses[0] >= 100:
#             result[-1] += 1
#             progresses.pop(0)
#             speeds.pop(0)
#             continue
#         progresses = list(map(lambda x, y: x+y, progresses, speeds))
#         if progresses[0] >= 100:
#             result.append(1)
#             progresses.pop(0)
#             speeds.pop(0)

#     return result


# print(solution(progresses, speeds))

# == == == == == == == == == == == == == == == == == == == == == == == == =


# 모의고사
# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다.
# 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	    return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

# answers = [1, 2, 3, 4, 5]
# answers = [3, 3, 2, 1, 5]
# -> [3]
answers = [5, 5, 4, 2, 3]
#  -> [1,2,3]


def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    student = {1: 0, 2: 0, 3: 0}

    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]:
            student[1] += 1
        if answers[i] == s2[i % len(s2)]:
            student[2] += 1
        if answers[i] == s3[i % len(s3)]:
            student[3] += 1
    max_score = max(student.values())
    return [i for i, j in student.items() if j == max_score]


print(solution(answers))
