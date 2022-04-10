import pywhatkit
# Usamos Un try-except
try:
  # Enviamos el mensaje
  pywhatkit.sendwhatmsg("+542324476498",  
                        "Mensaje De Prueba",
                        10,00)
  print("Mensaje Enviado")
  
except:
  print("Ocurrio Un Error")