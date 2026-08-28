import pandas as pd
import streamlit as st

st.set_page_config(layout="wide", page_title="Assessment Dashboard")

uploaded_file = st.sidebar.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.sidebar.title("Select Assessment Item")
    selected_name = st.sidebar.radio("Name", df["name"].tolist())

    selected_row = df[df["name"] == selected_name].iloc[0]

    st.header(selected_row["name"])

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("Description")
        st.write(
            selected_row["description"]
            if pd.notna(selected_row["description"])
            else "N/A"
        )
    with col2:
        st.subheader("Impact")
        st.write(
            selected_row["impact"] if pd.notna(selected_row["impact"]) else "N/A"
        )
    with col3:
        st.subheader("Remediation")
        st.write(
            selected_row["remediation"]
            if pd.notna(selected_row["remediation"])
            else "N/A"
        )
    with col4:
        st.subheader("Findings")
        st.write(
            selected_row["findings"]
            if pd.notna(selected_row["findings"])
            else "N/A"
        )
else:
    st.info("Please upload your Excel file from the sidebar.")