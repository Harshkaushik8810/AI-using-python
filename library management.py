class library:
    def __init__(self,listofbooks):
        self.books=listofbooks
    def display(self):
        print("==ALL Books present in this library are == :- ")
        for book in self.books:
            print("\t *" + book)

    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"Book:- {bookname} has been issued.")    
            self.books.remove(bookname)  
            return True      
        else:
            print("Sorry 🥺 This Book already been issued by someone else")    
            return False

    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning the book 😊")

class year1(library):
    def __init__(self,listofbooks):
        self.books=listofbooks
    def display(self):
        print("\tBooks present for 1st year student are :-\n ")
        for book in self.books:
            print("\t *" + book)
class year2(library):
    def __init__(self,listofbooks):
        self.books=listofbooks
    def display(self):
        print("\tBooks present for 2nd year student are :-\n ")
        for book in self.books:
            print("\t *" + book)
class year3(library):
    def __init__(self,listofbooks):
        self.books=listofbooks
    def display(self):
        print("\tBooks present for 3rd year student are :-\n ")
        for book in self.books:
            print("\t *" + book)
class year4(library):
    def __init__(self,listofbooks):
        self.books=listofbooks
    def display(self):
        print("\tBooks present for 4th year student are :-\n ")
        for book in self.books:
            print("\t *" + book)
    



class student:
    def request(self):
        self.book = input("Enter The Book You wanna borrow")
        return self.book
    def Return(self):
        self.book = input("Enter The Book You wanna return")
        return self.book
        

if __name__=="__main__":
    CenterLibrary=library(["web Technology","python","object oriented","css","operating system","automata","data structure","machine learning","Maths","discrete maths","Physics Engineering","Chemistry Engineering", "Mathematics Basic", "Electrical Engineering","Programming for Problem Solving","Basic Electrical Engineering ","Artificial Intelligence","Natural language processing","High Performance Computing","Cryptography and Network Security","Design & Development of Applications","Software Testing","Distributed Systems","Deep Learning","Service Oriented Architecture","Quantum Computing","Mobile Computing","Internet of Things","Cloud Computing","Software Project Management","Computer Architecture and Organization","Industrial Electronics","Optical Communication System","Advance Digital Design using Verilog","Data Analytics","Web Designing","Computer Graphics","Object Oriented System Design","\n"])
    b=year1(["Physics Engineering","Chemistry Engineering", "Mathematics Basic", "Electrical Engineering","Programming for Problem Solving","Basic Electrical Engineering "])
    c=year2(["microprocesor","COA","css","operating system","automata","data structure","machine learning","Math-4","discrete maths"])
    d=year3(["Computer Architecture and Organization","Industrial Electronics","Optical Communication System","Advance Digital Design using Verilog","Data Analytics","Web Designing","Computer Graphics","Object Oriented System Design"])
    e=year4(["Artificial Intelligence","Natural language processing","High Performance Computing","Cryptography and Network Security","Design & Development of Applications","Software Testing","Distributed Systems","Deep Learning","Service Oriented Architecture","Quantum Computing","Mobile Computing","Internet of Things","Cloud Computing","Software Project Management"])
    Student=student()
    while(True):
        welcomeMsg='''\n WELCOME TO THE STUDENT LIBRARY
        please choose an option :-\n
        1. list all the book 
        2. request a book
        3. return a book 
        4. exit the library 
        '''
        print(welcomeMsg)
        a=int(input("Enter your choice"))

        if a==1:
            CenterLibrary.display()
            print("**FIND BOOKS BY YEAR** \n")
            print("---Enter 1 for 1st year 2 for 2nd year 3 for 3rd year 4 for 4th year---\n")
            x=int(input("^^Enter the number^^"))
            if x==1:
                b.display()
            elif x==2:
                c.display()
            elif x==3:
                d.display()
            elif x==4:
                e.display()
            else:
                print("\t \n Main Menu")    
            
        elif a==2:
            CenterLibrary.borrowbook(Student.request())  
        elif a==3:
            CenterLibrary.returnbook(Student.Return())
        elif a==4:
            print("Thanks for using library! Have a great day ")
            exit()
        else:
            print("Invalid choice")