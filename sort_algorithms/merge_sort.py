def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array

    mid = n // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    ans = merge_sort(arr)
    print(ans)
