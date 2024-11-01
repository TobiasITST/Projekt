import json

def save_readable(my_file, result_dict):
    try:
        if my_file.find(".") == -1:
            my_file += ".txt"
        
        with open("readable_" + my_file, "w") as file:
            
            print(f"Saving readable output to {my_file}")
            
            if len(result_dict.keys()) > 0:
                
                file.write("Results:\n")
                
                for host in result_dict.keys():
                    file.write("-------------------------------------\n")
                    file.write(f"Host : {host}\n")
                    
                    for index, scan in enumerate(result_dict[host]):
                        
                        file.write('------------------\n')
                        file.write(f"Scan number: {index + 1}\n")
                        file.write(f"Scan argument: {scan["arguments"]}\n")
                        file.write(f"Timestamp: {scan["timestr"]}\n")
                
                        if "tcp" in scan["result"].keys():
                            file.write(f"\nProtocol : TCP\n")

                            for port, port_data in scan["result"]["tcp"].items():
                                file.write (f"Port: {port}\t"
                                        f"State : {port_data["state"]}\t"
                                        f"Service: {port_data["name"]}\t"
                                        f"{"Product: " + port_data["product"] + "\t" if port_data["product"] else ""}"
                                        f"{"Version: " + port_data["version"] + "\t" if port_data["version"] else ""}"
                                        "\n"
                                    )
                        else:
                            file.write(f"State : {scan["result"]["status"]["state"]}\n")                   
                    
                                # result_dict = {
                                #     "127.0.0.1": [{
                                #           arguments: "-oX - -p 22-443 -sV",
                                #           timestr: "Tue Oct 15 14:55:49 2024"
                                #           result: {}
                                #     }]    
                                # }
                        
            else:
                print("Results is empty. Open result file or do a nMap search.")
    
    except FileNotFoundError:
        print(f"Could not save to {"readable_" + my_file}. Try again")

def save_result_file(my_file, result_dict, type_string = None):
    
    try:
        if my_file.find(".json") == -1:
            my_file += ".json"
        elif my_file.find(".JSON") == -1:
            my_file += ".json"
        
        # Check if file exist? Ask overwrite or append?
            
        with open(my_file, "w") as file:
            print("--------------")
            print(f"Saving {type_string} to {my_file}")
    
            json.dump(result_dict, file, indent=4)
            
                   
    except FileNotFoundError:
        print(f"Could not save to {my_file}. Try again")

def open_result_file(my_file):
    try:
        with open(my_file, "r") as file:    
            print(f"Opening your file: '{my_file}'")
            return json.load(file)
                   
    except FileNotFoundError:
        print(f"Could not open '{my_file}' Try again")
    except json.JSONDecodeError:
        print(f"Could not parse '{my_file}' as JSON. Try again")

def open_file(my_file):
    try:
        with open(my_file, "r") as file:    
            print(f"Opening your file: '{my_file}'")
            return file.read()
                   
    except FileNotFoundError:
        print(f"Could not open '{my_file}' Try again")
           
def save_file(my_file, my_list, type_string = None):
    
    try:
        if my_file.find(".") == -1:
            my_file += ".txt"
        
        # Check if file exist? Ask overwrite or append?
            
        with open(my_file, "w") as file:
            
            print(f"Saving {type_string} to {my_file}")
            for item in my_list:
                file.write(item + "\n")
                   
    except FileNotFoundError:
        print(f"Could not save to {my_file}. Try again")