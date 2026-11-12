def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args 

def add_contact (args, contact):
    
    name, phone = args
    contact[name] = phone
    return "\nContact added."

def change_contact (args, contact: dict):
    
    name, phone = args

    if name in contact:
        contact[name] = phone
        return "\nContact updated."
    else:
        return "\nContact with that name is not exist"

def show_phone(args, contact):

    if len(args) < 1:
        return "\nPlease provide a name."
    name = args[0]
    if name in contact:
        return f"\nPhone number for {name} is {contact[name]}"
    else: 
        return f"\nContact number for {name} not found."

def all_contacts(contacts):
    
    if len(contacts) > 0:
        for contact in contacts:
            return f"{contact}: {contacts[contact]}"
    else:
        return "No contacts found."
    
def main():
    print("Welcome to the assistant bot!")
    contacts = {}
    while True:
        user_input = input("\nEnter a command: ").strip()

        if not user_input:
            continue

        command, *args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")

        elif command in ["close", "exit"]:
            print("Good bye!")
            return

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))
        
        elif command == "all":
            print("\n>>>> All contacts <<<<\n")
            print(all_contacts(contacts))
        
        else:
            print("\nInvalid command.")


if __name__ == "__main__":
    main()
