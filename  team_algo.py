# https://programmers.co.kr/learn/courses/30/lessons/12912

# 두 정수 사이의 합

# 문제 설명
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

# 제한 조건
# a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
# a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
# a와 b의 대소관계는 정해져있지 않습니다.
# 입출력 예
# a	b	return
# 3	5	12
# 3	3	3
# 5	3	12

# def solution(a, b):
#     min_num = min(a, b)
#     max_num = max(a, b)

#     return sum(range(min_num, max_num+1))


# print(solution(5, 3))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

# 문자열 다루기 기본
# 문제 설명
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

# 제한 사항
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.

# import re
# s = "123b4a"


# def solution(s):
#     if len(s) == 4 or len(s) == 6:
#         s_filter = re.sub('[^0-9]', '*', s)
#         if '*' in s_filter:
#             return False
#         return True
#     return False


# print(solution(s))


# 자연수 뒤집어 배열로 만들기
# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.
# 입출력 예
# n	    return
# 12345	[5,4,3,2,1]


# n = 12345


# def solution(n):
#     return [i for i in str(n)[::-1]]


# print(solution(n))


# 가운데 글자 가져오기
# 문제 설명
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 재한사항
# s는 길이가 1 이상, 100이하인 스트링입니다.
# 입출력 예
# s	        return
# "abcde"	    "c"
# "qwer"	    "we"

# def solution(s):
#     return s[len(s)//2] if len(s) % 2 else s[len(s)//2-1]+s[len(s)//2]


# print(solution(s))

# == == == == == == == == == == == == == == == == == == == == == == == == == ==
# 핸드폰 번호 가리기
# 문제 설명
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한
# 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

# 제한 조건
# s는 길이 4 이상, 20이하인 문자열입니다.
# 입출력 예
# phone_number	return
# "01033334444"	"*******4444"
# "027778888"	"*****8888"
import re
# phone_number = "4444"


# def solution(phone_number):
#     if len(phone_number) == 4:
#         return phone_number
#     return re.sub('[0-9]', '*', phone_number, len(phone_number)-4)


# print(solution(phone_number))

# == == == == == == == == == == == == == == == == == == == == == == == == == ==

# 나머지가 1이 되는 수 찾기
# 문제 설명
# 자연수 n이 매개변수로 주어집니다.
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요.
# 답이 항상 존재함은 증명될 수 있습니다.

# 제한사항
# 3 ≤ n ≤ 1, 000, 000
# 입출력 예
# n	result
# 10	3
# 12	11
n = 15


def solution(n):
    return min([i for i in range(1, n) if n % i == 1])


print(solution(n))
