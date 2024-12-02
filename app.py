import os
import sqlite3
import streamlit as st

# Função para verificar o login no banco de dados
def check_login(username, password):
    # Caminho do banco de dados
    db_path = os.path.join(os.path.dirname(__file__), 'users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Verifica as credenciais no banco de dados
    cursor.execute('''
    SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    user = cursor.fetchone()

    conn.close()
    return user is not None

# Interface do Streamlit
def login_page():
    st.title("Login")

    # Entradas de usuário
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    # Botão de login
    if st.button("Entrar"):
        if check_login(username, password):
            st.success("Login bem-sucedido!")
        else:
            st.error("Usuário ou senha incorretos!")

# Executar a página de login
if __name__ == "__main__":
    login_page()
