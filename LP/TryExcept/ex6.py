import datetime as dt
try:
    agora = dt.datetime.now()
    datanasc = dt.datetime.strptime(input("Digite sua data de nascimento no formato dd/MM/yyyy: "), "%d/%m/%Y")
    dias = (agora - datanasc).days
    if dias < 0:
        raise ValueError
    print(f"Voce tem {int(dias / 365)} anos.")
except ValueError:
    print("Valor invalido ou data de nascimento maior que a data atual.")