import random


def quick_sort(li):
    quick_sort_method(li, 0, len(li)-1)


def quick_sort_method(li, left, right):
    if left < right:
        partition_index = partition(li, left, right)
        quick_sort_method(li, left, partition_index-1)
        quick_sort_method(li, partition_index+1, right)


def partition(li, left, right):
    # 设定基准值
    p, index = left, left + 1

    # index 是左指针，i 为右指针
    for i in range(index, right+1):
        if li[i] < li[p]:
            li[i], li[index] = li[index], li[i]
            index += 1
    li[p], li[index-1] = li[index-1], li[p]  # 把基准值和 LR 指针位置值交换
    return index-1


if __name__ == '__main__':
    random_list = [random.randint(-100, 101) for i in range(10)]
    print(f'Unsorted list: {random_list}')
    quick_sort(random_list)
    print(f'Sorted list: {random_list}')
