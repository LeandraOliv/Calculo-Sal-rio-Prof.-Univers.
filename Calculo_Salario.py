"""
Programa: Calculo de salário de professor.
Descrição: Calcule o salário de um professor horista na Universidade XYZ. O programa deve perguntar o número de horas trabalhadas, calcular e imprimir na tela o valor do salário bruto,
do salário líquido e do total de descontos, sabendo que o desconto do imposto é 30% e que o valor da hora-aula é R$ 40,00.
Autor: Leandra Arruda de Oliveira
Data: 27/02/2025
Versão: 0.0.1
"""

# Alocação de memória

horas_trabalhadas = 0
valor_hora_aula = 0
valor_impostos = 0
salario_bruto = 0
salario_liquido = 0
total_dos_descontos = 0
resultado = 0


# Entrada de dados
horas_trabalhadas = ""
frase_1 = ""


#Processamento de dados
valor_hora_aula = 40
horas_trabalhadas = float(input("\nQuantas horas você trabalhou?: "))
valor_impostos = 70/100
resultado_1 = salario_bruto = horas_trabalhadas * valor_hora_aula
resultado_2 = salario_liquido = salario_bruto * valor_impostos
resultado_3 = total_dos_descontos = salario_bruto - salario_liquido


# Saída de dados
print(f"Seu salário bruto é R$ {resultado_1} ")
print(f"Seu salário liquido é R$ {resultado_2}")
print(f"O total de descontos deu R$ {resultado_3}") 


