#1 =============================================================================
INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1 
    SOMA = SOMA + K  

print(SOMA)


#2 =============================================================================
def pertence_fibonacci(numero):

    if numero < 0:
        return False

    a, b = 0, 1

    if numero == a or numero == b:
        return True
    
    while b < numero:
        a, b = b, a + b
        if b == numero:
            return True
    return False

def main1():
    try:
        numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        
        if pertence_fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
    
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main1()


#3 =============================================================================
import json

def carregar_dados(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data['faturamento_diario']

def calcular_menor_maior_faturamento(dados):
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    menor = min(valores)
    maior = max(valores)
    return menor, maior

def calcular_media_mensal(dados):
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    if not valores:
        return 0
    media = sum(valores) / len(valores)
    return media

def contar_dias_acima_media(dados, media):
    dias_acima_media = sum(1 for dia in dados if dia['valor'] > media)
    return dias_acima_media

def main2():
    dados = carregar_dados('faturamento.json')

    menor, maior = calcular_menor_maior_faturamento(dados)
    print(f"Menor valor de faturamento: {menor}")
    print(f"Maior valor de faturamento: {maior}")

    media = calcular_media_mensal(dados)
    print(f"Média mensal de faturamento: {media:.2f}")
    
    dias_acima_media = contar_dias_acima_media(dados, media)
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

if __name__ == "__main__":
    main2()


#4 =============================================================================
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

def calcular_percentuais(faturamento):
    total = sum(faturamento.values())
    
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
    
    return total, percentuais

def main3():
    total, percentuais = calcular_percentuais(faturamento)

    print(f"Valor total de faturamento: R${total:.2f}")
    
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main3()


#4 =============================================================================
def inverter_string(s):
    resultado = ''
    
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    
    return resultado

def main4():
    entrada = input("Digite uma string para inverter: ")

    string_invertida = inverter_string(entrada)
    
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main4()