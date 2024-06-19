n1 = int(input())
n2 = int(input())
n3 = int(input())

m = (n1+n2+n3)/3

if m>=60:
    print("Aprovado"    )
elif m>=40 and m < 60:
    print ("Recuperação")
elif m< 40:
    print("Reprovado")    
