
def palindromenumber(Number):
    temp = Number
    dumpy=0
    while temp > 0:
        dumpy = dumpy*10 + temp % 10

        temp = temp // 100

    return dumpy == Number

print(palindromenumber(11))