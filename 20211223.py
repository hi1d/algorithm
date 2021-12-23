# 나누어 떨어지는 숫자 배열
# 문제 설명
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

# 제한사항
# arr은 자연수를 담은 배열입니다.
# 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
# divisor는 자연수입니다.
# array는 길이 1 이상인 배열입니다.
# 입출력 예
# arr	            divisor	return
# [5, 9, 7, 10]	    5	    [5, 10]
# [2, 36, 1, 3]	    1	    [1, 2, 3, 36]
# [3,2,6]	        10	    [-1]

# array = [5, 9, 7, 10]
# divisor = 5


# def solution(array, divisor):
#     answer = [i for i in array if i % divisor == 0]
#     answer.sort()
#     return answer if len(answer) != 0 else [-1]


# print(solution(array, divisor))

# == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 약수의 합
# 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 제한 사항
# n은 0 이상 3000이하인 정수입니다.
# 입출력 예
# n	    return
# 12	28
# 5	    6

# n = 12


# def solution(n):
#     return sum([i for i in range(1, n+1) if n % i == 0])


# print(solution(n))

# == == == == == == == == == == == == == == == == == == == == == == == == == == =

# 정수 제곱근 판별
# 문제 설명
# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

# 제한 사항
# n은 1이상, 50000000000000 이하인 양의 정수입니다.
# 입출력 예
# n	    return
# 121	144
# 3	    -1

n = 3


# def solution(n):
#     n = n**(1/2)
#     n = str(n).split('.')
#     if len(n[1]) != 1:
#         return -1

#     return (int(''.join(n[0]))+1)**2


# print(solution(n))

# == == == == == == == == == == == == == == == == == == == == == == == == == == =

# 약수의 개수와 덧셈
# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다.
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고,
# 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ left ≤ right ≤ 1,000
# 입출력 예
# left	right	result
# 13	17	    43
# 24	27	    52

# left = 13
# right = 17


# def solution(left, right):
#     list = 0
#     for i in range(left, right+1):
#         count = 0
#         for j in range(1, i+1):
#             if i % j == 0:
#                 count += 1
#         if count % 2:
#             list -= i
#         else:
#             list += i
#     return list


# print(solution(left, right))

# == == == == == == == == == == == == == == == == == == == == == == == == == == =


# 최대공약수와 최소공배수
# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.
# 입출력 예
# n	    m	return
# 3	    12	[3, 12]
# 2	    5	[1, 10]

# n = 3
# m = 12

# def solution(n, m):
#     n_measure = {i for i in range(1, n+1) if n % i == 0}
#     m_measure = {j for j in range(1, m+1) if m % j == 0}

#     max_measure = max(n_measure & m_measure)
#     min_multiple = int(n*m/max_measure)

#     return [max_measure, min_multiple]


# print(solution(n, m))
# == == == == == == == == == == == == == == == == == == == == == == == == == == =

# 소수 찾기
# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.
# 입출력 예
# n	    result
# 10	4
# 5	    3

n = 10


def solution(n):
    sieve = [True] * int(n+1)
    list = []
    for i in range(2, int(n**0.5) + 1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    for i in range(2, n+1):
        if sieve[i] == True:
            list.append(i)
    return len(list)


print(solution(n))
