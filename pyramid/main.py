'''Write a program where a function takes an integer which is an odd number.
If it is an even number or zero, you can throw an exception and quit.

Program must print a grid of numbers where the middle number is the
highest and the numbers on either side become less and less.

eg.
python program.py 1
1

python program.py 3
111
121
111

python program.py 5
11111
12221
12321
12221
11111

python program.py 7
1111111
1222221
1233321
1234321
1233321
1222221
1111111
'''

import argparse
from pyramid import pyramid_grid


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="type in an odd number", type=int)
    args = parser.parse_args()
    pyramid = pyramid_grid(args.number)

    for row, col in pyramid:
        print(row, col)


if __name__ == '__main__':
    main()