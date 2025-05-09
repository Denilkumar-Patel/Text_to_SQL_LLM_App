from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import pyodbc
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

server= os.getenv("SQL_SERVER") 
database= os.getenv("SQL_DATABASE")

prompt="""
    You are an expert in converting English questions to SQL query!
    The SQL database has the name DbDenil_Training and has the following tables - [production].[brands], [production].[categories], [production].[products], [production].[stocks], [sales].[customers], [sales].[order_items], [sales].[orders], [sales].[staffs], [sales].[stores]
    also the sql code should not have ''' or "" or '' symbol in begining or end or in the entire output and sql word in output, output should be in this format SELECT * FROM [users]


    """

def get_gemini_response(question, prompt): 
    model=genai.GenerativeModel("gemini-1.5-pro-002")
    response=model.generate_content([prompt, question])    
    return response.text

def read_sql_query(sql, server, database):
    conn = pyodbc.connect(
        f"DRIVER={{SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )

    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows




# streamlit app

st.set_page_config(page_title="I can Retrive Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ", key="input")

submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, server, database
    )
    st.subheader("The Resposne is ")
    for row in data:
        print(row)
        st.header(row)