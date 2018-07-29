# Print the pattern
#       --3
#       --2
#       32123

for i in range(1,4):
    if (i<3):
        for j in range(1, 3):
            print("_", end=" ")

    if(i<2):
        for k in range(3, 4):
            print(k, end=" ")

    if(i==2):
        for l in range(2, 3):
            print(l, end=" ")

    if(i==3):
        for m in range(3, 0, -1):
            print(m, end=" ")
        for n in range(2,4):
            print(n, end=" ")
            
    print(" ")
        
