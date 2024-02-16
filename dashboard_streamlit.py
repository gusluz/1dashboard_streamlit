import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("H_Admission_Data.csv")

#CONFIG PAGE
st.set_page_config(
    page_title="Dashboard de Pacientes Cardíacos",
    page_icon=":heart:",
    layout="wide"
)
st.title("Dashboard de Pacientes Cardíacos")
st.subheader("Este dashboard mostra algumas análises sobre os dados de pacientes cardíacos admitidos em um hospital na Índia entre 2017 e 2019.")

#SIDEBAR
st.sidebar.header("Filtros")
start_date = st.sidebar.date_input("Data inicial", value=pd.to_datetime("2017-01-01"))
end_date = st.sidebar.date_input("Data final", value=pd.to_datetime("2019-12-31"))
gender = st.sidebar.selectbox("Sexo", options=["Todos", "M", "F"])

st.markdown("""
<style>
    .reportview-container {
        background-color: #defffa;
    }
    [data-testid=stSidebar] {
        background-color: #b3ffd6;
    }
</style>
""", unsafe_allow_html=True)

#FILTERS
if gender != "Todos":
    df = df[df["GENDER"] == gender]

df["D.O.A"] = pd.to_datetime(df["D.O.A"], format="%d/%m/%Y")
df["D.O.D"] = pd.to_datetime(df["D.O.D"], format="%d/%m/%Y")

df["YEAR"] = df["D.O.A"].dt.year.astype(str)

df = df[(df["D.O.A"] >= pd.to_datetime(start_date)) & (df["D.O.A"] <= pd.to_datetime(end_date))]

#1
df_mean = df.groupby(["AGE", "YEAR"])["DURATION OF STAY"].mean().reset_index()

#LINE GRAPHIC (MEAN DURATION OF STAY/AGE/YEAR)
fig1 = px.line(df_mean, x="AGE", y="DURATION OF STAY", color="YEAR", labels={
    "AGE": "Idade",
    "DURATION OF STAY": "Média de Dias Internados",
    "YEAR": "Ano"
})

fig1.update_layout(title="Média de Dias Internados por Idade")

st.plotly_chart(fig1, use_container_width=True)

#2
left, right = st.columns([1,4])

#CHECKBOX 
with left:
    dm = st.checkbox("Diabetes Mellitus", value=False)
    htn = st.checkbox("Hipertensão", value=False)
    smoking = st.checkbox("Tabagismo", value=False)
    alcohol = st.checkbox("Consumo de Álcool", value=False)

#FILTERS
if dm:
    df = df[df["DM"] == 1]
if htn:
    df = df[df["HTN"] == 1]
if smoking:
    df = df[df["SMOKING "] == 1]
if alcohol:
    df = df[df["ALCOHOL"] == 1]

#SCATTER GRAPH (AGE/DURATION OF STAY)
fig2 = px.scatter(df, x="AGE", y="DURATION OF STAY", color="YEAR", 
                  labels={
    "AGE": "Idade",
    "DURATION OF STAY": "Dias Internados",
    "YEAR": "Ano"
})

fig2.update_layout(title="Correlação entre Fatores de Risco e Dias Internados")

with right:
    st.plotly_chart(fig2, use_container_width=True)