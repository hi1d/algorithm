# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 예제 입력 1         예제 출력 1 
# Mississipi        ?

# 예제 입력 2         예제 출력 2 
# zZa               Z

# 예제 입력 3         예제 출력 3 
# z                 Z

# 예제 입력 4         예제 출력 4 
# baaa              A

# word = input()
# word = list(word.upper())
# result_dict = {chr(i):0 for i in range(65,91)}
# for i in word:
#     result_dict[i] += 1
# result = sorted(result_dict.items(),key=lambda x:x[1],reverse=True)
# if result[0][1] == result[1][1]:
#     print("?")
# else:
#     print(result[0][0])

# ==================================================================

# 문제
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 
# 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

# 크로아티아 알파벳	    변경
# č	                c=
# ć	                c-
# dž	            dz=
# đ	                d-
# lj	            lj
# nj	            nj
# š	                s=
# ž	                z=
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

# dž는 무조건 하나의 알파벳으로 쓰이고, 
# d와 ž가 분리된 것으로 보지 않는다. 
# lj와 nj도 마찬가지이다. 
# 위 목록에 없는 알파벳은 한 글자씩 센다.

# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다. 
# 알파벳 소문자와 '-', '='로만 이루어져 있다.

# 단어는 크로아티아 알파벳으로 이루어져 있다. 
# 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

# 예제 입력 1         예제 출력 1 
# ljes=njak           6
# 예제 입력 2         예제 출력 2 
# ddz=z=              3
# 예제 입력 3         예제 출력 3
# nljj                3
# 예제 입력 4        예제 출력 4    
# c=c=                2
# 예제 입력 5         예제 출력 5
# dz=ak               3

# input_word = input()
# alpha_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]
# result_count = 0
# for word in alpha_list:
#     if word in input_word[:]:
#         result_count += input_word.count(word)
#         input_word = input_word.replace(word, ",")
# result_count += len(input_word.replace(',','').strip())
# print(result_count)

# ==================================================================

# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. 
# N은 100보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 
# 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

# 예제 입력 1     예제 출력 1 
# 3               3
# happy
# new
# year

# 예제 입력 2     예제 출력 2
# 4               1
# aba
# abab
# abcabc
# a

# 예제 입력 3     예제 출력 3
# 5               4
# ab
# aa
# aca
# ba
# bb

# 예제 입력 4     예제 출력 4
# 2               0
# yzyzy
# zyzyz

# 예제 입력 5     예제 출력 5
# 1               1
# z

N = int(input())
result_count = 0
for _ in range(N):
    word = input()
    flag = True
    for i in word:
        word_count = word.count(i)
        if word_count >= 2 and str(i*word_count) not in word:
            flag = False
            break
    if flag:
        result_count+=1

print(result_count)    
        
    