cose_che_ho_sempre = ["Assi normali", "Assi medie", "Assi grandi", "Chiodi", "Martello", "Trapano"]
risposta_app = "Ok l'ho aggiunto alla lista!"

print("Ciao, sono l'app inventario!")
print("Questa è la lista di cose che non deve MAI mancare:")
print(cose_che_ho_sempre)
print()
cosa_che_manca = input("Cosa manca oggi?: ")


if cosa_che_manca == "assi normali":
    print("Mancano le ASSI NORMALI!")
elif cosa_che_manca == "assi medie":
    print("Mancano le ASSI MEDIE!")
elif cosa_che_manca == "assi grandi":
    print("Mancano le ASSI GRANDI!")
elif cosa_che_manca == "chiodi":
    print("Mancano i CHIODI!")
elif cosa_che_manca == "martello":
    print("Mancano i MARTELLI!")
elif cosa_che_manca == "trapano":
    print("Manca il TRAPANO!")
si_o_no = input("Vuoi aggiungerlo alla lista di cose da comprare?: ")

if si_o_no == "si":
    print("Ho aggiunto", str(cosa_che_manca))
    quantità = input("In che quantità?: ")
    if quantità == "1":
        print("Hai aggiunto x1:", str(cosa_che_manca))
    elif quantità == "2":
        print("Hai aggiunto x2:", str(cosa_che_manca))
    elif quantità == "3":
        print("Hai aggiunto x3:", str(cosa_che_manca))
    elif quantità == "4":
        print("Hai aggiunto x4:", str(cosa_che_manca))
else:
    print("Perfetto, lo aggiungerò in un altro momento!")
    cambio = input("Vuoi cambiare l'ordine?: ")
    if cambio == "si":
        cambio = input("Cosa vuoi aggiungere? : ")
    if cambio == "chiodi":
        cambio_quantità = input("Quanti ne vuoi aggiungere?: ")
        print("Hai aggiunto  CHIODI x: ", str(cambio_quantità))
    elif cambio == "assi normali":
        cambio_quantità = input("Quanti ne vuoi aggiungere?: ")
        print("Hai aggiunto ASSI NORMALI x:", str(cambio_quantità))
    elif cambio == "assi medie":
        cambio_quantità = input("Quanti ne vuoi aggiungere?: ")
        print("Hai aggiunto ASSI MEDIE x :", str(cambio_quantità))
    elif cambio == "assi grandi":
        cambio_quantità = input("Quanti ne vuoi aggiungere?: ")
        print("Hai aggiunto ASSI GRANDI x:", str(cambio_quantità))
    elif cambio == "martello":
        cambio_quantità = input("Quanti ne vuoi aggiungere?: ")
        print("Hai aggiunto MARTELLO x:", str(cambio_quantità))
    elif cambio == "trapano":
        cambio_quantità = input("Quanti ne vuoi aggiungere?: ")
        print("Hai aggiunto TRAPANO x:", str(cambio_quantità))
    else:
        cambio_quantità = input("In che quantità CAMBIO?:")
        if cambio_quantità == "1":
            print("Hai aggiunto x1:", str(cambio))
        elif cambio_quantità == "2":
            print("Hai aggiunto x2:", str(cambio))
        elif cambio_quantità == "3":
            print("Hai aggiunto x3:", str(cambio))
        elif cambio_quantità == "4":
            print("Hai aggiunto x4:", str(cambio))
        altro_cambio = input("Cos'altro manca?: ")
        if altro_cambio == "chiodi":
            print(risposta_app)

altro_che_manca = input("Cos'altro manca?: ")

if altro_che_manca == "trapano":
    altro_quantità = input("In che quantità?: ")
    print("Ho aggiunto TRAPANO x",str(altro_quantità))
if altro_che_manca == "assi grandi":
    altro_quantità = input("In che quantità?: ")
    print("Ho aggiunto ASSI GRANDI x", str(altro_quantità))
if altro_che_manca == "assi medie":
    altro_quantità = input("In che quantità?: ")
    print("Ho aggiunto ASSI MEDIE x", str(altro_quantità))
if altro_che_manca == "assi normali":
    altro_quantità = input("In che quantità?: ")
    print("Ho aggiunto ASSI NORMALI x", str(altro_quantità))
if altro_che_manca == "chiodi":
    altro_quantità = input("In che quantità?: ")
    print("Ho aggiunto CHIODI x", str(altro_quantità))
if altro_che_manca == "martello":
    altro_quantità = input("In che quantità?: ")
    print("Ho aggiunto MARTELLO x", str(altro_quantità))

while True:
    altro_loop = input("Cos'altro MANCA? inserisci prodotto o premi invio per confermare: ")
    if  altro_loop == "trapano":
        loop = input(" Ok, in che quantità?: ")
        print("Ho aggiunto TRAPANO x", str (loop))
    elif altro_loop == "chiodi":
        print("Ho aggiunto chiodi")
        loop = input(" Ok, in che quantità?: ")
        print("Ho aggiunto CHIODI x", str(loop))
    elif altro_loop == "martello":
        print("Ho aggiunto MARTELLO")
        loop = input(" Ok, in che quantità?: ")
        print("Ho aggiunto MARTELLO x", str(loop))
    elif altro_loop == "assi grandi":
        print("Ho aggiunto ASSI GRANDI")
        loop = input(" Ok, in che quantità?: ")
        print("Ho aggiunto ASSI GRANDI x", str(loop))
    elif altro_loop == "assi medie":
        print("Ho aggiunto ASSI MEDIE")
        loop = input(" Ok, in che quantità?: ")
        print("Ho aggiunto ASSI MEDIE x", str(loop))
    elif altro_loop == "assi normali":
        print("Ho aggiunto ASSI NORMALI")
        loop = input(" Ok, in che quantità?: ")
        print("Ho aggiunto ASSI NORMALI x", str(loop))

    else:
        print("Il tuo ordine è stato completato!")
        break