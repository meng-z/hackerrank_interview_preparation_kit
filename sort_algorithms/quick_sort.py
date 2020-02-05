def quick_sort(array):
    n = len(array)
    if n <= 1:
        return array

    pivot = array[0]
    # count items the same as the pivot
    pivot_count = 1
    left, right = [], []
    for i in range(1, n):
        if array[i] < pivot:
            left.append(array[i])
        elif array[i] == pivot:
            pivot_count += 1
        else:
            right.append(array[i])

    return quick_sort(left) + [pivot]*pivot_count + quick_sort(right)


if __name__ == '__main__':
    arr = [6, 5, 3, 2, 1, 8, 3, 7, 2, 4]
    ans = quick_sort(arr)
    print(ans)
