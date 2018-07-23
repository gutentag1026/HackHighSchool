#!/usr/bin/env python3
# convert decimal to binary 
# By <yhuang>

import sys

def convert(num, base=2):
    data = []
    digits = "0123456789ABCDEF"
    while num:
        data.append(digits[num % base])
        num //= base
    return "".join(data[::-1])


def main(args):
    if len(args) == 2:
        casted_arg  = int(args[1])
        print(f"""{convert(casted_arg)}
{convert(casted_arg, base=8)}
{convert(casted_arg, base=16)}""")

if __name__ == "__main__":
    main(sys.argv)
