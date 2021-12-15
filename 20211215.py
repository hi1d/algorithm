# 버블 정렬

input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return


bubble_sort(input)
print(input)

# 선택 정렬
input = [4, 6, 2, 9, 1]


def selection_sort(array):

    for i in range(len(array)-1):
        min_index = i
        for j in range(len(array)-i):
            if array[i+j] < array[min_index]:
                min_index = i+j
        array[i], array[min_index] = array[min_index], array[i]
    return


selection_sort(input)
print(input)

# 삽입 정렬

input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    for i in range(1, len(input)):
        for j in range(i):
            if array[i-j-1] > array[i-j]:
                array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
    return


insertion_sort(input)
print(input)
