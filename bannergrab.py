import socket
import getpass
delay = 20
def ban_no_pwd(host, port) :
    global delay
    # Making a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           
    try :
        s.settimeout(delay)
        if port == 80 :                                             
            s.connect((str(host), port))
            GET = 'GET / HTTP/1.1\nHost: '+ str(host) +'\n\n'  
            # Requesting for more the than ordinary three way handshake     
            s.sendall(str.encode(GET))
            banner = s.recvfrom(512)                                

        else :
            # normal TCP handshake and getting banner
            s.connect((str(host), port))                            
            banner = s.recvfrom(512)
        # part of code helps process received banner
        banner = banner[0]
        banner = banner.splitlines()                                
        for line in banner:
            line = str(line)
            ch_len = len(line)
            # This helps in removing all unnecessary parts of the line
            line = line.replace('\'','')                            
            print(line[1:ch_len:2])
         
    except Exception as er :
        print('Error : ' + str(er))                                 

    finally :
        s.close()                                                   


def ban_pwd(host,port):
    global delay
    # Making a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           
    try :
        s.settimeout(delay)
        if port == 80 :                                             
            s.connect((str(host), port))
            GET = 'GET / HTTP/1.1\nHost: '+ str(host) +'\n\n'       
            # Requesting for more the than ordinary three way handshake
            s.sendall(str.encode(GET))
            banner = s.recvfrom(512)                                

        else :
            # normal TCP handshake and getting banner
            s.connect((str(host), port))                            
            banner = s.recvfrom(512)
        # part of code helps process received banner
        banner = banner[0]
        banner = banner.splitlines()                                
        for line in banner:
            line = str(line)
            ch_len = len(line)
            # This helps in removing all unnecessary parts of the line
            line = line.replace('\'','')                            
            print(line[1::])
         
    except Exception as er :
        print('Error : ' + str(er))                                 

    finally :
        s.close()  

# Checking for any keyboard interrupts if availed
def input_any(msg) :                                               
    while True :
        try :
            return input(msg)
        except KeyboardInterrupt :
            print('You are not allowed to quit right now !')

def main() :
    global delay
    # Taking and validating user inputs
    host = input_any('Enter IP or URL : ')                         
    port = int(input_any('Enter port : '))
    if port < 1 or port > 65535 :
        print('Invalid input for port\nDefault set 80')
        port = 80
    if delay < 0 or delay > 100 :
        print('Invalid input for delay\nDefault set 5')
        delay = 5
    print('='*30 + 'Banner' +'='*30)
    # Calling function ban_no_pwd()
    ban_no_pwd(host, port)                                     
    print('\n\n')
    print("To unmask and understand, you need an Username and Password\n\n")
    value = input_any('Do you want to continue?\n 1.YES\n 2.NO\n')
    print('\n')
    if(value=='YES' or value == '1'):
        username = 'malware'
        password = 'Malware'
        user = input_any('Enter Username : ')
        if(user == username):
            pwd = getpass.getpass(prompt='Enter Password: ')
            print('\n')
            print('==============================Banner==============================')
            if (pwd == password):
                ban_pwd(host,port)

if __name__ == '__main__' :
    main()