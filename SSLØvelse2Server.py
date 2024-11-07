from socket import *
import threading
import ssl

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

def handle_client(connection_socket, address):
    print(address)
    sentence = connection_socket.recv(1024).decode()
    print(sentence)
    capitalized_sentence = sentence.upper()
    connection_socket.send(capitalized_sentence.encode())
    connection_socket.close()
    
certificatesDirectory = 'C:/certificates/'
privateKeyPath = certificatesDirectory + 'key.pem'
certificatePath = certificatesDirectory + 'certificate.pem'
privateKeyPassword = 'rasm'

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=certificatePath, keyfile=privateKeyPath, password=privateKeyPassword)
secureSocket = context.wrap_socket(serverSocket, server_side=True)
print('Server is ready to listen')

while True:
    connectionSocket, addr = secureSocket.accept()
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))    
    client_thread.start()
