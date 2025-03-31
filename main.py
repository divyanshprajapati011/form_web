import streamlit as st
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="form"
)

mycursor = db.cursor()


st.header("welcome to divycart ")

name = st.text_input("enter your name : ")
fname = st.text_input("enter your father name : ")
email = st.text_input("enter your email : ")
add = st.text_area("enter your text : ")
class_data = st.selectbox("select your class ",(1,2,3,4,5,6,7,8,9,10))

button = st.button("Done")

if button :
    # st.markdown(f"""
    # name : {name} , father name : {fname}, email : {email}, address : {add} , class data : {class_data}""")
    query="INSERT INTO entry(name, fname, email, `add`, class) VALUES (%s, %s, %s, %s, %s)"
    values=(name,fname,email,add,class_data)
    mycursor.execute(query,values)
    db.commit()
    st.success(f"Thank you, {name}! Your entry has been recorded.")

