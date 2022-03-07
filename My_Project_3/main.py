class Library:
   
   
    def __init__(self,GenresOfBooks,FantasyBooks,ScienceFictionBooks,MystryBooks,PoetryBooks,BiographyBooks,DonatedBooks):
        self.books=GenresOfBooks
        self.fantasy=FantasyBooks
        self.science=ScienceFictionBooks
        self.mystry=MystryBooks
        self.poetry=PoetryBooks
        self.biography=BiographyBooks
        self.donated=DonatedBooks

    def displayAvailableGenres(self):
        print("Genres of books Available in our Library are listed below: ")

        for book in self.books:
            print(" * " + book)

    def selectAGenres(self):
        a=input("Select a genre of book\n")

        if a=="Fantasy":
            for i in self.fantasy:
                print(" * " + i)

        elif a=="Science Fiction":
            for i in self.science:
                print(" * "+ i)

        elif a=="Mystry":
            for i in self.mystry:
                print(" * "+ i)

        elif a=="Poetry":
            for i in self.poetry:
                print(" * "+ i)

        elif a=="Biography":
            for i in self.biography:
                print(" * "+ i)

        elif a=="Donated Books":
            for i in self.donated:
                print(" * "+ i)

        else:
            print(f"The {a} genre is not available in our library.Please enter the genre availble in our library!")


    def borrowBook(self,bookName):
        if bookName in self.fantasy:
            print(f"You have beem issued a book {bookName}, please keep it safe and return it within 30 days!")
            self.fantasy.remove(bookName) 
            return True

        elif bookName in self.science:
            print(f"You have beem issued a book {bookName}, please keep it safe and return it within 30 days!")
            self.science.remove(bookName) 
            return True

        elif bookName in self.mystry:
            print(f"You have beem issued a book {bookName}, please keep it safe and return it within 30 days!")
            self.mystry.remove(bookName) 
            return True

        elif bookName in self.poetry:
            print(f"You have beem issued a book {bookName}, please keep it safe and return it within 30 days!")
            self.poetry.remove(bookName) 
            return True

        elif bookName in self.biography:
            print(f"You have beem issued a book {bookName}, please keep it safe and return it within 30 days!")
            self.biography.remove(bookName) 
            return True

        elif bookName in self.donated:
            print(f"You have beem issued a book {bookName}, please keep it safe and return it within 30 days!")
            self.donated.remove(bookName) 
            return True



        else:
            print(f"Sorry the {bookName} is either not available in our Library or it is borrowed by someone else! Please wait until the book will be back in library! ")
            return False
    
    def returningBook(self,bookName):

        if bookName=="The Game Of Thrones" or bookName=="The Name Of The Winds" or bookName=="The Way Of Kings" or bookName=="A Wizard Of Earthsea":
            print(f"Thank you for returning {bookName}")
            self.fantasy.append(bookName)
            return True

        elif bookName=="Pachinko" or bookName=="The Color Purple" or bookName=="Dune" or bookName=="Catch-22":
            print(f"Thank you for returning {bookName}")
            self.science.append(bookName)
            return True

        elif bookName=="Gone Girl"or bookName=="And then There were None" or bookName=="Rebecca" or bookName=="The girl on the train":
            print(f"Thank you for returning {bookName}")
            self.mystry.append(bookName)
            return True
        
        elif bookName=="On Love and Barley" or bookName=="Leaves of Grass" or bookName=="Milk and honey" or bookName=="Dont call us Dead":
            print(f"Thank you for returning {bookName}")
            self.poetry.append(bookName)
            return True
        
        elif bookName=="Swami Vivekanand" or bookName=="Elon Musk" or bookName=="Wings of Fire" or bookName=="Becoming":
            print(f"Thank you for returning {bookName}")
            self.biography.append(bookName)
            return True
        
        else:
            print(f"Thank you for donating {bookName}")
            self.donated.append(bookName)
            
            




class Student:

    def requestBook(self):
        self.book=input("Which book you want to borrow?\n")

        return self.book

    def returnBook(self):
        self.book=input("Which book you are donating/returning?\n")

        return self.book

if __name__=="__main__":

    DigitalLibrary=Library(["Fantasy","Science Fiction","Mystry","Poetry","Biography","Donated Books"],
                            ["The Game Of Thrones","The Name Of The Winds","The Way Of Kings","A Wizard Of Earthsea"],
                            ["Pachinko","The Color Purple","Dune","Catch-22"],
                            ["Gone Girl","And then There were None","Rebecca","The girl on the train"],
                            ["On Love and Barley","Leaves of Grass","Milk and honey","Dont call us Dead"],
                            ["Swami Vivekanand","Elon Musk","Wings of Fire","Becoming"],
                            ["The donated books will be appeared here!"]  )


    student=Student()


    Display='''\n~~~~~ Welcome to the Digital Library ~~~~~

        Please choose an option to proceed further

        1.Display the genres of books available in the Liabrary
        2.select a genres
        3.Borrow a book
        4.Donate/Return book
        5.Exit from the library'''

    print(Display)

    while(True):
        

        a=int(input("Enter your option!\n"))

       
        if a==1:
            DigitalLibrary.displayAvailableGenres()
        elif a==2:
            DigitalLibrary.selectAGenres()
        elif a==3:
            DigitalLibrary.borrowBook(student.requestBook())
        elif a==4:
            DigitalLibrary.returningBook(student.returnBook())
        elif a==5:
            print("Thank you for visiting The Digital Library!")
            exit()
        else:
            print("Please enter a valid choice!")




        


                

               


