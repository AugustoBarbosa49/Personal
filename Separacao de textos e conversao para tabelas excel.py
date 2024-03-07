import pandas as pd
import os

print("\n",
    "Este código consegue transformar textos em tabelas", 
      "\n", "desde que esses dados estejam separados de maneira organizada", 
      "\n", "e para isso você pode escolher colar um texto, abrir um arquivo", 
      "\n",  ".csv ou ainda um arquivo .txt.",
      "\n", "No caso de arquivos (.csv ou .txt), por garantia, procure utilizar",
      "\n", "o local exato dos arquivos e não apenas o nome dele.",
      "\n", "A fim de evitar possíveis erros, para as opções de colar um texto",
      "\n", "e arquivos .txt, as colunas serão automaticamente entituladas com ",
      "\n", "números inteiros começando em 1.",
      "\n")

localSalvar = input("Antes de começar, insira o local de seu computador onde quer que a planilha seja salva: ")
os.chdir(localSalvar)

opcao = input("Digite 'texto' para colar um texto próprio, 'csv' para, usar um aquivo .csv ou 'txt' para usar um arquivo .txt: ")

def SeparaTextos(Texto):
    separadorLinhas = input("Insira o separador que divide as linhas do texto: ")
    separadorColunas = input("Insira o separador que divide as colunas do texto: ")

    Texto = Texto.split(separadorLinhas)


    if separadorColunas != separadorLinhas:

        dados = []
        i = 0
        while i < len(Texto):
            NovaLinha = Texto[i].split(separadorColunas)
            dados.append(NovaLinha)
            i += 1

        tamanho = []
        for d in dados:
            tamanho.append(len(d))
        tamanho = max(tamanho)

        i = 1
        Colunas = []
        while i <= tamanho:
            Colunas.append(i)
            i += 1
    
    else:
        print("Parece que o separador de linhas e das colunas no seu texto são os mesmos")
        nCol =  input("Para que possamos criar a tabela, você precisará informar o número de colunas que a planilha: ")
        nCol = int(nCol)

        dados = []
        linha = []
        n = 1
        for i in Texto:
            if n/nCol > 1:
                dados.append(linha)
                linha = []
                n = 2
                linha.append(i)
            elif i == Texto[-1]:
                linha.append(i)
                dados.append(linha)
            else:
                linha.append(i)
                n += 1

        i = 1
        Colunas = []
        while i <= nCol:
            Colunas.append(i)
            i += 1
        
    return pd.DataFrame(data=dados, columns = Colunas)

match opcao:
    case "texto":
        Texto = input("Insira o texto a ser separado: ")

        Tabela = SeparaTextos(Texto)

        Tabela.to_excel("Texto Separado.xlsx")
        
        print("A separação ocorreu com sucesso!")

    case "csv":
        arquivo = input("Insira o local/nome do arquivo csv que deseja converter: ")
        Tabela = pd.read_csv(arquivo, encoding='unicode_escape')
        Tabela.to_excel("csv Transformado.xlsx")
        print("A separação ocorreu com sucesso!")

    case "txt":
        arquivo = input("Insira o local / nome do arquivo txt que quer converter: ")
        
        with open(arquivo, 'r') as Txt:
            Texto = Txt.read()

        Tabela = SeparaTextos(Texto)

        Tabela.to_excel("Dados txt separados.xlsx")
        print("A separação ocorreu com sucesso!")