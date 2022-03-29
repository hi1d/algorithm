# 문제
# 두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 
# 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.

# 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

# 출력
# 첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 3
# 1 45000
# 6 10
# 13 17
# 예제 출력 1 
# 45000
# 30
# 221

# def lcm(A,B):
#     return (A*B) // gcd(A,B)

# def gcd(A,B):
#     while A != 0:
#         B = B%A
#         A,B = B,A
#     return B

# import sys
# input = sys.stdin.readline
# T = int(input())
# for i in range(T):
#     A, B = map(int,input().split())
#     print(lcm(A,B))

# =============================================================

# 문제
# 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 10, 0 ≤ \(K\) ≤ \(N\))

# 출력
 
# \(\binom{N}{K}\)를 출력한다.

# 예제 입력 1 
# 5 2
# 예제 출력 1 
# 10

# import sys 

# input = sys.stdin.readline
# N,K = map(int, input().split())
# cache = [[1 if k==n or k==0 else 0 for k in range(K+1)] for n in range(N+1)]

# for i in range(1, N+1):
#     for j in range(1, K+1):
#         cache[i][j] = cache[i-1][j] + cache[i-1][j-1]

# print(cache[N][K])

# =============================================================

# 문제
# 재원이는 한 도시의 시장이 되었다. 
# 이 도시에는 도시를 동쪽과 서쪽으로 나누는 큰 일직선 모양의 강이 흐르고 있다. 
# 하지만 재원이는 다리가 없어서 시민들이 강을 건너는데 큰 불편을 겪고 있음을 알고 다리를 짓기로 결심하였다. 
# 강 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다. 
# 재원이는 강 주변을 면밀히 조사해 본 결과 강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)

# 재원이는 서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 한다. (이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.) 
# 재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다. 
# 다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.


# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)이 주어진다.

# 출력
# 각 테스트 케이스에 대해 주어진 조건하에 다리를 지을 수 있는 경우의 수를 출력한다.

# 예제 입력 1 
# 3
# 2 2
# 1 5
# 13 29
# 예제 출력 1 
# 1
# 5
# 67863915

import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    K,N = map(int, input().split())

    cache = [[1 if k==n or k==0 else 0 for k in range(K+1)] for n in range(N+1)]

    for i in range(1,N+1):
        for j in range(1, K+1):
            cache[i][j] = cache[i-1][j] + cache[i-1][j-1]
    print(cache[i][j])
