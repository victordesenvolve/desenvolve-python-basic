while True:
 numero = input("Informe seu número de celular: ")
 
 if len(numero) == 8 and numero.isdigit():
    numero_novo = '9' + numero
    numero_formatado = numero_novo[:5] + '-' + numero_novo[5:]
    print("Seu Número é:", numero_formatado)
    break
 if len(numero) == 9 and numero[0] == 9:
     numero_formatado = numero[:5] + '-' + numero[5:]
     print("Seu número é: ", numero_formatado)
     break
 else:
    print("Informe um número valido com oito ou nove digitos, que começe comm '9.")
  



   
    



   