# 길이가 n인 정수 배열 arr가 주어집니다. 
# arr를 다음과 같은 과정을 거쳐서 섞은 결과를 return 하도록 solution 함수를 완성해주세요.
# arr의 길이가 1이라면, arr를 그냥 그대로 두고 과정을 종료합니다.
# arr를 앞뒤로 뒤집습니다.
# 만약 arr의 길이가 짝수(2k)라면, 앞뒤로 길이가 k, k인 두 배열로 나눕니다.
# 만약 arr의 길이가 홀수(2k+1)라면, 앞뒤로 길이가 k+1, k인 두 배열로 나눕니다.
# 두 배열에 대해 이 과정을 다시 반복한 뒤, 다시 이어 붙입니다.

arr = [i for i in range(1,7)]

def solution(arr):
    if len(arr) == 1:
        return arr
    arr = arr[::-1]
    if len(arr) % 2:
        front = solution(arr[:len(arr)//2+1])
        back = solution(arr[len(arr)//2+1:])
    else:
        front = solution(arr[:len(arr)//2])
        back = solution(arr[len(arr)//2:])
    
    return front + back

print(solution(arr))