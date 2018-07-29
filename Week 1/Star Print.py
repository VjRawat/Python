#1
for i in range(1,4):                        
    for j in range(0,i):
        print("*", end=" ")
    print(" ")


#2
    
for i in range(1,4):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print(" ")


#3

for i in range(1,4):
    for j in range(i,4):
        print("*", end=" ")
    print(" ")



#4

for i in range(0,5):
    for j in range(4,i,-1):
        print(" ", end=" ")
    for k in range(0,i):
        print("*", end=" ")
    if(i>1):
        for l in range(1,i):
            print("*", end=" ")
    print(" ")
