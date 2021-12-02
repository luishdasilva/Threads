# Thread
# Descrição: Representa um thread
# Comando de inicialização: t1 = Thread(target=algumdef)

# Lock
# Lock é um bloqueio primitivo de aberto ou fechado
# lock = Lock()
# lock.acquire()
# lock.release()

# RLock
# RLock é um bloqueio primitivo que pode ter mais release e pode se diferenciar por
# aguentar arquitetura de contexto
# rlock = RLock()

# Condition
# Condition , são condições que são criadas para que uma thread espere até que uma condição
# seja realizada
# Con = Condition()

# Event
# Event é uma versão aonde varias Threads de ocorrência aguardam até um erro acontecer para ser executada
# threading.Event.set()
# threading.Event.wait()
# threading.Event.clear()

# Semaphore
# É um contador de recusos finitos compartilhado entre blocos de Threads
# threading.Semaphore.acquire()
# threading.Semaphore.release()

# BoundedSemaphore
# é semelante a semaphore porém nunca execede seu valor inicial
# class (value=1threading.BoundedSemaphore

# Timer
# É uma execução que só é executada após um tempo se passar
# T = Timer(30.0, Função)
# T.start()
# T.Cancel() para cancelar a execução

# Barrier
# é uma sinconização de numeros fixos que devem esperar um pelo outro para ser executados
# b = Barrier(2,timeout=5)
