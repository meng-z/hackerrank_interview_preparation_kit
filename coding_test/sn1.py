# insert 5 into the given integer N to get max possible value
def max_possible_value(N):
    str_N = str(N)
    i = 0
    if N >= 0:
        while i < len(str_N):
            if int(str_N[i]) < 5:
                return int(str_N[:i] + '5' + str_N[i:])
            else:
                i += 1
        return int(str_N[:i] + '5' + str_N[i:])
    else:
        while i < len(str_N):
            if i == 0:
                i += 1
                continue
            if int(str_N[i]) > 5:
                return int(str_N[:i] + '5' + str_N[i:])
            else:
                i += 1
        return int(str_N[:i] + '5' + str_N[i:])

if __name__ == '__main__':
    test_cases = [152, 565, 5671, 0, 670, 6705, -999, -123, -575, -515]
    for tc in test_cases:
        print(tc, max_possible_value(tc))
