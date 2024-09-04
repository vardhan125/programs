for row in range(11):
    for col in range(11):
        if row+col==5 or col-row==5 or row-col==5 or row+col==15:
            print("*",end="")
        else:
            print(end=" ")

    print()
