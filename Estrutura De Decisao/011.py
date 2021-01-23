# 11.	As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
# desenvolver o programa que calculará os reajustes.
# o	Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# o	salários até R$ 280,00 (incluindo) : aumento de 20%
# o	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# o	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# o	salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o	o salário antes do reajuste;
# o	o percentual de aumento aplicado;
# o	o valor do aumento;
# o	o novo salário, após o aumento.
def salario():
    sal = float(input('Digite o salario: '))
    if sal <= 200:
        nov_sal = sal + (sal * 0.2)
        tx = 20
    elif sal < 700:
        nov_sal = sal + (sal * 0.15)
        tc = 15
    elif sal < 1500:
        nov_sal = sal + (sal * 0.1)
        tx = 10
    else:
        nov_sal = sal + (sal * 0.1)
        tx = 10

    almento = nov_sal - sal
    print(f'''Salario anterior - R$ {sal:.2f}
          Percentual de aumento - {tx}%
          Valor do aumento - R$ {almento:.2f}
          Novo salário - R$ {nov_sal:.2f}''')

if __name__=='__main__':
    salario()