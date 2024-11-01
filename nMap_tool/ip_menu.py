# for regular expressions
import re

from my_file_module import open_file, save_file
 
# Make a regular expression
# for validating an Ip-address
regex = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
 
# Define a function for
# validate an Ip address
def valid_ip(ip_address, verbose = True): 
    # pass the regular expression
    # and the string in search() method
    if(re.search(regex, ip_address.split("/")[0])):
        
        if ip_address.find("/") != -1:
                        
            check = ip_address.split("/")[1]
            
            # /16 big enough
            if check not in ["16", "24"]:
                print(f"Invalid IP address, can't use /{check}.")
                return False
         
        if verbose: print("Valid IP address.")
        return True    
    else: 
        if verbose: print("Invalid IP address.")
        return False
        
    
def remove_from_list(ip_list, ip_address):
    if len(ip_list) > 0:
        try:
            ip_list.remove(ip_address)
            print(f"Removed {ip_address} from the list.")
        except ValueError:
            print(f"{ip_address} does not exist in the list.")
    else:
        print(f"List with IP addresses is empty. Open an IP list from file or add new address.")

def add_to_list(ip_list, ip_address):
    if ip_address in ip_list:
        print(f"{ip_address} does already exist in the list.")
    else:
        ip_list.append(ip_address)
        print(f"{ip_address} added to the list.")
        
def show_list(ip_list):
    if len(ip_list) > 0:
        print("\nCurrent IP address in the list:")
    else:
        print("List with IP addresses is empty. Open an IP list from file or add new address.")
    
    for ip in ip_list:
        print(ip)

def import_from_file(read_file):
    
    imported_list = []
    
    if len(read_file) > 0:
        imported_list = read_file.split("\n")
    
    list_to_return = []
    
    for item in imported_list:
        if item != "" and valid_ip(item, verbose = False):
            list_to_return.append(item)
        
    return list_to_return
 

def menu(ip_list, ip_file):
    
    valid_options = ("show", "open", "save", "add", "remove", "back", "--help")
    
    print("---------------------------------------------")
    
    menu_text = (
        "Ip address menu\n"
        "This menu have following commands:\n\n"
        "\tShow, show IP addresses in current list\n"
        "\tOpen, open desired IP address list from file\n"
        "\tSave, save current IP address list to file\n"
        "\tAdd, add an IP address to current list\n"
        "\tRemove, remove an IP address from current list\n"
        "\tBack, goes back to main menu. Careful! Save to file if you done any changes\n"
        "\t--help, show menu commands again\n"
    )
    
    print(menu_text)
    
    while True:
        print("---------------------------------------------")
        
        user_input = input("Enter a IP menu command: ").lower()
        
        if user_input in valid_options:
            
            match user_input:
                case "show":
                    show_list(ip_list)
                case "open":
                    ip_file = input("Wich file to open containing IP addresses: ")
                    ip_list = import_from_file(open_file(ip_file))
                    show_list(ip_list)
                case "save":
                    ip_file = input("Save list of IP addresses to file: ")
                    save_file(ip_file, ip_list, "IP addresses")
                case "add":
                    ip = input("Enter an IP address to add to list: ")
                    if valid_ip(ip):
                        add_to_list(ip_list, ip)
                case "remove":
                    ip = input("Enter an IP address to remove from list: ")
                    if valid_ip(ip):
                        remove_from_list(ip_list, ip)
                case "back":
                    break
                case "--help":
                    print(menu_text)
                case _:
                    print("Sorry could not do that. Try again!")
            
        else:
            print("Sorry could not do that. Try again!")
    return ip_list, ip_file
