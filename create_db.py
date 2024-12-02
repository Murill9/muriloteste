import sqlite3

# Conectar ao banco de dados (cria o arquivo 'users.db' se não existir)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Criar a tabela 'users' (caso ainda não exista)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Inserir um usuário padrão para testes (ignorar erros se já existir)
try:
    cursor.execute('''
    INSERT INTO users (username, password) VALUES (?, ?)
    ''', ('admin', 'admin123'))
except sqlite3.IntegrityError:
    print("Usuário padrão já existe.")

# Salvar e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados criado e populado com sucesso!")
