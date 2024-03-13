import pandas as pd
import os

# Instruções inciais
print("\n",
    "Este código consegue transformar textos em tabelas,", 
      "\n", "desde que esses dados estejam separados de maneira organizada.", 
      "\n", "Para isso você pode escolher colar um texto, abrir um arquivo", 
      "\n",  ".csv ou ainda um arquivo .txt.",
      "\n", "No caso de arquivos (.csv ou .txt), por garantia, procure utilizar",
      "\n", "o local exato dos arquivos e não apenas o nome dele.")

# Altera o local onde o python vai trabalhar
localSalvar = input("Antes de começar, insira o local de seu computador onde quer que a planilha seja salva: ")
os.chdir(localSalvar)

opcao = input("Digite 'colar' para colar um texto próprio, 'csv' para, usar um aquivo .csv ou 'txt' para usar um arquivo .txt: ")

# Procedimentos para separação de textos e arquivos .txt
def SeparaTextos(Texto):
    separadorLinhas = input("Insira o separador que divide as linhas do texto: ")
    separadorColunas = input("Insira o separador que divide as colunas do texto: ")

    Texto = Texto.split(separadorLinhas)


    if separadorColunas != separadorLinhas:

        # Para cada linha,  os dados serão separados em uma lista e essa lista é adicionada a outra lista
        dados = []
        i = 0
        while i < len(Texto):
            NovaLinha = Texto[i].split(separadorColunas)
            dados.append(NovaLinha)
            i += 1

        # Descobre o tamanho da maior linha
        tamanho = []
        for d in dados:
            tamanho.append(len(d))
        tamanho = max(tamanho)

        # Nomeia as colunas necessárias, baseado no tamanho da maior linha
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
            if n/nCol > 1: # Se o elemento analisado estiver numa posição além do número de colunas determinadas, a linha será pulada para a próxima
                dados.append(linha)
                linha = []
                n = 2
                linha.append(i)
            elif i == Texto[-1]: # Se o elemento analisado for o último da lista ele e sua linha serão adicionados aos dados antes do fim da repetição
                linha.append(i)
                dados.append(linha)
            else:
                linha.append(i)
                n += 1

        # Nomeia as colunas baseada no número fornecido
        i = 1
        Colunas = []
        while i <= nCol:
            Colunas.append(i)
            i += 1

    # Permite o usuário nomear as colunas criadas  
    nomear = input("Escreva 'S' se deseja nomear as colunas da tabela: ")

    if nomear == 'S':
        nomes = []
        for i in Colunas:
            print('Digite o nome da coluna número ', i, ":")
            a = input()
            nomes.append(a)
        Colunas = nomes

    return pd.DataFrame(data=dados, columns = Colunas)

match opcao:    # Análise das opção escolhida pelo usuário
    case "colar":
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