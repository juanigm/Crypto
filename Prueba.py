import pywhatkit
# Usamos Un try-except
try:
  # Enviamos el mensaje
  pywhatkit.sendwhatmsg("phonenumber",  
                        "Mensaje De Prueba",
                        10,00)
  print("Mensaje Enviado")
  
except:
  print("Ocurrio Un Error")