# 문제
# 다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }
# fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

# fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
# fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
# 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
# fibonacci(0)은 0을 출력하고, 0을 리턴한다.
# fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
# 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 
# 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

# 출력
# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

# 예제 입력 1 
# 3
# 0
# 1
# 3
# 예제 출력 1 
# 1 0
# 0 1
# 1 2
# 예제 입력 2 
# 2
# 6
# 22
# 예제 출력 2 
# 5 8
# 10946 17711

# import sys

# input = sys.stdin.readline
# T = int(input())

# num_list = [(1,0),(0,1),(1,1)]


# def fibonacci(N):
#     if len(num_list) <= N:
#         for i in range(len(num_list), N+1):
#             num_list.append((num_list[i-1][0]+num_list[i-2][0],num_list[i-1][1]+num_list[i-2][1]))
            
#     print(num_list[N][0], num_list[N][1])
            

# for _ in range(T):
#     N = int(input())
#     fibonacci(N)
    
# ==============================================================================

# 문제
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 

# 그리고 나서 세준이는 괄호를 모두 지웠다.

# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 식이 주어진다. 
# 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 
# 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

# 출력
# 첫째 줄에 정답을 출력한다.

# 예제 입력 1 
# 55-50+40
# 예제 출력 1 
# -35
# 예제 입력 2 
# 10+20+30+40
# 예제 출력 2 
# 100
# 예제 입력 3 
# 00009-00009
# 예제 출력 3 
# 0

# import sys

# input = sys.stdin.readline
# num = input().split('-')
# for i in range(len(num)):
#     num[i] = sum(map(int,num[i].split('+')))

# count = num[0]
# for j in num[1:]:
#     count -= j
# print(count)

