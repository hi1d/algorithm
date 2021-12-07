# 피보나치 수
# 고령화 및 운동부족으로 급격한 체력저하에 시달리는 재명.
# 급하게 헬스장을 방문해 보지만 백신 2차 접종이 안된 관계로 입성에 실패한다.
# 어쩔 수 없이 생활 운동의 대표종목 중 하나인 계단 오르기에 도전하는데,

# [질문]
# 계단은 한번에 1칸 혹은 최대 2칸까지 뛸 수 있다.
# 고로 계단이 3개가 있다면 꼭대기까지 오를 수 있는 방법은 총 3가지일 것이다.
# N개의 계단이 있을때 꼭대기까지 오를 수 있는 총 방법의 수를 구하는 Solution(N)을 작성하시오.

# N = 10


# def solution(N):
#     if N < 2:
#         return N
#     else:
#         return solution(N-1) + solution(N-2)


# fib = []
# n = []
# for i in range(1, N):
#     fib.append(solution(i))
#     n.append(i)

# print("N= ", n)
# print("sol= ", fib)

# 하샤드 수
# 문제 설명
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

# 제한 조건
# x는 1 이상, 10000 이하인 정수입니다.
# 입출력 예
# arr	return
# 10	true
# 12	true
# 11	false
# 13	false

arr = 36


def solution(arr):
    answer = True
    num = str(arr)
    num_list = []
    for i in range(len(num)):
        num_list.append(int(num[i]))
    sum_num = sum(num_list)

    if arr % sum_num == 0:
        answer = True
    else:
        answer = False
    return answer


print(solution(arr))
