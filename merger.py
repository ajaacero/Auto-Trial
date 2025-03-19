import streamlit as st
import pandas as pd

st.title("Dataset Merger and Viewer")

# upload dataset 1 and dataset 2
uploaded_file1 = st.file_uploader("Upload Dataset 1 (Excel)", type=["xlsx"])
uploaded_file2 = st.file_uploader("Upload Dataset 2 (Excel)", type=["xlsx"])

if uploaded_file1 and uploaded_file2:
    df1 = pd.read_excel(uploaded_file1)
    df2 = pd.read_excel(uploaded_file2)
    
    # pivot dataset 2 so each OPERATIONNAME becomes a column with REJECTQTY values
    df2_pivot = df2.pivot_table(index="CONTAINERNAME", 
                                 columns="OPERATIONNAME", 
                                 values="REJECTQTY", 
                                 aggfunc="sum").reset_index()

    # rename columns for clarity
    df2_pivot.columns = ["CONTAINERNAME"] + [f"REJECT_{col}" for col in df2_pivot.columns[1:]]

    # merge dataset 1 and the pivoted dataset 2
    df_merged = df1.merge(df2_pivot, on="CONTAINERNAME", how="left")
    df_merged.fillna(0, inplace=True)
    df_merged.sort_values(by="TRACKOUTDATE", inplace=True)
    
    st.subheader("Merged Dataset")
    st.write(df_merged)
    
    # download button for merged dataset
    @st.cache_data
    def convert_df(df):
        return df.to_excel(index=False, engine='openpyxl')
    
    st.download_button(label="Download Merged Dataset", 
                       data=convert_df(df_merged),
                       file_name="merged_dataset.xlsx",
                       mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
