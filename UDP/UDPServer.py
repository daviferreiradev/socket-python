from socket import *

# Define a porta do servidor
serverPort = 12000

# Cria o socket do servidor utilizando UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Associa o socket à porta para começar a escutar mensagens
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

# Loop infinito para receber mensagens dos clientes
while True:
    # Recebe uma mensagem do cliente (tamanho máximo de 2048 bytes)
    message, clientAddress = serverSocket.recvfrom(2048)

    # Converte a mensagem para maiúsculas
    modifiedMessage = message.decode().upper()

    # Envia a mensagem modificada de volta ao cliente
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
