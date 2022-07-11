import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        #print(f"Current book list: {list(self.book_list['book_name'])}")
        #print()
        
    def add_book(self, book_name, book_rating):
        #print(f"Adding {book_name} to the book list....")
        if book_name not in list(self.book_list['book_name']):
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [book_rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
            self.num_books += 1
            #print(f"{book_name} has been added to the book list.")
            #print(f"Current book list: {list(self.book_list['book_name'])}")
            return True
        else:
            #print(f"{book_name} is already in book list.")
            return False
        #print()
            
    def has_read(self,book_name):
        if book_name in list(self.book_list['book_name']):
            #print(f"You have already read {book_name}.")
            #print()
            return True
        else:
            #print(f"You have not yet read {book_name}.")
            #print()
            return False
        
    def num_books_read(self):
        #print(f"You have read {self.num_books} book(s) so far.")
        #print()
        return self.num_books
    
    def fav_books(self):
        fav = list(self.book_list[self.book_list['book_rating'] > 3]['book_name'])
        #print(f"Your favorite books are {fav}")
        #print()
        return fav
    
    
if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("War of the Worlds", 5)
    test_object.has_read("War of the Worlds")
    test_object.has_read("Pachinko")
    test_object.num_books_read()
    test_object.fav_books()