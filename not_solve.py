
# == == == == == == == == == == == == == == == == == == == == == == == == ==
# 조이스틱
# 문제 설명
# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.

# ▲ - 다음 알파벳
# ▼ - 이전 알파벳(A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동(첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동(마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)
# 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
# 만들고자 하는 이름 name이 매개변수로 주어질 때,
# 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

# 제한 사항
# name은 알파벳 대문자로만 이루어져 있습니다.
# name의 길이는 1 이상 20 이하입니다.
# 입출력 예
# name          return
# "JEROEN"	    56
# "JAN"	        23


# def solution(name):
#     count = up_and_down(name)
#     notA = list(filter(lambda x: name[x] != 'A', range(1, len(name))))

#     return count

def up_and_down(name):
    count = 0
    for i in name.upper():
        count += min(ord('Z')+1-ord(i), ord(i)-ord('A'))
    return count


def solution(name):
    answer = up_and_down(name)
    notA = list(filter(lambda x: name[x] != 'A', range(len(name))))
    A = list(filter(lambda x: name[x] == 'A', range(len(name))))
    if len(notA) == 0:
        return 0
    elif len(A) == 0:
        return answer + len(name)-1
    right = list(filter(lambda x: x > len(name)/2, notA))
    print(right)
    left = list(filter(lambda x: x < len(name)/2, notA))
    print(left)
    name_len = len(name)
    if len(left) == 0:
        left_index = (name_len - right[0]) * 2
        right_left = min(name_len, left_index) - 1
    else:
        right_left_index = (name_len - right[0]) * 2 + left[-1]
        left_right_index = (left[-1] * 2) + name_len - right[0]
        right_left = min(name_len-1, left_right_index, right_left_index)

    return right_left + answer


print(solution("JEROEN"))   # 56
print(solution("ABAAAAAAAAABB"))  # 7
print(solution("JAN"))      # 23
print(solution("BBBAAAB"))  # 8
print(solution("ABABAAAAABA"))  # 10
print(solution("CANAAAAANAN"))  # 48
print(solution("ABAAAAABAB"))  # 8
print(solution("ABABAAAAAB"))  # 8
print(solution("BABAAAAB"))  # 7
print(solution("ABAAB"))    # 5
print(solution("AAA"))  # 0
print(solution("ABAAAAAAABA"))  # 6
print(solution("AAB"))  # 2
print(solution("AABAAAAAAABBB"))  # 11
print(solution("ZZZ"))  # 5
print(solution("BBBBAAAAAB"))  # 10
print(solution("BBBBAAAABA"))  # 12
print(solution("BBBBAABBB"))  # 15
print(solution("BAABA"))    # 4
print(solution("BBABAAAB"))    # 9


# print(solution("ABABA"))    # 5
# print(solution("BABAB"))    # 6


# == == == == == == == == == == == == == == == == == == == == == == == == ==


# 구명보트
# 문제 설명
# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다.
# 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

# 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면
# 2번째 사람과 4번째 사람은 같이 탈 수 있지만
# 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.
# 입출력 예
# people	        limit	return
# [70, 50, 80, 50]	100	    3
# [70, 80, 50]	    100	    3

# people = [40, 50, 150, 160]
# limit = 200
people = [70, 50, 80]
limit = 100
# people = [100, 500, 500, 900, 950]
# limit = 1000
# people = [40, 50, 60, 90]
# limit = 100


# def solution(people, limit):
#     people.sort(reverse=True)
#     test = list(filter(lambda x: sum(x) <=
#                 limit, combinations(people, 2)))
#     count = 0
#     test_list = []
#     for i in test:
#         if i[0] not in test_list and i[1] not in test_list:
#             count += 1
#             test_list.append(i[0])
#             test_list.append(i[1])
#     if len(test_list) == 0:
#         count += len(people)
#     else:
#         count += len(test_list)

#     return count


# print(solution(people, limit))



# ===========================================================================

# 문제 설명
# 은퇴 후 치킨집 사장님이 된 종윤이는 고된 연습 끝에 1분에 2마리의 치킨을 튀길 수 있게 되었다. 이 소식을 들은 성구는 치킨집의 번창을 위해 X 마리의 치킨을 주문하였다.
# 하지만 종윤이는 나이가 들어 혼자 모든 치킨을 튀길 수 없었고, 알바들을 고용할지 고민한다. 알바들은 한 명당 1분에 F 마리의 치킨을 튀길 수 있지만, 수당으로 치킨 C 마리를 미리 줘야 일을 하겠다고 한다. 성격이 급한 성구에게 혼나지 않으려면 가능한 빨리 치킨을 튀겨서 보내줘야 한다.
# 종윤이가 알바들을 적절히 고용해서 성구가 주문한 X 마리의 치킨을 튀기는데 걸리는 최소 시간을 반환(return)하도록 solution 함수를 작성하시오. (반올림하여 소수점 6번째 자리까지의 값을 반환)
# 입력
# 알바 당 인건비(치킨): 1 <= C <= 10000
# 알바 당 치킨 생산량: 1 <= F <= 100
# 목표 치킨량: 1 <= X <= 100000
# 입출력 예
# C     F       X           Return
# 30.0  1.0     2.0         1.0
# 30.0  2.0     100.0       39.166667
# 30.5  3.14159 1999.1999   63.968001
# 500.0 4.0     2000.0      526.190476


C = 30.0
F = 2.0
X = 100.0

def no_alba(X):
    return X/2.0

def solution(C,F,X):
    alone = no_alba(X)
    together_min = 100000
    for i in range(1,10):
        alba = C/((F*(i-1))+2.0)
        print(alba)
        order = X / F*(i+2.0)
        print(order)
        together = alba + order
        print(together)
        print("----------------")
        # together = (C*i)/2.0 + X/(F*i+2.0)
        # print(together)
        # if together_min > together:
        #     together_min = together
    return
    # return round(min(alone, together_min),6)

print(solution(C,F,X))

