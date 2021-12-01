# 큐(Queue)
# : 먼저 집어 넣은 데이터가 먼저 나오는 FIFO (First in First Out) 구조로 저장하는 형식

# 스택과는 반대되는 개념

# EnQueue(입력), DeQueue(출력)를 통해 자료 입출력이 구현

# 큐가 꽉 차서 더 이상 자료를 넣을 수 없는 경우를 Overflow,
# 큐가 비어 있어 자료를 꺼낼 수 없는 경우를 Underflow

# [조건]
# 1. 큐는 최대 10개의 자료가 들어갈 수 있고, 10개를 넘으면 Overflow를 출력
# 2. 큐가 비어있는 상태에서 Dequeue를 실행하면 underflow를 출력

# [입력]
# 첫 줄에 입출력의 횟수를 입력
# 다음 줄 부터 입력 또는 출력 여부(d 또는 D)를 입력하고 입력(e 또는 E)일 경우는 자료 내용까지 입력
# e(E) 또는 d(D) 이외의 입력이 들어올 경우 큐의 최정 상태를 출력하며 프로그램이 종료

# [출력]
# 입출력 횟수가 끝나거나 프로그램이 중간에 종료되면 큐의 최종 상태를 출력.

count = int(input())
data = []
state = True

for i in range(count):
    if state == True:
        select_que = str(input())
        if select_que == 'e' or select_que == 'E':
            if len(data) > 9:
                print('overflow')
                state = False
            else:
                data_in = int(input())
                data.append(data_in)
        elif select_que == 'd' or select_que == 'D':
            if len(data) < 1:
                print('underflow')
                state = False
            else:
                data.pop(0)

        else:
            state = False
    else:
        break

for f in data:
    print(f, end=' ')

# while

# while state:
#     select_que = str(input())
#     if select_que == 'e' or select_que == 'E':
#         if len(data) > 9:
#             print('overflow')
#             state = False
#         else:
#             data_in = int(input())
#             data.append(data_in)
#     elif select_que == 'd' or select_que == 'D':
#         if len(data) < 1:
#             print('underflow')
#             state = False
#         else:
#             data.pop(0)
#     else:
#         state = False
