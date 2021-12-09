# 1~9까지의 정수값을 가지는 N에 대하여 오름차순으로 정리된 숫자 n이 있다고합시다
# 예를 들어 N = 5 일때 n = 12345,  N = 8 이면 n = 12345678 입니다
# N값이 주어졌을때 같은 길이의 (9부터 시작하는) 역순으로 이루어진 숫자 n을 출력하는 함수 solution(N)을 작성해주세요
# 결과값 예시)
# N = 5, n = 12345  ->  answer = 98765
# N = 8, n = 12345678  ->  answer = 98765432

N = 9


def solution(N):
    num = list(i for i in range(1, 10))
    reverse_num = num[:-N-1:-1]
    return reverse_num


print(solution(N))

# 이상한 문자 만들기
# 문제 설명
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
# 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
# 각 단어의 짝수번째 알파벳은 대문자로,
# 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

# 제한 사항
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
# 입출력 예
# s	                    return
# "try hello world"	    "TrY HeLlO WoRlD"
s = "try hello world"


# def solution(s):
#     split_list = s.split(' ')
#     result = []
#     for i in split_list:
#         print("i = ", i)
#         answer = ''
#         for j in range(len(i)):
#             print("j= ", j)
#             if j % 2 == 0:
#                 answer += i[j].upper()
#             else:
#                 answer += i[j].lower()
#         result.append(answer)
#     return ' '.join(result)


# print(solution(s))
