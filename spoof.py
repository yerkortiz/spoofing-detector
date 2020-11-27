"""
Este script envía un email usando un alías, pese a que
no suplanta totalmente al emisor en el header, es otra
forma de spoofing, notese que también es detectada por
el detector de spoofing.
"""
import yagmail
import os
import getpass
#from yagmail.headers import make_addr_alias_user
#from pprint import pprint
def userData():
    email = input('Email:')
    password = getpass.getpass('Password:')
    return email, password
def senser
sender_email, password = userData()
file = open('codeforces.html', 'r')
sender_alias='noreply@codeforces.com'
receptor_email = 'receptor@mail.com'
yag=yagmail.SMTP({sender_email:sender_alias}, password) 
yag.send(receptor_email, 'Codeforces Round 684', file.read())
file.close()
