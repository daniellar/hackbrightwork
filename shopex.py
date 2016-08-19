main_lists = {
    'WF': ['wine', 'cheese'],
    'TJ': ['ice cream', 'cookies'],
    'SW': ['vitawater', 'rice']
}


def add_new_list(nickname): 
    # add a new list with key as name of the list
    # make sure a list with this name doesn't already exist
    # deal with uppercase/lowercase
    nickname = nickname.lower()
    if nickname in main_lists:
        print "list exist"
    else:
        main_lists[nickname] = []




add_new_list("BR")
print main_lists

# = [almond milk, ice cream]





# if item in my_list:
#             print "Item already added!"
#         else:
#             # my_list.append(item)
#     
