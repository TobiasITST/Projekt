# nMap tool
- A python implementation of nMaP
- Host discovery
- Portscanning

### How to run
    example > python main.py -u
##### Arguments
| Flag | Description |
| :----------- | :----------- |
|`-u` or `--unprivileged`| Adds '--unprivileged' flag on nMap scan. Required for me on Windows machine|
|`-s` or `sudo`| Sets nMap scan with sudo mode. (**Does not work on Windows for me**)|
#### Menu structure:
##### Main menu
    - nMap, Enter the Nmap menu to run nMap scans, open result file etc.
    - IP, Enter the IP-address menu
    - Exit, exits this program and does NOT save any results
    - --help, show program commands again

##### nMap menu
    - nMap, execute nMap commands
    - Show, show result of current session
    - Open, open previous result from JSON-file
    - Save, save current session result to JSON-file
    - Show IP, show IP addresses in current list
    - Back, goes back to main menu. Careful! Save to file if you done any changes
    - --help, show menu commands again

##### Ip address menu
    - Show, show IP addresses in current list
    - Open, open desired IP address list from file
    - Save, save current IP address list to file
    - Add, add an IP address to current list
    - Remove, remove an IP address from current list
    - Back, goes back to main menu. Careful! Save to file if you done any changes
    - --help, show menu commands again

### Requires
- [python-nmap package](https://pypi.org/project/python-nmap/)
    - run `pip install python-nmap`
- [nMap](https://nmap.org/) installed and PATH linked to nMap (Atleast on Windows)

### Limitations
- Written and **only tested** on **Windows** machine
- **Can't use 'sudo'** in nMap scan on **Windows** machine
- Does not ask to append when saving results or IP list to file
- No nMap argument validation
