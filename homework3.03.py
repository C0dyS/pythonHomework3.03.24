

def add_to_dict(my_dict, key, PIB, email, nr, skype):
    my_dict[key] = (PIB, email, nr, skype)

def change_value(my_dict,key,value_index,new_value):
    value_index -= 1
    if key in my_dict:
        if 0 <= value_index < len(my_dict[key]):
            updated_tuple = tuple(new_value if i == value_index else value for i, value in enumerate(my_dict[key]))
            my_dict[key] = updated_tuple
        else:
            print("Index out of range for key '{}'".format(key))
    else:
        print("Key '{}' not found in dictionary".format(key))





def firm():
    firm_database = {}
    try:
        while True:
            choice = int(input('''choose:
            1 - to add new data
            2 - to remove existing data
            3 - to change data
            4 - check data
            else - to exit
            '''))
            if choice == 1:
                key, PIB, email, nr, skype = map(str, input(
                    'Please enter required data: employee, PIB, email, nr, skype').split())
                key = key.lower()
                PIB = PIB.lower()
                email = email.lower()
                nr = nr.lower()
                skype = skype.lower()
                add_to_dict(firm_database,key,PIB,email,nr, skype)
                print('data successfully added')
            elif choice == 2:
                key_var = str(input('please type employee name: ').lower())
                del firm_database[key_var]
            elif choice == 3:
                key_var, index, new_value = map(str, input(
                    'Input employee name, what element you want to change, and new element: ').split())
                key_var = key_var.lower()
                new_value = new_value.lower()
                change_value(firm_database, key_var, index, new_value)
                print('data successfully changed')
            elif choice == 4:
                key_var = str(input('please type employee to check: ').lower())
                print(firm_database.get(key_var))
            else:
                print('exiting the program')
                break
    except(ValueError):
        print('oops something went wrong')

firm()