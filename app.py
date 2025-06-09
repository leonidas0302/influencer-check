
import streamlit as st
import pandas as pd
import os

# Nome do arquivo Excel
FILE_NAME = "avaliacao_influenciadores.xlsx"

# Carrega os dados ou cria um DataFrame vazio
if os.path.exists(FILE_NAME):
    df = pd.read_excel(FILE_NAME)
else:
    columns = [
        "Nome",
        "@Usuário / Link Instagram",
        "Link TikTok",
        "Link YouTube",
        "Nº de Seguidores (IG)",
        "Nº de Seguidores (TikTok)",
        "Nº de Seguidores (YT)",
        "Gênero",
        "Fala de Moda?",
        "Público LGBT+?",
        "Estilo Visual",
        "Tom de Voz",
        "Região",
        "Faixa Etária do Público",
        "Afinidade com Marca (1 a 5)",
        "Comentários"
    ]
    df = pd.DataFrame(columns=columns)

st.title("🔍 Avaliação de Influenciadores")
st.markdown("Use esta ferramenta para avaliar o fit de influenciadores com sua marca.")

# Formulário para adicionar novo influenciador
with st.form("add_influencer"):
    st.subheader("Adicionar Novo Influenciador")
    nome = st.text_input("Nome")
    insta = st.text_input("@Usuário / Link Instagram")
    tiktok = st.text_input("Link TikTok")
    youtube = st.text_input("Link YouTube")
    seguidores_ig = st.number_input("Seguidores Instagram", 0)
    seguidores_tt = st.number_input("Seguidores TikTok", 0)
    seguidores_yt = st.number_input("Seguidores YouTube", 0)
    genero = st.selectbox("Gênero", ["Feminino", "Masculino", "Não-binário", "Outro", "Prefere não dizer"])
    fala_moda = st.selectbox("Fala de Moda?", ["Sim", "Não"])
    publico_lgbt = st.selectbox("Público LGBT+?", ["Sim", "Não"])
    estilo = st.text_input("Estilo Visual")
    tom = st.text_input("Tom de Voz")
    regiao = st.text_input("Região")
    faixa_etaria = st.text_input("Faixa Etária do Público")
    afinidade = st.slider("Afinidade com Marca (1 a 5)", 1, 5, 3)
    comentarios = st.text_area("Comentários")
    submit = st.form_submit_button("Adicionar")

    if submit:
        novo = pd.DataFrame([{
            "Nome": nome,
            "@Usuário / Link Instagram": insta,
            "Link TikTok": tiktok,
            "Link YouTube": youtube,
            "Nº de Seguidores (IG)": seguidores_ig,
            "Nº de Seguidores (TikTok)": seguidores_tt,
            "Nº de Seguidores (YT)": seguidores_yt,
            "Gênero": genero,
            "Fala de Moda?": fala_moda,
            "Público LGBT+?": publico_lgbt,
            "Estilo Visual": estilo,
            "Tom de Voz": tom,
            "Região": regiao,
            "Faixa Etária do Público": faixa_etaria,
            "Afinidade com Marca (1 a 5)": afinidade,
            "Comentários": comentarios
        }])
        df = pd.concat([df, novo], ignore_index=True)
        df.to_excel(FILE_NAME, index=False)
        st.success("Influenciador adicionado com sucesso!")

# Exibir a tabela atual
st.subheader("📋 Lista de Influenciadores")
st.dataframe(df, use_container_width=True)

# Opção para exportar os dados
st.download_button("📤 Baixar Excel", data=df.to_excel(index=False), file_name=FILE_NAME, mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
