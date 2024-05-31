# Time Complexity = thetha(n)
# Auxsillary space = constant (1)

##------------ Normal Way---------##

# def factorial ( number ):
#
#     multi=1
#     for i in range(2,number+1):
#         multi=multi*i
#
#     return multi

##---------- Rescurssive Way----------##
# Time Complexity = thetha(n)
# Auxsillary space = constant (n)

def factorial ( number ):
    if number==0:
        return 1
    return number * factorial(number-1)

if __name__ == "__main__":
    print(factorial(-100))