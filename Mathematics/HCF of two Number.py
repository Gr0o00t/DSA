#------------@@ \\NAVE// @@

# Time Complexity = thetha(n)
# Auxsillary space = constant (1)
def hcf_nave(num1,num2):

    if num1 < num2:
        for n in range(num1,1,-1):
            if (num1 % n)==0 and (num2 % n)==0:
                return n

    else:
        for n in range(num2,1,-1):
            if (num1 % n)==0 and (num2 % n)==0:
                return n

# #------------@@ \\Euclidean Algo// @@
#
# # Time Complexity = thetha(n)
# # Auxsillary space = constant (1)
def hcf_Euclidean(num1,num2):

    while Num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num2

# #------------@@ \\Optimized Euclidean Algo// @@

def hcf(num1,num2):
    if num2==0:
        return a
    return hcf(num2,num1%num2)

if __name__ == '__main__':
    print(hcf(200,100))