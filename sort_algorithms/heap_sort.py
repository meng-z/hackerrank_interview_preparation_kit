import heapq

def heap_sort(array):
    h = []
    for a in array:
        heapq.heappush(h, a)
    result = [heapq.heappop(h) for i in range(len(h))]
    return result


if __name__ == '__main__':
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    ans = heap_sort(arr)
    print(ans)
