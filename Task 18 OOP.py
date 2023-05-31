# Did this code with great help of mentor
# This code will help user choose to list email that are read or unread 
class Email:
    # Class variable, with default value, for emails
    has_been_read = False

    
    # The instance variables for emails
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        
    
    # A function turn has_been_read to True    
    def mark_as_read (self):
        self.has_been_read = True
        print("You have read the email.")


    # A function turn has_been_read to False
    def mark_as_not_read(self):
        self.has_been_read = False
        print("Unread email.")


# An empty list to store the email and its objects
inbox_list = [] 
email1 = Email("masha@gmail.com", "Task1", "Please complete your task")
email2 = Email("sasha@yahoo.com", "Task2", "This task due to end of April")
email3 = Email("syusan@i.co.ua", "Meeting", "Your meeting is on Monday at 12:30 PM")


# Adding emails to the inbox list
def populate_inbox():
    inbox_list.append(email1)
    inbox_list.append(email2)
    inbox_list.append(email3)
      
populate_inbox()

    
#  A function which prints the email’s subject_line, along with a corresponding number   
def list_emails():
    # Enumerating method where "index" is a corresponding number and "email" is a subject line (subject_line) of an email
    
    for index, email in enumerate(inbox_list):
        print(index, email.subject_line)
        


# A function which displays a selected email.
def read_email():
    # Calling fuction to display the email’s subject_line, along with a corresponding number
    list_emails()
    # Ask user to enter their's choosen index(email)
    index = int(input("\nEnter the index: "))
    # Calling index of the email
    email_choice  = inbox_list[index]
    # Display email address, subject line and content by using object of class Email
    print(email_choice.email_address)
    print(email_choice.subject_line)
    print(email_choice.email_content)
    # Changing email has_been_read to True by using class verible 
    email_choice.mark_as_read()   



#Create function for unread emails where class varible has_been_read chenge to False and displays email address/subject/content
def display_unread_emails():
    
        
    for index, email in enumerate(inbox_list):
        if email.has_been_read:
            print("No emails to read")
            break
        elif not email.has_been_read:
            print(email.email_address)  
            print(email.subject_line)
            print(email.email_content)
        else:
            ("Oops!")
     
        
    
# Menu option for user to read an email, view unread emails or quit application
def main():
    
    menu = True
# input - User should select one of the option
    while True:
        user_choice = int(input('''\nWould you like to:
            1. Read an email
            2. View unread emails
            3. Quit application

            Enter selection: '''))
            
        if user_choice == 1:
            # Calling function to display all read emails
            
            read_email()
            
                                                    
        elif user_choice == 2:
            # Calling function to display all unread emails
            
            display_unread_emails()
             

        elif user_choice == 3:
                # To exit application
                print("Goodbye")
                break
        else:
                print("Oops - incorrect input.")
main()