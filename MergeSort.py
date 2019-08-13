import random


def merge_sort(li):
    length = len(li)

    # 当数组元素小于 2，直接返回数组
    if length < 2:
        return li

    # 获取分割下标
    middle = length // 2

    # 开始归并排序(递归)
    return merge(merge_sort(li[0: middle]), merge_sort(li[middle: length]))


def merge(left, right):
    result = []
    while left is not None and len(left) > 0 \
            and right is not None and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left[:] = left[1:]
        else:
            result.append(right[0])
            right[:] = right[1:]

    while left is not None and len(left) > 0:
        result.append(left[0])
        left[:] = left[1:]

    while right is not None and len(right) > 0:
        result.append(right[0])
        right[:] = right[1:]

    return result


if __name__ == '__main__':
    random_list = [random.randint(-100, 101) for i in range(10)]
    print(f'Unsorted list: {random_list}')
    print('Sorted list: {0}'.format(merge_sort(random_list)))
