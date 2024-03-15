def calcular_energia_calibre(massa, velocidade):
    # Fórmula: Ec = (m.v²)/30860 *Sistema métrico*
    energia = (massa * velocidade**2) / 30860
    return energia

def arredondar_resultado(energia_calibre):
    # Arredonda o resultado para X casas decimais, usei zero neste script
    return round(energia_calibre, 0)

# Entrada do usuário para massa e velocidade
massa = float(input("Digite a massa do projetil em grains: "))
velocidade = float(input("Digite a velocidade do projetil em m/s: "))

# Chamada da função para calcular a energia
energia_calibre = calcular_energia_calibre(massa, velocidade)

# Chamada da função para arredondar o resultado
energia_calibre_arredondada = arredondar_resultado(energia_calibre)

# Exibição do resultado usando uma f-string
print(f"A energia deste calibre é: {energia_calibre_arredondada} joules")