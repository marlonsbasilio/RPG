# Importações de bibliotecas
import os
import re
from tkinter import Frame
from typing import List
from personagem import Personagem
from conta import Conta
from arquivo import Arquivo
# from tkinter import *
import customtkinter
from dataclasses import dataclass
from PIL import Image

# Classe responsável por unir todas as outras e também de chamar a função main()
@dataclass
class ContaDTO:
    username: str
    password: str
    chars: List[Personagem]

class Jogo:
    
    def __init__(self):
        self.__contas = Arquivo().leituraContas()
    
    def getContas(self):
        return self.__contas
    
    def setContas(self,novas_contas):
        self.__contas = novas_contas
    
    # Função responsavel por inserir uma conta no jogo
    def insereConta(self,usuario,senha):
        # Cria uma conta com a lista de personagens vazia e adiciona no vetor de contas
        nova_conta = Conta(usuario,senha,list())
        self.getContas().append(nova_conta)
        # Salva o arquivo da conta
        Arquivo().salvarConta(nova_conta)
    
    # Função responsavel por deletar uma conta no jogo
    def excluiConta(self,indice):
        # Deleta o arquivo da conta
        Arquivo().deletarConta(self.getContas()[indice])
        # Deleta a conta do vetor de contas
        del(self.getContas()[indice])
    
    def visualizaConta(self,indice):
        return self.getContas()[indice]
    
    # Função responsável por inserir um Personagem no jogo
    def inserePersonagem(self,apelido,classe,indice):
        usuario = self.getContas()[indice].getUsuario()
        # Cria um novo objeto do tipo personagem, insere ele na conta especifica do programa e salva seu arquivo
        novo_personagem = Personagem(usuario,apelido,classe)
        self.getContas()[indice].getPersonagens().append(novo_personagem)
        Arquivo().salvarPersonagem(novo_personagem,self.getContas()[indice])
    
    # Função responsável por deletar um personagem do jogo
    def excluiPersonagem(self,apelido,indice):
        # Deleta o arquivo do personagem e trata o arquivo conta dele
        Arquivo().deletarPersonagem(self.getContas()[indice[0]].getPersonagens()[indice[1]])
        # Deleta o personagem do vetor de contas
        del(self.getContas()[indice[0]].getPersonagens()[indice[1]])
    
    def visualizaPersonagem(self,indice):
        return self.getContas()[indice[0]].getPersonagens()[indice[1]]
    
    # Função responsável por verificar se uma conta específica existe no vetor de contas
    def verificaConta(self,usuario):
        contas = self.getContas()
        # Condição se o nome da conta é válido
        if re.search(';', usuario): return -2
        if re.search(',', usuario): return -2
        # Percorre todo o vetor de contas procurando uma conta com o mesmo usuario passado pelo parametro
        for i in range(0,len(contas)):
            if(contas[i].getUsuario() == usuario):
                return i # Retorna a posição da conta se encontrar um usuario igual ao parametro
        return -1 # Retorna -1 se não encontrar ninguém
    
    # Função responsável por verificar se um personagem específico existe no vetor de contas
    def verificaPersonagem(self,apelido):
        # Condição se o nome do personagem é válido
        if re.search(';', apelido): return -2
        if re.search(',', apelido): return -2
        # Percorre todo o vetor de contas
        for i in range(0,len(self.getContas())):
            # Percorre todo o vetor de personagens de cada conta procurando um apelido igual o passado pelo parametro
            lista_personagens = self.getContas()[i].getPersonagens()
            for j in range(0,len(lista_personagens)):
                if(lista_personagens[j].getApelido() == apelido):
                    vet = [i,j]
                    return vet # Se encontrar o personagem, retorna um vetor com posição da conta e posição do personagem
        return -1 # Se não encontrar retorna -1
    '''def listaContas(self):
        contas = self.getContas()
        for i in range(0,len(contas)):
            return self.getContas()'''
        

class Application(Frame):

    def limpaTela(self):
        list = self.grid_slaves()
        for l in list:
            l.destroy()
            
    def widgetsInserirConta(self):
        self.limpaTela()  
        self.text1 = StringVar()
        self.text2 = StringVar()
        self.nomeLabel = Label(self,text="Nome").grid(row=0)
        self.nome = Entry(self,textvariable=self.text1).grid(row=1)
        self.senhaLabel = Label(self,text="Senha").grid(row=2)        
        self.senha = Entry(self,textvariable=self.text2).grid(row=3)
        self.w1 = Button(self, text="Criar", command = self.iInsereConta).grid(row=4)  
        self.w2 = Button(self, text="Voltar", fg="red", command = self.widgetsMenuConta).grid(row=5)
        
    def iInsereConta(self):
        const = self.jogo.verificaConta(self.text1.get())
        if(const == -1): # Não existe conta com esse nome
            self.jogo.insereConta(self.text1.get(),self.text2.get())
            self.widgetsInserirConta()
            self.nomeLabel = Label(self,fg="blue",text="Conta criada com sucesso!").grid(row=6)
        else:
            self.widgetsInserirConta()
            self.nomeLabel = Label(self,fg="red",text="Essa conta já existe!").grid(row=6) 
        
    def widgetsDeletarConta(self):
        self.limpaTela()  
        self.text1 = StringVar()
        self.nomeLabel = Label(self,text="Nome").grid(row=0)
        self.nome = Entry(self,textvariable=self.text1).grid(row=1)
        self.w1 = Button(self, text="Deletar", command = self.iDeletarConta).grid(row=2)  
        self.w2 = Button(self, text="Voltar", fg="red", command = self.widgetsMenuConta).grid(row=3)
        
    def iDeletarConta(self):
        const = self.jogo.verificaConta(self.text1.get())
        if(const == -1): # Não existe conta com esse nome
            self.widgetsDeletarConta()
            self.nomeLabel = Label(self,fg="red",text="Essa conta não existe!").grid(row=4)
        else:
            self.jogo.excluiConta(const)
            self.widgetsDeletarConta()
            self.nomeLabel = Label(self,fg="blue",text="Conta deletada com sucesso").grid(row=4) 
        
    def widgetsVisualizarConta(self,opcao):
        print(opcao)
        # self.limpaTela()
        # self.text1 = StringVar()
        # self.nomeLabel = Label(self,text="Nome").grid(row=0)
        # self.nome = Entry(self,textvariable=self.text1).grid(row=1)
        # self.w1 = Button(self, text="Visualizar", command = self.iVisualizarConta).grid(row=2)  
        # self.w2 = Button(self, text="Voltar", fg="red", command = self.widgetsMenuConta).grid(row=3)
        
    def iVisualizarConta(self):
        const = self.jogo.verificaConta(self.text1.get())
        if(const == -1): # Não existe conta com esse nome
            self.widgetsVisualizarConta()
            self.nomeLabel = Label(self,fg="red",text="Essa conta não existe!").grid(row=4)
        else:
            self.widgetsVisualizarConta()
            self.nomeLabel = Label(self,text=self.jogo.visualizaConta(const)).grid(row=4) 
        
    def widgetsInserirPersonagem(self):
        self.limpaTela()  
        self.escolha = StringVar()
        self.text1 = StringVar()
        self.text2 = StringVar()
        self.nomeLabel = Label(self,text="Nome").grid(row=0)
        self.nome = Entry(self,textvariable=self.text1).grid(row=1)
        self.contaLabel = Label(self,text="Conta").grid(row=2)        
        self.conta = Entry(self,textvariable=self.text2).grid(row=3)
        escolha1 = Radiobutton(self,text='Mago', value='mago', variable = self.escolha).grid(row=4)  
        escolha2= Radiobutton(self,text='Guerreiro', value='guerreiro', variable = self.escolha).grid(row=5)   
        escolha3 = Radiobutton(self,text='Arqueiro', value='arqueiro', variable = self.escolha).grid(row=6) 
        escolha4 = Radiobutton(self,text='Sacerdote', value='sacerdote', variable = self.escolha).grid(row=7) 
        self.w1 = Button(self, text="Criar", command = self.iInserePersonagem).grid(row=8)  
        self.w2 = Button(self, text="Voltar", fg="red", command = self.widgetsMenuPersonagens).grid(row=9)
        
    def iInserePersonagem(self):
        verificaConta = self.jogo.verificaConta(self.text2.get())
        verificaPersonagem = self.jogo.verificaPersonagem(self.text1.get())
        classe = str(self.escolha.get())
        if(verificaConta == -1): # Não existe a conta onde se deseja armazenar
            self.widgetsInserirPersonagem()
            self.nomeLabel = Label(self,fg="red",text="Essa conta não existe!").grid(row=10)
        else:
            if(verificaPersonagem == -2): # Tem ',' ou ';'
                self.widgetsInserirPersonagem()
                self.nomeLabel = Label(self,fg="red",text="Nome inválido!").grid(row=10)
            elif(verificaPersonagem == -1): # Não existe o personagem
                print(classe)
                self.jogo.inserePersonagem(self.text1.get(),classe,verificaConta)
                self.widgetsInserirPersonagem()
                self.nomeLabel = Label(self,fg="blue",text="Personagem Criado!").grid(row=10)
            else:
                self.widgetsInserirPersonagem()
                self.nomeLabel = Label(self,fg="red",text="Esse nome já existe!").grid(row=10)
                
    def widgetsDeletarPersonagem(self):
        self.limpaTela()  
        self.text1 = StringVar()
        self.nomeLabel = Label(self,text="Personagem").grid(row=0)
        self.nome = Entry(self,textvariable=self.text1).grid(row=1)
        self.w1 = Button(self, text="Deletar", command = self.iDeletaPersonagem).grid(row=2)  
        self.w2 = Button(self, text="Voltar", fg="red", command = self.widgetsMenuPersonagens).grid(row=3)
        
    def iDeletaPersonagem(self):
        verificaPersonagem = self.jogo.verificaPersonagem(self.text1.get())
        if(verificaPersonagem == -1 or verificaPersonagem == -2): # Não existe a conta onde se deseja armazenar
            self.widgetsDeletarPersonagem()
            self.nomeLabel = Label(self,fg="red",text="Esse personagem não existe!").grid(row=4)
        else:
            self.jogo.excluiPersonagem(self.text1.get(),verificaPersonagem)
            self.widgetsDeletarPersonagem()
            self.nomeLabel = Label(self,fg="blue",text="Personagem deletado!").grid(row=4)
        
    def widgetsVisualizarPersonagem(self):
        self.limpaTela()  
        self.text1 = StringVar()
        self.nomeLabel = Label(self,text="Personagem").grid(row=0)
        self.nome = Entry(self,textvariable=self.text1).grid(row=1)
        self.w1 = Button(self, text="Visualizar", command = self.iVisualizaPersonagem).grid(row=2)  
        self.w2 = Button(self, text="Voltar", fg="red", command = self.widgetsMenuPersonagens).grid(row=3) 
        
    def iVisualizaPersonagem(self):
        verificaPersonagem = self.jogo.verificaPersonagem(self.text1.get())
        if(verificaPersonagem == -1 or verificaPersonagem == -2): # Não existe a conta onde se deseja armazenar
            self.widgetsVisualizarPersonagem()
            self.nomeLabel = Label(self,fg="red",text="Esse personagem não existe!").grid(row=4)
        else:
            self.widgetsVisualizarPersonagem()
            self.nomeLabel = Label(self,fg="blue",text=self.jogo.visualizaPersonagem(verificaPersonagem)).grid(row=4)
    
    def widgetsMenuPrincipal(self):
        conta = ContaDTO(username='juniordc159', password='12345',chars=[Personagem(conta='juniordc159',apelido='Char1',classe='Sacerdote'),Personagem(conta='juniordc159',apelido='Char2',classe='Guerreiro'),Personagem(conta='juniordc159',apelido='Char3',classe='Arqueiro'),Personagem(conta='juniordc159',apelido='Char4',classe='Guerreiro'),Personagem(conta='juniordc159',apelido='Char5',classe='Sacerdote')])
        
        image_path = os.path.join(os.path.dirname(__file__), 'gear2.png')
        print(image_path)
        image = customtkinter.CTkImage(dark_image=Image.open(image_path),size=(30,30))
        config_label = customtkinter.CTkButton(self.master, image = image,text='' ,command=self.widgetsVisualizarConta('foi'),width=25,height=25,fg_color='#444444',hover_color='#888888',corner_radius=15)
        config_label.place(relx=1, rely=0, x=-35, y=30, anchor='ne')
        
        user_label = customtkinter.CTkLabel(self.master, text=conta.username,font=("Helvetica",25,"bold"))
        user_label.place(x=30, y=30, anchor='nw')
        select_char_label = customtkinter.CTkLabel(self.master, text='Selecione seu Personagem:',font=("Helvetica",15,"bold"))
        select_char_label.place(x=30, y=100, anchor='nw')
        char_button = customtkinter.CTkButton(self.master, text='Criar Personagem', command=self.widgetsVisualizarConta('foi'),fg_color='#444444',hover_color='#888888',corner_radius=15)
        char_button.place(relx=1, rely=0, x=-25, y=100, anchor='ne')
        # frame_char = customtkinter.CTkFrame(self.master,corner_radius=20,width=540)
        # frame_char.place(x=30,y=145)
        frame_char = customtkinter.CTkScrollableFrame(self.master,corner_radius=20,width=320,height=50)
        frame_char.place(x=30,y=145)
        
        opcao_selecionada = customtkinter.StringVar()
        for i,char in enumerate(conta.chars):
            char_select_button = customtkinter.CTkRadioButton(frame_char,text=f'Nickname: {char.getApelido()}           Classe: {char.getClasse()}',variable=opcao_selecionada,value=char.getApelido())
            char_select_button.pack(padx=20,pady=20)
        fight_button = customtkinter.CTkButton(self.master, text='Batalhar', command=self.widgetsVisualizarConta(opcao_selecionada),fg_color='#900603',hover_color='#A91B0D',corner_radius=50,width=150,height=150)
        fight_button.place(x=570,y=190,anchor='ne')
        
    def widgetsMenuConta(self):
        nome_contas = os.listdir('contas/')
        
        # self.limpaTela()
        # self.w1 = Button(self, text="Voltar", fg="red", command = self.widgetsMenuPrincipal).grid(row=0)
        # self.w2 = Button(self, text="Inserir Conta", command = self.widgetsInserirConta).grid(row=1)        
        # self.w3 = Button(self, text="Deletar Conta", command = self.widgetsDeletarConta).grid(row=2)
        # self.w4 = Button(self, text="Visualizar Conta", command = self.widgetsVisualizarConta).grid(row=3)
        # self.tableLable = Label(self,fg="blue",text="Tabela de Contas").grid(column=1,row=0)
        # for i in range(0,len(nome_contas)):
        #     self.nomeLabel = Label(self,fg="red",text=self.jogo.visualizaConta(i)).grid(column=1,row=1+i)
            
    def widgetsMenuPersonagens(self):
        nome_contas = os.listdir('contas/')
        self.limpaTela()
        self.w1 = Button(self, text="Voltar", fg="red", command = self.widgetsMenuPrincipal).grid(row=0)
        self.w2 = Button(self, text="Inserir Personagem", command = self.widgetsInserirPersonagem).grid(row=1)        
        self.w3 = Button(self, text="Deletar Personagem", command = self.widgetsDeletarPersonagem).grid(row=2)
        self.w4 = Button(self, text="Visualizar Personagem", command = self.widgetsVisualizarPersonagem).grid(row=3)
        self.tableLable = Label(self,fg="blue",text="Tabela de Contas").grid(column=1,row=0)
        for i in range(0,len(nome_contas)):
            self.nomeLabel = Label(self,fg="red",text=self.jogo.visualizaConta(i)).grid(column=1,row=1+i)

    def __init__(self, master=None):
        self.jogo = Jogo()
        self.master = master
        self.widgetsMenuPrincipal()

root = customtkinter.CTk()
root.geometry("600x400")
app = Application(master=root)
root.title('Rpg APS')
root.mainloop()
root.destroy()