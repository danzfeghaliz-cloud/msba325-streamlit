# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 14:30:59 2025

@author: User
"""

import streamlit as st
import plotly.express as px
import pandas as pd

# Title and description
st.title("Interactive Visualizations with Streamlit")
st.write("This app explores the relationship between GDP per Capita and Life Expectancy across countries and years.")
st.markdown("""
**Goal.** Explore how economic prosperity relates to health outcomes using two linked views:
1) **Scatter:** GDP per capita vs. life expectancy for a chosen year.  
2) **Line chart:** GDP per capita over time for the selected continent.

**How to use it.**
- Move the **Year** slider to change the scatter’s data.
- Change the **Continent** dropdown to update the time-series.

**What to look for.**
- Countries with higher GDP per capita typically show higher life expectancy.
- Growth patterns differ by continent; some regions accelerate after 2000.
""")

# Load dataset (Gapminder sample, you can replace with your dataset)
df = px.data.gapminder()

# --- Interactivity 1: Year Slider ---
year = st.slider("Select Year", int(df['year'].min()), int(df['year'].max()), 2007)
filtered_df = df[df['year'] == year]

# Visualization 1: Scatter plot
st.subheader("GDP per Capita vs Life Expectancy")
fig1 = px.scatter(filtered_df,
                  x="gdpPercap", y="lifeExp",
                  size="pop", color="continent",
                  hover_name="country",
                  title=f"GDP vs Life Expectancy in {year}")
st.plotly_chart(fig1)

# --- Interactivity 2: Continent Dropdown ---
continent = st.selectbox("Select Continent", df["continent"].unique())
filtered_cont = df[df["continent"] == continent]

# Visualization 2: Line plot
st.subheader("GDP Growth over Time")
fig2 = px.line(filtered_cont,
               x="year", y="gdpPercap",
               color="country",
               title=f"GDP per Capita Trend in {continent}")
st.plotly_chart(fig2)

st.markdown("**Insights:** Use the slider to explore different years in the scatter plot, and the dropdown to view GDP trends for different continents.")
