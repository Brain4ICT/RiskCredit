import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Définition des équations pour chaque pays
equations = {
    "Egypt": lambda X: 0.0003 + (0.0184 * X[0]) + (-0.0148 * X[1]) + (-0.0189 * X[2]) + (-0.0065 * X[3]) + (0.0708 * X[4]) + (-0.1600 * X[5]) + (-0.0305 * X[6]) + (1.1360 * X[7]),
    "Morocco": lambda X: 0.0001 + (-0.0510 * X[0]) + (0.0117 * X[1]) + (0.0028 * X[2]) + (0.0378 * X[3]) + (-0.0336 * X[4]) + (0.0493 * X[5]) + (0.0751 * X[6]) + (0.9030 * X[7]),
    "SaudiArabia": lambda X: 0.0001 + (-0.1013 * X[0]) + (0.0615 * X[1]) + (0.0161 * X[2]) + (0.1099 * X[3]) + (-0.1256 * X[4]) + (0.0188 * X[5]) + (0.1397 * X[6]) + (0.8701 * X[7])
}

# Titre de l'application
st.title("A Web Application Sovereign Credit Risk Prediction")

# Sélection du pays
country = st.selectbox("Select a Country", list(equations.keys()))

# Entrée des valeurs des variables
st.subheader("Input the values for the 8 variables")
X = []
for i in range(1, 9):
    value = st.number_input(f"X{i}", value=0.0, format="%.4f")
    X.append(value)

# Bouton de prédiction
if st.button("Predict"):
    # Vérification des dimensions des entrées
    if len(X) == 8:
        # Calcul des 80 prochaines valeurs prévues
        forecast_horizon = 80
        forecast = []
        last_values = X[:]

        for _ in range(forecast_horizon):
            next_val = equations[country](last_values)
            forecast.append(next_val)
            last_values = last_values[1:] + [next_val]

        # Affichage des résultats
        st.subheader(f"Next {forecast_horizon} Predicted Values for {country}")
        fig, ax = plt.subplots()
        ax.plot(range(1, forecast_horizon + 1), forecast, marker="o", linestyle="-", color="b")
        ax.set_title(f"{country} - Predicted Values")
        ax.set_xlabel("Horizon")
        ax.set_ylabel("Predicted Value")
        st.pyplot(fig)
    else:
        st.error("Please provide all 8 input values.")
