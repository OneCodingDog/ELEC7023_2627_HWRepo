# Name: Zhong Ching Yu
# Assignment One
# ddl is 22/9/2026 23:59pm

choice = str(input("Which task do you want to view? (1/2)"))
if choice == "1":
	# Task A
	a = input("First number?")
	b = input("Second number?")
	op = input("Operator?")
	if op == '+' or op == '-' or op == '*' or op == '/':
	    print(a+op+b)
	    print(eval(str(a+op+b)))
	else:
	    print("Incorrect operator")

elif choice == "2":
	# Task B
	q = input("Please type in your question: ")

	if q == "hello":
	    print("Hello there!")
	elif q == "python":
	    print("Python is good")
	elif q == "jetson":
	    print("Jetson developed by Nvidia")
	elif q == "ai":
	    print("AI is AI")
	elif q == "name":
	    print("My name is Zhong Ching Yu")
	else:
	    print("Sorry, i can't answer it")




