# 스택(Stack)
# : 제한적으로 접근할 수 있는 나열 구조
# LIFO (Last In First Out) 선형구조
# Push : 자료를 넣는 것
# Pop : 자료를 꺼내는 것


# [문제]
# 푸시와 팝으로 스택에 자료를 넣고 빼는 작업을 진행하고, 스택의 마지막 상태를 출력하는 프로그램을 작성하시오.

# [조건]
# 1.스택은 최대 10개의 자료가 들어갈 수 있고, 10개를 넘으면 overflow를 출력한다.
# 2.스택이 비어있는 상태에서 pop을 실행하면 underflow를 출력한다.

# [입력]
# 첫 줄에 데이터 입력 횟수가 입력된다.
# 다음 줄 부터 0인 경우 푸시이고, 1인경우 팝이 일어난다.
# 0 또는 1 이외의 것을 입력하면 프로그램을 종료한다.
# 푸시인 경우에만 자료의 내용을 다음 줄에 입력한다.

# [출력]
# 데이터 입력이 모두 끝난 후 스택의 상태 (방향 : Bottom --> Top)


count = int(input())
data = []

state = 'true'

for i in range(count):
    if state == 'true':
        IN = int(input())
        if IN == 0:
            if len(data) < 10:
                data_in = input()
                data.append(data_in)
                print(data)
            else:
                print('overflow')
                state = 'false'

        elif IN == 1:
            if len(data) < 1:
                print('underflow')
                state = 'false'
            else:
                data.pop()
                print(data)
        else:
            state = 'false'
    else:
        break

for f in data:
    print(f, end=' ')
