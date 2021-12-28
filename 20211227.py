# [1차] 다트 게임
# 문제 설명
# 다트 게임
# 카카오톡에 뜬 네 번째 별! 심심할 땐? 카카오톡 게임별~

# 카카오톡 게임별의 하반기 신규 서비스로 다트 게임을 출시하기로 했다.
# 다트 게임은 다트판에 다트를 세 차례 던져 그 점수의 합계로 실력을 겨루는 게임으로, 모두가 간단히 즐길 수 있다.
# 갓 입사한 무지는 코딩 실력을 인정받아 게임의 핵심 부분인 점수 계산 로직을 맡게 되었다.
# 다트 게임의 점수 계산 로직은 아래와 같다.

# 다트 게임은 총 3번의 기회로 구성된다.
# 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시
# 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 옵션으로 스타상(*) , 아차상(#)
# 이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다.
# 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# 스타상(*)은 첫 번째 기회에서도 나올 수 있다.
# 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다.
# 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다.
# 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
# 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

# 입력 형식
# "점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
# 예) 1S2D*3T

# 점수는 0에서 10 사이의 정수이다.
# 보너스는 S, D, T 중 하나이다.
# 옵선은 *이나 # 중 하나이며, 없을 수도 있다.
# 출력 형식
# 3번의 기회에서 얻은 점수 합계에 해당하는 정수값을 출력한다.
# 예) 37

# 입출력 예제
# 예제	dartResult	answer	설명
# 1	    1S2D*3T	    37	11 * 2 + 22 * 2 + 33
# 2	    1D2S#10S	9	12 + 21 * (-1) + 101
# 3	    1D2S0T	    3	12 + 21 + 03
# 4	    1S*2T*3S	23	11 * 2 * 2 + 23 * 2 + 31
# 5	    1D#2S*3S	5	12 * (-1) * 2 + 21 * 2 + 31
# 6	    1T2D3D#	    -4	13 + 22 + 32 * (-1)
# 7	    1D2S3T*	    59	12 + 21 * 2 + 33 * 2

# import re


# def add_option(n, s, i):
#     if i == 0:
#         return

#     return True if s == '*' else False


# def num_option(n, s):
#     if s == "S":
#         return n
#     elif s == "D":
#         return n**2
#     elif s == "T":
#         return n**3
#     return


# def solution(dartResult):
#     dart_num = list(filter(None, re.split('[^0-9]', dartResult)))
#     dart_option = list(filter(None, re.split('[^S|D|T|#|*]', dartResult)))
#     answer = []
#     for i in range(len(dart_option)):
#         if len(dart_option[i]) == 1:
#             answer.append(num_option(int(dart_num[i]), dart_option[i]))
#         elif len(dart_option[i]) == 2:
#             if i == 0:
#                 num = num_option(int(dart_num[i]), dart_option[i][0])
#                 add = add_option(dart_option[i][1])
#                 if add:
#                     answer.append(num * 2)
#                 else:
#                     answer.append(num*-1)
#             else:
#                 num = num_option(int(dart_num[i]), dart_option[i][0])
#                 add = add_option(dart_option[i][1])
#                 if add:
#                     answer.append(answer[-1])
#                     answer.append(num * 2)
#                 else:
#                     answer.append(num*-1)
#         else:
#             continue

#     return sum(answer)


# print(solution('1D#2S*3S'))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 3진법 뒤집기
# 문제 설명
# 자연수 n이 매개변수로 주어집니다.
# n을 3진법 상에서 앞뒤로 뒤집은 후,
# 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.
# 입출력 예
# n	    result
# 45	7
# 125	229


# d = 45


# def solution(d):
#     n = 3

#     tmp = ''
#     while d:
#         tmp += str(d % n)
#         d = d // n

#     return int(str(tmp), 3)


# print(solution(d))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == =


# 2016년
# 문제 설명
# 2016년 1월 1일은 금요일입니다.
# 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아
# 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
# 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT
# 입니다.
# 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

# 제한 조건
# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
# 입출력 예
# a	    b	result
# 5	    24	"TUE"

# a = 5
# b = 24


# def solution(a, b):
#     week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
#     month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#     return week[(sum(month[:a-1])+b-1) % 7]


# print(solution(a, b))
