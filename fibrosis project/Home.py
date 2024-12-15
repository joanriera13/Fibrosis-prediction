import streamlit as st

def show_home():

    st.markdown("""
        <style>
        .title {
            text-align: center;  /* Centrar texto horizontalmente */
            font-size: 56px !important;    /* Tamaño de fuente ajustable */
            font-weight: bold;  /* Negrita */
        }
        .center-text {
            text-align: center;  /* Centrar texto horizontalmente */
            justify-content: center;
            align-items: center;
            font-size: 16px !important;    /* Tamaño de fuente ajustable */
            line-height: 1.5;   /* Espaciado entre líneas */
        }
        .stButton {
            display: flex;
            justify-content: center;
            padding: 10px 15px;           /* Tamaño del botón */
            border-radius: 12px;          /* Bordes redondeados */
            font-size: 16px;              /* Tamaño de la fuente */
            cursor: pointer;              /* Cambiar cursor */
        }
        </style>
        """, unsafe_allow_html=True)

    # Usar la clase .center-text para centrar el texto
    st.markdown('<p class="title">Lung Fibrosis Progression Prediction</p>', unsafe_allow_html=True)

    st.markdown("<p class='center-text'>LFPP is a web application that predicts the progression of a patient's lung fibrosis illness. This web uses a machine learning model trained on a dataset of patients with lung fibrosis in Spain. The model takes as input various features of the patient that you shall provide to predict the development of the patient.</p>", unsafe_allow_html=True)
        
    # Botón funcional con diseño personalizado
    if st.button("Start the questionnaire"):
        st.session_state.current_page = "Questionnaire"
        st.rerun()
