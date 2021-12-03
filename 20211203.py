# 숫자 문자열과 영단어
# 문제 설명
# 네오와 프로도가 숫자놀이를 하고 있습니다.
# 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.
# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"
# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다.
# s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

# 참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

# 숫자	영단어
# 0	zero
# 1	one
# 2	two
# 3	three
# 4	four
# 5	five
# 6	six
# 7	seven
# 8	eight
# 9	nine
# 제한사항
# 1 ≤ s의 길이 ≤ 50
# s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
# return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.
# 입출력 예
# s	                result
# "one4seveneight"	1478
# "23four5six7"	    234567
# "2three45sixseven"	234567
# "123"	            123

s = "one4seveneight"
# s = "23four5six7"


def solution(s):
    table = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
             'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for i in table:
        s = s.replace(i, table[i])
    return int(s)


print(solution(s))

# 시저 암호
# 문제 설명
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는
# 암호화 방식을 시저 암호라고 합니다.
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다.
# "z"는 1만큼 밀면 "a"가 됩니다.
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수,
# solution을 완성해 보세요.

# 제한 조건
# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.
# 입출력 예
# s	        n	result
# "AB"	    1	"BC"
# "z"	    1	"a"
# "a B z"	4	"e F d"


# s = str(input())
# n = int(input())

# s = "a B z"
# n = 4


# def solution(s, n):
#     answer = ''
#     for i in s:
#         a = ord(i)
#         if ord('A') <= a <= ord('Z'):
#             if a+n > ord('Z'):
#                 a += n-26
#             else:
#                 a += n
#         elif ord('a') <= a <= ord('z'):
#             if a+n > ord('z'):
#                 a += n-26
#             else:
#                 a += n
#         else:
#             a = 32
#         answer += chr(a)

#     return answer


# print(solution(s, n))
