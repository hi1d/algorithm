# [없는 숫자 더하기]

# [문제]
# 0부터 9까지의 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# 1 <= numbers의 길이 <= 9
# 0 <= numbers의 모든 수 <= 9
# numbers의 모든 수는 서로 다릅니다.

# 입출력 예
# numbers	        result
# [1,2,3,4,6,7,8,0]	14
# [5,8,4,0,6,7,9]	6

# numbers = [1, 2, 3, 4, 6, 7, 8, 0]
# numbers2 = [5, 8, 4, 0, 6, 7, 9]


# def solution(numbers):
#     return 45-sum(numbers)

# def solution(x): return sum(range(10))-sum(x)


# ==================================================================================

# [실패율]
# 슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다.
# 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다.
# 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

# 이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다.
# 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다.
# 오렐리를 위해 실패율을 구하는 코드를 완성하라.

# 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
# stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로
# 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

# 제한사항
# 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
# stages의 길이는 1 이상 200,000 이하이다.
# stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
# 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
# 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
# 입출력 예

# N	    stages                  	result
# 5	    [2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
# 4	    [4,4,4,4,4]	                [4,1,2,3]

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 4
# stages = [4,4,4,4,4]


def solution(N, stages):
    failed_rate = {i+1: 0 for i in range(N)}  # 0으로 초기화
    total_user = len(stages)

    for i in range(1, N+1):
        if total_user != 0:  # devision by zero 오류 방지 (0으로 나눌수 없다.)
            stage_user = stages.count(i)
            failed_rate[i] = stage_user / total_user
            total_user -= stage_user
        else:                # Keyerror 방지
            failed_rate[i] = 0

    return sorted(failed_rate, key=lambda x: failed_rate[x], reverse=True)

    # failed = sorted(failed_rate.items(), key=lambda x: x[1], reverse=True)
    # failed_rate = [i[0] for i in failed]
    # return failed_rate


print(solution(N, stages))

# =================== 두번째 시도 (성공) =============================
# N = 100
# stages = [2, 1, 2, 6, 2, 4, 3, 3]


# def solution(N, stages):
#     failed_rate = {}
#     total_user = len(stages)

#     for i in range(1, N+1):
#         if total_user != 0:
#             stage_user = stages.count(i)
#             failed_rate[i] = stage_user / total_user
#             total_user -= stage_user
#         else:
#             failed_rate[i] = 0
#     failed = sorted(failed_rate.items(), key=lambda x: x[1], reverse=True)
#     failed_rate = [i[0] for i in failed]
#     return failed_rate


# print(solution(N, stages))

# =================== 첫 시도 =============================
# def solution(N, stages):
#     answer = []
#     failed = {}
#     success_person = 0
#     failed_person = 0
#     #실패율 구하는 반복문
#     for i in range(1,N+1): # 해당 스테이지
#         for j in stages: # 해당 스테이지의 유저
#             if i < j:
#                 success_person += 1 # 스테이지 성공한 사람
#             elif i == j:
#                 failed_person += 1 # 스테이지 실패한 사람

#         failed_rate = failed_person / (success_person + failed_person)
#         #실패율 = 스테이지에 도달 했으나 실패한 플레이어 수 / 해당 스테이지에 도달 한 플레이어 수
#         failed[i] = failed_rate
#         success_person = 0
#         failed_person = 0

#     #실패율에 따른 정렬
#     failed = sorted(failed.items(),key = lambda item: item[1],reverse=True)
#     # failed 딕셔너리의 item 들을
#     # key = lambda item: item[1] // item[1] == value값으로 정렬한다.
#     # lambda 표현식의 의미는
#     # item이라는 매개변수를 가져와서 item의 1번째 인덱스 key[0]:value[1] 인 value값을 반환한다.
#     # sorted의 key에는 호출될 수 있는 함수가 들어간다. 함수 외 입력시 not callable 에러 발생.
#     for x in failed:
#         answer.append(x[0])

#     return answer
