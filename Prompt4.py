#declare class
class Dog:
    #initialization function that sets values of the data members 
    def __init__(self, arms, legs, eyes, tail, furry):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry
        
    #member function
    def describeMyDog(self):
        print(f"My dog's arms and legs are {self.arms} and {self.legs} feet long.")
        print(f"She has {self.eyes} eyes.")
        print(f"My dog has a tail: {self.tail}")
        print(f"My dog is furry: {self.furry}")      
        
#assign values to data members        
my_dog = Dog(0.5, 0.5, 2, True, False)
my_dog.describeMyDog()  #prints the function