print ('BEM VINDO A SUA CALCULADORA!!!!!!')

n1 = int(input('Digite seu primeiro numero: '))
n2 = int(input('Digite seu segundo numero: '))


opereção = input('''
        Escolha a operação que deseja realizar
        + para adição
        - para subtração
        * para multiplicação
        / para divisão
          ''')


# Adição

if opereção == '+':
    print(n1+n2)

# Subtração

elif opereção == '-':
    print(n1-n2)

# Multiplicação

elif opereção == '*':
    print(n1*n2)

# Divisão

elif opereção == '/':
    print(n1/n2)

else: ('Você não selecionou um operador valido.... ')