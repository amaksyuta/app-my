#!/usr/bin/env python


def fib(num: int) -> int:
    return num if num < 2 else fib(num-1)+fib(num-2)


def summ(one, two):
    return one + two


def main( ):
    print("Hello Function")
    fib(20)
    summ(2, 5)


if __name__ == "__main__":
    main( )
