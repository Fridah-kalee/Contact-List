#!/usr/bin/env python3.9
from contact import Contact
import random 

def create_contact(fname,lname,phone,email):
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(contact):
    contact.save_contact()

def del_contact(contact):
    contact.delete_contact()

def find_contact(number):
    return Contact.find_by_number(number)

def check_existing_contacts(number):
    return Contact.contact_exist(number)

def display_contacts():
    return Contact.display_contacts()


def main():
    # def generatePassword(stringLength=8):
    #     """Generate a random password string of letters and digits and special characters"""
    #     user_password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
    #     return ''.join(random.choice(password) for i in range(stringLength))
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()
    
    # print("Hello Welcome to your contact list. What is your password?")
    # user_password = input()
    # p= input("Input your password")
	# x = True
	# while x:  
	#     if (len(p)<6 or len(p)>12):
	#         break
	#     elif not re.search("[a-z]",p):
	#         break
	#     elif not re.search("[0-9]",p):
	#         break
	#     elif not re.search("[A-Z]",p):
	#         break
	#     elif not re.search("[$#@]",p):
	#         break
	#     elif re.search("\s",p):
	#         break
	#     else:
	#         print("Valid Password")
	#         x=False
	#         break
	
	# if x:
	#     print("Not a Valid Password")
    # while True:
    #     UserName = input ("Enter Username: ")
    #     PassWord = input ("Enter Password: ")

    #     if UserName == '' and PassWord == '':
    #         time.sleep(1)
    #         print ("Login successful!")
    #         logged()

    #     else:
    #         print ("Password did not match!")

    # def logged():
    #  time.sleep(1)
    #  print ("Welcome to ----")
    
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Contact")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
            print ('\n')
            print(f"New Contact {f_name} {l_name} created")

            print ('\n')

        elif short_code == 'dc':

            if display_contacts():
                print("Here is a list of all your contacts")

                print('\n')

                for contact in display_contacts():

                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                    print('\n')
                else:
                    print('\n')
                    print("You dont seem to have any contacts saved yet")

                    print('\n')
            elif short_code == 'fc':
                print("Enter the number you want to search for")

                search_number = input()
                if check_existing_contacts(search_number):

                    search_contact = find_contact(search_number)
                    print(f"{search_contact.first_name} {search_contact.last_name}")
                    print('-' * 20)

                    print(f"Phone number.......{search_contact.phone_number}")
                    print(f"Email address.......{search_contact.email}")
                else:
                    print("That contact does not exist")
            elif short_code == "ex":
                print("Bye .......")
                break

            else:
                print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()



                        