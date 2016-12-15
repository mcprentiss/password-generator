#!/usr/bin/env python3
"""Generate random passwords."""
# -*- coding: utf-8 -*-

import random

# import q
# tail -f /tmp/q
# @q
# q(fff)

def main():
    """ Main function of password."""
    try:
        fff = open('/usr/share/dict/words')
    except IOError:
        print('/usr/share/dict/word will not open')
    sss = [x.strip() for x in fff.readlines()]
    print(random.choice(sss).capitalize())
    pword = ''.join(random.choice(sss)).capitalize()
    # pword = ''.join(random.choice(sss) for i in range(1)).capitalize()
    lll = list(pword[0:8] + '!@#$%^&*' + str(random.randint(10000000, 99999999)))
    random.shuffle(lll)
    result = ''.join(lll)
    return result


if __name__ == '__main__':
    print(main())
