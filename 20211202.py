# 문제 설명
# 카카오에 입사한 신입 개발자 네오는 "카카오계정개발팀"에 배치되어,
# 카카오 서비스에 가입하는 유저들의 아이디를 생성하는 업무를 담당하게 되었습니다.
# "네오"에게 주어진 첫 업무는 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때,
# 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.
# 다음은 카카오 아이디의 규칙입니다.

# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
# "네오"는 다음과 같이 7단계의 순차적인 처리 과정을 통해 신규 유저가 입력한 아이디가
# 카카오 아이디 규칙에 맞는 지 검사하고 규칙에 맞지 않은 경우 규칙에 맞는 새로운 아이디를 추천해 주려고 합니다.
# 신규 유저가 입력한 아이디가 new_id 라고 한다면,

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# [문제]
# 신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, "네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성해 주세요.

# [제한사항]
# new_id는 길이 1 이상 1,000 이하인 문자열입니다.
# new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.
# new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정됩니다.

# [입출력 예]
# no	new_id	result
# 예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
# 예2	"z-+.^."	"z--"
# 예3	"=.="	"aaa"
# 예4	"123_.def"	"123_.def"
# 예5	"abcdefghijklmn.p"	"abcdefghijklmn"

import re

new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "z-+.^."
# new_id = "=.="


def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    print(f'1단계 : {new_id}')
    # 2단계
    # re.sub(pattern, repl, string, count=0, flags=0)
    # re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
    new_id = re.sub('[^a-zA-Z0-9-_.]', '', new_id)
    print(f'2단계 : {new_id}')
    # 3단계
    new_id = re.sub('[..]+', '.', new_id)
    print(f'3단계 : {new_id}')
    # 4단계
    new_id = re.sub('^[.] | [.]$', '', new_id)
    print(f'4단계 : {new_id}')
    # 5단계
    if new_id == '':
        new_id = 'a'
    print(f'5단계 : {new_id}')
    # 6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
    new_id = re.sub('^[.]|[.]$', '', new_id)
    print(f'6단계 : {new_id}')
    # 7단계
    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

# ===================== 첫 시도 ============================

# def solution(new_id):
#     answer = ''
#     # 1단계
#     new_id = new_id.lower()
#     print(f'1단계 : {new_id}')
#     # 2단계
#     # re.sub(pattern, repl, string, count=0, flags=0)
#     # re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
#     new_id = re.sub('[^a-zA-Z0-9-_.]', '', new_id)
#     print(f'2단계 : {new_id}')
#     # 3단계
#     new_id = re.sub('\.+', '.', new_id)
#     print(f'3단계 : {new_id}')
#     # 4단계
#     if new_id == '':
#         pass
#     else:
#         if new_id[0] == '.':
#             new_id = new_id[1:len(new_id)]

#         if new_id == '':
#             pass
#         elif new_id[::-1][0] == '.':
#             new_id = new_id[:len(new_id)-1]
#     print(f'4단계 : {new_id}')
#     # 5단계
#     if new_id == '':
#         new_id = 'a'
#     print(f'5단계 : {new_id}')
#     # 6단계
#     if len(new_id) > 15:
#         new_id = new_id[:15]
#         if new_id[::-1][0] == '.':
#             new_id = new_id[:len(new_id)-1]
#     print(f'6단계 : {new_id}')
#     # 7단계
#     if len(new_id) < 3:
#         while len(new_id) < 3:
#             new_id += new_id[-1]

#     return new_id


# print(solution(new_id))

# import re
# phone_number = "01033334444"


# def solution(phone_number):
#     return re.sub('[0-9]', '*', phone_number, len(phone_number)-4)


# print(solution(phone_number))
