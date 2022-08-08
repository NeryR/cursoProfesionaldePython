from datetime import datetime

# Este decorador sirve para definir cuanto tiempo tarda en ejecutarse el código e imprimirlo en la pantalla
def execution_time(func):
    # Con *args no importa la cantidad de argumentos que se le den a la función y con *kwargs no importa la cantidad de parámetros nombrados igual se va a ejecutar la función
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    # El _ se utiliza en el ciclo for cuando no importa la variable que se usará en el ciclo for
    for _ in range(1, 100000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre="Cesar"):
    print("Hola " + nombre)

random_func()
suma(5, 5)
saludo("Nery")

