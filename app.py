import scipy.stats
import streamlit as st
import time

st.header('Lanzar una moneda')

# Inicializar el gráfico
chart = st.line_chart([0.5])

# Función para emular el lanzamiento de una moneda
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)  # Corrección de 'size'
    mean = 0  # Inicialización de 'mean'
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])  # Actualizar gráfico con cada iteración
        time.sleep(0.05)
    
    return mean

# Interfaz de usuario
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

# Lógica principal
if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    final_mean = toss_coin(number_of_trials)  # Llamar a la función
    st.write(f'La probabilidad final de obtener "1" fue: {final_mean:.2f}')
