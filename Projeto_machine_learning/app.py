import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd 
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Projeto_machine_learning\pizzas.csv')

modelo = LinearRegression()
x = df[["Diametro"]]
y = df[["Preco"]]
modelo.fit(x, y)

# Função para calcular o preço estimado
def calcular_preco():
    try:
        # Obter valor inserido pelo usuário
        diametro = float(valor_diametro.get())
        
        # Fazer a previsão e mostrar o resultado
        preco_predito = modelo.predict(pd.DataFrame({"Diametro": [diametro]}))[0][0]
        messagebox.showinfo("Preço Estimado", f"O preço estimado para uma pizza de {diametro} cm é: R$ {preco_predito:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para o diâmetro.")

# Configurar a interface gráfica
interface = tk.Tk()
interface.title("Previsão de Preço de Pizza")
interface.geometry("500x300")
interface.configure(bg="#f0f0f5")

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14), background="#f0f0f5")
style.configure("TButton", font=("Helvetica", 12, "bold"), foreground="#333", background="#4CAF50")
style.map("TButton", background=[("active", "#45a049")])

header = ttk.Label(interface, text="Calculadora de Preço de Pizza", font=("Helvetica", 18, "bold"), foreground="#333")
header.pack(pady=20)

# Rótulo e campo de entrada
label_diametro = tk.Label(interface, text="Digite o diâmetro da pizza em cm:")
label_diametro.pack(pady=10)

valor_diametro = tk.Entry(interface)
valor_diametro.pack(pady=5)

# Botão para calcular o preço
botao_calcular = tk.Button(interface, text="Calcular Preço", command=calcular_preco)
botao_calcular.pack(pady=20)

# Executar a aplicação
interface.mainloop()