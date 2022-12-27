# [문제]
# Two’s complement is used to express negative numbers in binary. For example, the value 30 in signed 8- bit binary is 00011110,
# and the signed 8-bit two’s complement representation of -30 is 11100010. An easy way to convert from 00011110 to 11100010 is simply reverse 00011110 to become 11100001,
# and then add 1, which produces 11100010.
# Your job is to read in two positive integers, express them in 8-bit signed binary, then their negative values in two’s complement,
# and then the difference between the two in 8-bit signed binary.
# For example, the difference between 30 and 18 is 12, which in 8-bit signed binary is 00001100, or if you subtract 18 – 30, you get -12,
# which in two’s complement (signed 8-bit) is the reverse of 00001100 + 1, or 11110011 + 1, or 11110100.

# [입력]
# Several pairs of positive integers X and Y, each pair on one line, with 0

# [출력]
# For each pair of values, five 8-bit signed strings, representing X, Y, -X, -Y, and X-Y, with a blank line following each output set.

import sys

def binary(num, b):
    if (num < b) and (num > 0):
        return str(num)
    elif num < 0:
        num = 256 + num
    s = binary(num // b, b)
    return s + str(num % b)

while True:
    data = list(map(int,sys.stdin.readline().split()))
    if len(data) == 0: break

    for d in data:
        d = int(d)
        if d==0: pass
        else:
            result = binary(d,2).zfill(8)
            print('{} = {}'.format(d,result))

    for d in data:
        d = int(d)
        if d==0: pass
        else:
            result = binary(-d,2).zfill(8)
            print('{} = {}'.format(-d,result))

    for _ in range(1):
        d = int(data[0]) - int(data[1])
        if int(d)==0: pass
        else:
            result = binary(d,2).zfill(8)
            print('{} = {}'.format(d,result))
    print('')