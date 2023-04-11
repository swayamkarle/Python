class BookStore:
    def __init__ (self,title,autor,qty,price) :
        self.title=title
        self.autor=autor
        self.qty=qty
        self.price=price

    def get_data(self):
        print("Title:",self.title)
        print("Autor:",self.autor)
        print("Quantity:",self.qty)
        print("Price:",self.price)
        

bookstore=[]

n=int(input("Enter the number of books you want to enter:"))

for i in range(n):
    title=input("Enter Title:")
    author=input("Enter Author:")
    qty=int(input("Enter Quantity:"))
    price=float(input("Enter Price:"))

    bookstore.append(BookStore(title,author,qty,price))

for book in bookstore:
    book.get_data()
