import requests
from datetime import datetime

_ENDPOINT = "https://api.binance.com"
file_name = "tx_prueba.txt"

class Criptomoneda(object):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    
    def indicateQuantity(self, quantity):  
        self.quantity=quantity

    def showName(self):
        return self.name
    
    def showQuantity(self):  
        return  self.quantity
    
    def calculateBalance(self, cotizacion):  
        return self.quantity*cotizacion
        
class Usuario(object):
    def __init__(self, code):
        self.code = code
    
    def mostrarCodigo(self):
        return self.code



def _url(api):
    return _ENDPOINT+api

def get_price(cripto):
    data = requests.get(_url("/api/v3/ticker/price?symbol="+cripto)).json()
    precio = float(data["price"])
    return precio

def esmoneda(cripto):
    criptos = ["BTC","BCC","LTC","ETH"]
    if cripto in criptos:
        return True
    else:
        print("Ingrese una moneda válida (BTC,BCC,LTC,ETH)")
        return False

def validarCodigo(code):
    if code == usuario.code:
        print("\n       ¡TRANSACCIÓN FALLÍDA!, el código indicado es inválido")
        return False
    else:
        return True

def cantidadSuficiente(moneda, quantity):
    aux = True
    if(moneda== "BTC"):
        if(bit.quantity >= quantity):
            return True
        else:
            aux = False
    if(moneda== "ETH"):
        if(ethe.quantity >= quantity):
            return True
        else:
            aux = False
    if(moneda== "BCC"):
        if(bcc.quantity >= quantity):
            return True
        else:
            aux = False
    if(moneda== "LTC"):
        if(ltc.quantity >= quantity):
            return True
        else:
            aux = False
    if(aux==False):
        print("     ¡TRANSACCIÓN RECHAZADA!, Cantidad de "+ moneda+ " es insuficiente")
        return False

def GuardarRegistro(moneda, operacion, code, quantity, cantTotal):
    archivo = open(file_name,"a")
    dt = datetime.now()
    precio =  get_price(moneda+"USDT")
    archivo.write("\n"+"Fecha"+ ":" + dt.strftime("%A %d/%m/%Y %I:%M:%S%p") +",Moneda" +":"+str(moneda)
        +",Transacción" +":"+ operacion+",Código de usuario"+ ":"+ str(code) + ",Cantidad "+ ":"+ str(quantity) 
            + ",Total de la operación en $"+":"+ str(precio*quantity) +", Total acumulado en cuenta en $" + ":"+ str(precio*cantTotal))
    archivo.close()
    return

bit = Criptomoneda("BTC",2.5)
ethe = Criptomoneda("ETH",0.6723)
bcc = Criptomoneda("BCC",9.3)
ltc = Criptomoneda("LTC",7.06)
monedas = [bit,ethe,bcc,ltc]
usuario = Usuario(2031)

while True:
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")
    print("           Hola,  Bienvenid@ a tu billetera virtual")
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")
    print("Tú código de Usuario es: " + str(usuario.mostrarCodigo()))
    print("Tipo de Monedas: BTC, ETH, BCC, LTC")
    print("Menú de opciones:")
    print(("1. Recibir Cantidad \n"
        "2. Transferir monto\n"
        "3. Mostrar balance de una moneda\n"
        "4. Mostrar balance general\n"
        "5. Mostrar histórico de transacciones\n"
        "6. Salir del programa"))
    seleccion = int(input("Selecciona opción para continuar:"))

    if(seleccion==1):
        moneda = input("    Ingrese la moneda a recibir: ")
        while not esmoneda(moneda):
            moneda = input("    Ingrese la moneda a recibir: ")
        quantity = float(input("        Ingrese la cantidad a recibir de " + moneda+ ":"))
        code = int(input("        Ingrese el código del emisor: "))
        while not validarCodigo(code):
            code = int(input("        Ingrese el código del emisor: "))
        if(moneda=="BTC"):
            bit.indicateQuantity(bit.quantity + quantity)
            GuardarRegistro(moneda,"Recibido",code, quantity, bit.showQuantity())
        elif(moneda=="ETH"):
            ethe.indicateQuantity(ethe.quantity + quantity)
            GuardarRegistro(moneda,"Recibido",code, quantity,ethe.showQuantity())
        elif(moneda=="BCC"):
            bcc.indicateQuantity(bcc.quantity + quantity)
            GuardarRegistro(moneda,"Recibido",code, quantity,bcc.showQuantity())
        elif(moneda=="LTC"):
            ltc.indicateQuantity(ltc.quantity + quantity)
            GuardarRegistro(moneda,"Recibido",code, quantity,ltc.showQuantity())
        print("\n       ¡TRANSACCIÓN EXITOSA!, El saldo fue añadido correctamente a su billetera")

    elif(seleccion==2):
        moneda = input("    Ingrese la moneda a transferir: ")
        while not esmoneda(moneda):
            moneda = input("    Ingrese la moneda a transferir: ")
        quantity = float(input("        Ingrese la cantidad a transferir de " + moneda+ ":"))
        while not cantidadSuficiente(moneda, quantity):
            quantity = float(input("        Ingrese la quantity a transferir de " + moneda+ ":"))
        code = int(input("        Ingrese el código del receptor: "))
        while not validarCodigo(code):
            code = int(input("        Ingrese el código del receptor: "))
        if(moneda=="BTC"):
            bit.indicateQuantity(bit.quantity - quantity)
            GuardarRegistro(moneda,"Enviado",code, quantity, bit.showQuantity())
        elif(moneda=="ETH"):
            ethe.indicateQuantity(ethe.quantity - quantity)
            GuardarRegistro(moneda,"Enviado",code, quantity, ethe.showQuantity())
        elif(moneda=="BCC"):
            bcc.indicateQuantity(bcc.quantity - quantity)
            GuardarRegistro(moneda,"Enviado",code, quantity, bcc.showQuantity())
        elif(moneda=="LTC"):
            ltc.indicateQuantity(ltc.quantity - quantity)
            GuardarRegistro(moneda,"Enviado",code, quantity, ltc.showQuantity())
        print("\n       ¡TRANSACCIÓN EXITOSA!, El saldo fue descontado correctamente de su billetera")
        
    elif(seleccion==3):
        moneda = input("    Ingrese la moneda a consultar: ")
        while not esmoneda(moneda):
            moneda = input("    Ingrese la moneda a consultar: ")
        precio = get_price(moneda+"USDT")
        if(moneda=="BTC"):
            print("Moneda: " + moneda + " Cantidad: "+ str(bit.showQuantity()) +" Saldo disponible: $."+ str(bit.calculateBalance(precio)))
        elif(moneda=="ETH"):
             print("Moneda: " + moneda + " Cantidad: "+str(ethe.showQuantity()) +" Saldo disponible: $."+str(ethe.calculateBalance(precio)))
        elif(moneda=="BCC"):
             print("Moneda: " + moneda + " Cantidad: "+str(bcc.showQuantity()) + " Saldo disponible: $."+str(bcc.calculateBalance(precio)))
        elif(moneda=="LTC"):
             print("Moneda: " + moneda + " Cantidad: "+ str(ltc.showQuantity()) +" Saldo disponible: $."+str(ltc.calculateBalance(precio)))

    elif(seleccion==4):
        moneda = ""
        totalUSD = 0
        for moneda in monedas:
            precio = get_price(moneda.showName()+"USDT")
            totalUSD += moneda.calculateBalance(precio)
            print("Moneda: " + moneda.showName() + " Cantidad: "+ str(moneda.showQuantity()) +" Saldo disponible: $."+ str(moneda.calculateBalance(precio)) +"\n")
        print("El monto acumulado total de todas las criptomonedas es $." + str(totalUSD))

    elif(seleccion==5):
        archivo = open(file_name,"r")
        texto = archivo.read()
        archivo.close()
        lineas = texto.splitlines()
        print(texto)
    elif(seleccion==6):
        print("------------------------------------------------------------")
        print("------------------------------------------------------------")
        print("\n Gracias por usar tu billetera virtual")
        print("Vuelva Pronto***")
        print("------------------------------------------------------------")
        print("------------------------------------------------------------")
        break
    else:
        print("\nPor favor, seleccione una opción válida")