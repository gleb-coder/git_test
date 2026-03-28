import socket
import threading

nickname = input('Enter your Nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('100.70.109.7', 55556))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('Connection Error')
            client.close()
            break

def write():
    while True:
        text = input("")
        if text:
            message = f"{nickname}: {text}"
            client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()