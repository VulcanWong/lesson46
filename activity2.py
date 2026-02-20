class library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library:{self.name}")
        for book in self.bookslist:
            print(book)
    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender-book database has been updated. you can take the book now")
        else:
            print(f"book is already being used by{self.lendDict[book]}")
    def addBook(self, book):
            print("book has been added to the book list")
    def returnBook(self, book):
            self.lendDict.pop(book)
if __name__ == '__main__':
     books = library(['python', 'rich dad poor dad', 'harry potter', 'c++ Basics', 'Algorithms by CLRS'], "Let's Upskill")
     


     while(True):
        print(f"welcome to the {books.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
             print("please enter a vaild option")
             continue
        else:
             user_choice = int(user_choice)



        if user_choice == 1:
             books.displayBook()


        elif user_choice == 2:
             book = input("Enter the name of the book you want to lend:")

             user = input("Enter your name")
             books.lendBook(user, book)

        elif user_choice ==3:
             book = input("Enter the name of the book you want to add:")
             books.addBook(book)
        
        elif user_choice == 4:
             book = input("Enter the name of the book you want to return")
             books.returnBook(book)

        else:
             print("not a vaild option")


        print("press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c"and user_choice2!="q"):
             user_choice2 = input()
             if user_choice2 == "q":
                  exit()
             elif user_choice2 == "c":
                  continue
                