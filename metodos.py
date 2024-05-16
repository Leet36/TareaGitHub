import metodos2


def menu():
    print("Para agregar cliente, digite el numero (1)")
    print("Para Buscar Cliente => Consultar saldo, digite el numero (2)")
    print("Para Modificar Cliente, digite el numero (3)")
    print("Para Registrar movimiento, digite el numero (4)")
    print("Para Borrar cliente, digite el numero (5)")
    print("Para Salir, digite el numero (6)")

def ingresar_cliente():
    sistema = metodos2.cargar_db()
    data_cliente = dict()
    id = input("Identificacion: ")
    data_cliente['nombre'] = input("Nombre..: ").upper()
    data_cliente['apellido1'] = input("Primer apellido..: ").upper()
    data_cliente['apellido2'] = input("Segundo apellido..: ").upper()
    sistema[id] = data_cliente
    metodos2.almacenar_db(sistema)

def busqueda():
    identificacion=input("Ingrese el numero de identificacion que desea consultar..:")
    sistema = metodos2.cargar_db()
    if identificacion in sistema:
        print("Identificacion..: "+identificacion)
        data_cliente = sistema[identificacion]
        print("Nombre..: "+data_cliente['nombre'].upper())
        print("Primer apellido..: "+data_cliente['apellido1'].upper())
        print("Segundo apellido..: "+data_cliente['apellido2'].upper())
        print("Saldo actual..:$ "+str(+data_cliente['saldo']))
        print("------------------------------------------------------")


def modificar():
        identificacion=input("Ingrese el numero de identificacion del cliente..:")
        sistema = metodos2.cargar_db()    
        if identificacion in sistema:
         print("Identificacion..: "+identificacion)
         data_cliente = sistema[identificacion]
         print("Nombre actual..:"+data_cliente['nombre'].upper())
         print("Primer apellido actual..:"+data_cliente['apellido1'].upper())
         print("Segundo apellido actual..:"+data_cliente['apellido2'].upper())
         nuevonombre=input("Ingrese el nuevo nombre..:")
         nuevoapellido1=input("Ingrese el nuevo primer apellido..:")
         nuevoapellido2=input("Ingrese el nuevo segundo apellido..:")
         data_cliente['nombre']=nuevonombre
         data_cliente['apellido1']=nuevoapellido1
         data_cliente['apellido2']=nuevoapellido2
         metodos2.almacenar_db(sistema)

    
def registrar():
        identificacion=input("Ingrese el numero de identificacion del cliente..:")
        sistema = metodos2.cargar_db()    
        if identificacion in sistema:
         print("Identificacion..: "+identificacion)
         data_cliente = sistema[identificacion]
         print("Saldo actual..:$ "+str(+data_cliente['saldo']))
         print("------------------------------------------------------")
         compra=float(input("Ingrese el monto de la compra..:$"))
         abono=float(input("Ingrese el monto a abonar..:$"))
         saldot=data_cliente['saldo']
         subtotal=compra+saldot
         nuevosaldo= (saldot+compra)-abono
         print("Desglose de la transaccion..:")
         print("Monto de la compra..:$"+str(compra))
         print("Saldo inicial..:$"+str(saldot))
         print("Sub total..:$"+str(subtotal))
         print("Abono..:$"+str(abono))
         print("Saldo actual..:$"+str(nuevosaldo))
         print("------------------------------------------------------")
         data_cliente['saldo']=nuevosaldo
         metodos2.almacenar_db(sistema)

def borrar():
        identificacion=input("Ingrese el numero de identificacion del cliente..:")
        sistema = metodos2.cargar_db()    
        if identificacion in sistema:
         print("Identificacion..: "+identificacion)
         data_cliente = sistema[identificacion]
         del data_cliente['apellido1']
         del data_cliente['apellido2']
         del data_cliente['nombre']
         print("El registro a sido borrado")
         metodos2.almacenar_db(sistema)