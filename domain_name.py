import re


def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


if __name__ == '__main__':
    url1 = "http://github.com/carbonfive/raygun"
    url2 = "http://www.zombie-bites.com"
    url3 = "https://www.cnet.com"
    url4 = "icann.org"

    print(domain_name(url3))
