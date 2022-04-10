
            except:
                print("Ocurrio Un Error")
                time.sleep(5)
    if(priceSlp >= 0.10):
            try:
                pywhatkit.sendwhatmsg_instantly("+5492324476498",  f"El SLP subió a 0.10! \nPrecio actual: ${priceSlp}")
                print("Mensaje Enviado")
                time.sleep(3600)
            except:
                print("Ocurrio Un Error")
                time.sleep(5)
    else:
        time.sleep(5)
    

