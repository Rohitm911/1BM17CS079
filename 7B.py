def disp():
    print(" ",end="")
    for j in range(3):
        for i in range(3):
            print("-",end="")
        print("",end=" ")
    print(" ")
    for i in range(4):
        print("| ",end="  ")
    print("")
for i in range(3):
    disp()
