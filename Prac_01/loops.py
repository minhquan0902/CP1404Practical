for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0 ,100,10):
    print(i, end=' ')
print()

for i in range(20,1,-1):
    print(i, end=' ')
print()

stair= int(input("Input the number of stairs: "))
for i in range(0, stair,1):
    print('*', end=' ')
print()

print("    ")
print("    ")
for i in range(0,stair):
    for j in range(0, i+1):
        print("*", end=' ')
    print("\r")