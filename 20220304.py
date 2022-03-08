# 1   2   6   7   15
# 3   5   8   14  16
# 4   9   13  17  22
# 10  12  18  21  23
# 11  19  20  24  25


# 1   2   6   7
# 3   5   8   13
# 4   9   12  14
# 10  11  15  16

r = 4
c = 6

max_count = 8
line_max = (max_count*2)-1
count = 1
count_max = 1
list = []
for i in range(1, line_max+1):
    num_list = []
    if i > max_count:
        count_max -= 1
    else:
        count_max += 1
    for j in range(1, count_max):
        num_list.append(count)
        count += 1
    if i % 2:
        num_list.sort(reverse=True)
    list.append(num_list)

list_count = 0
result = [[]*max_count for i in range(max_count)]
for n, i in enumerate(list):
    for j in range(len(i)):
        index = 0
        if n > (line_max//2):
            index = n-(line_max//2)
        result[j+index].append(i[j])

for i in result:
    print(i)
print(result[r-1][c-1])


# =======================================================================
# row = []
# line = []
# list_len = len(list)
# for i in range(list_len):
#     sorted_list = sorted(list[i])
#     row.append(sorted_list[list_len//2])
#     line_line = []
#     for j in range(len(list)):
#         line_line.append(list[j][i])
#     line_line.sort()
#     line.append(line_line[list_len//2])

# result = 0
# for i in row:
#     if i in line:
#         result+=1
