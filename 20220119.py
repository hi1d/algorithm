# Hello Goorm !

# 이 문제는 여러분이 입력하신 숫자만큼 'Hello Goorm !'을 출력하면 되는 기본적인 문제입니다.

# 입력

# 100 이하의 자연수

# 출력

# 입력한 수 만큼 Hello Goorm !


# 입출력 예 1)

# 입력: 1

# 출력: Hello Goorm !


# 입출력 예 2)

# 입력: 5

# 출력:

# Hello Goorm !

# Hello Goorm !

# Hello Goorm !

# Hello Goorm !

# Hello Goorm !

# user_input = input()
# for i in range(user_input):
#     print("Hello Goorm !")

# ==============================================================

# 삼각형의 넓이

# 입력받은 밑변과 높이를 이용하여 삼각형의 넓이를 구하는 프로그램을 작성하십시오.


# 입력

# 밑변과 높이 순서대로 (정수형, 간격은 공백으로)

# 출력

# 삼각형의 넓이( 소수점 첫 번째 자리까지)

# 입/출력 예시

# 예시 1
# 입력
# 5010
# 출력
# 250.0
# 예시 2
# 입력
# 3892
# 출력
# 1748.0

# w, h = input().split()
# print((int(w)*int(h))/2)

# ==============================================================

# 공백 없애기

# 이 문제는 입력된 문자열에서 공백을 제거하여 출력하는 프로그램을 작성하는 것 입니다.

# 예를 들어 "This is Sparta !" 가 입력 되었다면 "ThisisSparta!"가 출력되도록 하면 되는 것 입니다.

# 입력

# 50자 이내의 문장

# 출력

# 입력에서 공백이 제거된 문장 ( 입출력 예시 참고 )


# 입/출력 예시
# 예시 1
# 입력
# IamGoorm!
# 출력
# IamGoorm!
# 예시 2
# 입력
# ThisisSparta
# 출력

# user_input = input()
# output = user_input.replace(' ', '')
# print(output)

# ==============================================================
# Bubble Sort

# Bubble sort는 인접한 원소를 검사하여 정렬하는 것을 반복하는 정렬이다.
# Time complexity면에서는 좋지 않지만 단순하게 작성할 수 있는 장점이 있어서 자주 사용된다.
# Bubble sort로 오름차순 정렬을 진행하는 프로그램을 작성하십시오.


# 입력

# 첫 번째 줄에 Bubble 정렬을 진행할 수(들)의 개수를 입력하고

# 둘째 줄에 해당 개수에 맞게 수를 입력한다.

# 출력

# Bubble sort가 완료된 형태의 수열


# 입/출력 예시

# 예시 1
# 입력
# 5
# 96327
# 출력
# 23679
# 예시 2
# 입력
# 3
# 321
# 출력
# 123

# count = input()
# array = input().split()

# for i in range(len(array)):
#     for j in range(i+1, len(array)):
#         if array[i] > array[j]:
#             array[i], array[j] = array[j], array[i]

# print(' '.join(array))

# ==============================================================
# 거스름돈

# 모든 물건의 값이 1000원 이하인 가게가 있습니다.
# 이곳에서 파는 물건들의 가격대비 품질이 좋아서 하루에 하나의 제품만 구매할 수 있음에도 불구하고 항상 손님이 붐빈다고 합니다.

# 직원들의 수고를 덜어주기 위해 거스름돈을 거슬러주는 일을 자동으로 해주는 프로그램을 만들려고 합니다.
# 1000원을 받고 500원, 100원, 50원 그리고 10원으로 단위가 큰 동전을 우선으로 거슬러주는 프로그램을 작성하십시오.


# 입력

# 물건 가격 (일의 자리는 0인 1000 이하의 자연수)

# 출력

# 500원, 100원, 50원, 10원 순으로 거스름돈 동전의 수


# 입/출력 예시
# 예시 1
# 입력
# 430
# 출력
# 1012
# 예시 2
# 입력
# 770
# 출력
# 0203

# user_input = int(input())
# num = 1000 - user_input
# num_list = [0, 0, 0, 0]
# num_list[0] = str(num // 500)
# num -= (500*int(num_list[0]))
# num_list[1] = str(num // 100)
# num -= (100*int(num_list[1]))
# num_list[2] = str(num // 50)
# num -= (50*int(num_list[2]))
# num_list[3] = str(num // 10)
# num -= (10*int(num_list[3]))
# print(' '.join(num_list))

# ==============================================================

# 가장 큰 수
# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
# 입출력 예
# numbers	            return
# [6, 10, 2]	        "6210"
# [3, 30, 34, 5, 9]	    "9534330"

# numbers = [6, 10, 2]


# def solution(numbers):
#     str_num = list(map(str, numbers))
#     str_num.sort(key=lambda x: x*3, reverse=True)

#     return str(int(''.join(str_num)))


# print(solution(numbers))

# ==============================================================

import re
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"


def solution(s):
    s = re.split('[{}]', s)
    s.sort(key=lambda x: len(x))
    result = []
    for i in s:
        if i != ',' and i != '':
            i = i.split(',')
            for j in i:
                if int(j) not in result:
                    result.append(int(j))
    return result


print(solution(s))
