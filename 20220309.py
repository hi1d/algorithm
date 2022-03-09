# N개의 문자 'a' 및 또는 'b'로 구성된 문자열 S가 주어지면
# 'a'문자가 모두 'b' 문자보다 먼저 발생하면 True를 반환하고
# 그렇지 않으면 False를 반환하는 함수 솔루션을 작성
# 예 :
# 1. 주어진 S = "aabbb", 함수는 True 반환
# 2. S = "ba"가 주어지면 함수는 False 반환
# 3. S = "aaa", 함수는 True 반환, 'b'는 S에서 발생할 필요가 없습니다.
# 4. S = "b"가 주어지면 함수는 True 반환 'a'는 S에서 발생할 필요가 없습니다.
# 5. S = "abba"가 주어지면 함수는 False 반환
# N은 1~300,000 범위내 정수
# 문자열 S는 'a'및 또는 'b' 문자로만 구성됩니다.

S = "abbbbbbbbbbbbbbbb"

def solution(S):
    list = []
    if 'a' not in S:
        return True
    for i in S:
        list.append(i)
        if i == 'a' and 'b' in list:
            return False
    return True

# print(solution(S))

# =============================================================
# John은 여행을 좋아합니다. 그는 수년에 걸쳐 많은 도시를 방문했습니다.
# 그는 도시를 방문할 때마다 몇장의 사진을 찍어 컴퓨터에 저장합니다.
# 각 사진에는 확장자가 있는 이름("jpg", "png" 또는 "jpeg")이 있으며
# 사진을 찍은 도시 이름과 사진의 시간 및 날짜에 대한 기록이 있습니다.
# 예 : "phto.jpg, 바르샤바, 2013-09-05 14:08:15".
# 드문 경우지만 시간대 차이로 인해 다른 위치의 사진이 시간과 날짜를 공유할 수도 있습니다.
# John은 컴퓨터에 사진을 정리하는 방식이 엉망이 된 것을 알아차렸습니다.
# 그는 사진을 재구성하고 싶어합니다. 먼저 그는 도시별로 사진을 그룹화하기로
# 결정한 다음, 각 그룹내에서 사진을 찍은 시간별로 정렬하고 마지막으로 1부터 시작하여
# 사진에 연속적인 자연수를 할당합니다. 그런 다음 모든 사진의 이름을 바꾸려고 합니다.
# 각 사진의 새 이름은 도시 이름으로 시작하고 그 뒤에 해당 사진에 이미 할당된 번호가 와야합니다.
# 각 그룹의 모든 사진 수는 길이가 동일해야 합니다.(이 그룹에서 가장 큰 수의 길이와 동일.)
# 따라서 John은 숫자에 선행 0을 추가해야 합니다. 사진의 새 이름은 확장자로 끝나야 하며
# 동일하게 유지 되어야 합니다.
# 당신의 임무는 각 사진의 새로운 이름을 찾아 존을 돕는 것입니다.
# John의 각 사진 형식은 "<<photoname>>. <<extension>>, <<city_name>>,yyyy-mm-dd hh:mm:ss",
# 여기서 "<<photoname>>", "<<extension>>","<<city_name>>"은 영문 알파벳으로만 구성
# 각각 사진명, 파일명, 확장자, 도시명을 입력합니다. 사진의 이름은 고유하지 않을 수 있습니다.
# M개의 사진 목록을 나타내는 문자열이 주어지면 모든 사진의 새 이름 목록을 나타내는 문자열 반환
# (사진의 순서는 동일해야함)
# 예를 들어 주어진 문자열 :
# photo.jpg, 바르샤바, 2013-09-05 14:08:15
# john.png, 런던, 2015-06-20 15:13:22
# myFriends.png, 바르샤바, 2013-09-05 14:07:13
# 에펠.jpg, 파리, 2015-07-23 08:03:02
# pisatower.jpg, 파리, 2015-07-22 23:59:59
# BOB.jpg, 런던, 2015-08-05 00:02:03
# notredame.png, 파리, 2015-09-01 12:00:00
# me.jpg, 바르샤바, 2013-09-06 15:40:22
# a.png, 바르샤바, 2016-02-13 13:33:50
# b.jpg, 바르샤바, 2016-01-02 15:12:22
# c.jpg, 바르샤바, 2016-01-02 14:34:30
# d.jpg, 바르샤바, 2016-01-02 15:15:01
# e.png, 바르샤바, 2016-01-02 09:49:09
# f.png, 바르샤바, 2016-01-02 10:55:32
# g.jpg, 바르샤바, 2016-02-29 22:13:11
# 함수는 다음을 반환해야합니다.
# 바르샤바02.jpg
# 런던1.png
# 바르샤바01.png
# 파리2.jpg
# 파리1.jpg
# 런던2.jpg
# 파리3.png
# 바르샤바03.jpg
# 바르샤바09.png
# 바르샤바07.jpg
# 바르샤바06.jpg
# 바르샤바08.jpg
# 바르샤바04.png
# 바르샤바05.png
# 바르샤바10.jpg
# 바르샤바에서 찍은 사진이 10장(01부터 10까지), 런던에서 찍은 사진 두장(1부터 2까지),
# 파리에서 찍은 사진 세장(1부터 3까지)이 있기 때문입니다.
# 사진의 새 이름은 지정된 문자열과 동일한 순서로 반환됩니다.
# 다음과 같이 가정합니다
# M은 1~100 범위내의 정수
# 각 연도는 2000~2020 범위내의 정수
# 입력 문자열의 각 줄은 "<<photoname>>, <<extension>>,<<city_name>>, yyyy-mm-dd hh:mm:ss"형식이고
# 줄은 개행 문자로 구분됩니다.
# 각 사진 이름(확장자 없음)과 도시이름은 영어 알파벳에서 1자 이상 20자 이하로 구성
# 도시의 각 이름은 대문자로 시작하고 그 뒤에 소문자가 옵니다.
# 같은 위치에서 찍은 두 장의 사진이 같은 날짜와 시간을 공유하지 않습니다.
# 각 확장자는 "jpg", "png" 또는 "jpeg" 입니다.
# 솔루션에서 정확성에 중점을 둡니다. 솔루션의 성능은 평가의 초점이 아닙니다.

def solution(pictures):
    pictures = pictures.split('\n')
    area = []
    area_count = {}
    for i in range(len(pictures)):
        pictures[i] = pictures[i].split(",")        
        area_name = pictures[i][1].strip()
        if area_name not in area:
            area.append(area_name)
        try:
            area_count[area_name] += 1
        except KeyError:
            area_count[area_name] = 1
    temp = sorted(pictures, key=lambda x : (x[2],x[1]))
    area_index = {'result':{i:1 for i in area}}
    for i in temp:
        area_name = i[1].strip()
        file_extension = i[0].split('.')[-1]
        if area_count[area_name] >= 10:
            count = area_index['result'][area_name]
            count = f"{count}".zfill(len(f"{area_count[area_name]}"))
            i[0] = area_name + count + '.' + file_extension
            area_index['result'][area_name] +=1
        else:
            i[0] = area_name + f"{area_index['result'][area_name]}" + '.' +file_extension
            area_index['result'][area_name] +=1
    result = []
    for i in pictures:
        result.append(''.join(i[0]))
    return '\n'.join(result)

print(solution('photo.jpg, 바르샤바, 2013-09-05 14:08:15\njohn.png, 런던, 2015-06-20 15:13:22\nmyFriends.png, 바르샤바, 2013-09-05 14:07:13\n에펠.jpg, 파리, 2015-07-23 08:03:02\npisatower.jpg, 파리, 2015-07-22 23:59:59\nBOB.jpg, 런던, 2015-08-05 00:02:03\nnotredame.png, 파리, 2015-09-01 12:00:00\nme.jpg, 바르샤바, 2013-09-06 15:40:22\na.png, 바르샤바, 2016-02-13 13:33:50\nb.jpg, 바르샤바, 2016-01-02 15:12:22\nc.jpg, 바르샤바, 2016-01-02 14:34:30\nd.jpg, 바르샤바, 2016-01-02 15:15:01\ne.png, 바르샤바, 2016-01-02 09:49:09\nf.png, 바르샤바, 2016-01-02 10:55:32\ng.jpg, 바르샤바, 2016-02-29 22:13:11'))




