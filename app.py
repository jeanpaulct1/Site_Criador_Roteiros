import streamlit as st
from brain import ScriptEngine

# ---------------------------------------------------------
# UI REFINADA (Foco em Contraste e Organização)
# ---------------------------------------------------------
st.set_page_config(page_title="Script Pro 2.5", layout="centered")

st.markdown("""
    <style>
    /* 1. Remove o fundo branco da barra superior (Header) */
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
    }

    /* 2. Garante que o fundo da aplicação cubra toda a tela */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* 3. Estilização das Labels (Aumentadas e em Negrito) */
    label, .stMarkdown p {
        font-size: 19px !important;
        font-weight: bold !important;
        color: #1e293b !important;
    }

    /* 4. Botão com Texto Branco Puro e Legível */
    .stButton>button {
        background: #1e293b;
        color: #ffffff !important; /* Cor branca garantida */
        border: none;
        padding: 18px;
        border-radius: 12px;
        font-size: 16px;
        font-weight: bold;
        transition: 0.3s;
        width: 100%;
        text-transform: uppercase;
    }
    
    .stButton>button:hover {
        background: #334155;
        color: #ffffff !important;
    }

    /* 5. Ajuste das Abas (Tabs) para combinar com o fundo */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent !important;
    }

    .script-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# INTERFACE
# ---------------------------------------------------------
st.title("🎬 Script Generator Pro")
st.write("Configure os detalhes abaixo para gerar seus roteiros.")

# Layout em colunas
col1, col2 = st.columns(2)

with col1:
    produto = st.text_input("📦 Nome do Produto")
    publico = st.text_input("👥 Público-alvo")

with col2:
    tom = st.selectbox("🎭 Tom de voz", ["Persuasivo", "Educativo", "Cômico", "Urgente"])
    estilo = st.selectbox("🎬 Formato", ["TikTok/Reels", "YouTube Shorts", "Vídeo de Vendas"])

# ... (mantenha seu código de CSS e interface anterior)

if st.button("Gerar 3 Opções de Roteiro"):
    if produto:
        API_KEY = st.secrets["GEMINI_API_KEY"]
        engine = ScriptEngine(API_KEY)
        
        with st.spinner("🧠 IA redigindo roteiros..."):
            texto_gerado = engine.generate_script(produto, publico, tom, estilo)
            
            # DIVISÃO PRECISA:
            # O split vai criar uma lista baseada no marcador ###SEPARADOR###
            partes = texto_gerado.split("###SEPARADOR###")
            
            # Remove espaços em branco extras de cada parte
            partes = [p.strip() for p in partes if p.strip()]
            
            tab1, tab2, tab3 = st.tabs(["Roteiro 1", "Roteiro 2", "Roteiro 3"])
            
            with tab1:
                conteudo = partes[0] if len(partes) > 0 else "Erro ao gerar roteiro 1."
                st.markdown(f'<div class="script-card">{conteudo}</div>', unsafe_allow_html=True)
            with tab2:
                conteudo = partes[1] if len(partes) > 1 else "Erro ao gerar roteiro 2."
                st.markdown(f'<div class="script-card">{conteudo}</div>', unsafe_allow_html=True)
            with tab3:
                conteudo = partes[2] if len(partes) > 2 else "Erro ao gerar roteiro 3."
                st.markdown(f'<div class="script-card">{conteudo}</div>', unsafe_allow_html=True)