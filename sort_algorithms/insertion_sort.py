def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        if array[i-1] > array[i]:
            idx = i
            tmp = array[i]
            for j in range(i-1, -1, -1):
                if array[j] > tmp:
                    array[j+1] = array[j]
                    idx = j
                else:
                    break
            array[idx] = tmp
    return array


if __name__ == '__main__':
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    ans = insertion_sort(arr)
    print(ans)
