import tkinter as tk
import receber_som
import manda_som

class Main():
    def __init__(self):
        self.texto = []
        self.send_click = False
        self.loop = None
        self.send_selected = False
        self.recebe = receber_som.TextGetter(1234)
        self.manda = manda_som.SendText()
        self.window = tk.Tk()
        self.window.title('TrashTalk')
        # self.window.geometry("300x200")
        # self.window.configure(background = 'dim gray')
        self.window.resizable(False, False)

        # self.window.rowconfigure(0)
        # self.window.rowconfigure(1)
        # self.window.rowconfigure(2)
        # self.window.rowconfigure(3)
        
        # self.window.columnconfigure(0)
        # self.window.columnconfigure(1)
        # self.window.columnconfigure(2)
        # self.window.columnconfigure(3)
        self.window.rowconfigure(5, weight=1)
        self.window.columnconfigure(5, weight=1)

        v = tk.IntVar()

        self.rb1 = tk.Radiobutton(self.window, text="Receive", variable=v, value=1, font = ("Monospace",12), command=self.receive)
        self.rb2 = tk.Radiobutton(self.window, text="Send", variable=v, value=2, font = ("Monospace",12), command=self.ok, )
        self.rb1.grid(row=0,column=0, sticky="e")
        self.rb2.grid(row=0,column=1, sticky="w")

        # self.e1 = tk.Entry(self.window, state='disable')
        # self.e1.grid(row=1, column=0, columnspan=4, rowspan=2,sticky="nswe")
        self.text_receive = tk.StringVar()
        self.text_receive.set("")

        self.label = tk.Label(self.window)
        self.label.configure(textvariable = self.text_receive)
        self.label.grid(row=1, column=0)
        


        self.e2 = tk.Entry(self.window)
        self.e2.grid(row=4, column=0)
        self.e2['state'] = 'disabled'
        self.send_button = tk.Button(self.window, text = "Send",font = ("Monospace",12))
        self.send_button.grid(row = 4, column = 2)
        self.send_button.configure(command =self.send)
        self.send_button['state'] = 'disabled'

        # self.receive_button = tk.Button(self.window, text = "Receive",font = ("Monospace",12))
        # self.receive_button.grid(row = 3, column = 0, columnspan=1)
        # # self.send_button.configure(command = )
    def ok(self):
        
        self.send_button['state'] = 'normal'
        self.e2['state'] = 'normal'
        self.label['text'] = ''
        self.send_selected = True

    def send(self):
        if self.send_selected:
            text = self.e2.get()
            self.manda.send_socket(text)
            self.e2.delete(0, 'end')
            print (text)
        else:
            print('nao')
        #comandos para mandar
    def receive(self):
        # self.manda.send_socket("alo alo alo alo quem é sou eu bola de fogo krebao")
        self.send_button['state'] = 'disabled'
        self.e2['state'] = 'disabled'
        # self.label['text'] = 'alo'
        # print('rrr')
        socket = self.recebe.initialize_socket()
        self.plot_text()
    
    def plot_text(self):
        # self._job = None
        # print(self._job)
        text = self.recebe.getText()
        self.texto.append(text)
        # if self.send_click == False:
        if text != '&':
            self.put_char_label(text)
            self.loop = self.window.after(7000, self.plot_text())
        else: 
            print("é &")
            self.recebe.close_socket()
            self.window.after_cancel(self.loop)
            self.window.update()

    def put_char_label(self, character):
        texto = self.text_receive.get() + character
        # self.label['text'] = self.label['text'] + character
        # self.text_receive.set(texto)
        # self.text_receive.trace("w", self.callback)
        self.text_receive.set(texto)
        # print(self.text_receive.get())
        self.window.update()

    def iniciar(self):
        self.window.mainloop()



app = Main()
app.iniciar()