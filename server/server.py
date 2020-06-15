from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

HOST ='loaclhost'
PORT = 5500
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Wating For Connection...")
    
