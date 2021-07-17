from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ('Arial', '10')
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer['pady'] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text='Digite algo: ')
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Impressão de texto", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)


        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Imprimir"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificarSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def verificarSenha(self):
        texto = self.nome.get()
        self.mensagem['text'] = texto


root = Tk()
Application(root)
root.mainloop()
