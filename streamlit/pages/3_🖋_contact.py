import streamlit as st

st.title ("Contact")

st.write("If you have any questions, comments, or suggestions for improvement, please don't hesitate to reach out. Your feedback is valuable to me!")

if "my_iput" not in st.session_state:
    st.session_state["my_input"] = ""

my_input =st.text_input("Type your text here",st.session_state["my_input"])
submit = st.button("Submit")

if submit:
     st.session_state["my_input"] = my_input
     st.write("Thank you for your feedback!")

