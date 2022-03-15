# import
import pandas as pd

tabelaElfico = pd.read_excel('elfi2.xlsx')
ptInput = input("Insira a palavra em portugues: ")

if(tabelaElfico['Port'] == ptInput).any():
    linha = tabelaElfico['Port'] == ptInput
    outElfi = tabelaElfico.loc[linha, 'Elfi'].values[0]
    print(f"{ptInput} em elfico é {outElfi}")

else:
    print("Erro de digitação ou a palavra desejada não existe no banco de dados")




