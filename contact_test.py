# import pyperclip
import unittest # importing unittest module
from contact import Contact # importing contact from contact class

class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        self.new_contact= Contact("James","Muriuki","0712345678","james@ms.com") # create contact object
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"james@ms.com")

    def test_save_contact(self):
        self.new_contact.save_contact() #saving new contact
        self.assertEqual(len(Contact.contact_list),1)

    def tearDown(self):
        # '''
        #     tearDown method that does clean up after each test case has run.
        #     '''
        Contact.contact_list= []
        

    def test_save_multiple_contact(self):
            #      '''
            # test_save_multiple_contact to check if we can save multiple contact
            # objects to our contact_list
            # '''
        self.new_contact.save_contact()
        test_contact= Contact("Test","user","0712345678","test@gmail.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    def test_delete_contact(self) :
        # '''
        #     test_delete_contact to test if we can remove a contact from our contact list
        #     '''
        self.new_contact.save_contact()
        test_contact= Contact("Test","user","0712345678","test@gmail.com")
        test_contact.save_contact()

        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_find_contact_by_number(self):
        self.new_contact.save_contact()
        test_contact= Contact("Test","user","0711223344","test@gmail.com")
        test_contact.save_contact()

        found_contact= Contact.find_by_number("0711223344")
        self.assertEqual(found_contact.phone_number,test_contact.phone_number)

    def test_contact_exists(self):
        self.new_contact.save_contact()
        test_contact= Contact("Test","user","0711223344","test@gmail.com")
        test_contact.save_contact()

        contact_exists =Contact.contact_exists("0711223344")
        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):  
        self.assertEqual(Contact.display_contacts(),Contact.contact_list)

    # def test_copy_email(self):
    #     self.new_contact.save_contact()
    #     Contact.copy_email("0712345678")
    #     self.assertEqual(self.new_contact.email,pyperclip.paste())
      


            




if __name__== '__main__':
    unittest.main()




       
        