import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link = re.search(r"^.+src=\"([^\"]+).+$",s)

    if link:
        link = link.groups(1)

        return link[0].replace("/embed","")
    else:
        return False


...


if __name__ == "__main__":
    main()