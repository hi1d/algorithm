# K번째 수

# [문제]
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

# 예 ) array가 [1,5,2,6,3,7,4]
#     i = 2
#     j = 5
#     k = 3 이라면,

#     1.array의 2번째부터 5번째까지 자르면 [5,2,6,3]입니다.
#     2. 1에서 나온 배열을 정렬하면 [2,3,5,6]입니다.
#     3. 2에서 나온 배열의 3번째 숫자는 5 입니다.

# 배열 array, [i,j,k]를 원소를 가진 2차원 배열 commands가 매개변수로 주어 질 때,
# commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록
# solution 함수를 작성하라.

# [제한사항]
# 1. array의 길이는 1 이상 100 이하
# 2. array의 각 원소는 1이상 100 이하
# 3. commands의 길이는 1이상 50 이하
# 4. commands의 각 원소는 길이가 3


def solution(array, commands):
    answer = []
    for a in commands:
        a_slice = array[(a[0]-1):a[1]]
        a_slice.sort()
        answer.append(a_slice[(a[2]-1)])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))


# ====================첫 시도======================
# def solution(commands):
#     data = commands[0][0][i-1:j]
#     data.sort()
#     data = data[k-1]
#     return data


# array = []
# state = True
# while state:
#     print("Array 입력 (입력 종료 : 0)")
#     array_data = int(input())

#     if 0 < array_data < 100 and 0 < len(array) + 1 < 102:
#         array.append(array_data)
#     else:
#         state = False

# print("i 입력")
# i = int(input())
# print("j 입력")
# j = int(input())
# print("k 입력")
# k = int(input())

# commands = [[0] * 1 for a in range(2)]
# commands[0][0] = array
# commands[1][0] = i, j, k

# print(solution(commands))
