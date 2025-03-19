import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# app title
st.title("Manufacturing Insights Dashboard")

# file upload
st.sidebar.header("Upload Excel Files")
dataset1 = st.sidebar.file_uploader("Upload Dataset 1 (Production Data)", type=["xlsx", "csv"])
dataset2 = st.sidebar.file_uploader("Upload Dataset 2 (Defect Data)", type=["xlsx", "csv"])

# insight selection
st.sidebar.header("Select Insights")
options = st.sidebar.multiselect("Choose Analysis:", [
    "Machine-Specific Issues", "Process Steps Analysis", "Devices Defect Analysis"
])

if dataset1 and dataset2:
    df1 = pd.read_excel(dataset1) if dataset1.name.endswith("xlsx") else pd.read_csv(dataset1)
    df2 = pd.read_excel(dataset2) if dataset2.name.endswith("xlsx") else pd.read_csv(dataset2)
    
    st.write("### Preview of Dataset 1:")
    st.dataframe(df1.head())
    st.write("### Preview of Dataset 2:")
    st.dataframe(df2.head())
    
    if "Machine-Specific Issues" in options:
        st.subheader("Machine-Specific Defect Trends")
        machine_defects = df2.groupby("RESOURCENAME")["DEFECT_COUNT"].sum().reset_index()
        fig, ax = plt.subplots()
        ax.bar(machine_defects["RESOURCENAME"], machine_defects["DEFECT_COUNT"], color='blue')
        plt.xticks(rotation=90)
        plt.xlabel("Machine")
        plt.ylabel("Defect Count")
        plt.title("Defects per Machine")
        st.pyplot(fig)
    
    if "Process Steps Analysis" in options:
        st.subheader("Defects by Process Steps")
        process_defects = df2.groupby("FROMSTEP")["DEFECT_COUNT"].sum().reset_index()
        st.bar_chart(process_defects.set_index("FROMSTEP"))
    
    if "Devices Defect Analysis" in options:
        st.subheader("Defects per Device")
        device_defects = df2.groupby("PRODUCT")["DEFECT_COUNT"].sum().reset_index()
        st.bar_chart(device_defects.set_index("PRODUCT"))
else:
    st.warning("Please upload both datasets to proceed.")
