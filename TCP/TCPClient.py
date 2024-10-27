from socket import * 

# Define o nome do servidor e a porta para comunicação
serverName = '127.0.0.1'  # Use 'localhost' ou IP do servidor
serverPort = 12000

# Cria o socket do cliente utilizando TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Conecta o socket ao servidor
clientSocket.connect((serverName, serverPort))

# Lê uma mensagem do usuário para enviar ao servidor
sentence = input('Input lowercase sentence: ')

# Envia a mensagem codificada para o servidor
clientSocket.send(sentence.encode())

# Recebe a resposta do servidor (tamanho máximo de 1024 bytes)
modifiedSentence = clientSocket.recv(1024)

# Exibe a resposta do servidor
print(f"From Server: {modifiedSentence.decode()}")

# Fecha o socket do cliente
clientSocket.close()
