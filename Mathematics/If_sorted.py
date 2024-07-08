lst=[30,20,10]

def check_sorted(lst):
    temp= lst[0]
    for num in lst[1:]:
        if num > temp:
            temp = num      
        else:
            return False
    return True


print( check_sorted(lst))