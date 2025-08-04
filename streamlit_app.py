import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime

# Login system
def login():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == st.secrets["auth"]["username"] and password == st.secrets["auth"]["password"]:
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid username or password")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()

st.title("📊 Currency Automation Tender Dashboard")

# Load data
df = pd.read_csv("data.csv", parse_dates=["Tender Date"])

# Filters
product_filter = st.selectbox("Select Product", options=["All"] + sorted(df["Product"].unique().tolist()))
state_filter = st.selectbox("Select State", options=["All"] + sorted(df["State"].unique().tolist()))

filtered_df = df.copy()
if product_filter != "All":
    filtered_df = filtered_df[filtered_df["Product"] == product_filter]
if state_filter != "All":
    filtered_df = filtered_df[filtered_df["State"] == state_filter]

st.markdown("### 🗃 Tender Data")
st.dataframe(filtered_df)

st.markdown("### 📍 Tenders by State")
state_chart = filtered_df["State"].value_counts().reset_index()
state_chart.columns = ["State", "Count"]
st.bar_chart(state_chart.set_index("State"))

st.markdown("### 🔝 Products in Demand")
product_chart = filtered_df["Product"].value_counts().reset_index()
product_chart.columns = ["Product", "Count"]
st.bar_chart(product_chart.set_index("Product"))