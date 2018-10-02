import random
import socket

gen_numb = random.randint(1, 10)

def create_socket():
    # этот будем использовать, чтобы принимать данные
    sock = socket.socket()
    sock.bind(('', 9090))
    # допустимое кол-во подключений
    sock.listen(1)
    # accept возвращает кортеж с двумя элементами: новый сокет(чтобы отправлять, он будет прослушиваться клиентом)
    # и адрес клиента
    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        command, arg = data.decode('utf-8').split(',')
        if command == 'guess':
            result = check(int(arg))
            conn.send(bytes(result, 'utf-8'))
        else:
            conn.send(bytes('Вы прислали неверную команду', 'utf-8'))
            conn.close()


def check(hidden_number: int):
    print(hidden_number)
    result = {
        '>': 'more',
        '<': 'less',
        '=': 'correct'
    }

    if hidden_number == gen_numb:
        return result['=']
    elif hidden_number < gen_numb:
        return result['<']
    elif hidden_number > gen_numb:
        return result['>']


if __name__ == '__main__':
    create_socket()
