my_list = [ "x", "y"]


def show_list():
    print my_list

def add_item():
    while True:   
        item = raw_input("Add item:").lower()

        if item in my_list:
            print "Item already added!"
        else:
            my_list.append(item)
            break
    print my_list

def remove_item():
    
    item = raw_input("Remove item:").lower()
    if item in my_list:
        my_list.remove(item)
    else:  
        print "Item does not exist."

    print my_list


def main():
    while True:
        # Menu seletion process
        print "Select Option"
        print "0 - Main menu" 
        print "1 - Show List"
        print "2 - Add item to list"
        print "3 - Remove item from list"
        print "4 - Exit when finished"

        selection = int(raw_input("Option Selection:"))
        # - END

        # Carrying out selection process
        if selection == 0:
            continue

        if selection == 1:
            show_list()

        if selection == 2:
            add_item()

        if selection == 3:
            remove_item()

        if selection == 4:
            break
        # - END

# def main():
#     # Menu seletion process
#     print "Select Option"
#     print "0 - Main menu" 
#     print "1 - Show List"
#     print "2 - Add item to list"
#     print "3 - Remove item from list"
#     print "4 - Exit when finished"

#     selection = int(raw_input("Option Selection:"))
#     # - END

#     # Carrying out selection process
#     if selection == 1:
#         show_list()

#     if selection == 2:
#         add_item()

#     if selection == 3:
#         remove_item()

#     if selection == 4:
#         return

#     main()
#     # - END



# check list // if exists, then print// if not exist, then add item ;; remove == print list

    # "1" = print my_list

# item = raw_input("prompt").lower()
# print item

# my_list.append(item)
# print my_list

# my_list.remove(item)
# print my_list

# my_list.sort()
# print my_list







if __name__ == '__main__':
    main()


 # if items in shopping_list:
 #            print("You already added this!")
        
 #        if(items == "exit"):
 #            break
 #        else:
 #            shopping_list.append(items)
