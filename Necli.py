import random


saldo=4500
Internet=2500
Telefonia=2100
hamburguesa=1400
pizza=1200
perro=800
Salchipapa=1800
Arepa=2300
Tv=1700
repetir="s"
for f in range(3,-1,-1):
    Cel=input("Dijite Cel\n")
    Clave=input("Dijite Clave\n")
    
    if(Cel=="1234" and Clave=="1234"):
        while repetir=="s" or repetir=="S":
            Opcion=int(input(f"Benvenido a Nequi su saldo es de {saldo} Que funcion quieres hacer\n1. Saca \n2. Envia\n3. Recarga \n4. Pagar Serivicios\n5. Domicilio\n6. Salir \n"))
            if(Opcion==1):
                Tipo=int(input("Dijite si quiere cajero o punto fisico \n1. Cajero \n1. Punto Fisico\n"))
                if(Tipo==1 and saldo>2000):
                    codigo = ""
                    for i in range(6):
                        codigo += str(random.randint(0, 9))
                        
                    Retiro=int(input(f"Su codigo para poder retirar es {codigo}\n Ahora dijite el valor a retirar su saldo es {saldo}\n"))
                    saldo=saldo-Retiro
                    if(saldo>Retiro):
                        print(f"Su saldo actual despues de el retiro de dinero es de {Retiro}")

                if(Tipo==2 and saldo>2000):
                        input("Cuanto desea retirar su saldo es de ",saldo)
                else:
                    print("No te alcanza !!!Recargue!!!")
            elif(Opcion==2):
                numero=input("Dijite el numero al que le enviara el dinero\n")
                valorenviado=int(input(f"Dijite la cantidad de dinero que Enviara !Recuerde que su saldo es de {saldo}\n"))
                if(saldo>valorenviado):
                    saldo=saldo-valorenviado
                    print(f"Uste envio {valorenviado} a el numero {numero} y su saldo actual es de {saldo}")
                else:
                    print("No puedes enviar mas dinero de el que tienes")

            elif(Opcion==3):
                recarga=int(input("Dijete la cantidad de dinero a recargar\n"))
                saldo=saldo+recarga
                print("Su saldo + la recarga da un total de ",saldo)
            elif(Opcion==4):
                servicio=int(input("Dijite lo que quiere pagar \n1. Internet\n2. Telefonia \n3. Tv\n"))
                if(servicio==1):
                    saldo=saldo-Internet
                    print(f"Usted pago  2500 Internet y su saldo actual es de {saldo} ")
                elif(servicio==2):
                    saldo=saldo-Telefonia
                    print(f"Usted pago 2100 de Telefonia y su saldo actual es de {saldo}")
                elif(servicio==3):
                    saldo=saldo-Tv
                    print(f"Usted pago 1700 de Tv y su saldo actual es de {saldo}")
                else:
                    print("Deje de hacer un willson y marque un numero valido")
            elif(Opcion==5):
                Domicilio=int(input("Dijite que tipo de domicilio eligira \n1. Comida \n2. Transporte\n"))
                if(Domicilio==1):
                    Comida=int(input("Que quiere comer \n1. Hamburguesa\n2. Pizza\n3. Perro\n4. Salchipapa\n5. Arepa\n"))
                    if(Comida==1 and saldo>hamburguesa):
                        hamburguesa1=int(input(f"Dijte la cantidad de hamburguesas que desea comprar , la hamburguesa tiene un costo de 1400 y su saldo es de {saldo}"))
                        total=hamburguesa*hamburguesa1
                        print("No le alcanza")
                        if(saldo>total):
                            saldo=saldo-hamburguesa
                            print(f"Uste compro {hamburguesa1} hamburguesas y su saldo quedo en{saldo}")
                    elif(Comida==2 and saldo>=pizza):
                        pizza1=int(input("Dijte la cantidad de Pizzas que desea comprar , la Pizza tiene un costo de 1200\n"))
                        total=total-pizza*pizza1
                        if(saldo>total):
                            salod=saldo-pizza
                            print(f"Uste compro {pizza1} Pizza y su saldo quedo en{saldo}")
                    elif(Comida==3 and saldo>=perro):
                        Perro1=int(input("Dijte la cantidad de Perros que desea comprar , la Perro tiene un costo de 800\n"))
                        total=perro*Perro1
                        print("No le alcanza")
                        if(saldo>total):    
                            print(f"Uste compro {Perro1} Perros y su saldo quedo en {saldo}")
                    elif(Comida==4 and saldo>=Salchipapa):
                        Salchipapa1=int(input("Dijte la cantidad de Perros que desea comprar , la Salchipapa tiene un costo de 1800\n"))
                        total=Salchipapa*Salchipapa1
                        print("No le alcanza")
                        if(saldo>total):
                            saldo=saldo-Salchipapa
                            print(f"Uste compro {Salchipapa1} Salchipapa y su saldo quedo en{saldo}")
                    elif(Comida==5 and saldo>=Arepa):
                        Arepa1=int(input("Dijte la cantidad de Salchipapa que desea comprar , la Arepa tiene un costo de 2300\n"))
                        total=Arepa*Arepa1
                        print("No le alcanza")
                        if(saldo>total):
                            print(f"Uste compro {Arepa1} Arepa y su saldo quedo en{saldo}")
                    else:
                        print("Dijte un numero valido")
                elif(Domicilio==2):
                    Transporte=int(input("Dijite su forma de transporte \n1. Picap \n2. Uber"))
                    if(Transporte==1):
                        Picap=int(input("Si sale de su localidad se le cobrara un recargo de 2200 ,si no su tarifa normal sera de 1300 , saldra de la localidad \n1. Si \n2. No \n   "))
                        if(Picap==1):
                            saldo=saldo-4200
                            print(f"Uste salio de su localidad entonces el total de el viage es de 4200 y su saldo quedo {saldo}")
                        elif(Picap==2):
                            saldo=saldo-1300
                            print(f"Uste no salio de la localidad entonces su viaje es de 1300 y su saldo quedo en {saldo} ")
                        else:
                            print("Dijte un numero valido")
                    elif(Transporte==2):
                        Uber=int(input("El uber cobra un recardo por ser de noche de 3000 y de dia 1400 ,Viaje de \n1. Dia \n2. Noche"))
                        if(Uber==1):
                            saldo=saldo-4400
                            print(f"Usted cojio el Uber de noche entonces el recargo nocturno es de 3000 y su saldo quedo en{saldo} ")
                        elif(Uber==2):
                            saldo=saldo-1400
                            print(f"Usted cojio el uber de Dia por lo tanto no se le cobrara recargo y su saldo es de {saldo} ")
                        else:
                            print("Dijte un numero valido")
            elif Opcion==6:
                repetir=input("Si quiere seguir s o n")
        break    
    else:
        print(f"!!Oooops esto no esta bien te quedan {f} intentos")
        









