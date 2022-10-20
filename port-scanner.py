import socket,sys

def connect(host):
    print('Scanning host:', host)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        port=443
        connection = s.connect_ex((host, port))    #NOTE: connect() needs a tuple!
        if (connection == 0):
            print('Port {} is open'.format(port))
        s.close()
    except KeyboardInterrupt:
        print('Exiting because you pressed Ctrl + C')
        sys.exit()
    except socket.error:
        print('Couldn\'t connect to Server')

if __name__ == '__main__':
    userInput = input('Enter the Server address(URL) to check for open ports: ')
    remoteServerIP  = socket.gethostbyname(userInput)
    print('Server IP:',remoteServerIP)
    connect(remoteServerIP)
