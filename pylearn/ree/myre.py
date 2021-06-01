"""
author: lxz
"""

import re


class MyRe:

    def __init__(self):
        pass

    def match_test(self):
        self = self
        line = 'Cats are smarter than dogs'
        match_obj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
        if match_obj:
            print(match_obj.group(1))
            print(match_obj[2])
        else:
            print('nothing match')

    def split_test(self):
        self = self
        line = 'a b     c'
        res_split = re.split(r'\s+', line)
        print(res_split)
        line = 'a,; b   ,;,; c  '
        res_split = re.split(r'[\s,;]+', line.strip(' '))
        print(res_split)


if __name__ == '__main__':
    myRe = MyRe()
    myRe.match_test()
    myRe.split_test()

