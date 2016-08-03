shoplist = []


def add_item(item):
    newshoplist = shoplist.append(item)
    return newshoplist


def remove_item(item):
    newshoplist = shoplist.remove(item)
    return newshoplist
   

def main():
    while(True):
        choice = raw_input("Do you want to add or remove something to the list? ").lower()
        if choice == "add":
            item = raw_input("Which item would you like to add? ").lower()
            if item in shoplist:
                print "This item is already in the list."
            else:
                add_item(item)
        elif choice == "remove":
            item = raw_input("Which item would you like to remove? ").lower()
            if item not in shoplist:
                print "This item is not in the list."
            else:
                remove_item(item)
        else:
            print "Only add or remove were options."
        print "Your current shopping list is:", shoplist

if __name__ == '__main__':
    main()