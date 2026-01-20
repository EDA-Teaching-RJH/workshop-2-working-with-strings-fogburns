import math  
print("To workout Hypotenuse(C) Enter A and B Below...")
def main():
    global A
    global B
    A=float(input("Provide A: "))
    B=float(input("provide B: "))
def pythag(A,B):
    global C
    c=(A**2+B**2)
    C=math.sqrt(c)
    print("C is :"+str(C))
main()
pythag(A,B)
