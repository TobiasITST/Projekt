import ip_menu
import nmap_menu
import argparse

# Script written and tested on windows machine
# Requires 'python-nmap'

# Know Issues
# unreachable Ip gives state: up...
# Can't run with root privileges on windows...

# Not implemented: question to append result to file
def main():

    parser = argparse.ArgumentParser(
        prog="nMap_tool",
        description="My crypto tool for symetric encryption and decryption")
        
    parser.add_argument("-u", "--unprivileged", action= "store_true", help="run nMap scan as unprivileged")
    parser.add_argument("-s", "--sudo", action="store_true", help="run nMap scan as sudo")
    
    args = parser.parse_args()
    
    valid_options = ("nmap", "ip", "--help", "exit")
    ip_list = []
    ip_file = None
    result_dict = {}
    result_file = None
    
    menu_text = ("\nWelcome to my little nMap python program!\n"
        "This program have following commands:\n\n"
        "\tnMap, Enter the Nmap menu to run nMap scans, open result file etc.\n"
        "\tIP, Enter the IP-address menu\n"
        "\tExit, exits this program and does NOT save any results\n"
        "\t--help, show program commands again\n"
    ) 
    print(args.unprivileged)
    print(menu_text)
    
    while True:
        print("---------------------------------------------")
        
        user_input = input("Enter a main menu command: ").lower()
        
        if user_input in valid_options:
            
            match user_input:
                case "nmap":
                    nmap_menu.menu(result_dict, result_file, ip_list, ip_file, args)
                case "ip":
                    ip_list, ip_file = ip_menu.menu(ip_list, ip_file)
                case "exit":
                    break
                case "--help":
                    print(menu_text)
                case _:
                    print("Sorry could not do that. Try again!")
            
        else:
            print("Sorry could not do that. Try again!")
        
        

if __name__ == "__main__":
    main()