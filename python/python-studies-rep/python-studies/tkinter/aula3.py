import tkinter

janela = tkinter.Tk()

#T�tulo da janela:
janela.title('Sistema de Cadastro 2.0')

#Modificando a cor da janela:
janela['bg'] = 'green'

#Modificando o tamanho da janela:
#janela.geometry('300x300')
#janela.geometry('+100+100')
janela.geometry('300x300+100+100')

#fica executando o loop infinito para detectar qualquer
#mudan�as na janela.

janela.mainloop()

#Pesquisar como trabalhar somente com "Single Instance".