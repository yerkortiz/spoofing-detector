import getpass
import imaplib
import re
import os
"""
    La entrada de getMsgID:
    el email del usuario, su contraseña, el email del emisor
    y el servicio de host del mail del usuario, 
    que por defecto esta con gmail.
    La salida de la función es la lista de todos los message ID
    de los mails recibidos por el usuario receptor, 
    que han sido enviados por el mail emisor.
"""
def getMsgId(user_email, password, sender, host = 'imap.gmail.com'):
    email = imaplib.IMAP4_SSL(host)
    email.login(user_email, password)
    email.select('INBOX')
    typ, data = email.search(None, 'FROM ' + sender)
    id_list = []
    for x in data[0].split():
        typ, data = email.fetch(x, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
        msgId = data[0][1].decode('UTF-8')[12:].replace('<', '').replace('>', '').replace("\n","").replace("\r","")
        print(msgId)  
        id_list.append(msgId)
    return id_list

"""
    checkIdList recibe como entrada una lista de message ID y
    una expresión regular, por defecto tiene una regex que acepta
    muchos posibles msg ID, retorna true si y solo si todos los ID
    hacen match con la expresión regular, retorna false para
    el caso complementario
"""
def checkIdList(id_list, reg_exp = '^[0-9a-z\.A-Z\@\-\_]{1,100}$'):
    for x in id_list:
        if(not re.match(reg_exp, x)):
            print('Este es un message-id enviado por un emisor potencialmente falso\n', x)
            return False
    return True

"""
    importData lee un archivo que contiene el email emisor
    y su correspondiente expresion regular, tanto el email como
    expresión regular deben usar una única linea en el archivo,
    de lo contrario no se podrán importar correctamente.
"""
def importData(filename ='sender_data.txt', path=os.getcwd()):
    file = open(path+filename, 'r')
    l = []
    for x in file:
        l.append(x.replace('\n', ''))
    reg_exp = ""
    for x in l[1:]:
        reg_exp += x
    return l[0], reg_exp

"""
    userData permite leer los datos del usuario, su email, password
    y el host correspondiente.
"""
def userData():
    email = input('Email:')
    password = getpass.getpass('Password:')
    return email, password
#nota: para variar de sender_data, en import data cambiar nombre
# al archivo que se abre.
if __name__ == "__main__":
    filename = '/sender_data.txt'
    sender, reg_exp = importData(filename)
    email, password = userData()
    host = 'imap.gmail.com' 
    
    id_list = getMsgId(email, password, sender, host) 
    if checkIdList(id_list, reg_exp):
        print("Todos los message id hacen match con la expresion: \n", reg_exp)
    else:
        print("Hay por lo menos un mensaje falso")
    
