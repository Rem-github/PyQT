
import socket
from ipaddress import ip_address
from subprocess import Popen, PIPE
import platform
from threading import Thread


def host_ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '1', str(ip)]
    reply = Popen(args, stdout=PIPE, stderr=PIPE)
    code = reply.wait()
    if code == 0:
        return print(f'{ip} Узел доступен')
    else:
        return print(f'{ip} Узел не доступен')


def host_range_ping(user_ip, numb):
    test_ip = ip_address(user_ip)
    for i in range(numb):
        ip = test_ip + i
        ping_thread = Thread(target=host_ping, args=(ip, ))
        ping_thread.start()


try:
    user_ip = socket.gethostbyname(input('Введите IP '))
    numb = int(input('Ввведите количество адресов для тестировния '))
    if int(user_ip.split('.')[3]) + numb > 255:
        print('Количество выходит за предеы 4-го октета')
    else:
        host_range_ping(user_ip, numb)
except:
    print('Не корректное имя хоста или IP адрес')
