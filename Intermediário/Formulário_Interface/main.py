import PySimpleGUI as sg

class Window:
    def __init__(self):
        layout = [
            [sg.Text('Nome'),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade'),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita cartão?')],
            [sg.Radio('Sim','cartões',key='accept_card'),sg.Radio('Não','cartões',key='no_accept_card')],
            [sg.Slider(range=(0,100),default_value=0,orientation='h',size=(15,20),key='slider_speed')],
            [sg.Button('Enviar')],
            [sg.Output(size=(30,10))]
        ]
        self.window = sg.Window('Dados do Usuário').layout(layout)
    def start(self):
        while True:
            self.button, self.values = self.window.Read()
            if self.button is None:
                break
            nome = self.values['nome']
            idade = self.values['idade']
            accept_gmail = self.values['gmail']
            accept_outlook = self.values['outlook']
            accept_yahoo = self.values['yahoo']
            accept_card = self.values['accept_card']
            no_accept_card = self.values['no_accept_card']
            speed_script = self.values['slider_speed']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita gmail: {accept_gmail}')
            print(f'Aceita Outlook: {accept_outlook}')
            print(f'Aceita Yahoo: {accept_yahoo}')
            print(f'Aceita Cartão: {accept_card}')
            print(f'Não Aceita Cartão: {no_accept_card}')
            print(f'Velocidade Scripts: {speed_script}')
screen = Window()
screen.start()