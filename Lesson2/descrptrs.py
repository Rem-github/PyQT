import logging
logger = logging.getLogger('server_dist')


# Дескриптор для описания порта:
class Port:
    def __set__(self, instance, value):
        if not 1023 < value < 65536:
            logger.critical(
                f'Попытка запуска сервера с указанием неподходящего порта {value}. Допустимы адреса с 1024 до 65535.')
            exit(1)
        instance.__dict__[self.attr_name] = value

    def __set_name__(self, owner, attr_name):
        self.attr_name = attr_name            # с версии 3.6 вместо __init__ используем __set_name__ и аттрибуту назначаем дескриптор
                                            # так port = Port(), вместо port = Port('port')

