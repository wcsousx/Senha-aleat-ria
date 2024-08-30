from random import choice
import string

tamanhoSenha = int(input('Quantos dígitos você quer? '))
caracteres = string.ascii_letters + string.digits + string.punctuation 
senhaSegura = ''

for i in range(tamanhoSenha):
    senhaSegura += choice(caracteres)

print("A senha gerada é:", senhaSegura)  
