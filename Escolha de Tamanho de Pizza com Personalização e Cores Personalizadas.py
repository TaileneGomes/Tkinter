import tkinter as tk
from tkinter import messagebox

# Função para calcular o total a pagar
def calcular_total():
    try:
        quantidade = int(entry_quantidade.get())
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser um número positivo.")

        tamanho = var_tamanho.get()
        preco_base = precos[tamanho]
        total = preco_base * quantidade
        
        for ingrediente, var in check_vars.items():
            if var.get():
                total += precos_ingredientes[ingrediente] * quantidade

        label_total.config(text=f"Total a pagar: R$ {total:.2f}")
        return total
    except ValueError as e:
        messagebox.showerror("Erro de entrada", str(e))
        return None

# Função para confirmar o pedido
def confirmar_pedido():
    total = calcular_total()
    if total is not None:
        resposta = messagebox.askyesno("Confirmar Pedido", f"O total é R$ {total:.2f}. Deseja confirmar o pedido?")
        if resposta:
            messagebox.showinfo("Pedido Confirmado", "Seu pedido foi confirmado com sucesso!")
        else:
            messagebox.showinfo("Pedido Cancelado", "Seu pedido foi cancelado.")

# Configurações principais
root = tk.Tk()
root.title("Escolha o Tamanho da Pizza")

# Widgets
label_titulo = tk.Label(root, text="Escolha o Tamanho da Pizza")
label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Opções de tamanhos e preços
tamanhos = ["Pequena", "Média", "Grande"]
precos = {"Pequena": 15.00, "Média": 22.00, "Grande": 28.00}

var_tamanho = tk.StringVar(value=tamanhos[0])
label_tamanho = tk.Label(root, text="Tamanho:")
label_tamanho.grid(row=1, column=0, sticky='e')
option_tamanho = tk.OptionMenu(root, var_tamanho, *tamanhos)
option_tamanho.grid(row=1, column=1, sticky='w')

label_quantidade = tk.Label(root, text="Quantidade:")
label_quantidade.grid(row=2, column=0, sticky='e')

entry_quantidade = tk.Entry(root)
entry_quantidade.grid(row=2, column=1, sticky='w')

# Ingredientes adicionais e seus preços
ingredientes = ["Queijo Extra", "Pepperoni", "Bacon"]
precos_ingredientes = {"Queijo Extra": 2.00, "Pepperoni": 3.00, "Bacon": 4.00}

check_vars = {}
row = 3
for ingrediente in ingredientes:
    var = tk.BooleanVar()
    check_vars[ingrediente] = var
    check_button = tk.Checkbutton(root, text=ingrediente, variable=var)
    check_button.grid(row=row, column=0, columnspan=2, sticky='w')
    row += 1

# Botão para fazer o pedido
button_pedir = tk.Button(root, text="Pedir", command=confirmar_pedido)
button_pedir.grid(row=row, column=0, columnspan=2, pady=10)

# Label para exibir o total
label_total = tk.Label(root, text="Total a pagar: R$ 0.00")
label_total.grid(row=row+1, column=0, columnspan=2)

# Executar a aplicação
root.mainloop()
