#python program to print a square shaped patter filled with stars

def square(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
    pass
    

square(10)

