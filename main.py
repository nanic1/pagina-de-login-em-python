from tkinter import *
from tkinter import messagebox
import database

#Cria tela de exibição

jan = Tk()
jan.title("Mobi Banco - Login")
jan.geometry("800x600")
jan.configure(background="White")
jan.resizable(width=False, height=False)
jan.iconbitmap(default="logo.ico")

#--IMAGENS--
logoMobi = PhotoImage(file="logo.png")


#--WIDGETS--
frameEsquerda = Frame(jan, width=300, height=600, bg="midnightblue", relief="raise")
frameEsquerda.pack(side=LEFT)
frameDireita = Frame(jan, width=490, height=600, bg="midnightblue", relief="raise")
frameDireita.pack(side=RIGHT)

LogoLabel = Label(frameEsquerda, image=logoMobi, bg="MIDNIGHTBLUE")
LogoLabel.place(x=20, y=130)

UserLabel = Label(frameDireita, text="Login:", font=("Century Gothic", 25), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=20, y=120)

UserEntrada = Entry(frameDireita, width=28, font=("Century Gothic", 15))
UserEntrada.place(x=140, y=135)

SenhaLabel = Label(frameDireita, text="Senha:", font=("Century Gothic", 25), bg="MIDNIGHTBLUE", fg="White")
SenhaLabel.place(x=20, y=170)

SenhaEntrada = Entry(frameDireita, width=28, font=("Century Gothic", 15), show="•")
SenhaEntrada.place(x=140, y=185)

def Login():
    User = UserEntrada.get()
    Senha = SenhaEntrada.get()
    database.cursor.execute("SELECT * FROM users WHERE (log = %s AND senha = %s)", (User, Senha))
    VerificarLogin = database.cursor.fetchone()
    try:
        if User in VerificarLogin and Senha in VerificarLogin:
            messagebox.showinfo(title="Informações de Login", message="Login realizado com sucesso!")
    except:
        messagebox.showerror(title="Informações de Login", message="Não foi possivel realizar seu login. Verifique seus dados e tente novamente")

#--Botoes--
def Registrar():
    #Remover Widgets da tela de Login
    LoginButton.place(x=5000, y=5000)
    RegistrarButton.place(x=5000, y=5000)

    NomeLabel = Label(frameDireita, text="Nome:", font=("Century Gothic", 25), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=20, y=20)

    NomeEntrada = Entry(frameDireita, width=28, font=("Century Gothic", 15))
    NomeEntrada.place(x=140, y=35)

    EmailLabel = Label(frameDireita, text="Email:", font=("Century Gothic", 25), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=20, y=70)
    
    EmailEntrada = Entry(frameDireita, width=28, font=("Century Gothic", 15))
    EmailEntrada.place(x=140, y=85)

    def CadastrarDataBase():
        NomePy = NomeEntrada.get()
        EmailPy = EmailEntrada.get()
        UserPy = UserEntrada.get()
        SenhaPy = SenhaEntrada.get()
        
        if (NomePy == "" or EmailPy == "" or UserPy == "" or SenhaPy == ""):
            messagebox.showerror(title="Erro", message="Preencha todos os campos.")
        else:
            database.cursor.execute("INSERT INTO users(nome, email, log, senha) VALUES (%s, %s, %s, %s)", (NomePy, EmailPy, UserPy, SenhaPy))
            database.conexao.commit()
            messagebox.showinfo(title="Informação de registro", message="Registro concluido!")

    CadastroButton = Button(frameDireita, text="Cadastrar", width=20, command=CadastrarDataBase)
    CadastroButton.place(x= 100, y=250)

    def VoltarLogin():
        #--Voltando pra tela de Login--
        NomeLabel.place(x=5000)
        NomeEntrada.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntrada.place(x=5000)
        CadastroButton.place(x=5000)
        VoltarButton.place(x=5000)
        #--Trazendo os botoes anteriores de volta
        LoginButton = Button(frameDireita, text="Logar", width=20)
        LoginButton.place(x=100, y=250)

        RegistrarButton = Button(frameDireita, text="Registrar", width=20, command=Registrar)
        RegistrarButton.place(x=100, y=280)


    VoltarButton = Button(frameDireita, text="Voltar", width=20, command=VoltarLogin)
    VoltarButton.place(x=100, y=280)

LoginButton = Button(frameDireita, text="Logar", width=20, command=Login)
LoginButton.place(x=100, y=250)

RegistrarButton = Button(frameDireita, text="Registrar", width=20, command=Registrar)
RegistrarButton.place(x=100, y=280)


jan.mainloop()