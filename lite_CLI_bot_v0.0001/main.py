contact_list = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give me correct name please."
        except TypeError:
            return "Give me correct name and phone please."
        except IndexError:
            return "Give me name and phone please."

    return inner




def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
        name, phone = args
        if name not in contacts.keys():
            contacts[name] = phone
            return "Contact added."
        else:
            return "The contact is exist"

@input_error
def check_contact(args, contacts):
        name = args
        return f"Phone nomber: {contacts[name[0]]}"

@input_error
def change_contact_number(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contact_list[name] = phone
        return "Number chenging"
    else:
        return f"Contact Name: \"{name}\" - doesn't exist. Please check the Name and try again"      


@input_error    
def all_contacts(contacts):
    list=''
    if len(contacts) == 0:
        return "List is empty"
    for item in contacts.keys():
            list+= f"Name: \"{item}\" Phone: {contact_list[item]}\n"
    return list       

def main():
    print("Welcome to the assistant bot!")
    while True:
        global contact_list 
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contact_list))
            
        elif command == "all":
            print(all_contacts(contact_list))  
              
        elif command == "phone":
            print(check_contact(args, contact_list))
            
        elif command == "change":    
            print(change_contact_number(args, contact_list))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
