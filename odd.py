#!/usr/bin/env python3

from datetime import datetime
# Original odds list
# odds = [ 1, 3, 5, 7, 9,11,13,15,17,19, 
#         21, 23, 25, 27, 29, 31, 33, 35, 
#         37, 39, 41, 43, 45, 47, 49, 51, 
#         53, 55, 57, 59 ]

# odds list using list comprehension
# odds = [x for x in range(1, 60) if x % 2 == 1]

# odds list using range(start, stop, step)
odds = list(range(1,60,2))
right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print('This minute seems a little odd.')
else:
     print('Not an odd minute.')   