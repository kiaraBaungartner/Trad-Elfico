# input do mes em pt
# ler as tabelas
# ver qual mes bate cm ele
# transformar o mes em pt para elf

# import
import pandas as pd

tabelaElfico = pd.read_excel('elfi2.xlsx')
ptInput = input("Insira a palavra em portuges: ")

#print(tabelaElfico)

if(tabelaElfico['Port'] == ptInput).any():
    linha = tabelaElfico['Port'] == ptInput
    outElfi = tabelaElfico.loc[linha, 'Elfi'].values[0]
    print(f"{ptInput} em elfico é {outElfi}")

else:
    print("Erro de digitação ou a palavra desejada não existe no banco de dados")




