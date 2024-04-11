import socket
from termcolor import colored
import pyfiglet


def intro():
    # executing the welcome message, and more
    text = "P.Scanner"
    intro_text = pyfiglet.figlet_format(text, font="standard")
    print(colored("Welcome to,", "red"))
    print(colored(intro_text, 'white'))


def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print(colored(f"[+] Connection to the port no.{port} is Sucessfull.", 'green'))
    except:
        pass


def scan(ip_address, target_ports):
    # used to scan the port of the target, and the for loop helps us to go through the ports from 1 to user defined.
    print(colored(f"[+] Scanning {ip_address}.", 'yellow'))
    for port in range(1, target_ports+1):
        scan_port(ip_address, port)


def start_scan():
    # giving instructions to the user for inputs.
    print(colored("if there are more targets, seperate it by a comma , ", "magenta", attrs=['bold']))
    targets = input("[*] Enter the targets: ")
    ports = int(input("[*] Enter the numbers of the port, you want to scan."))
    # checking for multiple targets.
    if "," in targets:
        # if there are multiple targets:
        print(colored("[+] Scanning Multiple Targets.", 'green'))
        # splitting the target into arrays and then looping through the array.
        for target in targets.split(","):
            # sending each target to the scan function where we loop through the ports,
            # so we can scan the ports range user specified for all targets.
            scan(target.strip(" "), ports)
    else:
        scan(targets, ports)


intro()
start_scan()
