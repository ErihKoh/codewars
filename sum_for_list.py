def prime_factors(n):
    n = abs(n)  # беремо абсолютне значення, бо множники завжди додатні
    factors = set()  # тут зберігатимемо прості множники (у множині дублікати автоматично зникнуть)
    d = 2
    while d * d <= n:  # достатньо перевіряти до sqrt(n)
        while n % d == 0:  # якщо n ділиться на d
            factors.add(d)  # додаємо d у множники
            n //= d  # ділимо n на d (зменшуємо n)
        d += 1  # переходимо до наступного можливого дільника
    if n > 1:  # якщо залишився простий множник > 1
        factors.add(n)
    return factors


def sum_for_list(I):
    """
    Для масиву I повертає список [p, sum] для кожного простого числа p,
    де sum — сума всіх чисел, які діляться на p.
    Реалізація без використання collections.
    """
    prime_sums = {}  # звичайний словник

    for number in I:
        factors = prime_factors(number)
        for p in factors:
            if p in prime_sums:
                prime_sums[p] += number
            else:
                prime_sums[p] = number

    # Сортуємо за зростанням простих чисел
    result = [[p, prime_sums[p]] for p in sorted(prime_sums)]
    return result


if __name__ == '__main__':
    list_1 = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
    print(sum_for_list(list_1))
