# 소수 나열하기
# 문제 : 정수를 입력 했을 때, 그 정소 이하의 소수를 모두 반환하시오.

# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

# input = 20


# def solution(input):
#     prime_list = []
#     for i in range(2, input+1):
#         print(prime_list)
#         for j in prime_list:
#             if i % j == 0 and j*j <= i:
#                 break
#         else:
#             prime_list.append(i)
#     return prime_list


# print(solution(input))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

# 문자열 뒤집기
# 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자를 모두 0, 혹은 모두 1로 같게 만들어야한다.
# 할 수 있는 행동은 연속된 하나의 숫자를 잡고 모두 뒤집는 것이다.
# 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.

# string = "011110"


# def solution(str):
#     count_all_zero = 0
#     count_all_one = 0

#     if str[0] == '0':
#         count_all_one += 1
#     elif str[0] == '1':
#         count_all_zero += 1

#     for char in range(len(str)-1):
#         if str[char] != str[char+1]:
#             if str[char+1] == '0':
#                 count_all_one += 1
#             elif str[char+1] == '1':
#                 count_all_zero += 1

#     return min(count_all_one, count_all_zero)


# print(solution(string))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self, value):
#         self.head = Node(value)

#     def append(self, value):
#         cur = self.head
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = Node(value)

#     def print_all(self):
#         cur = self.head
#         while cur is not None:
#             print(cur.data)
#             cur = cur.next

#     def get_node(self, index):
#         node = self.head
#         count = 0
#         while count < index:
#             node = node.next
#             count += 1
#         return node

#     def add_node(self, index, value):
#         new_node = Node(value)

#         if index == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return

#         node = self.get_node(index-1)
#         next_node = node.next
#         node.next = new_node
#         new_node.next = next_node
#         return

#     def delete_node(self, index):
#         if index == 0:
#             self.head = self.head.next
#             return

#         node = self.get_node(index-1)
#         node.next = node.next.next
#         return


# linked_list = LinkedList(5)
# linked_list.append(12)
# linked_list.append(8)
# linked_list.append(4)
# linked_list.append(17)
# linked_list.add_node(1, 6)
# linked_list.delete_node(0)
# linked_list.print_all()

# LinkedList
# 문제 : 다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오.

# 예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
# 각각 678,354 이므로 두개의 총합
# 678 + 354 = 1032 를 반환해야한다.

# [6] -> [7] -> [8]
# [3] -> [5] -> [4]

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self, value):
#         self.head = Node(value)

#     def append(self, value):
#         cur = self.head
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = Node(value)


# def get_num(linked_list):
#     cur = linked_list.head
#     sum_num = 0
#     while cur is not None:
#         sum_num = sum_num * 10 + cur.data
#         cur = cur.next
#     return sum_num


# def get_linked_list_sum(linked_list_1, linked_list_2):
#     list_num_1 = get_num(linked_list_1)
#     list_num_2 = get_num(linked_list_2)
#     return list_num_1+list_num_2


# linked_list_1 = LinkedList(6)
# linked_list_1.append(7)
# linked_list_1.append(8)


# linked_list_2 = LinkedList(3)
# linked_list_2.append(5)
# linked_list_2.append(4)

# print(get_linked_list_sum(linked_list_1, linked_list_2))
# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

# 이진탐색

# finding_target = 8
# finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# def is_existing_target_number_binary(target, array):
#     min_num = 0
#     max_num = len(array) - 1
#     half_num = (max_num + min_num) // 2

#     while min_num <= max_num:
#         if array[half_num] == target:
#             return True
#         elif array[half_num] < target:
#             min_num = half_num + 1
#         else:
#             max_num = half_num - 1
#         half_num = (max_num + min_num) // 2

#     return False


# result = is_existing_target_number_binary(finding_target, finding_numbers)
# print(result)

# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# 무작위수 찾기
# 문제 : 다음과 같이 숫자로 이루어진 배열이 있을 때, 2가 존재한다면 True,
# 존재하지 않는다면 False를 반환하시오.

# finding_target = 2
# finding_numbers = [0, 3, 5, 6, 1, 2, 4]


# def is_exist_target_number_binary(target, numbers):
#     numbers.sort()
#     min_num = 0
#     max_num = len(numbers)-1
#     half_num = (max_num + min_num) // 2
#     while min_num <= max_num:
#         if numbers[half_num] == target:
#             return True
#         elif numbers[half_num] < target:
#             min_num = half_num + 1
#         else:
#             max_num = half_num - 1
#         half_num = (min_num + max_num) // 2
#     return False


# result = is_exist_target_number_binary(finding_target, finding_numbers)
# print(result)
# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

# 재귀함수 - 카운트다운

# def count_down(number):
#     if number < 0:
#         return
#     print(number)
#     count_down(number - 1)


# count_down(60)
# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# 재귀함수 - 팩토리얼

# def factorial(n):
#     if n == 1:
#         return 1

#     return n * factorial(n-1)


# print(factorial(5))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

# 재귀함수 - 회문문장
string = 'lololol'

# def palindrome(str):
#     n = len(str)
#     for i in range(n):
#         if string[i] != string[n-1-i]:
#             return False

#     return True


# def palindrome(str):
#     if len(str) <= 1:
#         return True

#     if str[0] != str[-1]:
#         return False

#     return palindrome(str[1:-1])


# print(palindrome(string))

# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# 링크드 리스트 끝에서 K번째 값 출력하기
# 문제 : 링크드 리스트의 끝에서 K번째 값을 반환하시오.


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self, value):
#         self.head = Node(value)

#     def append(self, value):
#         cur = self.head
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = Node(value)

#     def get_kth_node_from_last(self, k):
#         count = 1
#         cur = self.head

#         while cur.next is not None:
#             cur = cur.next
#             count += 1

#         target_cur = count - k
#         cur = self.head

#         for i in range(target_cur):
#             cur = cur.next

#         return cur


# linked_list = LinkedList(6)
# linked_list.append(7)
# linked_list.append(8)

# print(linked_list.get_kth_node_from_last(2).data)
# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

# 배달의 민족 배달 가능
# 문제 : 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때,
# 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.

# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.

# shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
# shop_orders = ["오뎅", "콜라", "만두"]


# def is_available_to_order(menus, orders):
#     for ord in orders:
#         if ord not in menus:
#             return False
#     return True


# result = is_available_to_order(shop_menus, shop_orders)
# print(result)
# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

# 더하거나 빼거나
# 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# 사용할 수 있는 숫자가 담긴 배열 numbers,
# 타겟 넘버 target_number이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서
# 타겟 넘버를 만드는 방법의 수를 반환하시오.

numbers = [2, 3, 1]
target_number = 0
result_count = 0


def solution(array, target, current_index, current_sum):
    if current_index == len(array):
        if current_sum == target:
            global result_count
            result_count += 1
        return

    solution(array, target, current_index + 1,
             current_sum + array[current_index])

    solution(array, target, current_index + 1,
             current_sum - array[current_index])


solution(numbers, target_number, 0, 0)
print(result_count)
