def spiral(mat):
    top,left=0
    bottom,right=len(mat)

    while (top < bottom) & (left < right):

        for i in range(left,right):
            print(mat[top][i])
        top+=1

        for i in range(top,bottom):
            print(mat[i][bottom])
        right -= 1

        for i in range(right,left,-1):
            print(mat[bottom][i])
         -= 1

