" This code is simple calculator, it will ask user to insert two numbers and operator and will calculate outcome. The equations will be writen in the text file"
#loop for defensive program.
while True: 
    try:
        # Input of  first number.
        x = int(input("Enter first number : ")) 
        break           
    except ValueError:
         # Gives error if entered wrong value
        print("Oops! That was not a valid number. Try again... ")
if x < 0:
         # Prevention of +-/* by 0 
        raise Exception('Error, please enter an intenger greater than 0 .')      
                    
while True:
        try:
             # Input of second number.
            y = int(input("Enter second number : "))
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again... ")
if y < 0:
        # Prevention of +-/* by 0
        raise Exception('Error, please enter an intenger greater than 0.') 


while True:
        try:
            #Input of operation.
            z = input("Enter operation +, - , * , /  : ")  
            break
        except ValueError:
           print ("Wrong operation")
                            
if z == "-":
        # Outcome of calculation.    
        print(f"{x} - {y} = {x-y}\n") 
        file_name = "equation.txt"
        # 'a' - Any data being written will be inserted at the end after the existing data in text file.
        file = open(file_name, 'a+') 
        # The equation is written in the text file.
        file.write(f"{x} - {y} = {x-y}\n") 
        file.close()
elif z == "+":
        print(f"{x} + {y} = {x + y}\n")
        file_name = "equation.txt"
        file = open(file_name, "a+")
        file.write(f"{x} + {y} = {x + y}\n")
        file.close()
elif z == "*":
        print(f"{x} * {y} = {x * y}")
        file_name = "equation.txt"
        file = open(file_name, "a+")
        file.write(f"{x} * {y} = {x * y}\n")
        file.close()
elif z == "/":
        while True:
                try:                                      
                    print(f"{x} / {y} = {x / y}")
                    file_name = "equation.txt"
                    file = open(file_name, "a+")
                    file.write(f"{x} / {y} = {x / y}\n")
                    file.close()
                    break
                except ZeroDivisionError:
                    print("Error. Sorry, you can't divide by zero.")           
                break

else:
         # If user entered unappropriate operator it will display error
        print("Wrong operator")
        




'''**************PART TWO*****************'''
'''The program will run and give the user options: to continue to insert numbers and operators to create equation or second 
option to write the text file name and read from text file'''
        
the_option = input("Please enter one of the options: 1 (enter two numbers greater than 0) or 2 (open the txt file) : ")

if the_option == "1":

    #loop for defensive program. Repeating same code above if user choose oprion "1"
    while True: 
        try:
            x = int(input("Enter first number : "))
            break           
        except ValueError:
            print("Oops! That was not a valid number. Try again... ")
    if x < 0:
        raise Exception('Error, please enter an intenger greater than 0.')        
                    
    while True:
        try:
            y = int(input("Enter second number  : "))
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again... ")
    if y < 0:
        raise Exception('Error, please enter an intenger greater than 0.') 


    while True:
        try:
            z = input("Enter operation +, - , * , /  : ")  
            break
        except ValueError:
            print ("Wrong operation")

    if z == "-":
        print(f"{x} - {y} = {x-y}")
        file_name = "equation.txt"
        file = open(file_name, "a+")
        file.write(f"{x} - {y} = {x-y}\n")
        file.close()
    elif z == "+":
        print(f"{x} + {y} = {x + y}")
        file_name = "equation.txt"
        file = open(file_name, "a+")
        file.write(f"{x} + {y} = {x + y}\n")
        file.close()
    elif z == "*":
        print(f"{x} * {y} = {x * y}")
        file_name = "equation.txt"
        file = open(file_name, "a+")
        file.write(f"{x} * {y} = {x * y}\n")
        file.close()
    elif z == "/":
            while True:
                try:                  
                    print(f"{x} / {y} = {x / y}")
                    file_name = "equation.txt"
                    file = open(file_name, "a+")
                    file.write(f"{x} / {y} = {x / y}\n")
                    file.close()
                    break
                except ZeroDivisionError:
                    print("Error. Sorry, you can't divide by zero. ")    
                break
    else:
        print("Wrong operator")        
   
# Program will asks user to enter the name of text file to read from it.
elif the_option == "2": 

    file_name = "equation.txt"
    file = open(file_name, "r")

    file_name = input("Please enter the name of the txt file: ")
    file = None
    try:
        # 'r' - For reading from the text file.
        file = open(file_name, 'r') 
        # Reads each line in the text file
        read_lines = file.read()
        print(read_lines)
        file.close()
    except FileNotFoundError:
        print("The file that you are trying to open does not exist")
    
    finally:
        if file is not None:
            file.close()
else:
    print()

