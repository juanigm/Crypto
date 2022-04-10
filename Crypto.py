
import requests
import time
import pywhatkit

headers = {
        'X-CMC_PRO_API_KEY': '66dad4bf-993f-4a7a-ab60-a05e3aa0db22',
        'Accepts': 'application/json'
        }

params = {
        'start': '1',
        'limit': '400',
        'convert': 'USD'
        }

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

price = 0
priceSlp = 0

while True:
    print("Obteniendo Datos")
    json = requests.get(url, params = params, headers = headers).json()
    coins =  json['data']
    for coin in coins:
        if coin['symbol'] == 'SLP':
            priceSlp = round(coin['quote']['USD']['price'],5)
        if coin['symbol'] == 'AXS':
            price = round(coin['quote']['USD']['price'],7)
    print("Datos obtenidos")
    print(price)
    if(price <= 130): 
            try:
                pywhatkit.sendwhatmsg_instantly("+5492324476498", f"El AXS bajó de los $130 \nPrecio actual: ${price}", 15, True, 5)
                pywhatkit.sendwhatmsg_instantly("+5492324531926", f"El AXS bajó de los $130 \nPrecio actual: ${price}", 15, True, 5)
                pywhatkit.sendwhatmsg_instantly("+5492324526219", f"El AXS bajó de los $130 \nPrecio actual: ${price}", 15, True, 5)
                pywhatkit.sendwhatmsg_instantly("+5491141692701", f"El AXS bajó de los $130 \nPrecio actual: ${price}", 15, True, 5)
                
                pywhatkit.close_tab(3)
                print("Mensaje Enviado")
                time.sleep(1800)
            except:
                print("Ocurrio Un Error")
                time.sleep(5)
    if(priceSlp >= 0.10):
            try:
                pywhatkit.sendwhatmsg_instantly("+5492324476498",  f"El SLP subió a 0.10! \nPrecio actual: ${priceSlp}")
                pywhatkit.sendwhatmsg_instantly("+5492324531926", f"El SLP subió a 0.10! \nPrecio actual: ${priceSlp}", 15, True, 5)
                pywhatkit.sendwhatmsg_instantly("+5492324526219", f"El SLP subió a 0.10! \nPrecio actual: ${priceSlp}", 15, True, 5)
                pywhatkit.sendwhatmsg_instantly("+5491141692701", f"El SLP subió a 0.10! \nPrecio actual: ${priceSlp}", 15, True, 5)
                print("Mensaje Enviado")
                time.sleep(1800)
            except:
                print("Ocurrio Un Error")
                time.sleep(5)
    else:
        time.sleep(300)

    

