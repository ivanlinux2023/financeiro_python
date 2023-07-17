import tkinter as tk
from tkinter import messagebox
import pickle
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt

class SistemaContas:
    def __init__(self):
        self.contas_a_receber = {}
        self.contas_a_pagar = {}
        self.carregar_dados()

    def adicionar_conta_receber(self):
        cliente = self.entry_cliente.get()
        valor = float(self.entry_valor.get())
        if cliente:
            if cliente in self.contas_a_receber:
                self.contas_a_receber[cliente] += valor
            else:
                self.contas_a_receber[cliente] = valor
            self.salvar_dados()
            messagebox.showinfo("Sucesso", "Conta a receber adicionada com sucesso!")
        else:
            messagebox.showerror("Erro", "Digite o nome do cliente.")
        self.limpar_campos()

    def adicionar_conta_pagar(self):
        fornecedor = self.entry_fornecedor.get()
        valor = float(self.entry_valor.get())
        if fornecedor:
            if fornecedor in self.contas_a_pagar:
                self.contas_a_pagar[fornecedor] += valor
            else:
                self.contas_a_pagar[fornecedor] = valor
            self.salvar_dados()
            messagebox.showinfo("Sucesso", "Conta a pagar adicionada com sucesso!")
        else:
            messagebox.showerror("Erro", "Digite o nome do fornecedor.")
        self.limpar_campos()

    def gerar_relatorio_pdf(self):
        nome_arquivo = "relatorio_contas.pdf"
        pdf = canvas.Canvas(nome_arquivo, pagesize=letter)
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(100, 750, "Relatório de Contas")

        y = 700  # Posição inicial para escrever o relatório

        # Relatório de Contas a Receber
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(100, y, "Contas a Receber:")

        y -= 20  # Espaçamento
        for cliente, valor in self.contas_a_receber.items():
            pdf.setFont("Helvetica", 10)
            pdf.drawString(120, y, f"Cliente: {cliente}")
            pdf.drawString(320, y, f"Valor: {valor}")
            y -= 15  # Espaçamento

        # Relatório de Contas a Pagar
        y -= 20  # Espaçamento
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(100, y, "Contas a Pagar:")

        y -= 20  # Espaçamento
        for fornecedor, valor in self.contas_a_pagar.items():
            pdf.setFont("Helvetica", 10)
            pdf.drawString(120, y, f"Fornecedor: {fornecedor}")
            pdf.drawString(320, y, f"Valor: {valor}")
            y -= 15  # Espaçamento

        pdf.save()
        messagebox.showinfo("Sucesso", f"Relatório gerado em {nome_arquivo}")

    def gerar_grafico(self):
        categorias = ["Contas a Receber", "Contas a Pagar"]
        valores = [sum(self.contas_a_receber.values()), sum(self.contas_a_pagar.values())]

        plt.bar(categorias, valores)
        plt.xlabel("Categorias")
        plt.ylabel("Valor")
        plt.title("Contas a Receber vs Contas a Pagar")
        plt.show()

    def limpar_campos(self):
        self.entry_cliente.delete(0, tk.END)
        self.entry_fornecedor.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)

    def salvar_dados(self):
        try:
            with open("dados.pickle", "wb") as arquivo:
                dados = (self.contas_a_receber, self.contas_a_pagar)
                pickle.dump(dados, arquivo)
        except IOError:
            messagebox.showerror("Erro", "Erro ao salvar os dados.")

    def carregar_dados(self):
        try:
            with open("dados.pickle", "rb") as arquivo:
                dados = pickle.load(arquivo)
                self.contas_a_receber, self.contas_a_pagar = dados
        except FileNotFoundError:
            print("Nenhum dado encontrado.")

    def exibir_janela_principal(self):
        root = tk.Tk()
        root.title("Sistema de Contas")
        root.geometry("400x400")

        label_cliente = tk.Label(root, text="Cliente:")
        label_cliente.pack()
        self.entry_cliente = tk.Entry(root)
        self.entry_cliente.pack()

        label_fornecedor = tk.Label(root, text="Fornecedor:")
        label_fornecedor.pack()
        self.entry_fornecedor = tk.Entry(root)
        self.entry_fornecedor.pack()

        label_valor = tk.Label(root, text="Valor:")
        label_valor.pack()
        self.entry_valor = tk.Entry(root)
        self.entry_valor.pack()

        btn_add_receber = tk.Button(root, text="Adicionar Conta a Receber", command=self.adicionar_conta_receber)
        btn_add_receber.pack()

        btn_add_pagar = tk.Button(root, text="Adicionar Conta a Pagar", command=self.adicionar_conta_pagar)
        btn_add_pagar.pack()

        btn_relatorio_pdf = tk.Button(root, text="Gerar Relatório em PDF", command=self.gerar_relatorio_pdf)
        btn_relatorio_pdf.pack()

        btn_grafico = tk.Button(root, text="Gerar Gráfico", command=self.gerar_grafico)
        btn_grafico.pack()

        root.mainloop()

    def exibir_janela_login(self):
        login_window = tk.Tk()
        login_window.title("Login")
        login_window.geometry("200x120")

        label_usuario = tk.Label(login_window, text="Usuário:")
        label_usuario.pack()
        self.entry_usuario = tk.Entry(login_window)
        self.entry_usuario.pack()

        label_senha = tk.Label(login_window, text="Senha:")
        label_senha.pack()
        self.entry_senha = tk.Entry(login_window, show="*")
        self.entry_senha.pack()

        btn_login = tk.Button(login_window, text="Login", command=self.fazer_login)
        btn_login.pack()

        login_window.mainloop()

    def fazer_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario == "edsonjuliene" and senha == "192718cauemanu":
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.exibir_janela_principal()  # Exibir a janela principal do sistema
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
            self.entry_usuario.delete(0, tk.END)
            self.entry_senha.delete(0, tk.END)

sistema = SistemaContas()
sistema.exibir_janela_login()
