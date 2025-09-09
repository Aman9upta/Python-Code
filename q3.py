def remove_last(lst):
    if lst:
        lst.pop()
        #original list
        my_list = [10,20,30,40]
        remove_last(my_list)
        print("list after remove_last:", my_list)