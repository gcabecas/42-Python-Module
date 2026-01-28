def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


def IsPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def Primes():
    n = 2
    while True:
        if IsPrime(n):
            yield n
        n += 1


def main():
    print("=== Game Data Stream Processor ===\n")
    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    fib_gen = fibonacci()
    for _ in range(9):
        print(next(fib_gen), end=", ")
    print(next(fib_gen))
    print("Prime numbers (first 5): ", end="")
    prime_gen = Primes()
    for _ in range(4):
        print(next(prime_gen), end=", ")
    print(next(prime_gen))


if __name__ == "__main__":
    main()
