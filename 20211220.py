# 직사각형 별찍기
# 문제 설명
# 이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

# 제한 조건
# n과 m은 각각 1000 이하인 자연수입니다.

# 예시
# 입력

# 5 3
# 출력

# *****
# *****
# *****

# n, m = map(int, input().strip().split(' '))

# print(('*'*n+'\n')*m)

# == == == == == == == == == == == == == == == == == == == == == == == == == == =

# x만큼 간격이 있는 n개의 숫자
# 문제 설명
# 함수 solution은 정수 x와 자연수 n을 입력 받아,
# x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

# 제한 조건
# x는 -10000000 이상, 10000000 이하인 정수입니다.
# n은 1000 이하인 자연수입니다.
# 입출력 예
# x	    n	answer
# 2	    5	[2,4,6,8,10]
# 4	    3	[4,8,12]
# -4	2	[-4, -8]

# x = 2
# n = 5


# def solution(x, n):

#     return [x*i for i in range(1, n+1)]


# print(solution(x, n))

# == == == == == == == == == == == == == == == == == == == == == == == == == == =

# 문제 설명
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
# 입출력 예
# arr1	            arr2	        return
# [[1,2],[2,3]]	    [[3,4],[5,6]]	[[4,6],[7,9]]
# [[1],[2]]	        [[3],[4]]	    [[4],[6]]

arr1 = [[1, 2, 3, 1], [4, 5, 6, 4], [7, 8, 9, 1]]
arr2 = [[2, 3, 4, 2], [5, 6, 7, 5], [8, 9, 1, 2]]

# 0       1
# 1, 2     2, 3
# 3, 4     5, 6

# arr1 : [[1, 2, 3, 4], [4, 5, 6, 7], [1, 2, 3, 3]]
# arr2 : [[3, 2, 1, 5], [6, 5, 4, 9], [4, 5, 6, 7]]
# answer : [[4, 4, 4, 9], [10, 10, 10, 16], [5, 7, 9, 10]]


# def solution(arr1, arr2):
#     answer = [[] for i in range(len(arr1))]

#     for i in range(len(arr1)):
#         for j in range(len(arr1[i])):
#             answer[i].append(arr1[i][j]+arr2[i][j])

#     return answer


# print(solution(arr1, arr2))

# == == == == == == == == == == == == == == == == == == == == == == == == == == =

# 콜라츠 추측
# 문제 설명
# 1937년 Collatz란 사람에 의해 제기된 이 추측은,
# 주어진 수가 1이 될때까지 다음 작업을 반복하면,
# 모든 수를 1로 만들 수 있다는 추측입니다.
# 작업은 다음과 같습니다.

# 1-1. 입력된 수가 짝수라면 2로 나눕니다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
# 예를 들어, 입력된 수가 6이라면 6→3→10→5→16→8→4→2→1 이 되어 총 8번 만에 1이 됩니다.
# 위 작업을 몇 번이나 반복해야하는지 반환하는 함수, solution을 완성해 주세요.
# 단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.

# 제한 사항
# 입력된 수, num은 1 이상 8000000 미만인 정수입니다.

# n = 626331


# def solution(num):
#     result = 0
#     while True:
#         if result > 500:
#             return -1
#         if num != 1:
#             if num % 2:
#                 num = num*3 + 1
#             else:
#                 num = num/2
#         else:
#             return result
#         result += 1
#     return


# print(solution(n))

# == == == == == == == == == == == == == == == == == == == == == == == == == == =


# 나머지가 1이 되는 수 찾기
# 문제 설명
# 자연수 n이 매개변수로 주어집니다.
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를
# return 하도록 solution 함수를 완성해주세요.
# 답이 항상 존재함은 증명될 수 있습니다.

# 제한사항
# 3 ≤ n ≤ 1,000,000
# 입출력 예
# n	result
# 10	3
# 12	11

# def solution(n):
#     return min([i for i in range(1, n) if n % i == 1])


# print(solution(10))
# == == == == == == == == == == == == == == == == == == == == == == == == == == =

# 제일 작은 수 제거하기
# 문제 설명
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수,
# solution을 완성해주세요.
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고,
# [10]면 [-1]을 리턴 합니다.

# 제한 조건
# arr은 길이 1 이상인 배열입니다.
# 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.
# 입출력 예
# arr	    return
# [4,3,2,1]	[4,3,2]
# [10]	    [-1]

# arr = [4, 3, 2, 1]


# def solution(arr):
#     if len(arr) > 1:
#         arr.pop(arr.index(min(arr)))
#         return arr
#     return [-1]


# print(solution(arr))

# == == == == == == == == == == == == == == == == == == == == == == == == == == =

# 같은 숫자는 싫어
# 문제 설명
# 배열 arr가 주어집니다.
# 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다.
# 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.

# 예를 들면,

# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 배열 arr의 크기 : 1,000,000 이하의 자연수
# 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
# 입출력 예
# arr	answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	[4,3]

arr = [4, 4, 4, 3, 3]


def solution(arr):
    answer = []

    for i in arr:
        if answer[-1:] == [i]:
            continue
        answer.append(i)

    return answer


print(solution(arr))
