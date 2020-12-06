#Ejercicio
# Atbash Cipher Tool
def rubiencrypt(cadena):
    outText = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    #iteramos las letras en la cadena
    for letter in cadena:
        # si es mayuscula
        if letter in uppercase:
            # obtenemos el indice de donde esta en la lista de las mayusculas
            index = uppercase.index(letter)
            # Segun donde esta buscamos la posicion negativa ya que es su lado contrario 
            crypting = (-(index+1)) % 26
            # a nuestro resultado le agregamos lo encriptado
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        # si es minuscula
        elif letter in lowercase:
            # obtenemos el indice de donde esta en la lista de las mayusculas
            index = lowercase.index(letter) 
            # Segun donde esta buscamos la posicion negativa ya que es su lado contrario 
            crypting = (-(index+1)) % 26
            # a nuestro resultado le agregamos lo encriptado            
            newLetter = lowercase[crypting]
            outText.append(newLetter)
        elif letter ==" ":
          outText.append(" ")
    return outText

def printresult(resultado):
  text='';
  for i in resultado:
    text+=i
  return text
code = rubiencrypt(input("Escribe la cadena a encriptar:\t"))

print("Mensaje Encriptado:\t"+printresult(code))