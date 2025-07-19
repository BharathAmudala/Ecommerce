import streamlit as st
import pandas as pd

st.title("Walmart Sales  Dashboard")

# Load data
df = pd.read_csv("Walmart_Sales.csv")

st.header("Data Preview")
st.dataframe(df.head())

st.header("Summary Statistics")
st.write(df.describe())

st.header("Store Selection")
store_options = df['Store'].unique()
selected_store = st.selectbox("Select Store:", store_options)

filtered_df = df[df['Store'] == selected_store]
st.subheader(f"Sales Data for Store {selected_store}")
st.line_chart(filtered_df[['Weekly_Sales']].reset_index(drop=True))

st.header("Holiday Flag Distribution")
st.bar_chart(df['Holiday_Flag'].value_counts())

st.header("Temperature vs Weekly Sales")
st.scatter_chart(df[['Temperature', 'Weekly_Sales']])

st.markdown("---")
st.markdown("Sample Streamlit app for Walmart Sales data. Modify and extend as needed.")
