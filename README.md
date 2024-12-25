# Library Management System

This project is a Python-based Library Management System that allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books. The system is implemented using Test-Driven Development (TDD) principles to ensure code reliability and maintainability.

## Features

1. **Add Books**:
   - Users can add new books to the library.
   - Each book has the following attributes:
     - Unique ISBN
     - Title
     - Author
     - Publication Year

2. **Borrow Books**:
   - Users can borrow books if they are available.
   - The system ensures that the book is not already borrowed.
   - If a book is unavailable, an error is raised.

3. **Return Books**:
   - Users can return borrowed books.
   - The system updates the availability status of the returned book.

4. **View Available Books**:
   - Users can view a list of all books currently available in the library.

## Project Structure

The project consists of the following files:

- **`library_management_system.py`**: Contains the main implementation of the library management system.
- **`test_library_management_system.py`**: Contains unit tests for the library management system.
- **`README.md`**: This file, which explains the project and provides instructions on how to use it.

## Installation and Setup

Follow these steps to set up and run the project:

1. **Install Python**:
   - Download Python from [python.org](https://www.python.org/) and install it.
   - Ensure Python is added to your system's PATH.

2. **Clone the Repository**:
   - Clone this repository to your local machine using:
     ```bash
     git clone <repository-url>
     ```

3. **Navigate to the Project Directory**:
   - Open a terminal and navigate to the project folder:
     ```bash
     cd LibraryManagementSystem
     ```

4. **Install Required Libraries**:
   - This project does not have external dependencies. Ensure Python's `unittest` module is available (it is included by default).

## How to Run the Project

### Run the Main Code:

1. Open the terminal in the project directory.
2. Run the following command to execute the main file:
   ```bash
   python library_management_system.py
   ```
3. Follow the instructions in the code to add, borrow, return, or view books.

### Run Unit Tests:

1. Open the terminal in the project directory.
2. Run the following command to execute the tests:
   ```bash
   python -m unittest test_library_management_system.py
   ```
3. The output will display the results of the test cases.

## Test-Driven Development (TDD)

This project follows TDD principles:

1. **Write Tests First**:
   - Unit tests are written for each feature before implementing the functionality.

2. **Implementation**:
   - Features are implemented to pass the written tests.

3. **Refactoring**:
   - Code is refactored for clarity and maintainability while ensuring all tests continue to pass.

## Code Design Principles

- **Clean Code**:
  - Readable variable and method names.
  - Comments to explain complex logic.
- **SOLID Principles**:
  - Single Responsibility Principle: Each class and method has a single, well-defined purpose.
- **Error Handling**:
  - Meaningful errors are raised when operations fail (e.g., borrowing an unavailable book).

## Example Usage

1. **Adding Books**:
   ```python
   library.add_book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
   library.add_book("67890", "1984", "George Orwell", 1949)
   ```

2. **Borrowing a Book**:
   ```python
   library.borrow_book("12345")
   ```

3. **Returning a Book**:
   ```python
   library.return_book("12345")
   ```

4. **Viewing Available Books**:
   ```python
   available_books = library.view_available_books()
   for book in available_books:
       print(book)
   ```


## License

This project is open-source and available under the MIT License.

---

Feel free to contribute to this project by creating issues or submitting pull requests!
