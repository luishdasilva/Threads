# Crie uma função proc1 que imprime uma mesnagem "Processo 1" e siga as instruções:
import threading
from threading import Thread

class fun:

    def funcao(self):
        print('Processo 1')

# a) inicialize essa função a partir de um objeto thread t1
b = fun()
t1 = Thread(target=b.funcao)
t1.start()
# b) Consulte se o objeto thread criado esta ativo
print(t1.is_alive())
# c) Consulte o nome da thread ativa atualmente
print(threading.currentThread())
# d) consulte o indentificador de thead do thread atual
print(threading.get_ident())
# e) Consulte a quantidade de threads ativas atualmente
print(threading.active_count())
# f) Retorne uma lista com todos os threads ativos atualmente
print(threading.enumerate())