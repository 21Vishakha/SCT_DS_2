# app.py

import pandas as pd
import streamlit as st
import plotly.express as px

# ---- Page Config ----
st.set_page_config(page_title="Titanic Dashboard", layout="wide")

# ---- Load Data ----
df = pd.read_csv("train.csv")
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# ---- KPIs ----
total_passengers = len(df)
total_survivors = df['Survived'].sum()
total_dead = total_passengers - total_survivors
survival_rate = round(total_survivors / total_passengers, 2)

avg_age = round(df['Age'].mean(), 2)
avg_fare = round(df['Fare'].mean(), 2)
common_class = df['Pclass'].mode()[0]

# ---- Header ----
st.markdown("<h1 style='text-align: center; color: white;'>🚢 Titanic Survival Analysis</h1>", unsafe_allow_html=True)

# ---- KPIs Section ----
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("🎯 Survival Rate", f"{survival_rate}")
kpi2.metric("👥 Total Passengers", f"{total_passengers}")
kpi3.metric("✅ Total Survivors", f"{total_survivors}")
kpi4.metric("❌ Total Casualties", f"{total_dead}")

# ---- Survival by Class & Family Size ----
col1, col2 = st.columns(2)

with col1:
    fig1 = px.histogram(df, x='Pclass', color='Survived', barmode='group',
                        title="Survival by Passenger Class", color_discrete_sequence=px.colors.sequential.Oranges)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.histogram(df, x='FamilySize', color='Survived', barmode='group',
                        title="Survival by Family Size", color_discrete_sequence=px.colors.sequential.Oranges)
    st.plotly_chart(fig2, use_container_width=True)

# ---- Survival Pie Chart ----
fig3 = px.pie(df, names='Survived', title="Overall Survival Breakdown", hole=0.5,
              color='Survived', color_discrete_map={0: '#A0522D', 1: '#D2691E'})
st.plotly_chart(fig3, use_container_width=True)

# ---- Demographics Header ----
st.markdown("<h1 style='text-align: center; color: white;'>👤 Demographics & Fare Analysis</h1>", unsafe_allow_html=True)

# ---- More KPIs ----
kpi5, kpi6, kpi7 = st.columns(3)
kpi5.metric("📏 Average Age", f"{avg_age}")
kpi6.metric("💵 Average Fare", f"{avg_fare}")
kpi7.metric("🎟️ Most Common Class", f"{common_class}")

# ---- Age & Gender Distribution ----
col3, col4 = st.columns(2)

with col3:
    fig4 = px.histogram(df, x='Age', nbins=20, title="Age Distribution of Passengers",
                        color_discrete_sequence=px.colors.sequential.Oranges)
    st.plotly_chart(fig4, use_container_width=True)

with col4:
    fig5 = px.pie(df, names='Sex', title="Passenger Distribution by Gender",
                  color='Sex', color_discrete_map={'male': '#CD853F', 'female': '#F4A460'})
    st.plotly_chart(fig5, use_container_width=True)

# ---- Fare Distribution by Class ----
fig6 = px.histogram(df, x='Fare', color='Pclass', barmode='group',
                    title="Fare Distribution by Passenger Class",
                    color_discrete_sequence=px.colors.sequential.Oranges)
st.plotly_chart(fig6, use_container_width=True)