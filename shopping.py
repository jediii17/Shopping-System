mess = ('''
Weclome to MWA ONLINE SHOPPING

''')
print(mess)

shoppingList = [{"id": 1001, "Name": "SOAP", "Available": 76,
                 "Price": 20, "Original_Price": 16}, {"id": 1002, "Name": "SHAMPOO", "Available": 55,
                                                      "Price": 8, "Original_Price": 6}, {"id": 1003, "Name": "BREAD", "Available": 95,
                                                                                         "Price": 45, "Original_Price": 38}, {"id": 1004, "Name": "SPEAKER", "Available": 87,
                                                                                                                              "Price": 399, "Original_Price": 320}, {"id": 1005, "Name": "CHEESE", "Available": 61,
                                                                                                                                                                     "Price": 108, "Original_Price": 79}]

shoppingList1 = shoppingList
temp = []
order = ""


def adminLoginWindow():
    print("\n=====================")
    print("1.Display shopping list")
    print("2.Add item")
    print("3.Remove item")
    print("4.Check the item")
    print("5.Total Items")
    print("6.Logout")
    print("=====================")


def adminDisplayMenuWindow():
    print("Id\tName\t\tAvailable\tPrice\tOriginal Price")
    print("====================================================")
    for d in shoppingList:
        print(
            f'{d["id"]}\t{d["Name"]}\t\t{d["Available"]}\t\t{d["Price"]}\t{d["Original_Price"]}')


def addproducts():
    n = int(input("Enter the no. of items to add : "))
    for i in range(n):
        new_id = int(input("Enter id : "))
        new_Name = input("Enter Name : ")
        new_Available = int(input("Enter Available : "))
        new_Price = int(input("Enter Price : "))
        new_original = int(input("Enter the original price : "))
        d = [{"id": new_id, "Name": new_Name, "Available": new_Available, "Price": new_Price,
              "Original_Price": new_original}]
        shoppingList.extend(d)
        totalitem()
        adminDisplayMenuWindow()


def removeproducts():
    dressId = int(input("Enter the id need to be deleted : "))
    found = False
    ctr = 0
    for d in shoppingList1:
        found = d["id"] == dressId
        if found == True:
            del shoppingList[ctr]
        else:
            temp.append(d)
        ctr = ctr + 1

    print("Deleting item....")
    if len(temp) == d:
        print(f"{dressId} not found")
    else:
        print(f"{dressId}'s one available is removed from the list")
    totalitem()
    adminDisplayMenuWindow()


def availableproducts():
    Total = 0
    print("\n")
    for d in shoppingList:
        print(f'{d["Name"]} = {d["Available"]}')
        Total += (d["Available"])
    print("\nTotal available item is : ", Total)


def totalitem():
    count = len(shoppingList)
    print("total item is : ", count)


def logoutwindow():
    print("\n\nWelcome to YXZ ONLINE SHOPPING\n")
    login()


def adminOptions():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 2:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        addproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 3:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        removeproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 4:
        availableproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 5:
        totalitem()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 6:
        logoutwindow()
    else:
        print("\nInvalid Choice. Please try again")
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()


def userLoginWindow():
    print("=====================\n")
    print("1.Display shopping list")
    print("2.Place order")
    print("3.Cancel order")
    print("4.Logout")
    print("\n======================")


def userDisplayMenuWindow():
    print("Id\tName\t\tAvailable\tPrice")
    print("===================================================")
    for d in shoppingList:
        print(f'{d["id"]}\t{d["Name"]}\t\t{d["Available"]}\t\t{d["Price"]}')


def user_id():
    userDisplayMenuWindow()
    p_id = int(input("\nEnter the id : "))


def placeOrder():
    order_number = 1425486587
    userDisplayMenuWindow()
    p_id = int(input("\nEnter the id : "))

    for d in shoppingList:
        if d["id"] == p_id:
            print("\nId\tName\tAvailable\tPrice")
            print("=============================================================")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
            order = '{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}'
            conform = input(
                "\ntype 'Y' to place order otherwise 'N': ")

            if conform == 'Y' or conform == 'y':
                print("\nSuccessfully placed order {} {}".format(
                    d["id"], d["Name"]))
                order_number += 1
                print("Your tracking number is : ", order_number)
                d["Available"] -= 1
                break

            elif conform == 'N' or conform == 'n':
                print(
                    "The order is not placed. Happy shopping!!!!")
                break
            else:
                print("\nYou have entered wrong option. Please try again\n")
                conform = input(
                    "\nDo you want to place an order Y/N : ")
                break

    if d["id"] != p_id:
        print("\nYou have entered invalid id. Please try again\n")
        user_id()


def cancelOrder():
    found = False
    temp = []
    order_id = input("Enter the order ID : ")
    for d in shoppingList:
        found = d["id"] == order_id
        if found != True:
            temp.append(d)
    if len(temp) == d:
        print(f'{order_id} is not found')
    else:
        print(f'{order_id} is removed from the placed order')


def userChoiceOptions():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        userDisplayMenuWindow()
        print("\n\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 2:
        placeOrder()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 3:
        cancelOrder()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 4:
        print("\nThank you for shopping, Come again!!\n")
        exit()
    else:
        print("Invalid Choice. Please try again")
    exit()


def login():
    tp = input(

        '''Login as Admin type (admin)
Login as User type (user)

enter username: ''')
    if tp == 'Admin' or tp == 'admin':
        password = input("Enter the password : ")
        if password == "shop1":
            adminLoginWindow()
            adminOptions()
        else:
            print("Invalid password. Please try again")

    elif tp == 'User' or tp == 'user':
        password = input("Enter the password : ")
        if (password == "shop2"):
            userLoginWindow()
            userChoiceOptions()
        else:
            print("Invalid password. Please try again")
    else:
        print("Invalid user type. Please try again")


login()
