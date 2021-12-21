# 자릿수 더하기
# 문제 설명
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# 제한사항
# N의 범위 : 100,000,000 이하의 자연수
# 입출력 예
# N	answer
# 123	6
# 987	24

N = 123


def solution(n):
    return sum(int(i) for i in str(n))


print(solution(N))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

# 서울에서 김서방 찾기
# 문제 설명
# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아,
# "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요.
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# 제한 사항
# seoul은 길이 1 이상, 1000 이하인 배열입니다.
# seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# "Kim"은 반드시 seoul 안에 포함되어 있습니다.
# 입출력 예
# seoul 	        return
# ["Jane", "Kim"]	"김서방은 1에 있다"

seoul = ["Jane", "Kim"]


def solution(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다"


print(solution(seoul))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

# 문자열 내 p와 y의 개수
# 문제 설명
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

# 제한사항
# 문자열 s의 길이 : 50 이하의 자연수
# 문자열 s는 알파벳으로만 이루어져 있습니다.
# 입출력 예
# s	        answer
# "pPoooyY"	true
# "Pyy"	    false

s = "pPoooyY"


def solution(s):
    return s.lower().count('p') == s.lower().count('y')


print(solution(s))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

# 부족한 금액 계산하기
# 문제 설명
# 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다.
# 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다.
# 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
# 단, 금액이 부족하지 않으면 0을 return 하세요.

# 제한사항
# 놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
# 처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
# 놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수
# 입출력 예
# price 	money	count	result
# 3	        20	    4	    10

price = 3
money = 20
count = 4


def solution(price, money, count):

    for i in range(1, count+1):
        money -= price*i
    if money > 0:
        return 0
    return abs(money)


print(solution(price, money, count))
