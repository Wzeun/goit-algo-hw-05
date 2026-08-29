def input_error(func):

    def inner(*args, **kwargs):

        try:
            # здесь вызываем исходную функцию
            return func(*args, **kwargs)

        except ValueError:
            return "Give me name and phone please."

        except KeyError:
            return "Contact not found."

        except IndexError:
            return "Enter user name."

    return inner
#Enter the argument for the command

def parse_input(command):
    command, *args = command.split()
    command = command.strip().lower()
    return command, args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added: " + name

@input_error
def change_contact(args, contacts):
    name, new_phone = args

    if name in contacts:
        contacts[name] = new_phone
        return "Contact changed: " + name

    return "Contact not found."

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

    return "Contact not found."

@input_error
def show_all(contacts):
    result = ""

    for name, phone in contacts.items():
        result += name + ": " + phone + "\n"

    return result


def main():
    contacts = {}

    while True:
        print("Enter a command please:")
        user_input = input()

        command, args = parse_input(user_input)

        if command in ["exit", "quit", "close"]:
            print("Goodbye!")
            break

        elif command == "hello":
            print("Hello can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command")


if __name__ == "__main__":
    main()