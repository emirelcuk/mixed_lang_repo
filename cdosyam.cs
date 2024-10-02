using System;
using System.Collections.Generic;

class Book
{
    public string Title { get; set; }
    public string Author { get; set; }
    public string ISBN { get; set; }

    public override string ToString()
    {
        return $"Title: {Title}, Author: {Author}, ISBN: {ISBN}";
    }
}

public class Library
{
    private readonly List<Book> _books;

    public Library()
    {
        _books = new List<Book>();
    }

    public void AddBook(Book book)
    {
        if (book != null && !_books.Exists(b => b.ISBN == book.ISBN))
        {
            _books.Add(book);
        }
    }

    

    public Book FindBookByIsbn(string isbn)
    {
        return _books.FirstOrDefault(book => book.ISBN == isbn);
    }
}


    public void ListBooks()
    {
        if (books.Count == 0)
        {
            Console.WriteLine("No books in the library.");
            return;
        }
        foreach (var book in books)
        {
            Console.WriteLine(book);
        }
    }
}

class LibraryManager
{
    static void Main(string[] args)
    {
        var library = new Library();
        bool running = true;

        while (running)
        {
            Console.WriteLine("\nLibrary Management System");
            Console.WriteLine("1. Add Book");
            Console.WriteLine("2. Remove Book");
            Console.WriteLine("3. Search Book");
            Console.WriteLine("4. List Books");
            Console.WriteLine("5. Exit");
            Console.Write("Choose an option: ");
            int choice = int.Parse(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    Console.Write("Book Title: ");
                    string title = Console.ReadLine();
                    Console.Write("Book Author: ");
                    string author = Console.ReadLine();
                    Console.Write("Book ISBN: ");
                    string isbn = Console.ReadLine();
                    library.AddBook(new Book(title, author, isbn));
                    Console.WriteLine("Book added.");
                    break;

                case 2:
                    Console.Write("Enter ISBN of the book to remove: ");
                    string isbnToRemove = Console.ReadLine();
                    library.RemoveBook(isbnToRemove);
                    Console.WriteLine("Book removed.");
                    break;

                case 3:
                    Console.Write("Enter title of the book to search: ");
                    string searchTitle = Console.ReadLine();
                    var foundBook = library.FindBookByTitle(searchTitle);
                    if (foundBook != null)
                    {
                        Console.WriteLine("Book Found: " + foundBook);
                    }
                    else
                    {
                        Console.WriteLine("Book not found.");
                    }
                    break;

                case 4:
                    Console.WriteLine("Books in the library:");
                    library.ListBooks();
                    break;

                case 5:
                    running = false;
                    Console.WriteLine("Exiting program.");
                    break;

                default:
                    Console.WriteLine("Invalid choice.");
                    break;
            }
        }
    }
}
