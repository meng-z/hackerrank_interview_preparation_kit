def selection_sort(array):
    n = len(array)
    for i in range(n):
        # use min_idx to store the minimum at this iteration
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[min_idx], array[i] = array[i], array[min_idx]
    return array


if __name__ == '__main__':
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    ans = selection_sort(arr)
    print(ans)
