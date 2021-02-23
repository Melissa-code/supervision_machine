#!/usr/bin/env python
# -*- coding: utf-8 -*-


def encode_b64(s):
    #
    # (1)
    #
    lst = []
    for car in s:
        lst.append(car)
    #
    # (2)
    #
    position = 0
    for element in lst:
        lst[position] = ord(element)
        position = position + 1
    #
    # (3)
    #
    position = 0
    for element in lst:
        lst[position] = bin(element)
        position = position + 1
    #
    # (4)
    #
    position = 0
    for element in lst:
        lst[position] = element[2:len(element):1]
        position = position + 1
    #
    # (5)
    #
    position = 0
    for element in lst:
        while len(lst[position]) < 8:
            lst[position] = '0' + lst[position]
        position = position + 1
    #
    # (6)
    #
    st = ''
    for element in lst:
        st = st + element
    #
    # (7)
    #
    lst = []
    for position in range(0, len(st), 6):
        lst.append(st[position:position + 6])
    #
    # (8)
    #
    while len(lst[len(lst) - 1]) < 6:
        lst[len(lst) - 1] = lst[len(lst) - 1] + '0'
    #
    # (9)
    #
    position = 0
    for element in lst:
        lst[position] = int(lst[position], base=2)
        position = position + 1
    #
    # (10)
    #
    tbl_b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    position = 0
    for element in lst:
        lst[position] = tbl_b64[element]
        position = position + 1
    #
    # (11)
    #
    st = ''
    for element in lst:
        st = st + element
    #
    # (12)
    #
    while len(st) % 4 != 0:
        st = st + '='
    return st


def decode_b64(s):
    return 'Decoded...'


def main():
    print('Base 64 encoder/decoder')
    #
    # Infinite loops until user enters 'x' to exit
    #
    while True:
        user_choice = input('(E)ncode, (D)ecode or e(X)it:')
        if user_choice.upper() == 'X':
            print('Exiting!')
            break
        if user_choice.upper() not in ('E', 'D'):
            print('Invalide choice!')
            continue
        while True:
            user_input = input('Enter your string or e(X)it:')
            if user_input.upper() == 'X':
                break
            if user_choice.upper() == 'E':
                print('Encoded string: {}'.format(encode_b64(user_input)))
            else:
                print('Decoded string: {}'.format(decode_b64(user_input)))


if __name__ == '__main__':
    main()
