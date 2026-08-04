def fibonacci_memoize(n, cache={0: 0, 1: 1}):
    if n not in cache:
        cache[n] = fibonacci_memoize(n - 1) + fibonacci_memoize(n - 2)

    return cache[n]


if __name__ == '__main__':
    n = 100

    print(fibonacci_memoize(n))
