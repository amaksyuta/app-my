def main( ):
    print("Hello Function")


def fib(num: int) -> int:
    return num if num < 2 else fib(num-1)+fib(num-2)


if __name__ == "__main__":
    main( )
    