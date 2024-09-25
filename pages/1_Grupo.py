import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="Grupo Responsável", page_icon=":house:", layout='wide')

# Função para carregar e redimensionar a imagem
def load_and_resize_image(image_path, new_width=1600, new_height=800):
    image = Image.open(image_path).convert("RGBA")
    resized_image = image.resize((new_width, new_height))
    buffered = BytesIO()
    resized_image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Carregar a imagem de fundo e converter para base64
background_image_path = "Imagens/capa4.png"  # Substitua pelo caminho real da sua imagem
background_image_base64 = load_and_resize_image(background_image_path)

# Definir a imagem de fundo
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    .stApp {{
        background: url(data:image/png;base64,{background_image_base64}) no-repeat center center fixed;
        background-size: cover;
        color: #ffffff;  /* Cor do texto principal */
    }}

    /* Centralizando o conteúdo */
    .block-container {{
        padding: 5% 15%;
    }}

    h1 {{
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #800020;  /* Título bordô */
        text-align: center;
        font-size: 3em;  /* Diminuído para 3em */
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 20px;
    }}

    .student-badge {{
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        background-color: rgba(255, 255, 255, 0.8);
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# Nome dos componentes do grupo
student_data = [
    {"nome": "Antônio Leão", "matricula": "RM349640"},
    {"nome": "Frederico Quesado", "matricula": "RM352633"},
    {"nome": "Lucas Tabelini", "matricula": "RM352725"},
    {"nome": "Renan Carneiro", "matricula": "RM352715"},
    {"nome": "Vanessa Andrade", "matricula": "RM352921"},
]

# Título da página
st.markdown('<h1>Grupo Responsável</h1>', unsafe_allow_html=True)

# Dividir em duas colunas
left_column, right_column = st.columns(2)

# Exibir informações dos alunos usando badges
for i, student in enumerate(student_data):
    column = left_column if i % 2 == 0 else right_column
    with column:
        st.markdown(
            f"""
            <div class="student-badge">
                <p><strong>Nome:</strong> {student['nome']}</p>
                <p><strong>Número de Matrícula:</strong> {student['matricula']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
