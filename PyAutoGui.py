import pyautogui
from time import sleep

pyautogui.PAUSE = 0.2 # Define um tempo de espera entre os comandos dados através da 'pyautogui'

# Define as funções

# Procura a imagemt na tela e clica nela
def procurar_imagem (foto):
    # Leva o mouse para o canto da tela para não atrapalhar
    # a identificação por imagem do programa
    pyautogui.moveTo(1, 1)
    sleep(0.5)

    # Procura a imagem indicada 7 vezes aquardando o computador
    # terminar de carregar a interface gráfica do programa
    for i in range(7):
        try:
            pyautogui.click(foto)
            return
        except:
            sleep(1)

    # Se a imagem não for encontrada retorna uma mensagem de erro
    pyautogui.alert(text='Erro: ' + foto + ' não encontrado', title='Erro ao procurar imagem', button='OK')  
    exit()

# Procura a imagem na tela com o scroll do mouse e clica nela
def procurar_com_scroll (foto):
    for i in range(10):
        try:
            pyautogui.click(foto)
            return
        except:
            pyautogui.scroll(-500)
            sleep(0.5)
    
    # Se a imagem não for encontrada retorna uma mensagem de erro
    pyautogui.alert(text='Erro: ' + foto + ' não encontrado', title='Erro ao procurar imagem usando o scroll do mouse', button='OK')  
    exit()

# Executa o Spotify pelo Menu Iniciar
pyautogui.press(['win'])
pyautogui.write('Spotify')
pyautogui.press(['return'])

# Aguarda o Spotify abrir e o coloca em tela cheia
sleep(3)
pyautogui.hotkey('win', 'up')
sleep(1)

# Clica em 'Buscar'
procurar_imagem('icone_buscar.png')

# Procura "Iron Maiden"
sleep(0.5) # Delay para aguardar o processamento do computador
pyautogui.write('Iron Maiden')
pyautogui.press(['return'])

# Clica em 'Iron Maiden'
procurar_imagem('Iron_Maiden_Titulo.png')

# Procura a Discografia
sleep(1)
procurar_com_scroll('Iron_Maiden_Discografia.png')

# Procura o Disco 'Piece of Mind'
sleep(1)
procurar_com_scroll('Iron_Maiden_Disco.png')

# Procura a música 'To Tame a Land' e a coloca para tocar
sleep(1)
procurar_com_scroll('Iron_Maiden_Musica.png')
pyautogui.click() # Simula o duplo clique para colocar a musica para tocar

# Tira uma screenshot da tela
pyautogui.screenshot('Screenshot_Musica.png')

# Fecha o programa
exit()



