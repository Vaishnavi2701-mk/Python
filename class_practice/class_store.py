class Product:
    def __init__(self,productcode,name,price):
        self.productcode=productcode
        self.name=name
        self.price=price


class Store:

    def __init__ (self):
        self.productlist=[]
        self.shoppingcart=[]

    def addproduct(self,product):
        self.productlist.append(product)

    def display(self):
        for product in self.productlist:
            print(f"{product.productcode}\t{product.name}\t{product.price}")

    def addtoShoppingCart(self,product):
        for item in self.productlist:
            if item.productcode==product:
                self.shoppingcart.append(item)
                print(f"{item.name} added to cart")
                return
        print("Item which you looking for is not present in the store")

    def removeFromCart(self,product):
        for item in self.shoppingcart:
            if item.productcode==product:
                self.shoppingcart.remove(item)
                print(f"The item {item.name} removed from the shopping cart")
                return
        print("The product with this code is not available in the shopping cart")

    def generateBill(self):
        price=0
        for product in self.shoppingcart:
            price+=product.price
        print(f"The total bill is {price}")

    def displayShoppingCart(self):
        for item in self.shoppingcart:
            print(f"{item.name}")
if __name__=="__main__":
    store=Store()
    store.addproduct(Product(1,"Chocolates",50))
    store.addproduct(Product(2,"Butter       ",40))
    store.addproduct(Product(3,"Samolina",40))
    store.addproduct(Product(4,"Corn Flour",50))
    store.addproduct(Product(5,"Biscuits",20))
    
    print("*** Your Options are ****\n1)Diplay Product\n2)Add your product to shopping cart\n3)Remove product from shopping cart\n4)View the shopping cart\n5)Generate Bill\n6)Exit")
    while(True):
        option=int(input("Enter your option\n"))
        if option==1:
            store.display()
        
        elif option==2:
            code=int(input("Enter the product code: "))
            store.addtoShoppingCart(code)
        elif option==3:
            code=int(input("Enter the product code: "))
            store.removeFromCart(code)
        
        elif option==4:
            store.displayShoppingCart()
        
        elif option==5:
            store.generateBill()
        
        elif option==6:
            exit()
        
        else:
            print("Please enter a valid choice!")
        


