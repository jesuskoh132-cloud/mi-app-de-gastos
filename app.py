import streamlit as st
import PIL.Image
import google.generativeai as genai

st.set_page_config(page_title="Scanner de Gastos", page_icon="💰")
st.title("💸 Mi Asistente de Gastos Inteligente")

with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("Pega tu Gemini API Key aquí:", type="password")
    st.info("Consíguela gratis en Google AI Studio")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    archivo = st.file_uploader("Sube una imagen del recibo", type=["jpg", "png", "jpeg"])

    if archivo:
        imagen = PIL.Image.open(archivo)
        st.image(imagen, caption="Ticket cargado", use_container_width=True)
        if st.button("Analizar con IA"):
            with st.spinner("Leyendo..."):
                prompt = "Analiza la imagen. Haz una tabla de productos y precios. Dime el total y clasifica el gasto."
                resultado = model.generate_content([prompt, imagen])
                st.markdown(resultado.text)
else:
    st.warning("👈 Introduce tu API Key para empezar.")
