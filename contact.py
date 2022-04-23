# import pyperclip
class Contact:

    contact_list= [] #empty contact list
    def __init__(self,first_name,last_name,phone_number,email):
    
        # '''
        # __init__ method that helps us define properties for our objects.

        # Args:
        # first_name: New contact first name.
        # last_name: New contact last name.
        # phone_number: New contact phone number.
        # email: New contact email.
        
        # '''
        self.first_name=first_name
        self.last_name=last_name
        self.phone_number=phone_number
        self.email=email

    def save_contact(self):
        Contact.contact_list.append(self)

    def delete_contact(self):
        Contact.contact_list.remove(self) 

    @classmethod
    def find_by_number(cls,phone_number):
    # '''
    #     Method that takes in a number and returns a contact that matches that number.

    #     Args:
    #         number: Phone number to search for
    #     Returns :
    #         Contact of person that matches the number.
    #     '''

     for contact in cls.contact_list:
        if contact.phone_number==phone_number:
            return contact

    @classmethod
    def contact_exists(cls,phone_number):
        # '''
        # Method that checks if a contact exists from the contact list.
        # Args:
        #     number: Phone number to search if it exists
        # Returns :
        #     Boolean: True or false depending if the contact exists
        # '''
        for contact in cls.contact_list:
            if contact.phone_number ==phone_number:
                return True

        return False 

    @classmethod
    def display_contacts(cls): 
        return cls.contact_list 

    # @classmethod
    # def copy_email(cls,phone_number):
    #     contact_found = Contact.find_by_number(phone_number)
    #     pyperclip.copy(contact_found.email)             
   

    



