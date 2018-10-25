#!/usr/bin/env python3

word = 'bottles'
for beer_num in range(99, 0, -1):
    print(beer_num, word, 'of beer on the wall.')
    print(beer_num, word, 'of beer.')
    print('Take one down.')
    print('Pass it around.')
    if beer_num == 1:
        print('No more bottles of beer on the wall.')
    else:
        # original subtracting 1 from beer_num
        # new_num = beer_num - 1

        # subtracting 1 from beer_num
        beer_num -= 1
        if beer_num == 1:
            word = 'bottle'
        print(beer_num, word, 'of beer on the wall.')
    print()