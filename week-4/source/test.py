import streamlit as st

st.logo('./logo.png')


def get_name():
    st.write("Thai")
agree = st.checkbox("I agree",on_change=get_name)
if agree:
    st.write("Great!")

st.radio(
    "Your favorite color:",
    ['Yellow', 'Bleu'],
    captions = ['Vàng', 'Xanh']
)

option = st.selectbox(
    "Your contact:",
    ("Email", "Home phone", "Mobile phone"))

st.write("Selected:", option)

options = st.multiselect(
    "Your favorite colors:",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"])

st.write("You selected:", options)

color = st.select_slider(
    "Your favorite color:",
    options=["red", "orange", "violet"])
st.write("My favorite color is", color)

st.divider()

if st.button("Say hello"):
    st.write("Hello")
else:
    st.write("Goodbye")

st.link_button(
    "Go to Google",
    "https://www.google.com.vn/")

st.divider()
title = st.text_input(
    "Movie title:", "Life of Brian"
)
st.write("The current movie title is", title)

st.divider()

uploaded_files = st.file_uploader(
    "Choose files", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)\

st.divider()

number = st.number_input("Insert a number")
st.write("The current number is ", number)

values = st.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

st.divider()
with st.form("my_form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input('First Name')
    l_name = col2.text_input('Last Name')
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("First Name: ", f_name, " - Last Name:", l_name)