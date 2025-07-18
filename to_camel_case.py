import re


def to_camel_case(text: str) -> str:
    if len(text) == 0:
        return ''
    t_list = re.split(r'[-_]+', text)
    t_list = [x.capitalize() for x in t_list]
    res = ''.join(t_list)
    if text[0].isupper():
        return res

    return res[0].lower() + res[1:]


def toCamelCase(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])


if __name__ == '__main__':
    t = 'A-cat-was_evil'
    print(to_camel_case(t))
