def countdigit(digit):
    count = 0
    while digit > 0:
        count += 1
        digit = digit // 10

    return count


print(countdigit())
