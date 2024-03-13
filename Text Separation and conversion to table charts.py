import pandas as pd
import os

# Instructions
print("\n",
    "This code can transform texts into table charts", 
      "\n", "as long as the data is separeted in an organized way.", 
      "\n", "To do so, you can chose between: pasting a text directly",
      "\n", "here, opening a .csv file or opening a .txt file. If you", 
      "\n", "chose a file (.csv or .txt), use its entire path instead",
      "\n", "of just its name.")

# Alters the directory python will work on (and saves your file)
SavePath = input("Before we start, insert the path you want to save the final table chart: ")
os.chdir(SavePath)

option = input("Type 'paste', to paste a typed text, 'csv' to open a .csv file or 'txt' to open a .txt file: ")

# Procedures to separate pasted text and .txt files
def SeparaTextos(Text):
    RowSeparator = input("Insert the row separator of you text: ")
    ColumnSeparator = input("Insert the column separator of you text: ")

    Text = Text.split(RowSeparator)


    if ColumnSeparator != RowSeparator:

        # In each row, data will be separated into a list and this list is added to another list
        data = []
        i = 0
        while i < len(Text):
            NewRow = Text[i].split(ColumnSeparator)
            data.append(NewRow)
            i += 1

        # Finds the size of the longest row
        size = []
        for d in data:
            size.append(len(d))
        size = max(size)

        # Names the columns, based on the size of the biggest one
        i = 1
        Columns = []
        while i <= size:
            Columns.append(i)
            i += 1
    
    else:
        print("Seems like the row separator and the column separators are the same ")
        nCol =  input("To create a table chart, you'll need to inform the number of columns it'll have ")
        nCol = int(nCol)

        data = []
        row = []
        n = 1
        for i in Text:
            if n/nCol > 1: # If the element is in a position beyond the determined number of columns, it'll skip to the next row
                data.append(row)
                row = []
                n = 2
                row.append(i)
            elif i == Text[-1]: # If the element is the last one, it and its row will be added before the end of the loop
                row.append(i)
                data.append(row)
            else:
                row.append(i)
                n += 1
        
        # Names the columns based in the number of columns informed
        i = 1
        Columns = []
        while i <= nCol:
            Columns.append(i)
            i += 1
        
        # Allows user to name the columns created
        NameOrNot = input("Type 'Y' if you wish to name the columns: ")

        if NameOrNot == 'Y':
            Names = []
            for i in Columns:
                print("Write the name of the column number" , i, ":")
                a = input()
                Names.append(a)
            Columns = Names
        
    return pd.DataFrame(data = data, columns = Columns)

match option:   # Analisis of the user choice
    case "paste":
        Text = input("Type/Paste the text to be separated: ")

        Chart = SeparaTextos(Text)

        Chart.to_excel("Separated Text.xlsx")
        
        print("The separation process went successfully!")

    case "csv":
        file = input("Insert the path/csv file name you want to convert: ")
        Chart = pd.read_csv(file, encoding='unicode_escape')
        Chart.to_excel("csv Table Chart.xlsx")
        print("The separation process went successfully!")

    case "txt":
        file = input("Insert the path/txt file name you want to convert: ")
        
        with open(file, 'r') as Txt:
            Text = Txt.read()

        Chart = SeparaTextos(Text)

        Chart.to_excel("Txt file separated.xlsx")
        print("The separation process went successfully!")