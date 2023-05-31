
'''This code will read each line with certaine format with two different sections for names and birthdates'''


file = open("DOB.txt", 'r') # Reading mode
lines = file.readlines() 
contents = "\nNames\n" # Adds new line "Names" to the lines 
print(contents)
for line in lines:  #Loop for lines with names
    
    temp = line.strip(",")
    temp = line.split() #Spliting each line as a list
    the_line = temp[0:2] #Index for each word 
    list_1 = " ".join(the_line)
    
    print (list_1)
    
file.close()

file = open("DOB.txt", 'r') 
lines = file.readlines()
contents = "\nBirthdate\n"
print(contents)
for line in lines:  # Second loop for berthdate
    
    temp = line.strip(",")
    temp = line.split()
    the_line = temp[2:4] #Index for each word and number
    list_1 = " ".join(the_line)
    
    print (list_1)
    
file.close()