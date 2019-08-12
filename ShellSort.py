# 希尔排序（Shell's Sort）
# 希尔排序是插入排序的改良版，插入排序在原数组基本有序时，效率最高，而希尔排序就是在无序数组进行
# 全部插入排序之前，进行优化处理

# 希尔排序在数组中采用跳跃式分组的策略，通过某个增量将数组元素划分为若干组，然后分组进行插入排序，
# 随后逐步缩小增量，继续按组进行插入排序操作，直至增量为1


import random


def shell_sort(li):
    # 处理增量
    gap, length = 1, len(li)
    while gap < length:
        gap = gap * 3 + 1

    while gap > 0:
        for i in range(gap, length):
            temp, j = li[i], i-gap
            while j >= 0 and li[j] > temp:
                li[j+gap] = li[j]
                j -= gap
            li[j+gap] = temp
        gap = gap // 3


if __name__ == '__main__':
    random_list = [random.randint(-100, 101) for i in range(10)]
    print(f'Unsorted list: {random_list}')
    shell_sort(random_list)
    print(f'Sorted list: {random_list}')
