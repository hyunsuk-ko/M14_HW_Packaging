import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): # Add a book and test if it is in `book_list`
        test_1 = BookLover('Adam Driver', 'adriver@gmail.com', 'rom-com')
        testValue = test_1.add_book("Marriage Story", 5)
        message = "Test value is not true."
        self.assertTrue(testValue, message)
        
    def test_2_add_book(self): # Add the same book twice. Test if it's in `book_list` only once. 
        test_2 = BookLover('Dainel Day-Lewis', 'ddl@gmail.com', 'drama')
        test_2.add_book("Marriage Story", 5)
        testValue = test_2.add_book("Marriage Story", 5)
        message = "Test value is not false."
        self.assertFalse(testValue, message)
        
    def test_3_has_read(self): # Pass a book in the list and test the answer is `True`.
        test_3 = BookLover('Meryl Strip', '.mstrip()@gmail.com', 'action')
        test_3.add_book("Mamma mia", 5)
        testValue = test_3.has_read("Mamma mia")
        message = "Test value is not true."
        self.assertTrue(testValue, message)
         
    def test_4_has_read(self): # Pass a book NOT in the list and use `assert False` to test if the answer is `True`
        test_4 = BookLover('Joaquin Phoneix', 'phoenixsuns@gmail.com', 'thriller')
        testValue = test_4.has_read("Joker")
        message = "Test value is not false."
        self.assertFalse(testValue, message)
        
    def test_5_num_books_read(self): # Add some books to the list, and test num_books matches expected.
        test_5 = BookLover('Brad Pitt', 'breadfeet@gmail.com', 'sci-fi')
        test_5.add_book("World War Z", 5)
        test_5.add_book("The Curious Case of Benjamin Button", 5)
        num_books = 2
        message = "First value and second value are not equal !"
        self.assertEqual(num_books, test_5.num_books_read(), message)
        
    def test_6_fav_books(self): # Add some books with ratings to the list, making sure some of them have rating > 3.
                            # Your test should check that the returned books have rating  > 3.
        test_6 = BookLover('Emma Stone', 'estone@gmail.com', 'rom-com')
        test_6.add_book("La La Land", 5)
        test_6.add_book("Cruella", 4)
        test_6.add_book("Birdman", 4)
        test_6.add_book("Crazy Stupid Love", 3)
        
        actual = test_6.fav_books()
        expected = ["La La Land", "Cruella", "Birdman"]
        message = "First value and second value are not equal !"
        self.assertEqual(actual, expected)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=3)