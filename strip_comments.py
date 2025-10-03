
def strip_comments(strng, markers):
    list_2 = strng.split('\n')
    for s in markers:
        list_2 = [v.split(s)[0].rstrip() for v in list_2]

    return '\n'.join(list_2)


if __name__ == '__main__':
    str_1 = 'a #b\nc\nd $e f g'
    mark = ['#', '$']
    print(strip_comments(str_1, mark))
