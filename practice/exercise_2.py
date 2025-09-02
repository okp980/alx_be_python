class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author} has {self.pages} pages"
    
    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, pages={self.pages})"
    
def main():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    print(book)
    print(repr(book))
if __name__ == "__main__":
    main()