import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Hola. ¿Qué tipo de vivienda necesitamos hoy?",
    page_icon="👋",
)

st.write("# Bienvenido a Tutecho Search. La herramienta de búsqueda de Idealista 👋")

st.sidebar.success("Define tu búsqueda.")
"""
# Encuentra hoy qué hay en Idealista para Tutecho!

Dinos el número de habitaciones que necesitas, la zona y el alquiler máximo que se podría pagar.

Te mostramos los pisos que se ajustan más lo que nos has pedido.
"""

num_hab = st.slider("Numero de habitaciones", 1, 10, 1)
alquiler = st.slider("Alquiler a pagar €", 1, 3000, 0)



st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

"""
Tenemos estos pisos disponibles
"""
df2 = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df2)
