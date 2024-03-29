# 选择排序（Selection Sort）
# 选择排序遍历数组，以当前遍历到的数做基准，继续遍历接下来的数组，找到最小的数与基准数做交换


import random


def selection_sort(li):
    length = len(li)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if li[min_index] > li[j]:
                min_index = j

        li[i], li[min_index] = li[min_index], li[i]


if __name__ == '__main__':
    random_list = [random.randint(-100, 101) for i in range(10)]
    print(f'Unsorted list: {random_list}')
    selection_sort(random_list)
    print(f'Sorted list: {random_list}')
