def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(1, n-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array


def bubble_sort_v2(array):
    n = len(array)
    for i in range(n):
        # if at ith iteration, there is no swap, it means the sort finished
        flag = 1
        for j in range(1, n-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                flag = 0
        if flag:
            break
    return array


if __name__ == '__main__':
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    ans = bubble_sort_v2(arr)
    print(ans)
