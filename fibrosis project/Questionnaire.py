import streamlit as st
import model
from model import prediccion

def show_questionnaire():
    st.title("Qüestionari de Fibrosi Pulmonar")

    respostes_fumador = ["Sí, actiu.", "No, i mai ho ha estat.", "No, però és ex-fumador."]
    
    edat = st.number_input("Quants d'anys té el/la pacient?", min_value=0, max_value=125)
    
    fvc = st.number_input("Percentatge de FVC (Capacitat Vital Forçada):", min_value = 0, max_value = 200)  
    
    dlco = st.number_input("Percentatge de DLCO (Difusió de monòxid de carboni):", min_value = 0, max_value = 200)
    
    fumador = st.radio("És fumador?", respostes_fumador)
    for i in respostes_fumador:
        if fumador == i:
            valor_fumador = i
            break
        
    gen_mut = st.radio("Té alguna mutació genètica estudiada?", ["Sí.", "No."])
    if gen_mut == "Sí.":
        gen_mut_bool = 1
    else:
        gen_mut_bool = 0
        
    com = st.radio("Té alguna comorbiditat associada?", ["Sí.", "No."])
    if com == "Sí.":
        com_bool = 1
    else:
        com_bool = 0
    
    ipf = st.radio("El / La pacient té diagnòstic d'IPF (Fibrosi Pulmonar Idiopàtica)?", ["Sí.", "No."])
    
    if ipf == "Sí.":
        valor_ipf = 'IPF'
    else:
        valor_ipf = 'No IPF'
    
    fam_esp = st.radio("Hi ha antecedents familiars de fibrosi pulmonar o és un cas esporàdic?", ["Existeixen antecedents familiars.", "És esporàdic."])                    
                  
    rad_pat = st.radio("Quin és el patró radiològic del / de la pacient?", ["UIP.", "UIP probable.", "UIP indeterminat.", "No UIP."])
    
    path_pat = st.radio("Quin és el patró patològic del / de la pacient?", ["UIP.", "UIP probable.", "Vasculitis necrotitzant.", "Granulomatosi.", "AFOP.", "RB-ILD.", "OP.", "CHP.", "NSIP.", "Inconclús.", "Ningun."])
    
    st.text("")
    
    if st.button("Enviar respostes"):
        st.write(f"Edat: {edat}.")
        st.write(f"Percentatge de FVC: {fvc}%.")
        st.write(f"Percentatge de DLCO: {dlco}%.")
        st.write(f"Fumador: {fumador}")
        st.write(f"Mutació genètica: {gen_mut}")
        st.write(f"Comorbiditat: {com}")
        st.write(f"Diagnòstic d'IPF: {ipf}")
        st.write(f"Antecedents familiars: {fam_esp}")
        st.write(f"Patró radiològic: {rad_pat}")
        st.write(f"Patró patològic: {path_pat}")
        
        variables = [valor_fumador, edat, path_pat[:-1], fam_esp[:-1], valor_ipf, com_bool, gen_mut_bool, rad_pat[:-1], fvc, dlco]
        resposta = prediccion(variables)
        
        if resposta == 0:
            st.markdown(
                "<p style='font-size:24px; font-weight:bold; color: orange'>Resultat: La malaltia del pacient no progressarà negativament, però igualment es recomana tenir cura del pacient i estudiar la seva evolució.</p>",
                unsafe_allow_html=True
            )
        if resposta == 1:
            st.markdown(
                "<p style='font-size:24px; font-weight:bold; color: red'>Resultat: La malaltia del pacient progressarà negativament.</p>",
                unsafe_allow_html=True
            )
        
        if st.button("Tornar a l'inici."):
            st.session_state.current_page = "Home"
            st.rerun()