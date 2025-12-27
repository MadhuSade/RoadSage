import streamlit as st
import joblib

model = joblib.load("road_sage_model.pkl")

st.title("🚦 RoadSage – Traffic Congestion Prediction")

vehicles = st.number_input("Vehicle Count", min_value=0)
hour = st.number_input("Hour (0–23)", min_value=0, max_value=23)
weekday = st.number_input("Weekday (0=Mon, 6=Sun)", min_value=0, max_value=6)
junction = st.number_input("Junction ID", min_value=1)

if st.button("Predict Traffic"):
    result = model.predict([[vehicles, hour, weekday, junction]])[0]

    labels = {0:"Low 🟢", 1:"Medium 🟡", 2:"High 🔴"}
    st.success(labels[result])

    if result == 2:
        st.warning("Heavy traffic ahead!")
    elif result == 1:
        st.info("Moderate traffic")
    else:
        st.success("Road is clear")
