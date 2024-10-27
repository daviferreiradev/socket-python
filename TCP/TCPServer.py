from socket import *

# Define a porta do servidor
serverPort = 12000

# Cria o socket do servidor utilizando TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Associa o socket à porta e começa a escutar por conexões
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

# Loop infinito para aceitar conexões dos clientes
while True:
    # Aceita uma nova conexão do cliente
    connectionSocket, addr = serverSocket.accept()

    # Recebe uma mensagem do cliente (tamanho máximo de 1024 bytes)
    sentence = connectionSocket.recv(1024).decode()

    # Converte a mensagem para maiúsculas
    capitalizedSentence = sentence.upper()

    # Envia a mensagem modificada de volta ao cliente
    connectionSocket.send(capitalizedSentence.encode())

    # Fecha a conexão com o cliente
    connectionSocket.close()
