# Funcionalidades de memória (utilizar widgets do tkinter)
def adicionar_memoria_interface():
    nome = entrada_nome_memoria.get()
    valor_str = entrada_valor_memoria.get()
    try:
        valor = float(valor_str)
        adicionar_memoria(nome, valor)
        messagebox.showinfo("Informação", f"Valor '{valor}' armazenado na memória com nome '{nome}'.")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido!")

label_nome_memoria = Label(aba_basica, text="Nome:")
label_nome_memoria.pack()
entrada_nome_memoria = Entry(aba_basica)
entrada_nome_memoria.pack()

label_valor_memoria = Label(aba_basica, text="Valor:")
label_valor_memoria.pack()
entrada_valor_memoria = Entry(aba_basica)
entrada_valor_memoria.pack()

botao_adicionar_memoria = Button(aba_basica, text="Adicionar", command=adicionar_memoria_interface)
botao_adicionar_memoria.pack()

def remover_memoria_interface():
    nome = entrada_nome_memoria_remover.get()
    remover_memoria(nome)
    messagebox.showinfo("Informação", f"Valor com nome '{nome}' removido da memória.")

label_nome_memoria_remover = Label(aba_basica, text="Nome:")
label_nome_memoria_remover.pack()
entrada_nome_memoria_remover = Entry(aba_basica)
entrada_nome_memoria_remover.pack()

botao_remover_memoria = Button(aba_basica, text="Remover", command=remover_memoria_interface)
botao_remover_memoria.pack()

def consultar_memoria_interface():
    nome = entrada_nome_memoria_consultar.get()
    valor = consultar_memoria(nome)
    if valor is not None:
        messagebox.showinfo("Informação", f"Valor do nome '{nome}': {valor}")
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

label_nome_memoria_consultar = Label(aba_basica, text="Nome:")
label_nome_memoria_consultar.pack()
entrada_nome_memoria_consultar = Entry(aba_basica)
entrada_nome_memoria_consultar.pack()

botao_consultar_memoria = Button(aba_basica, text="Consultar", command=consultar_memoria_interface)
botao_consultar_memoria.pack()

def limpar_memoria_interface():
    limpar_memoria()
    messagebox.showinfo("Informação", "Memória limpa.")

botao_limpar_memoria = Button(aba_basica, text="Limpar Memória", command=limpar_memoria_interface)
botao_limpar_memoria.pack()

# Funções de memória
def adicionar_memoria(nome, valor):
    pass
    # ... (implementar a lógica para adicionar o valor à memória)def remover_memoria(nome):
    # ... (implementar a lógica para remover o valor da memória)def consultar_memoria(nome):
    # ... (implementar a lógica para consultar o valor na memória)def limpar_memoria():
    # ... (implementar a lógica para limpar a memória

    # Funções de memória (adicionar, remover, consultar, limpar)label_titulo_memoria = tk.Label(aba_memoria, text="Memória")label_titulo_memoria.pack()

# ... (implementar interfaces para as funções de memória)