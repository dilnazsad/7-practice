def isPrime(n):

    if n <= 1:
        return False

    for i in range(3, n):
        if n % i == 0:
            return False

    return True


def printPrime(n):
    for i in range(n, n * 2):
        if isPrime(i):
            print(i, end=" ")


if __name__ == "__main__":
    n = 40
    printPrime(n)

