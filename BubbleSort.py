import random


def bubble_sort(li):
    length = len(li)
    for i in range(length):
        for j in range(i+1, length):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]


if __name__ == '__main__':
    random_list = [random.randint(-100, 101) for i in range(10)]
    print(f'Unsorted list: {random_list}')
    bubble_sort(random_list)
    print(f'Sorted list: {random_list}')
