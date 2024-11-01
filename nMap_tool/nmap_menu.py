from my_file_module import open_result_file, save_result_file, save_readable
from ip_menu import show_list
from my_nmap import my_nmap

def show_result(result_dict):
    
    if len(result_dict.keys()) > 0:
        print("\nCurrent results:")
        
        for host in result_dict.keys():
            
            print('-------------------------------------')
            print(f"Host : {host}")
             
            for index, scan in enumerate(result_dict[host]):
                
                print('------------------')
                print(f"Scan number: {index + 1}")
                print(f"Scan argument: {scan["arguments"]}")
                print(f"Timestamp: {scan["timestr"]}")
        
                if "tcp" in scan["result"].keys():
                    print(f"\nProtocol : TCP")

                    for port, port_data in scan["result"]["tcp"].items():
                        print (f"Port: {port}\t"
                                f"State : {port_data["state"]}\t"
                                f"Service: {port_data["name"]}\t"
                                f"{"Product: " + port_data["product"] + "\t" if port_data["product"] else ""}"
                                f"{"Version: " + port_data["version"] + "\t" if port_data["version"] else ""}"
                            )
                else:
                    print(f"State : {scan["result"]["status"]["state"]}")                   
            
                        # result_dict = {
                        #     "127.0.0.1": [{
                        #           arguments: "-oX - -p 22-443 -sV",
                        #           timestr: "Tue Oct 15 14:55:49 2024"
                        #           result: {}
                        #     }]    
                        # }
                
    else:
        print("Results is empty. Open result file or do a nMap search.")
    
    

def menu(result_dict, result_file, ip_list, ip_file, args):
    
    valid_options = ("nmap", "show", "open", "save", "show ip", "back", "--help")
    
    print("---------------------------------------------")
    
    menu_text = (
        "nMap menu!\n"
        "This menu have following commands:\n\n"
        "\tnMap, execute nMap commands\n"
        "\tShow, show result of current session \n"
        "\tOpen, open previous result from JSON-file\n"
        "\tSave, save current session result to JSON-file\n"
        "\tShow IP, show IP addresses in current list\n"
        "\tBack, goes back to main menu. Careful! Save to file if you done any changes\n"
        "\t--help, show menu commands again\n"
    )
    
    print(menu_text)
    
    while True:
        print("---------------------------------------------")
        
        user_input = input("Enter a nMap menu command: ").lower()
        
        if user_input in valid_options:
            
            match user_input:
                case "nmap":
                    my_nmap(result_dict, ip_list, args)
                case "show":
                    show_result(result_dict)
                case "open":
                    
                    result_file = input("Wich file to open containing saved results: ")
                    result_dict = open_result_file(result_file)
                    if result_dict:
                        show_result(result_dict)
                    
                case "save":
                    
                    if len(result_dict.keys()) > 0:
                        result_file = input("Save nMap result to file: ")
                        save_result_file(result_file, result_dict, "nMap result")
                        save_readable(result_file, result_dict)
                    else:
                        print("No result to save. Do a nMap search and save the result.")
                        
                case "show ip":
                    show_list(ip_list)
                case "back":
                    break
                case "--help":
                    print(menu_text)
                case _:
                    print("Sorry could not do that. Try again!")
            
        else:
            print("Sorry could not do that. Try again!")