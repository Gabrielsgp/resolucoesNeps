import os

# Definições oficiais do Neps
LINGUAGENS = ["Python", "CSharp"]
DIFICULDADES = ["Super Facil", "Facil", "Medio", "Dificil", "Super Dificil"]
CATEGORIAS = ["Basicos", "Tecnicas", "Estruturas", "Matematica", "Grafos", "Strings"]

def limpar_nome(nome):
    """Remove caracteres inválidos para pastas do Windows"""
    return nome.strip().replace(" ", "_").replace("?", "").replace(":", "")

def obter_texto_multilinha():
    """Captura múltiplas linhas de texto até o usuário digitar 'FIM'"""
    print("\n--- Cole o ENUNCIADO abaixo. ---")
    print("--- Quando terminar, digite 'FIM' em uma nova linha e dê Enter. ---")
    linhas = []
    while True:
        try:
            linha = input()
            if linha.strip().upper() == "FIM":
                break
            linhas.append(linha)
        except EOFError:
            break
    return "\n".join(linhas)

def criar_exercicio():
    print("=== AUTOMAÇÃO NEPS ===")
    
    # 1. Escolha da Linguagem
    print("Linguagem:")
    for i, lang in enumerate(LINGUAGENS):
        print(f"[{i}] {lang}")
    try:
        l_idx = int(input("Escolha: "))
        linguagem = LINGUAGENS[l_idx]
    except: return

    # 2. Escolha da Categoria
    print("\nCategoria:")
    for i, cat in enumerate(CATEGORIAS):
        print(f"[{i}] {cat}")
    try:
        c_idx = int(input("Escolha: "))
        categoria = CATEGORIAS[c_idx]
    except: return

    # 3. Escolha da Dificuldade
    print("\nDificuldade:")
    for i, dif in enumerate(DIFICULDADES):
        print(f"[{i}] {dif}")
    try:
        d_idx = int(input("Escolha: "))
        dificuldade = DIFICULDADES[d_idx]
    except: return

    # 4. Dados do Problema
    nome_raw = input("\nNome do Exercicio (ex: Soma Simples): ")
    if not nome_raw: return
    
    url_prob = input("Link do Neps (Cole a URL ou deixe vazio): ")
    
    # AQUI: Captura o texto longo
    descricao = obter_texto_multilinha()

    # Criação dos Caminhos
    nome_pasta = limpar_nome(nome_raw)
    caminho_final = os.path.join(os.getcwd(), linguagem, categoria, nome_pasta)
    
    if not os.path.exists(caminho_final):
        os.makedirs(caminho_final)
        
        # --- CRIA O README COM O TEXTO COLADO ---
        with open(os.path.join(caminho_final, "README.md"), "w", encoding="utf-8") as f:
            f.write(f"# {nome_raw}\n\n")
            f.write(f"**Neps Academy**\n")
            f.write(f"- **Dificuldade:** {dificuldade}\n")
            f.write(f"- **Categoria:** {categoria}\n")
            if url_prob:
                f.write(f"- **Link:** [{url_prob}]({url_prob})\n")
            f.write(f"\n## Enunciado\n")
            f.write(descricao) # Escreve o texto que você colou
            f.write(f"\n\n## Notas\n")

        # --- CRIA O ARQUIVO DE CÓDIGO ---
        if linguagem == "Python":
            arquivo = "main.py"
            conteudo = f"# Solução para: {nome_raw}\n# Link: {url_prob}\n\ndef main():\n    # Cole sua solução aqui\n    pass\n\nif __name__ == '__main__':\n    main()"
        else:
            arquivo = "Program.cs"
            conteudo = f"// Solução para: {nome_raw}\n// Link: {url_prob}\nusing System;\n\nclass Program {{\n    static void Main() {{\n        \n    }}\n}}"

        caminho_arquivo_cod = os.path.join(caminho_final, arquivo)
        with open(caminho_arquivo_cod, "w", encoding="utf-8") as f:
            f.write(conteudo)
        
        print(f"\n[SUCESSO] Exercício criado em: {caminho_final}")
        
        # Abre o arquivo de código direto no VS Code para você começar
        os.system(f"code \"{caminho_arquivo_cod}\"")
        
    else:
        print("\n[!] Já existe uma pasta com esse nome nessa categoria.")

if __name__ == "__main__":
    criar_exercicio()