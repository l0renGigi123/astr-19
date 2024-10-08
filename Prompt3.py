#define function
def f(x):
    return x**3 + 8
    
#define main func, tell program what to do with f(x)
def main():
    
    x = 9 
    result = f(x)
    print(result)
    
    if result > 27:
        print("YAY!")
    
#executing main first        
if __name__=="__main__":
    main()