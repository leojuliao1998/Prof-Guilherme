import tkinter as tk
from tkinter import messagebox

# 1. O NOSSO DICIONÁRIO DE MATERIAIS (Igualzinho ao seu!)
guia_reciclagem = {
    "garrafa pet": "Lixeira Vermelha (Plástico). Lembre-se de amassar para ocupar menos espaço! 🍾",
    "plastico": "Lixeira Vermelha (Plástico). Lembre-se de amassar para ocupar menos espaço! 🍾",
    "garrafa": "Lixeira Vermelha (Plástico). Lembre-se de amassar para ocupar menos espaço! 🍾",
    "sacola": "Lixeira Vermelha (Plástico). Se estiver limpa, pode ser reciclada. 🛍️",
    "lata de refrigerante": "Lixeira Amarela (Metal). Muito fácil de reciclar! 🥤",
    "lata": "Lixeira Amarela (Metal). Muito fácil de reciclar! 🥤",
    "metal": "Lixeira Amarela (Metal). Muito fácil de reciclar! 🥤",
    "papelão": "Lixeira Azul (Papel). Precisa estar seco e sem gordura. 📦",
    "folha de papel": "Lixeira Azul (Papel). Pode rasgar, mas evite picar muito. 📄",
    "papel": "Lixeira Azul (Papel). Pode rasgar, mas evite picar muito. 📄",
    "copo de vidro": "Lixeira Verde (Vidro). Se estiver quebrado, embrulhe no jornal por segurança! 🥛",
    "vidro": "Lixeira Verde (Vidro). Se estiver quebrado, embrulhe no jornal por segurança! 🥛",
    "resto de comida": "Lixeira Marrom (Orgânico). Ótimo para compostagem! 🍎",
    "comida": "Lixeira Marrom (Orgânico). Ótimo para compostagem! 🍎",
    "casca de fruta": "Lixeira Marrom (Orgânico). Vai virar adubo para plantas! 🍌",
    "fruta": "Lixeira Marrom (Orgânico). Vai virar adubo para plantas! 🍌",
    "celular velho": "Descarte Especial! Leve a postos de coleta em lojas de eletrônicos ou operadoras. Contém metais pesados. 📱",
    "celular": "Descarte Especial! Leve a postos de coleta em lojas de eletrônicos ou operadoras. Contém metais pesados. 📱",
    "fio eletrico": "Lixeira Amarela (Metal) ou postos de reciclagem de eletrônicos. O cobre interno é valioso! 🔌",
    "fio": "Lixeira Amarela (Metal) ou postos de reciclagem de eletrônicos. O cobre interno é valioso! 🔌",
    "lampada led": "Descarte Especial! Leve a pontos de coleta específicos. Não jogue no lixo comum! 💡",
    "lampada": "Descarte Especial! Leve a pontos de coleta específicos. Não jogue no lixo comum! 💡",
    "caixa de leite": "Lixeira Azul (Papel/Tetra Pak). Lembre-se de dar uma enxaguada rápida para não cheirar mal! 🥛📦",
    "pote de iogurte": "Lixeira Vermelha (Plástico). Retire o excesso de produto antes de descartar. 🍧",
    "caixa de pizza": "Atenção! Se a parte de baixo tiver muita gordura, vai para o Lixo Comum. A tampa limpa vai para a Lixeira Azul (Papel). 🍕📦",
    "papel aluminio": "Lixeira Amarela (Metal). Se não estiver muito sujo de comida, faça uma bolinha e recicle! 🌯",
    "escova de dentes": "Lixeira Cinza (Lixo Comum/Não reciclável). Embora seja plástico, a mistura de materiais dificulta a reciclagem. 🪥",
    "papel higienico": "Lixeira Cinza (Lixo Comum/Rejeito). Nunca coloque no lixo reciclável! 🧻",
    "esponja de cozinha": "Lixeira Cinza (Lixo Comum). Dica: existem programas especiais de reciclagem de esponjas na internet! 🧽",
    "cartela de remedio": "Descarte Especial! Leve las cartelas até uma farmácia que tenha coletor correto. 💊",
    "remedio vencido": "Descarte Especial! Nunca jogue na privada ou no lixo comum. Leve até uma farmácia cadastrada. 🧪",
    "remedio": "Descarte Especial! Nunca jogue na privada ou no lixo comum. Leve até uma farmácia cadastrada. 🧪",
    "oleo de cozinha": "Descarte Especial! Espere esfriar, guarde em uma garrafa PET e leve a um ponto de coleta. 🛢️🍳",
    "oleo": "Descarte Especial! Espere esfriar, guarde em uma garrafa PET e leve a um ponto de coleta. 🛢️🍳",
    "espelho quebrado": "Lixeira Verde (Vidro) ou Lixo Comum. Embrulhe MUITO BEM em papelão ou jornal! 🪞💥",
    "espelho": "Lixeira Verde (Vidro) ou Lixo Comum. Embrulhe MUITO BEM em papelão ou jornal! 🪞💥",
    "roupa velha": "Doação ou Retalhos. Se estiver em bom estado, doe! 👕",
    "roupa": "Doação ou Retalhos. Se estiver em bom estado, doe! 👕",
    "pote de plastico": "Lixeira Vermelha (Plástico). Se estiver velho, tente reutilizar em casa antes de descartar! 🫙",
    "pote de conserva": "Lixeira Verde (Vidro). Lave bem e retire a tampa de metal. 🫙✨",
    "caixa de ovo": "Lixeira Azul (Papel). Geralmente é feita de papelão reciclado! 🥚📦",
    "filtro de cafe": "Lixeira Marrom (Orgânico). O filtro de papel e o pó de café podem ir juntos para a compostagem! ☕🍂",
    "caderno velho": "Lixeira Azul (Papel). Pode reciclar, mas retire a capa plástica e o espiral de metal primeiro! 📒",
    "caderno": "Lixeira Azul (Papel). Pode reciclar, mas retire a capa plástica e o espiral de metal primeiro! 📒",
    "caneta": "Lixeira Cinza (Lixo Comum). A mistura de plásticos e a tinta dificultam muito a reciclagem. 🖊️",
    "lapis": "Lixeira Cinza (Lixo Comum). Por ser feito de madeira tratada e grafite. ✏️",
    "prego": "Lixeira Amarela (Metal). Cuidado para não furar o saco de lixo! 🔩",
    "parafuso": "Lixeira Amarela (Metal). Junte com outros metais para facilitar a triagem. 🪛",
    "tinta": "Descarte Especial! Sobras de tinta líquida não devem ir ao lixo comum. Leve a ecopontos. 🎨",
    "fralda": "Lixeira Cinza (Lixo Comum/Rejeito). Nunca tente reciclar fraldas descartáveis! 👶🧷",
    "absorvente": "Lixeira Cinza (Lixo Comum/Rejeito). Vai direto para o lixo comum doméstico. 🩸",
    "fio dental": "Lixeira Cinza (Lixo Comum). É feito de nylon e não é reciclável. 🦷",
    "pneu": "Descarte Especial! Fabricantes e lojas de pneus são obrigados por lei a recolher. 🛞",
    "guarda chuva": "Lixo Comum ou Descarte Separado. Separe o tecido da estrutura de metal! ☂️",
    "chinelo velho": "Lixeira Cinza (Lixo Comum). Borrachas e sandálias velhas geralmente vão para o rejeito. 🩴",
    "chinelo": "Lixeira Cinza (Lixo Comum). Borrachas e sandálias velhas geralmente vão para o rejeito. 🩴",
    
    # === MAIS MATERIAIS E SUAS ALTERNATIVAS ===
    "pilhas": "Descarte Especial! Leve a um posto de coleta em supermercados ou farmácias. 🔋",
    "pilha": "Descarte Especial! Leve a um posto de coleta em supermercados ou farmácias. 🔋",
    "baterias": "Descarte Especial! Não jogue no lixo comum pois contamina o solo. 📱",
    "bateria": "Descarte Especial! Não jogue no lixo comum pois contamina o solo. 📱",
    "carregador": "Descarte Especial! Leve a postos de coleta de lixo eletrônico (e-waste). Não jogue no lixo comum. 🔌🔋",
    "carregador de celular": "Descarte Especial! Leve a postos de coleta de lixo eletrônico (e-waste). Não jogue no lixo comum. 🔌🔋",
    "fone de ouvido": "Descarte Especial! Componentes internos e fios devem ser reciclados junto com eletrônicos. 🎧",
    "fone": "Descarte Especial! Componentes internos e fios devem ser reciclados junto com eletrônicos. 🎧",
    "frasco de perfume": "Lixeira Verde (Vidro). Se possível, remova a tampa plástica ou a válvula de metal! 🧴✨",
    "perfume": "Lixeira Verde (Vidro). Se possível, remova a tampa plástica ou a válvula de metal! 🧴✨",
    "desodorante aerosol": "Lixeira Amarela (Metal). Certifique-se de que a lata está totalmente vazia antes de descartar! 💨🥫",
    "desodorante": "Lixeira Amarela (Metal). Certifique-se de que a lata está totalmente vazia antes de descartar! 💨🥫",
    "tubo de pasta de dente": "Lixeira Cinza (Lixo Comum). A mistura de plástico e alumínio nas camadas do tubo dificulta a reciclagem tradicional. 🪥🧴",
    "pasta de dente": "Lixeira Cinza (Lixo Comum). A mistura de plástico e alumínio nas camadas do tubo dificulta a reciclagem tradicional. 🪥🧴",
    "marmita de isopor": "Lixeira Vermelha (Plástico). O isopor é um tipo de plástico! Precisa estar bem limpo e sem restos de comida. 🍱",
    "isopor": "Lixeira Vermelha (Plástico). O isopor é um tipo de plástico! Precisa estar bem limpo e sem restos de comida. 📦",
    "copo descartavel": "Lixeira Vermelha (Plástico). Embora seja reciclável, o ideal é reduzir o uso! Lave antes de descartar. 🥛",
    "copo descartável": "Lixeira Vermelha (Plástico). Embora seja reciclável, o ideal é reduzir o uso! Lave antes de descartar. 🥛",
    "talher de plastico": "Lixeira Vermelha (Plástico). Se não estiver muito quebrado, lave e tente reutilizar antes de jogar fora! 🍴",
    "talher de plástico": "Lixeira Vermelha (Plástico). Se não estiver muito quebrado, lave e tente reutilizar antes de jogar fora! 🍴",
    "frasco de amaciante": "Lixeira Vermelha (Plástico). Plástico rígido e super reciclável. Dê uma enxaguada rápida! 🧴",
    "amaciante": "Lixeira Vermelha (Plástico). Plástico rígido e super reciclável. Dê uma enxaguada rápida! ZG",
    "garrafa de amaciante": "Lixeira Vermelha (Plástico). Plástico rígido e super reciclável. Dê uma enxaguada rápida! 🧴",
    "frasco de detergente": "Lixeira Vermelha (Plástico). Retire o excesso de espuma e descarte na coleta seletiva. 🧴🧼",
    "detergente": "Lixeira Vermelha (Plástico). Retire o excesso de espuma e descarte na coleta seletiva. 🧴🧼",
    "vaso de planta": "Lixeira Vermelha (Plástico). Se for daqueles pretos ou marrons comuns, limpe a terra antes de descartar! 🪴",
    "vaso": "Lixeira Vermelha (Plástico). Se for daqueles pretos ou marrons comuns, limpe a terra antes de descartar! 🪴",
    "bexiga": "Lixeira Cinza (Lixo Comum). Feita de látex, não passa pelo processo de reciclagem tradicional. 🎈",
    "balao": "Lixeira Cinza (Lixo Comum). Feita de látex, não passa pelo processo de reciclagem tradicional. 🎈",
    "balão": "Lixeira Cinza (Lixo Comum). Feita de látex, não passa pelo processo de reciclagem tradicional. 🎈",
    "chave": "Lixeira Amarela (Metal). Chaves velhas de latão, ferro ou alumínio são 100% recicláveis! 🔑",
    "chave velha": "Lixeira Amarela (Metal). Chaves velhas de latão, ferro ou alumínio são 100% recicláveis! 🔑",
    "oculos": "Doação ou Lixo Comum. Se as lentes estiverem inteiras, procure projetos sociais que coletam armações! 👓",
    "óculos": "Doação ou Lixo Comum. Se as lentes estiverem inteiras, procure projetos sociais que coletam armações! 👓",
    "guardanapo de papel": "Lixeira Marrom (Orgânico) ou Lixo Comum. Se estiver usado ou engordurado, pode ir para a compostagem doméstica! 🧻",
    
    # === ÚLTIMA LEVA DE MATERIAIS ===
    "batom": "Lixeira Cinza (Lixo Comum). A embalagem costuma reter muito produto e mistura plásticos diferentes. 💄",
    "embalagem de maquiagem": "Lixeira Cinza (Lixo Comum). Geralmente são plásticos mistos difíceis de separar na reciclagem. 🪞",
    "maquiagem": "Lixeira Cinza (Lixo Comum). Geralmente são plásticos mistos difíceis de separar na reciclagem. 🪞",
    "algodao": "Lixeira Cinza (Lixo Comum/Rejeito). Se tiver fluidos corporais ou química, vai para o lixo comum doméstico. 🧽",
    "algodão": "Lixeira Cinza (Lixo Comum/Rejeito). Se tiver fluidos corporais ou química, vai para o lixo comum doméstico. 🧽",
    "cotonete": "Lixeira Cinza (Lixo Comum). As hastes plásticas e o algodão usado não são recicláveis. 🧼",
    "clipe": "Lixeira Amarela (Metal). Por ser metal puro, pode ser reciclado se descartado junto com outros metais. 📎",
    "clips": "Lixeira Amarela (Metal). Por ser metal puro, pode ser reciclado se descartado junto com outros metais. 📎",
    "envelope com plastico bolha": "Atenção! Separe o papel externo (Lixeira Azul) do plástico bolha interno (Lixeira Vermelha - Plástico). ✉️🫧",
    "envelope": "Lixeira Azul (Papel). Se tiver aquela janela de plástico transparente, tente retirá-la antes. ✉️",
    "fita adesiva": "Lixeira Cinza (Lixo Comum). A cola e o material plástico colante inviabilizam a reciclagem. 🎞️",
    "fita": "Lixeira Cinza (Lixo Comum). A cola e o material plástico colante inviabilizam a reciclagem. 🎞️",
    "embalagem de salgadinho": "Lixeira Cinza (Lixo Comum). É um plástico do tipo BOPP (metalizado por dentro). Pouco reciclado no Brasil. 🍿",
    "salgadinho": "Lixeira Cinza (Lixo Comum). É um plástico do tipo BOPP (metalizado por dentro). Pouco reciclado no Brasil. 🍿",
    "embalagem de biscoito": "Lixeira Cinza (Lixo Comum). Plásticos metalizados ou muito finos vão para o rejeito. 🍪",
    "embalagem de bolacha": "Lixeira Cinza (Lixo Comum). Plásticos metalizados ou muito finos vão para o rejeito. 🍪",
    "biscoito": "Lixeira Cinza (Lixo Comum). Plásticos metalizados ou muito finos vão para o rejeito. 🍪",
    "bolacha": "Lixeira Cinza (Lixo Comum). Plásticos metalizados ou muito finos vão para o rejeito. 🍪",
    "canudo": "Lixeira Vermelha (Plástico). Embora seja plástico, por ser muito pequeno, evite usar ou procure pontos de reciclagem específicos. 🥤",
    "canudinho": "Lixeira Vermelha (Plástico). Embora seja plástico, por ser muito pequeno, evite usar ou procure pontos de reciclagem específicos. 🥤",
    "rolha de cortica": "Lixeira Marrom (Orgânico) ou Artesanato. Cortiça natural é biodegradável e ótima para compostagem! 🍾",
    "rolha de cortiça": "Lixeira Marrom (Orgânico) ou Artesanato. Cortiça natural é biodegradável e ótima para compostagem! 🍾",
    "rolha": "Lixeira Marrom (Orgânico) ou Artesanato. Cortiça natural é biodegradável e ótima para compostagem! 🍾",
    "pendrive": "Descarte Especial! Consiste em lixo eletrônico. Leve a pontos de coleta específicos. 💾",
    "pen drive": "Descarte Especial! Consiste em lixo eletrônico. Leve a pontos de coleta específicos. 💾",
    "cd": "Lixeira Cinza (Lixo Comum) ou Projetos de Artesanato. Feito de policarbonato e alumínio, raramente reciclado. 💿",
    "dvd": "Lixeira Cinza (Lixo Comum) ou Projetos de Artesanato. Feito de policarbonato e alumínio, raramente reciclado. 💿",
    "guarda napo": "Lixeira Marrom (Orgânico) ou Lixo Comum. Se estiver usado ou engordurado, vai para a compostagem doméstica! 🧻",
    "guardanapo": "Lixeira Marrom (Orgânico) ou Lixo Comum. Se estiver usado ou engordurado, vai para a compostagem doméstica! 🧻"
}

# 2. A FUNÇÃO DE BUSCA (Agora com o truque do event=None)
def buscar_material(event=None):
    objeto = entrada_texto.get().lower().strip()
    
    if objeto in guia_reciclagem:
        resposta = guia_reciclagem[objeto]
        # Atualiza o texto do resultado na tela
        label_resultado.config(text=f"Resultado:\n{resposta}", fg="green")
    else:
        # Se não encontrar, mostra um aviso em texto e também uma caixinha de alerta pop-up
        label_resultado.config(text="Material não encontrado...🤷", fg="red")
        messagebox.showinfo("Dica Geral", "Se for reciclável limpo, use a coleta seletiva. Se estiver sujo, vai para o lixo comum! 🗑️")

# 3. CONFIGURAÇÃO DA JANELA VISUAL
janela = tk.Tk()
janela.title("Assistente de Reciclagem 🌍")
janela.geometry("800x600") # Aumentei um pouquinho para acomodar bem o texto

# === O TRUQUE DE MESTRE COMAÇA AQUI ===
# Criamos um "Frame" (uma caixa invisível) que vai segurar todos os nossos textos e botões
container = tk.Frame(janela)

# Usamos o .pack com expand=True para que essa caixa invisível fique perfeitamente 
# centralizada no meio da janela (tanto na horizontal quanto na vertical)
container.pack(expand=True)

# 4. COMPONENTES VISUAIS (Agora anexados dentro do 'container' em vez de 'janela')
titulo = tk.Label(container, text="ASSISTENTE DE RECICLAGEM", font=("Arial", 20, "bold"))
titulo.pack(pady=20)

instrucao = tk.Label(container, text="Digite utilizando letras minúsculas, sem acento e no singular:", font=("Arial", 13))
instrucao.pack()

entrada_texto = tk.Entry(container, font=("Arial", 16), width=30)
entrada_texto.pack(pady=13)

# === AQUI ESTÁ A LINHA NOVA DO ENTER ===
# Ela vincula a tecla Enter à caixa de texto
entrada_texto.bind("<Return>", buscar_material)

botao_buscar = tk.Button(container, text="Verificar Descarte🔍", font=("Arial", 15, "bold"), bg="#4CAF50", fg="white", command=buscar_material)
botao_buscar.pack(pady=10)

label_resultado = tk.Label(container, text="", font=("Arial", 16), wraplength=450, justify="center")
label_resultado.pack(pady=20)

janela.mainloop()