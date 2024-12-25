import unittest
from library_management_system import Library

class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        self.library.add_book("67890", "1984", "George Orwell", 1949)

    def test_add_book(self):
        self.library.add_book("11223", "To Kill a Mockingbird", "Harper Lee", 1960)
        self.assertEqual(len(self.library.view_available_books()), 3)

    def test_add_duplicate_book(self):
        with self.assertRaises(ValueError):
            self.library.add_book("12345", "Duplicate", "Author", 2023)

    def test_borrow_book(self):
        self.library.borrow_book("12345")
        self.assertEqual(len(self.library.view_available_books()), 1)

    def test_borrow_unavailable_book(self):
        self.library.borrow_book("12345")
        with self.assertRaises(ValueError):
            self.library.borrow_book("12345")

    def test_return_book(self):
        self.library.borrow_book("12345")
        self.library.return_book("12345")
        self.assertEqual(len(self.library.view_available_books()), 2)

    def test_return_unavailable_book(self):
        with self.assertRaises(ValueError):
            self.library.return_book("00000")

if __name__ == "__main__":
    unittest.main()
