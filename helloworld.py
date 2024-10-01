# comments
#describe what program does

#function prints Hello World!
def PrintHelloWorld():
	print("Hello World!")

#main function. preforms all tasks of program
def main():
	PrintHelloWorld()

#design programs that other programs can use (modules)
#which function should be executed first. Which one is the main one?
if __name__=="__main__":
	main()
