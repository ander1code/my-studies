from tkinter import *

#tkinter = Tk Interface. N�o faz parte do Python.
#N�o recomendado para o uso no mercado. Possui poucos recursos.

#widget -> qualquer parte do projeto grafico. 
#container -> Onde est� os widgets do projeto.
#       container possui widgets.

#top-level window -> Janela que se sobrep�e.
#frame -> Organiza��o de uma janela.
#child-parent -> widget dentro de um container (por exemplo).
#parent-child -> container possui widgets (por exemplo).

janela = Tk()
Label(janela, text='Hello, World!').pack()
janela.mainloop()