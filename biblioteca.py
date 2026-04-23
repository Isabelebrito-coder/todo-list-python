import sqlite3

# =========================
# CONEXÃO COM BANCO
# =========================

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# =========================
# CRIAR TABELAS
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

conn.commit()

# =========================
# FUNÇÕES LIVROS
# =========================

def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")

    cursor.execute(
        "INSERT INTO livros (titulo, autor) VALUES (?, ?)",
        (titulo, autor)
    )
    conn.commit()
    print("✅ Livro cadastrado!")


def listar_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    print("\n📖 Lista de livros:")
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for livro in livros:
            print(f"ID: {livro[0]} | {livro[1]} - {livro[2]}")


def remover_livro():
    listar_livros()
    try:
        id_livro = int(input("Digite o ID do livro: "))
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
        conn.commit()
        print("❌ Livro removido!")
    except:
        print("Erro ao remover livro.")


# =========================
# FUNÇÕES USUÁRIOS
# =========================

def cadastrar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")

    cursor.execute(
        "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
        (nome, email)
    )
    conn.commit()
    print("✅ Usuário cadastrado!")


def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    print("\n👤 Lista de usuários:")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario[0]} | {usuario[1]} - {usuario[2]}")


def remover_usuario():
    listar_usuarios()
    try:
        id_usuario = int(input("Digite o ID do usuário: "))
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
        conn.commit()
        print("❌ Usuário removido!")
    except:
        print("Erro ao remover usuário.")


# =========================
# MENU
# =========================

def menu():
    print("\n📚 SISTEMA DE BIBLIOTECA")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Remover livro")
    print("4 - Cadastrar usuário")
    print("5 - Listar usuários")
    print("6 - Remover usuário")
    print("0 - Sair")


# =========================
# LOOP PRINCIPAL
# =========================

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        remover_livro()

    elif opcao == "4":
        cadastrar_usuario()

    elif opcao == "5":
        listar_usuarios()

    elif opcao == "6":
        remover_usuario()

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("❌ Opção inválida")

# fechar conexão ao sair
conn.close()
