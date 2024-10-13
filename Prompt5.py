import numpy as np

#creates the table
def createChart(start, end, numEntries):
    #table of x vs. sin(x)
    x_values = np.linspace(start, end, numEntries) #array of x values
    sin_values = np.sin(x_values)
    return x_values, sin_values #return the values in the table
    
def printChart(x_values, sin_values):
    #Print the table of x vs. sin(x)
    print(f"{'x':<10} {'sin(x)':<10}") #<10 takes up 10 spaces
    print("-" * 20)
    for x, sin_x in zip(x_values, sin_values): #pairs x with y
        print(f"{x:<10.3f} {sin_x:<10.3f}")#print x with 10 digits and 3 after decimal point

def main():
    start = 0
    end = 2
    numEntries = 1000
    
    x_values, sin_values = createChart(start, end, numEntries)
    printChart(x_values, sin_values)

if __name__ == "__main__":
    main()
    

