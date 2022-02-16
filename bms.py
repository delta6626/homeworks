#All variables required 
active = True
cats = {}
message = """
Press 1 to create a new category
Press 2 to delete a category
Press 3 to add a product to a category
Press 4 to delete a product from a category
Press 5 to show all categories and products
Press 6 to get number of products in a category
Press 7 to get frequency of a product in a category
Press 8 to get total number of products and categories
Press 9 to quit
"""

#Welcome the user
print("Welcome to BMS !")
print(message)

#All functions required
def newCat():
    catname = input("Enter category name : ").lower()
    if catname in cats:
        print("This category already exists.")
    else:
        cats[catname] = []
        print("Successfully added category ",catname)

def deleteCat():
    catname = input("Enter category name : ").lower()
    if catname in cats:
        del cats[catname]
        print("Successfully deleted category ",catname)
    else:
        print("The category doesn't exist.")

def addProduct():
    catname = input("Which category would you like to add this product in?").lower()
    if catname in cats:
        productName = input("Enter product name : ").lower()
        cats[catname].append(productName)
        print("Product added.")
    else:
        print("This category doesn't exist. Add the category and try again.")

def removeProduct():
    catname = input("Which category would you like to remove this product from?").lower()
    if catname in cats:
        productName = input("Enter the product to be removed : ").lower()
        if productName in cats[catname]:
            cats[catname].remove(productName)
            print("Product removed.")
        else:
            print("The specified product doesn't exist.")
    else:
        print("The specified category doesn't exist.")
def view():
    if len(cats)!=0:
        print("Here's all your categories along with products : ")
        print(cats)
    else:
        print("No categories exist. Please create one and try again.")

def numProd():
    catname = input("Enter the name of category : ").lower()
    if catname in cats:
        n = len(cats[catname])
        print("Number of products in this category :",n)
    else:
        print("This category doesn't exist.")

def frequency():
    catname = input("Enter the name of category : ").lower()
    if catname in cats:
        prodName = input("Enter the name of the product : ").lower()
        x = 0
        for i in cats[catname]:
            if i==prodName:
                x+=1
        print("Frequency of the specified product : ",x)
    else:
        print("This category doesn't exist.")

def totCatProd():
    nCat,nProd = len(cats),0
    for i in cats:
        nProd+=len(cats[i])
    print("You have",nCat,"categories and",nProd,"products in total.")

# Main loop
while(active):
    try:
        alpha = int(input("What would you like to do?"))
        if(alpha ==1):
            newCat()
        elif(alpha ==2):
            deleteCat()
        elif(alpha == 3):
            addProduct()
        elif(alpha == 4):
            removeProduct()
        elif(alpha == 5):
            view()
        elif(alpha == 6):
            numProd()
        elif(alpha == 7):
            frequency()
        elif(alpha == 8):
            totCatProd()
        elif(alpha == 9):
            quit()
        else:
            print("Invalid Option.\n",message)
    except ValueError:
        print("Invalid Value. Please enter a number.")