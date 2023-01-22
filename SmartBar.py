lista_bevande_maggiorenni = ["Birra", "Vino", "Vodka lemon", "Spumante"]
lista_bevande_minorenni = ["Coca-cola", "Fanta", "The al limone", "The alla pesca"]


print("Ciao, benvenuto nell'app SmartBar! ")
print("Prima di continuare, quest'app ha la funzionalità di consigliare i drink in base alla tua età!")
cliente = input("Quanti anni hai? :")

if int(cliente) < 18:
    print("sei MINORENNE, ecco le bevande che abbiamo a disposizione ")
    print(lista_bevande_minorenni)
    scelta_cliente = input("Quale bevanda scegli?: ")
    if scelta_cliente.lower() == "coca-cola":
        print("Hai scelto COCA-COLA, vuoi aggiungere altro al tuo ordine?: ")
    elif scelta_cliente.lower() == "fanta":
        print("Hai scelto FANTA, vuoi aggiungere altro al tuo ordine? ")
    elif scelta_cliente.lower() == "the al limone":
        print("Hai scelto THE AL LIMONE, vuoi aggiungere altro al tuo ordine? ")
    elif scelta_cliente.lower() == "the alla pesca":
        print("Hai scelto THE ALLA PESCA, vuoi aggiungere altro al tuo ordine? ")
else:
    print("sei MAGGIORENNE, ecco le bevande che abbiamo a dispozione")
    print(lista_bevande_maggiorenni)
    scelta_cliente = input("Quale bevanda scegli? ")
    if scelta_cliente.lower() == "birra":
        print("Hai scelto BIRRA, vuoi aggiungere altro al tuo ordine? ")
    elif scelta_cliente.lower() == "vino":
        print("Hai scelto VINO, vuoi aggiungere altro al tuo ordine? ")
    elif scelta_cliente.lower() == "vodka lemon.":
        print("Hai scelto VODKA LEMON, vuoi aggiungere altro al tuo ordine? ")
    elif scelta_cliente.lower() == "spumante":
        print("Hai scelto SPUMANTE, vuoi aggiungere altro al tuo ordine? ")

while True:
    aggiunta = input("Digita per aggiungere altro, altrimenti premi invio per confermare l'ordine: ")


    if aggiunta == "birra":
        print("Hai aggiunto BIRRA x1")
    elif aggiunta == "vino":
        print("Hai aggiunto VINO 1x")
    elif aggiunta == "vodka lemon":
        print("Hai aggiunto VODKA LEMON x1")
    elif aggiunta == "spumante":
        print("Hai aggiunto SPUMANTE x1")
    elif aggiunta == "coca-cola":
        print("Hai aggiunto COCA-COLA x1")
    elif aggiunta == "fanta":
        print("Hai aggiunto FANTA x1")
    elif aggiunta == "the alla pesca":
        print("Hai aggiunto THE ALLA PESCA x1")
    elif aggiunta == "the al limone":
        print("Hai aggiunto THE AL LIMONE x1")
    elif aggiunta != ():
        print("Il tuo ordine è completo, grazie per aver scelto SmartBar!")
        break




































