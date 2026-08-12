# 1. CRIANDO O NOSSO DICIONÁRIO DE MATERIAIS
# Aqui guardamos o objeto (chave) e a instrução de descarte (valor) com os emojis no final.
guia_reciclagem = {
    "garrafa pet": "Lixeira Azul (Plástico). Lembre-se de amassar para ocupar menos espaço! 🍾",
    "sacola": "Lixeira Azul (Plástico). Se estiver limpa, pode ser reciclada. 🛍️",
    "lata de refrigerante": "Lixeira Amarela (Metal). Muito fácil de reciclar! 🥤",
    "papelão": "Lixeira Azul (Papel). Precisa estar seco e sem gordura. 📦",
    "folha de papel": "Lixeira Azul (Papel). Pode rasgar, mas evite picar muito. 📄",
    "copo de vidro": "Lixeira Verde (Vidro). Se estiver quebrado, embrulhe em jornal por segurança! 🥛",
    "resto de comida": "Lixeira Marrom (Orgânico). Ótimo para compostagem! 🍎",
    "casca de fruta": "Lixeira Marrom (Orgânico). Vai virar adubo para plantas! 🍌",
    "pilha": "Descarte Especial! Leve a um posto de coleta em supermercados ou farmácias. 🔋",
    "bateria": "Descarte Especial! Não jogue no lixo comum pois contamina o solo. 📱",
    
    # === NOVOS MATERIAIS PARA O SEU DICIONÁRIO ===
        # Eletrônicos e Eletrodomésticos
    "celular velho": "Descarte Especial! Leve a postos de coleta em lojas de eletrônicos ou operadoras. Contém metais pesados. 📱",
    "fio eletrico": "Lixeira Amarela (Metal) ou postos de reciclagem de eletrônicos. O cobre interno é valioso! 🔌",
    "lampada led": "Descarte Especial! Leve a pontos de coleta específicos (como grandes redes de home center). Não jogue no lixo comum! 💡",
    
    # Embalagens do dia a dia
    "caixa de leite": "Lixeira Azul (Papel/Tetra Pak). Lembre-se de dar uma enxaguada rápida para não cheirar mal! 🥛📦",
    "pote de iogurte": "Lixeira Azul (Plástico). Retire o excesso de produto antes de descartar. 🍧",
    "caixa de pizza": "Atenção! Se a parte de baixo tiver muita gordura, vai para o Lixo Comum. A tampa limpa vai para a Lixeira Azul (Papel). 🍕📦",
    "papel aluminio": "Lixeira Amarela (Metal). Se não estiver muito sujo de comida, faça uma bolinha e recicle! 🌯",
    
    # Banheiro e Higiene (Geralmente Não Recicláveis)
    "escova de dentes": "Lixeira Cinza (Lixo Comum/Não reciclável). Embora seja plástico, a mistura de materiais dificulta a reciclagem. 🪥",
    "papel higienico": "Lixeira Cinza (Lixo Comum/Rejeito). Nunca coloque no lixo reciclável! 🧻",
    "esponja de cozinha": "Lixeira Cinza (Lixo Comum). Dica: existem programas especiais de reciclagem de esponjas na internet! 🧽",
    
    # Medicamentos e Saúde
    "cartela de remedio": "Descarte Especial! Leve as cartelas (vizinhas ou cheias) até uma farmácia que tenha coletor correto. 💊",
    "remedio vencido": "Descarte Especial! Nunca jogue na privada ou no lixo comum. Leve até uma farmácia cadastrada. 🧪",
    
    # Outros materiais
    "oleo de cozinha": "Descarte Especial! Espere esfriar, guarde em uma garrafa PET e leve a um ponto de coleta (vira sabão ou biodiesel!). 🛢️🍳",
    "espelho quebrado": "Lixeira Verde (Vidro) ou Lixo Comum. Embrulhe MUITO BEM em papelão ou jornal e escreva 'CUIDADO: VIDRO' para proteger os coletores. 🪞💥",
    "roupa velha": "Doação ou Retalhos. Se estiver em bom estado, doe! Se estiver rasgada, use como pano de chão ou procure pontos de logística reversa têxtil. 👕",
    # === MAIS MATERIAIS PARA O SEU DICIONÁRIO ===
    
    # Cozinha e Alimentos
    "pote de plastico": "Lixeira Azul (Plástico). Se estiver velho, tente reutilizar em casa antes de descartar! 🫙",
    "pote de conserva": "Lixeira Verde (Vidro). Lave bem e retire a tampa de metal (que vai para a lixeira amarela). 🫙✨",
    "caixa de ovo": "Lixeira Azul (Papel). Geralmente é feita de papelão reciclado e pode ser reciclada de novo! 🥚📦",
    "filtro de cafe": "Lixeira Marrom (Orgânico). O filtro de papel e o pó de café podem ir juntos para a compostagem! ☕🍂",
        
    # Escritório e Estudos
    "caderno velho": "Lixeira Azul (Papel). Pode reciclar, mas retire a capa plástica e o espiral de metal primeiro! 📒",
    "caneta": "Lixeira Cinza (Lixo Comum). A mistura de plásticos e a tinta dificultam muito a reciclagem. 🖊️",
    "lapis": "Lixeira Cinza (Lixo Comum). Por ser feito de madeira tratada e grafite, não vai na reciclagem de papel. ✏️",
        
    # Construção, Manutenção e Ferramentas
    "prego": "Lixeira Amarela (Metal). Cuidado para não furar o saco de lixo! 🔩",
    "parafuso": "Lixeira Amarela (Metal). Junte com outros metais para facilitar a triagem. 🪛",
    "tinta": "Descarte Especial! Sobras de tinta líquida não devem ir ao lixo comum. Leve a ecopontos da sua cidade. 🎨",
    
    # Higiene e Cuidados Pessoais
    "fralda": "Lixeira Cinza (Lixo Comum/Rejeito). Nunca tente reciclar fraldas descartáveis! 👶🧷",
    "absorvente": "Lixeira Cinza (Lixo Comum/Rejeito). Vai direto para o lixo comum doméstico. 🩸",
    "fio dental": "Lixeira Cinza (Lixo Comum). É feito de nylon e não é reciclável. 🦷",
    
    # Outros Objetos Comuns
    "pneu": "Descarte Especial! Fabricantes e lojas de pneus são obrigados por lei a recolher os pneus velhos (logística reversa). 🛞",
    "guarda chuva": "Lixo Comum ou Descarte Separado. Separe o tecido (lixo comum) da estrutura de metal (lixeira amarela), se conseguir! ☂️",
    "chinelo velho": "Lixeira Cinza (Lixo Comum). Borrachas e sandálias velhas geralmente vão para o rejeito, a menos que a marca tenha posto de coleta. 🩴"
}

# 2. MENSAGEM DE BOAS-VINDAS
print("=== ASSISTENTE DE RECICLAGEM E SUSTENTABILIDADE ===")
print("Descubra o lugar correto para cada tipo de resíduo! 🌍")
print("Para digitar utilize letras minúsculas e não é necessário acentuação em palavra que tenham!")

# 3. O LOOP COMEÇA AQUI
# Criamos uma variável de controle. Enquanto ela for True (Verdadeira), o programa não para.
programa_ativo = True

while programa_ativo:
    print("\n--------------------------------------------------")
    # Pedimos o objeto ou a palavra 'sair'
    objeto = input("Digite o material (ou digite 'sair' para fechar): ").lower()

    # PASSO A: Verificar se o usuário quer fechar o programa
    if objeto == "sair":
        programa_ativo = False # Isso faz o 'while' parar na próxima rodada!
        print("\nEncerrando o assistente... 🖥️")
    
    # PASSO B: Se não for para sair, procuramos o objeto no dicionário
    elif objeto in guia_reciclagem:
        resposta = guia_reciclagem[objeto]
        print(f"\nResultado: {resposta}")
        
    # PASSO C: Se não for 'sair' e não estiver no dicionário, dá a mensagem de erro
    else:
        print("\nHum, não encontrei esse material específico... 🤷‍♂️")
        print("Dica geral: Se for reciclável limpo, use a coleta seletiva. 🗑️")

# 4. MENSAGEM FINAL (Só aparece quando o loop termina)
print("\nObrigado por cuidar do nosso planeta! 💚🌱")