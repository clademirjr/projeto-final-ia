import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import textwrap

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="DevHelper Sischef", page_icon="🛠️", layout="centered")

st.title("🛠️ DevHelper Sischef")
st.caption("Agente de IA para Engenharia de Software – MVP")

with st.expander("Como usar", expanded=False):
    st.markdown(
        "- Cole um trecho de **código Python** ou um **log de erro**.\n"
        "- Selecione o objetivo (documentar, refatorar, diagnosticar, gerar testes).\n"
        "- Clique em **Gerar Sugestões**."
    )

if not API_KEY:
    st.warning("Defina a variável GEMINI_API_KEY no arquivo .env para usar o agente.")
else:
    genai.configure(api_key=API_KEY)

task = st.selectbox(
    "O que você precisa?",
    ["Documentar e explicar", "Sugerir nomes/refatorar", "Diagnosticar erro", "Gerar testes (básico)"]
)

code_or_error = st.text_area("Cole aqui o código ou erro", height=220, placeholder="def soma(a,b):\n    return a+b")

def build_prompt(task: str, content: str) -> str:
    base_policy = textwrap.dedent(f"""
    Você é um assistente de engenharia de software. Responda de forma estruturada, objetiva e com blocos de código quando necessário.
    Sempre inclua um pequeno **checklist** de boas práticas ao final.
    Tarefa: {task}
    Conteúdo do usuário a seguir.
    """)
    return base_policy + "\n\nCONTEÚDO:\n" + content.strip()

def call_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")
    resp = model.generate_content(prompt)
    return resp.text if hasattr(resp, "text") else str(resp)

col1, col2 = st.columns(2)
with col1:
    temperature = st.slider("Criatividade (temperature)", 0.0, 1.0, 0.3, 0.1)
with col2:
    top_p = st.slider("Top-p", 0.0, 1.0, 0.9, 0.05)

if st.button("🚀 Gerar Sugestões", use_container_width=True):
    if not code_or_error.strip():
        st.error("Cole um conteúdo para analisar.")
    else:
        with st.spinner("Gerando..."):
            prompt = build_prompt(task, code_or_error)
            # Nota: Para simplificar, temperature/top_p não são aplicados no SDK básico.
            try:
                output = call_gemini(prompt)
                st.markdown(output)
            except Exception as e:
                st.error(f"Falha ao chamar o modelo: {e}")
