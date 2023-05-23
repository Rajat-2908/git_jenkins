for i in range (1,11):
    if i == 1:
        print('       %d' %i,end=" ")
    else:
        print('  %d'%i,end=" ")
print("\n   +--------------------------------------------")


for i in range(1,11):
    if i<10:
        print(" ",end="")
    print(i,"| ",end="")
    for j in range(1,11):
        print("%3d"%(i*j),end=" ")
    print(" ")
print("")

