genero = input('Qual seu genero?')
idade = int(input('Qual sua idade?'))
tempotrabalho = int(input('Qual o seu tempo trabalhado?'))

a = (genero == 'feminino' and idade > 59) or (genero == 'masculino' and idade > 64)
b = tempotrabalho > 30
c = idade >= 60 and tempotrabalho >= 25
aposentar = a or b or c
print (a, b, c, aposentar)