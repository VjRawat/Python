triangle1 = 3
triangle2 = 1
triangle3 = 0

for i in range(4):
    for k in range(triangle1):
        print("_", end=" ")
    for k in range(triangle2):
        print("*", end=" ")
    for k in range(triangle3):
         print("*", end=" ")
    print("\n")
    triangle1 -= 1
    triangle2 +=1
    triangle3 +=1
        
