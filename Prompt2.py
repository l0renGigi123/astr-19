
def PrintNums():
    a=2.1
    b=3.4
    c=6
    d=3
    print("Sum of two floating point numbers: " + str(a+b))
    print(type(a+b))
    print("Difference between two integers: " + str(c-d))
    print(type(c-d))
    print("Product of a floating point number and an integer: " + str(a*b))
    print(type(a*b))
    
def main():
    PrintNums()
    
if __name__=="__main__":
    main()
