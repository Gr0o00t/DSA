
# Time Complexity = big O ( Log(min(a,b))
def gcd(a, b):

    if b==0:
        return a

    return gcd(b,a%b)

def lcm(a,b):
    return a*b // gcd( a, b)

if __name__ == "__main__":
    a=4
    b=5
    print(lcm(a,b))