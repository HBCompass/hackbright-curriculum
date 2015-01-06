"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import add, subtract, multiply, divide, square, cube, mod, power

def main():
	# Your code goes here
	
	print "Enter your math problem in prefix notation. For example + 1 2. Enter q to quit."

	while True:	
		
		try:
			mathproblem = raw_input("> ")

			tokens = mathproblem.split(" ")

			if tokens[0] == "q":
				break

			else:

				if tokens[0] == "+":
					print(add(int(tokens[1]),(int(tokens[2]))))

				elif tokens[0] == "-":
					print(subtract(int(tokens[1]),(int(tokens[2]))))

				elif tokens[0] == "*":
					print(multiply(int(tokens[1]),(int(tokens[2]))))

				elif tokens[0] == "/":
					print(divide(int(tokens[1]),(int(tokens[2]))))

				elif tokens[0] == "square":
					print(square(int(tokens[1])))

				elif tokens[0] == "cube":
					print(cube(int(tokens[1])))

				elif tokens[0] == "mod":
					print(mod(int(tokens[1]),(int(tokens[2]))))

				elif tokens[0] == "power":
					print(power(int(tokens[1]),(int(tokens[2]))))

		except ValueError:
			print "I don't understand. Please enter a valid math problem or press q to quit."

if __name__ == '__main__':
    main()
