import tkinter as tk

class Main():
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title('TrashTalk')
        # self.window.geometry("300x200")
        # self.window.configure(background = 'dim gray')
        self.window.resizable(False, False)

        self.window.rowconfigure(0)
        self.window.rowconfigure(1)
        self.window.rowconfigure(2)
        
        self.window.columnconfigure(0)
        self.window.columnconfigure(1)
        self.window.columnconfigure(2)

        self.e1 = tk.Entry(self.window, state='disable')
        self.e1.grid(row=0, column=0, columnspan=4,sticky="nswe")

        self.e2 = tk.Entry(self.window)
        self.e2.grid(row=1, column=0)

        v = tk.IntVar()

        self.rb1 = tk.Radiobutton(self.window, text="Receive", variable=v, value=1, font = ("Monospace",12), command=self.receive)
        self.rb2 = tk.Radiobutton(self.window, text="Send", variable=v, value=2, font = ("Monospace",12), command=self.ok)
        self.rb1.grid(row=2,column=0)
        self.rb2.grid(row=2,column=2)


        self.send_button = tk.Button(self.window, text = "Send",font = ("Monospace",12))
        self.send_button.grid(row = 1, column = 2)
        self.send_button.configure(command =self.send)

        # self.receive_button = tk.Button(self.window, text = "Receive",font = ("Monospace",12))
        # self.receive_button.grid(row = 3, column = 0, columnspan=1)
        # # self.send_button.configure(command = )
    def ok(self):
        return True

    def send(self):
        if self.ok():
            text = self.e2.get()
            print (text)
        else:
            print('nao')
        #comandos para mandar
    def receive(self):
        
        print('rrr')




    def iniciar(self):
        self.window.mainloop()



app = Main()
app.iniciar()