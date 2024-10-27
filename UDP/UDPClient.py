from socket import * 

# Define o nome do servidor e a porta para comunicação
serverName = '127.0.0.1'  # Use 'localhost' ou IP do servidor
serverPort = 12000

# Cria o socket do cliente utilizando UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Lê uma mensagem do usuário para enviar ao servidor
message = input('Input lowercase sentence: ')

# Envia a mensagem codificada para o servidor
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Recebe a resposta do servidor (tamanho máximo de 2048 bytes)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Exibe a resposta do servidor
print(f"Modified message from server: {modifiedMessage.decode()}")

# Fecha o socket do cliente
clientSocket.close()
