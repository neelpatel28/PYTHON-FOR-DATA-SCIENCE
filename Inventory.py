class Inventory:
    def __init__(self, price, category, manufacturer, sub_products=None):
        self.price = price
        self.category = category
        self.manufacturer = manufacturer
        if sub_products is None:
            self.sub_products = []
        else:
            self.sub_products = sub_products

    def display_details(self):
        print("\nDisplaying the detials :")
        print("Price: {}".format(self.price))
        print("Category: {}".format(self.category))
        print("Manufacturer: {}".format(self.manufacturer))

        if self.sub_products:
            print("Sub-Products:")
            for sub_product in self.sub_products:
                print("Sub product ",self.sub_products.index(sub_product))
                sub_product.display_details()

class ElectronicProduct(Inventory):
    def __init__(self, price, category, manufacturer, warranty_period):
        super().__init__(price, category, manufacturer)
        self.warranty_period = warranty_period

    def display_details(self):
        super().display_details()
        print("Warranty Period: {}".format(self.warranty_period))

# Usage
b = True
while b == True:
    try:
        a = True
        while a == True:
            print("\nWelcome to the Inventory!\n")
            price = float(input("Enter price of product : "))
            if price >= 0:
                a = False
            else:
                a = True
                break
            c = True
            while c == True:
                category = input("Enter the category (alphabetic): ")

                if not category.isalpha():
                    print("Category should only contain alphabetic values. Please re-enter.")
                    continue
                else:
                    c = False
            
            manufacturer = input("Enter name of manufacturer (alphanumeric): ")
            d = True
            while d == True:
                if not manufacturer.isalnum():
                    print("Manufacturer should only contain alphanumeric values. Please re-enter.")
                    continue
                else:
                    d = False
                    
            warranty_period = int(input("Enter the warranty period (in Months): "))
            
            electronic_product = ElectronicProduct(price, category, manufacturer, warranty_period)
            
            num_sub_products = int(input("Enter the number of sub-products: "))
            
            for _ in range(num_sub_products):
                sub_price = float(input("Enter sub-product price: "))
                sub_category = input("Enter sub-product category : ")
                
                if not sub_category.isalpha():
                    print("OOPs! Invalid Name . Please re-enter.")
                    continue
                sub_manufacturer = input("Enter sub-product manufacturer : ")
                
                sub_product = Inventory(sub_price, sub_category, sub_manufacturer)
                electronic_product.sub_products.append(sub_product)
            choice = input("Press d (to display) or 'exit' to exit : ").lower()
            r = True
            while r == True:
                if choice == "d":
                    # Displaying details
                    electronic_product.display_details()
                    r = False
                    break
                elif choice == "exit":
                    # Displaying details
                    electronic_product.display_details()
                    r = False
                    break
                

    except ValueError as ve:
        print("Error: {}".format(ve))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))