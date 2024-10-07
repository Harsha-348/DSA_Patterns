#python program to print a half equilateral shaped pattern filled with stars

n=int(input("enter the number:"))

for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()
pass

#python program to print reverse half equilateral in star shaped pattern

n=int(input("enter the number:"))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()
pass
