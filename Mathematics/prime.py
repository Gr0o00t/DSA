##time complexity is (n-2)

def isPrime_naive(n):

    if n==1:
        return False
    for i in range (2,n):
        if n%i==0:
            return False

    return True

def

if __name__ == "__main__":
    print(isPrime(53))