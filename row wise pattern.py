def row(a):
    for i in range(1,a):

        for j in range(1,a):
            if i % 2 != 0:
                print("1",end=" ")
            else:
                print("0",end=" ") 
        print( )
row(6)