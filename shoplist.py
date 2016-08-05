def add_item(shoplist):
    item = raw_input("Which item would you like to add? ").lower()
    if item in shoplist:
        print "This item is already in the list."
    else:
        shoplist.append(item)

def remove_item(shoplist):
    item = raw_input("Which item would you like to remove? ").lower()
    if item not in shoplist:
        print "This item is not in the list."
    else:
        shoplist.remove(item)

def main():
    shoplist = []
    choice = None
    while choice != "quit":
        choice = raw_input("Do you want to add or remove something to the list? (Type 'quit' to exit.) ").lower()
        if choice == "add":
            add_item(shoplist)
        elif choice == "remove":
            remove_item(shoplist)
        else:
            print "Only add or remove were options."
        print "Your current shopping list is:", shoplist

if __name__ == '__main__':
    main()