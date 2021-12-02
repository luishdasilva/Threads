# Crie uma função proc1 e proc2 que imprime a mensagem "Processo 1" e "Processo 2"
import threading
from threading import Thread
import time

class funcao:

    def proc1(self):
        print("Processo 1")


    def proc2(self):
        print("Processo 2")


# a) Inicialize as funções a partir de um objeto Thread t1 e t2
f = funcao()
c = Condition()
t1 = Thread(target=f.proc1)
t1.start()

#d
print(t1.is_alive())
print('Resposta d')
time.sleep(30)

t2 = Thread(target=f.proc2)
t2.start()
#d
print(t2.is_alive())
time.sleep(30)

# b) Consulte se os objetos criados estão ativos
#print(t1.is_alive())
#print(t2.is_alive())
# c) Importe o modulo time e crie um delay de tempo em cada uma das funções sendo
# sleep 5 e 30 segundos em proc1 e proc2

# d)Consulte rapidamente (antes de 30 segundos) se cada um dos objetos thread esta ativo
# e imprima na tela


