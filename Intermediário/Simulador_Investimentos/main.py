# Importando Bibliotecas:
import pandas as pd
import matplotlib.pyplot as plt

# Calculando Juros Simples:
def calculate_simple_interest(principal,rate,time):
    return principal*(1+rate*time)

# Calculando Juros Compostos:
def calculate_compound_interest(principal,rate,time):
    return principal*(1+rate)**time

# Simulador de Investimentos:
def investment_simulator(principal,rate,months):
    rate/=100
    data = {
        'Month': list(range(1,months+1)),
        'Simple Interest': [],
        'Compound Interest': []
    }

    # Calculando Rendimentos Por Mês:
    for month in data['Month']:
        simple = calculate_simple_interest(principal, rate, month)
        compound = calculate_compound_interest(principal, rate, month)
        data['Simple Interest'].append(simple)
        data['Compound Interest'].append(compound)
    df = pd.DataFrame(data)
    print(df)

    # Criando o gráfico:
    plt.figure(figsize=(10, 6))
    plt.plot(df['Month'], df['Simple Interest'], label='Juros Simples', marker='o')
    plt.plot(df['Month'], df['Compound Interest'], label='Juros Compostos', marker='o')
    plt.title('Crescimento do Investimento ao Longo do Tempo')
    plt.xlabel('Meses')
    plt.ylabel('Montante (R$)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Configurando Main
if(__name__=='__main__'):
    print('=== Investment Simulator ===')
    principal = float(input('Enter the value initial: R$'))
    rate = float(input('Enter the tax of interest monthly: %'))
    months = int(input('Enter the time of investment[month]: '))
    investment_simulator(principal, rate, months)