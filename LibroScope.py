# 1. Cuenta el número de veces que aparece cada personaje ¿en todo el libro? No, solo en una página.
class LibraryDatabase():
    def getAllBookTitles(self):
        # TODO: Add pagination
        books = self.getBooks()
        return [book for book in books]
    
    def getBooks(self):
        return {
            "harry potter": ["From Hermione: Dear Harry, I miss you.\nHey Harry! This is Ron. - Ron", "From Harry: Dear Hermione, I miss you too.\n- Harry"],
            "sherk": ["From Donkey:\nDear Sherk, You're run of toilet paper.\nP.D. The cookie man is sleeping in your bed - Donkey\n\nFrom Cookie man:\nHello Sherk! You're run of toilet paper 🙈 - Cookie man"],
            "cinderella": ["- Cinderella! Its almost 3 a.m. Let's goo! - Mouse 1\n- Cinderella! YOU FORGOT YOUR LEFT SHOE! - Mouse 2\n- So? - Cinderella"]
        }
        
    def getBookByName(self, bookName):
        books = self.getBooks()
        return books.get(bookName, None)
    
    def getBookCharacters(self, book):
        books = {
            "harry potter": ["Hermione", "Harry", "Ron"],
            "sherk": ["Sherk", "Donkey", "Cookie man"],
            "cinderella": ["Cinderella", "Fairy Godmother", "Mouse 1", "Mouse 2"]
        }
        return books.get(book, [])
    

class Library():
    def __init__(self, database: LibraryDatabase):
        """ Inicializa la biblioteca con una base de datos y una lista de libros. """
        self.database = database
        
    def countCharactersWithoutCountFunction(self):
       pass

    def countCharacters(self, book, character):
        return book.count(character)
        
    def getAllBookCharactersCount(self, _):
        print("Hello!:D\nThis feature is under construction. Please get back later.")
        return None

    def getBookPageCharactersCount(self, bookName, page = 0):
        """ Count the occurrences of each character in bookPage. """
        count = {}
        book = self.database.getBookByName(bookName) # List with all pages content
        
        if book is None:
            print("Invalid book name.")
            return None
        
        if page < 0 or page >= len(book):
            print("The page you're asking for does not exist.")
            return None

        bookPage = book[page] # Convertir la página a minúsculas
        print(bookPage)
        
        bookPage = bookPage.lower() # Convertir la página a minúsculas
        characters = self.database.getBookCharacters(bookName) # Lista de personajes

        # The next line was generated with Chatgpt
        # Prompt: Use dictionary comprehension for better performance and readability
        count = {c.lower(): self.countCharacters(bookPage, c.lower()) for c in characters}
        return count

def validatePageInput(bookPage):
    if len(bookPage) == 0:
        return True
    try:
        bookPage = int(bookPage)
        return bookPage
    except ValueError:
        return None

# Main Code
def main():
    database = LibraryDatabase()
    library = Library(database)
    charactersCount = None
    bookName = ""
    bookPage = ""
    
    bookTitles = library.database.getAllBookTitles()
    print("Available books: ", bookTitles)
    
    while(bookName == ""):
        bookName = input("Book: ").lower()

    if bookName not in bookTitles:
        print("Invalid book name.\nGood bye.")
        return

    bookPage = input("Page (empty for all): ")
    bookPage = validatePageInput(bookPage)

    if bookPage is None: 
        print("Invalid page.\nGood bye.")
        return

    print("..............")
    
    if isinstance(bookPage, bool) and bookPage == True:
        charactersCount = library.getAllBookCharactersCount(bookName)
    else: 
        charactersCount = library.getBookPageCharactersCount(bookName, bookPage)

    print("..............")
    print("count: ", charactersCount)

main()
