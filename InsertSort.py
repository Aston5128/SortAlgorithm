# 插入排序（Insert Sort）
# 插入排序把数组分为两列，第一列为有序列，中间的是需要插入的数，后面的是无序列


import random


def insert_sort(li):
    length = len(li)
    for i in range(length):
        temp, j = li[i], i
        while j > 0 and temp < li[j-1]:
            li[j] = li[j-1]
            j -= 1
        if j != i:
            li[j] = temp


if __name__ == '__main__':
    random_list = [random.randint(-100, 101) for i in range(10)]
    print(f'Unsorted list: {random_list}')
    insert_sort(random_list)
    print(f'Sorted list: {random_list}')
