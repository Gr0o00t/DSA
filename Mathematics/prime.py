##time complexity is (n-2)

def isPrime_naive(n):

    if n==1:
        return False
    for i in range (2,n):
        if n%i==0:
            return False

    return True


# TIme Complexity = bif O( square root of n)
def isPrime_Divisors(num1):
    if num1 == 1:
        return False

    i=2
    while (i*i<=num1):
        if num1%i==0:
            return False
        i+=1
    return True


# Time Complexity is 3 times faster than previous approach
def isPrime(n):

    if n == 1:
        return False

    if n == 2 or n ==3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i=5

    while (i*i <= n):
        if n % i == 0 or n %(i+2) == 0:
            return False
        i+=6

    return True

if __name__ == "__main__":
    print(isPrime(51))