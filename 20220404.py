# 문제
# 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 

# 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 

# 블랙잭은 카지노마다 다양한 규정이 있다.

# 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.

# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 

# 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 

# 그런 후에 딜러는 숫자 M을 크게 외친다.

# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 

# 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

# 입력
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

# 출력
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

# 예제 입력 1 
# 5 21
# 5 6 7 8 9
# 예제 출력 1 
# 21
# 예제 입력 2 
# 10 500
# 93 181 245 214 315 36 185 138 216 295
# 예제 출력 2 
# 497

# import sys

# input = sys.stdin.readline
# N, M = map(int, input().split())
# card_list = list(map(int, input().split()))
# result = 0
# for i in range(len(card_list)):
#     for j in range(i+1, len(card_list)):
#         for k in range(j+1, len(card_list)):
#             if card_list[i] + card_list[j] + card_list [k] > M:
#                 continue
#             result = max(result, card_list[i]+card_list[j]+card_list[k])

# print(result)

# ===================================================================================

# 문제
# 조규현과 백승환은 터렛에 근무하는 직원이다. 

# 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 

# 다음은 조규현과 백승환의 사진이다.



# 이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 

# 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

# 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 
# 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 
# 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
# 각 테스트 케이스는 다음과 같이 이루어져 있다.

# 한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. 
# x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, 
# r1, r2는 10,000보다 작거나 같은 자연수이다.

# 출력
# 각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 
# 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.

# 예제 입력 1 
# 3
# 0 0 13 40 0 37
# 0 0 3 0 7 4
# 1 1 1 1 1 5
# 예제 출력 1 
# 2
# 1
# 0

# import sys
# import math

# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())

#     distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

#     if distance == 0 and r1 == r2:
#         print(-1)
#     elif abs(r1-r2) == distance or abs(r1+r2) == distance:
#         print(1)
#     elif abs(r1-r2) < distance < r1+r2:
#         print(2)
#     else:
#         print(0)

# 문제
# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 
# 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 
# 따라서 245는 256의 생성자가 된다. 
# 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 
# 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 출력
# 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

# 예제 입력 1 
# 216
# 예제 출력 1 
# 198

import sys

input = sys.stdin.readline
N = int(input())
result = 0
for i in range(1, N+1):
    num = sum(list(map(int, str(i))))
    if i+num == N:
        result = i
        break

print(result)