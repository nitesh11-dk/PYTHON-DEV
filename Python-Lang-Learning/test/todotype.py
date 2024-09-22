
sop_List = ["bread" , "pizza" ,  "burger"] ;

def add_items():
    item = input("enter the single  item name you want to add \n")
    sop_List.append(item)
    print(f"added in {sop_List}" )
    


def remove_item():
    item = input("enter the single  item name you want to remove \n")
    sop_List.remove(item)
    print(f"removed from {sop_List}" )



def showItem():
    print(f" the items are {sop_List}")




while True:
    print(". write Add to add items \n")
    print(". write Remove to remove items \n")
    print(". write List to show items \n")
    perform = input("..... \n")

    if perform == "Add":
        add_items()
    elif perform == "Remove":
        remove_item()
    elif perform == "List":
        showItem()
    else:
        print("Enter the proper operation")

    exit = input("Do you want to exit? Press 'Y' ")
    if exit == "Y":
        break