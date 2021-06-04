from openpyxl import Workbook

# Cria a planilha
arquivo = Workbook()
aba1 = arquivo.worksheets[0]
aba1.title = 'Aba 1'

# Coloca os valores nas celulas 'A1', 'A2', 'A3', 'A4' e 'A5'
for i in range(5):
    aba1[f'A{ i + 1 }'] = i + 1

# Coloca a célula que soma os valores
aba1[f'A6'] = '=SUM(A1:A5)'

# Salva o arquivo
arquivo.save('Openpyxl\Planilha.xlsx')

# Cria e renomeia uma nova aba
aba2 = arquivo.create_sheet()
aba2.title = 'Aba 2'
aba2['C3'] = 'Teste 123'

# Salva o arquivo para sobrescrever as mudanças
arquivo.save('Openpyxl\Planilha.xlsx')

