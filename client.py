import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
while True:
    sock.send(bytes('guess, %s' % input('Введите число: '), 'utf-8'))

    data = sock.recv(1024)

    if data.decode('utf-8') == 'correct':
        print(data.decode('utf-8'))
        sock.close()
        break

    print(data.decode('utf-8'))
