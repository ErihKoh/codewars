def max_sequence(arr):
    if len(arr) == 0:
        return 0
    max_current = max_global = arr[0]

    for x in arr[1:]:
        max_current = max(x, max_current + x)
        max_global = max(max_global, max_current)
    if max_global < 0:
        return 0

    return max_global


def maxSequence(arr):
    max, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0: curr = 0
        if curr > max: max = curr
    return max


if __name__ == '__main__':
    t_list = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
    print(max_sequence(t_list))
