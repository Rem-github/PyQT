
import socket
from ipaddress import ip_address
from subprocess import Popen, PIPE
import platform



def host_ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '1', str(ip)]
    reply = Popen(args, stdout=PIPE, stderr=PIPE)
    code = reply.wait()
    if code == 0:
        return print(f'{ip} Узел доступен')
    else:
        return print(f'{ip} Узел не доступен')


try:
    user_ip = socket.gethostbyname(input('Введите IP '))
    host_ping(ip_address(user_ip))
except:
    print('Не корректное имя хоста или IP адрес')