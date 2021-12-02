# 두 개 뽑아서 더하기

# [문제]
# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더 해서
# 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# numbers의 길이는 2이상 100 이하 입니다.
# numbers의 모든 수는 0 이상 100 이하입니다.

numbers = [2, 1, 3, 4, 1]


def solution(numbers):
    answer = []
    count = len(numbers)
    for i in numbers:
        for j in numbers[:-count]:
            answer.append(i+j)

        count -= 1

    return sorted(list(set(answer)))

# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i]+numbers[j])
#             print(f"i={i} / j={j} / answer={answer}")

#     return sorted(list(set(answer)))


print(solution(numbers))
