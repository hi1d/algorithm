# 문제
# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 
# 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 15
# push 1
# push 2
# front
# back
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# front
# 예제 출력 1 
# 1
# 2
# 2
# 0
# 1
# 2
# -1
# 0
# 1
# -1
# 0
# 3

# from collections import deque
# import sys

# input = sys.stdin.readline
# N = int(input())
# q = deque()
# for _ in range(N):
#     command = input().split()
#     if command[0] == 'push':
#         q.append(command[1])
#     elif command[0] == 'pop':
#         if len(q):
#             print(q.popleft())
#         else:
#             print(-1)
#     elif command[0] == 'size':
#         print(len(q))
#     elif command[0] == 'empty':
#         if len(q):
#             print(0)
#         else:
#             print(1)
#     elif command[0] == 'front':
#         if len(q):
#             print(q[0])
#         else:
#             print(-1)
#     elif command[0] == 'back':
#         if len(q):
#             print(q[-1])
#         else:
#             print(-1)

# ==============================================================================================

# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 

# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 

# 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 

# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 

# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 

# 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 

# V부터 방문된 점을 순서대로 출력하면 된다.

# 예제 입력 1 
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 예제 출력 1 
# 1 2 4 3
# 1 2 3 4
# 예제 입력 2 
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1
# 예제 출력 2 
# 3 1 2 5 4
# 3 1 4 2 5
# 예제 입력 3 
# 1000 1 1000
# 999 1000
# 예제 출력 3 
# 1000 999
# 1000 999

# import sys
# from collections import deque

# def dfs(graph, root):
#     visit = {}
#     stack = []

#     stack.append(root)
#     while len(stack):
#         node = stack.pop()
#         if node not in visit:
#             visit[node] = True
#             stack.extend(sorted(graph[node], reverse= True))
#     return ' '.join(map(str,visit.keys()))

# def bfs(graph, root):
#     visit = {}
#     q = deque()

#     q.append(root)
#     while len(q):
#         node = q.popleft()
#         if node not in visit:
#             visit[node] = True
#             q.extend(sorted(graph[node]))

#     return ' '.join(map(str,visit.keys()))

# input = sys.stdin.readline
# N, M, V = map(int, input().strip().split())

# graph = {i : [] for i in range(1,N+1)}
# for i in range(M):
#     num1, num2 = map(int, input().strip().split())
#     graph[num1].append(num2)
#     graph[num2].append(num1)
    
# print(dfs(graph, V))
# print(bfs(graph, V))

# ==============================================================================================

# 문제
# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 
# 단, N은 홀수라고 가정하자.

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
# 단, N은 홀수이다. 
# 그 다음 N개의 줄에는 정수들이 주어진다. 
# 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# 출력
# 첫째 줄에는 산술평균을 출력한다. 
# 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

# 둘째 줄에는 중앙값을 출력한다.

# 셋째 줄에는 최빈값을 출력한다. 
# 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

# 넷째 줄에는 범위를 출력한다.

# 예제 입력 1 
# 5
# 1
# 3
# 8
# -2
# 2
# 예제 출력 1 
# 2
# 2
# 1
# 10
# 예제 입력 2 
# 1
# 4000
# 예제 출력 2 
# 4000
# 4000
# 4000
# 0
# 예제 입력 3 
# 5
# -1
# -2
# -3
# -1
# -2
# 예제 출력 3 
# -2
# -2
# -1
# 2
# 예제 입력 4 
# 3
# 0
# 0
# -1
# 예제 출력 4 
# 0
# 0
# 0
# 1
# (0 + 0 + (-1)) / 3 = -0.333333... 이고 이를 첫째 자리에서 반올림하면 0이다. -0으로 출력하면 안된다.

import sys
from collections import Counter

def mean(N_list):
    print(round(sum(N_list)/len(N_list)))

def median(N_list):
    print(N_list[len(N_list)//2])

def mode(N_list):
    N_list = Counter(N_list)
    count_num = N_list.most_common()
        
    if len(count_num) > 1 and count_num[0][1] == count_num[1][1] :
        print(count_num[1][0])
    else:
        print(count_num[0][0]) 

def scope(N_list):
    print(N_list[-1] - N_list[0])

def run(N_list):
    mean(N_list)
    median(N_list)
    mode(N_list)
    scope(N_list)

input = sys.stdin.readline
N = int(input())
N_list = sorted([int(input()) for _ in range(N)])
run(N_list)

