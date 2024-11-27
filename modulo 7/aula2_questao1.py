
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]


data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data_nascimento.split("/")


mes_nome = meses[int(mes) - 1]


print(f"Você nasceu no dia {dia} de {mes_nome} de {ano}.")
