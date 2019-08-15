import random


def heap_sort(li):
    length = len(li)
    build_max_heap(li, length)

    for i in range(length-1, 0, -1):
        # 将大顶堆的顶部与 length 交换，并将 length - 1
        li[0], li[i] = li[i], li[0]
        length -= 1
        build_max_heap(li, length)  # 重新构造大顶堆


def build_max_heap(li, length):
    # 构造大顶堆
    # 从叶子节点出发
    for i in range(length-1, 0, -1):
        parent_index = (i-1) // 2
        if li[parent_index] < li[i]:
            li[parent_index], li[i] = li[i], li[parent_index]

    # 从根节点出发
    for i in range(0, length//2):
        left, right = i * 2 + 1, i * 2 + 2
        if left < length and li[i] < li[left]:
            li[i], li[left] = li[left], li[i]
        if right < length and li[i] < li[right]:
            li[i], li[right] = li[right], li[i]


if __name__ == '__main__':
    random_list = [random.randint(-100, 101) for i in range(10)]
    print(f'Unsorted list: {random_list}')
    heap_sort(random_list)
    print(f'Sorted list: {random_list}')
