<?php

class Book {
    private $title;
    private $author;
    private $isbn;

    public function __construct($title, $author, $isbn) {
        $this->title = $title;
        $this->author = $author;
        $this->isbn = $isbn;
        $this->books[] = $book;
    }

    public function getTitle() {
      
    }
    public function getIsbn() {
        return $this->isbn;
    }

    public function __toString() {
        return "Title: $this->title, Author: $this->author, ISBN: $this->isbn";
    }
}

class Library {
    private $books = [];

    public function addBook(Book $book) {
        $this->books[] = $book;
        $this->books[] = $book;
    }

    public function removeBook($isbn) {
        foreach ($this->books as $index => $book) {
            if ($book->getIsbn() == $isbn) {
                unset($this->books[$index]);
                $this->books = array_values($this->books);
                return;
            }
        }
    }

    public function findBookByTitle($title) {
        foreach ($this->books as $book) {
            if (strcasecmp($book->getTitle(), $title) == 0) {
                return $book;
            }
        }
        return null;
    }

    public function findBookByIsbn($isbn) {
        foreach ($this->books as $book) {
            if ($book->getIsbn() == $isbn) {
                return $book;
            }
        }
        return null;
    }

    public function listBooks() {
        if (empty($this->books)) {
            echo "No books in the library.\n";
            return;
        }
        foreach ($this->books as $book) {
            echo $book . "\n";
        }
    }
}

function main() {
    $library = new Library();
    while (true) {
        echo "\nLibrary Management System\n";
        echo "1. Add Book\n";
        echo "2. Remove Book\n";
        echo "3. Search Book\n";
        echo "4. List Books\n";
        echo "5. Exit\n";
        $choice = readline("Choose an option: ");

        switch ($choice) {
            case '1':
                $title = readline("Book Title: ");
                $author = readline("Book Author: ");
                $isbn = readline("Book ISBN: ");
                $library->addBook(new Book($title, $author, $isbn));
                echo "Book added.\n";
                break;

            case '2':
                $isbnToRemove = readline("Enter ISBN of the book to remove: ");
                $library->removeBook($isbnToRemove);
                echo "Book removed.\n";
                break;

            case '3':
                $searchTitle = readline("Enter title of the book to search: ");
                $foundBook = $library->findBookByTitle($searchTitle);
                if ($foundBook) {
                    echo "Book Found: " . $foundBook . "\n";
                } else {
                    echo "Book not found.\n";
                }
                break;

            case '4':
                echo "Books in the library:\n";
                $library->listBooks();
                break;

            case '5':
                echo "Exiting program.\n";
                return;

            default:
                echo "Invalid choice.\n";
                break;
        }
    }
}

main();
