import pyautogui 
import time

#passo 1 entrar no site
pyautogui.PAUSE=0.5
pyautogui.press("win") # apertar a teclado windowns
pyautogui.write("brave") # acessar o navegador
pyautogui.press("enter") # apertar para confirmar



#passe 2 fazer login

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # endereço de acesso
pyautogui.press("enter")
time.sleep(3) # pause para frear o carregamento do codigo em si contra a pagina
pyautogui.click(x=496, y=402) # positição criada atraves do arquivo auxiliar pra determinar posição mouse
pyautogui.write("cassiosp1504@gmail.com")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.click(x=442, y=505)
pyautogui.write("1234")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)


# passo 3 importar a base de dados com pandas (pip install pandas no terminal)

import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)


# passo 4 cadastrar produto



# para cada lliha executar todos estes comandos

for linha in tabela.index:
    pyautogui.click(x=423, y=288)  # selecionar o campo de produto
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")


    # selecionar marca do produto com import da planilha da base dados

    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")


    # selecionar tipo do produto   com import da planilha da base dados

    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo)) 
    pyautogui.press("tab")


    # selecionar categoria com import da planilha da base dados

    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))  
    pyautogui.press("tab")


    # selecionar preço unitario dp custo do produto  com import da planilha da base dados

    preco = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco))  
    pyautogui.press("tab")


    # custo do produto  com import da planilha da base dados

    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))  
    pyautogui.press("tab")



    # selecionar observação com import da planilha da base dados

    obs = tabela.loc[linha,"obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))       
    pyautogui.press("tab")


    # enter para enviar as informaçoes ao banco de dados do site

    pyautogui.press("enter")

    # levar a tela pra cima

    pyautogui.scroll(5000)























