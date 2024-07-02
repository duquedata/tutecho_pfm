import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Encuentra hoy qué hay en Idealista para Tutecho!

Dinos el número de habitaciones que necesitas, la zona y el alquiler máximo que se podría pagar.

Te mostramos los pisos que se ajustan más lo que nos has pedido.
"""

num_hab = st.slider("Numero de habitaciones", 1, 10, 1)
alquiler = st.slider("Alquiler a pagar €", 1, 3000, 0)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_hab * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(alquiler),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))

"""
Tenemos estos pisos disponibles
"""
df2 = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df2)
