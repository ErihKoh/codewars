# def sum_of_intervals(intervals):
#     # Сортуємо інтервали за початком
#     intervals = sorted(intervals, key=lambda x: x[0])
#     total = 0
#     current_start, current_end = intervals[0]
#
#     for start, end in intervals[1:]:
#         if start <= current_end:  # Перетин
#             current_end = max(current_end, end)
#         else:  # Немає перетину
#             total += current_end - current_start
#             current_start, current_end = start, end
#
#     # додаємо останній інтервал
#     total += current_end - current_start
#     return total

def sum_of_intervals(intervals):
    covered = set()
    for start, end in intervals:
        covered.update([*range(start, end)])
    return len(covered)


if __name__ == '__main__':
    list_1 = [
        [1, 4],
        [7, 10],
        [3, 5]
    ]

    print(sum_of_intervals(list_1))
