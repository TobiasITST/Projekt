import nmap
from ip_menu import valid_ip

def print_result(nm, result):
    
    for host in result.keys():
        
        print('------------------')
        print(f"Host : {host} ({result[host]["hostnames"][0]["name"]})")
        print(f"State : {result[host]["status"]["state"]}")
        
        if "tcp" in result[host].keys() and result[host]["status"]["state"] == "up":
            print(f"\nProtocol : TCP")

            for port, port_data in result[host]["tcp"].items():
                print (f"Port: {port}\t"
                        f"State : {port_data["state"]}\t"
                        f"Service: {port_data["name"]}\t"
                        f"{"Product: " + port_data["product"] + "\t" if port_data["product"] else ""}"
                        f"{"Version: " + port_data["version"] + "\t" if port_data["version"] else ""}"
                       )
        else:
            print("Did not scan or could not found any TCP ports")

    if int(nm.scanstats()["downhosts"]) > 0:
        print('------------------')
        print(f"Status: {nm.scanstats()["downhosts"]} host(s) down of {nm.scanstats()["totalhosts"]}")
        

def my_nmap(result_dict, ip_list, args):
    
    try:
        nm = nmap.PortScanner()
        host = ""
        
        if len(ip_list) != 0:
            while True:
                usr_input = input("Scan hosts from current IP-list (Y/N)?: ").lower()
                if usr_input == "y" or usr_input == "n":
                    break    
        else:
            usr_input = "n"
            print("No IP addresses in the IP list.")  
        
        if usr_input == "n":
            usr_input = input("Specify IP of a new host(s): ").strip()
            ips = usr_input.split(" ")
            
            for h in ips:
                if valid_ip(h):
                    host += h + " "
                else:
                    print("Please try again.")
                    return                    
        elif usr_input == "y":
            for ip in ip_list:
                host += ip + " "
        
        host = host.strip()
                
        # Check for arguments
        # Challangening to check valid format for ports. 
        # User need to add specific ports in arguments
        # Relying on catching nMap error to enlighten the user
        while True:
                usr_input = input("Arguments for nMap search (Y/N)?: ").lower()
                if usr_input == "y" or usr_input == "n":
                    match usr_input:
                        case "y":
                            arguments = input("Enter the Arguments: ")
                            break
                        case "n":
                            arguments = None
                            break
        
        # Can't run with root privileges on windows... 
        # --unprivileged flag required on my windows enviroment
        
        if arguments == None and args.unprivileged == False:
            result = nm.scan(hosts = host, sudo = args.sudo)["scan"]
        
        elif arguments == None and args.unprivileged == True:
            result = nm.scan(hosts = host, arguments = "--unprivileged", sudo = args.sudo)["scan"]
        
        elif arguments != None and args.unprivileged == False: 
            result = nm.scan(hosts = host, arguments = arguments, sudo = args.sudo)["scan"]
        
        elif arguments != None and args.unprivileged == True:
            arguments += " --unprivileged" 
            result = nm.scan(hosts = host, arguments = arguments, sudo = args.sudo)["scan"]

        print("-------------------------------------------------")
        print("Command: " + nm.command_line())
        print_result(nm, result)
        
        found_new = False
        new_ips = []
        
        for host in result.keys():
            if host not in ip_list:
                found_new = True
                new_ips.append(host)
        
        while found_new:
            print("-------------------------------------------------")
            usr_input = input("Add newly discovered IP addresses to search list? (Y/N)?: ").lower()
            if usr_input == "y" or usr_input == "n":
                match usr_input:
                    case "y":
                        for x in new_ips: ip_list.append(x)
                        break
                    case "n":
                        break
        
        print("-------------------------------------------------")
        
        while True:
            usr_input = input("Add recent result to result list? (Y/N)?: ").lower()
            if usr_input == "y" or usr_input == "n":
                match usr_input:
                    case "y":
                        # result_dict = {
                        #     "127.0.0.1": [{
                        #           arguments: "-oX - -p 22-443 -sV",
                        #           timestr: "Tue Oct 15 14:55:49 2024"
                        #           result: {}
                        #     }]    
                        # }
                        for host in result.keys():
                            
                            if host in result_dict.keys() and len(result_dict[host]) > 0:
                                
                                result_dict[host].append({
                                    "timestr": nm.scanstats()["timestr"],
                                    "arguments": nm.command_line(),
                                    "result": result[host]
                                    }
                                )
                            else:
                                result_dict[host] = []
                                result_dict[host].append({
                                    "timestr": nm.scanstats()["timestr"],
                                    "arguments": nm.command_line(),
                                    "result": result[host]
                                    }
                                )   
                        break
                    case "n":
                        break        
   
    except nmap.PortScannerError as error:
        print("--------------")
        print("Error:\n" + error.value)
    except FileNotFoundError as error:
        print("--------------")
        print("Error: Problem with 'python-nMap' module. Possibly problem with sudo on windows")