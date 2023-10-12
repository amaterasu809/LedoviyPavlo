def search(sorted_list, number):
    list_right = 0
    list_left = len(sorted_list) - 1

    while list_right <= list_left:
        list_mid = (list_right + list_left) // 2
        if sorted_list[list_mid] == number:
            print("Number exists. Position: " + str(list_mid))
            return
        elif sorted_list[list_mid] < number:
            list_right = list_mid + 1
        else:
            list_left = list_mid - 1
    print ("Position to add is: " + str(list_right))
    return 

sorted_list = [1, 3, 5, 7, 9, 11]

while True:
    number = input("Insert number to add: ")
    number = int(number)
    position = search(sorted_list, number)
    