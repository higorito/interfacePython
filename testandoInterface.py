from optparse import Values
import PySimpleGUI as sg

class Tela:
    def __init__(self):
        layout = [
            [sg.Text('Nome',size=(6,0)),sg.Input(size=(10,0),key='nome'),sg.Text('Idade',size=(6,0)),sg.Input(size=(10,0),key='idade')], #aq ta criando o nome e label  //size é o tamanho q vai utilizar na linha
            
            #criando box
            [sg.Text('Selecione os e-mails.')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook')],
            [sg.Text('Aceita Cartão')],
            [sg.Radio('Sim','cartoes',key='aceitaCartao'),sg.Radio('Não','cartoes',key='naoAceitaCartao')],
            [sg.Button('Enviar Dados')],
            [sg.Slider(range=(0,100),default_value=0,orientation='h',size=(25,15),key='sliderVel')],
            [sg.Output(size=(40,10))]
        ]
        #self.janela foi para mante-la aberta
        self.janela = sg.Window("Dados Usuario").layout(layout)
        
    
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            #para acessar e classificar os dados é necessario a key ali em cima e esses sel.values com o nome da key
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            vel_media = self.values['sliderVel']


            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'Aceita Cartao: {aceita_cartao}')
            print(f'Velocidade media: {vel_media}')

tela = Tela()
tela.Iniciar()