import streamlit as st
import mysql.connector
from mysql.connector import Error

st.header("Welcome to Divycart")

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="form"
    )

    if db.is_connected():
        st.success("Connected to the database")

    mycursor = db.cursor()

    name = st.text_input("Enter your name: ")
    fname = st.text_input("Enter your father's name: ")
    email = st.text_input("Enter your email: ")
    add = st.text_area("Enter your address: ")
    class_data = st.selectbox("Select your class", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    button = st.button("Done")

    if button:
        query = "INSERT INTO entry(name, fname, email, `add`, class) VALUES (%s, %s, %s, %s, %s)"
        values = (name, fname, email, add, class_data)
        try:
            mycursor.execute(query, values)
            db.commit()
            st.success(f"Thank you, {name}! Your entry has been recorded.")
        except Error as e:
            st.error(f"Error: {e}")
            db.rollback()

except Error as e:
    st.error(f"Error connecting to MySQL: {e}")
