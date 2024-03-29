import streamlit as st

st.set_page_config(
    page_title = "Immo Prediction App",
    page_icon = "👋"
)

st.title(" 👋  Welcome ")
st.title("Welcome to Immo Eliza's Real Estate Price Prediction 🚀 ")
st.write("Hi there! Welcome to Immo Eliza's Real Estate Price Prediction page.")
st.write("I'm a student at BeCode, and as part of a big project, I've developed a machine learning model to make price predictions on real estate sales in Belgium for the real estate company Immo Eliza.")
st.write("The main goal of this project was to provide accurate price predictions for houses and apartments in Belgium, helping Immo Eliza's clients make informed decisions.")

# Create a session state variable to manage navigation
session_state = st.session_state.get("session_state", {"selected_page": None})

st.write("- Houses")
st.write("- Apartments (in maintenance)")


#st.write("Choose the type of real estate for which you'd like to make a prediction:")
# Handle button click events
# if st.button("Houses"):
#     # Redirect to the "houses" page
#     st.query_params(page="houses")
# elif st.button("Apartments (In Progress)"):
#     # Redirect to the "apartments" page
#     st.query_params(page="apartments")

st.write("  👈    Please select a real estate type in the sidebar.")

st.write("Please note that the prediction functionality for apartments is still in progress. Stay tuned for updates!")





st.sidebar.write("Made by Van Hoeke Caroline")
st.sidebar.write("Data-Science and AI student @Becode")
st.sidebar.write("Project: Immo-Eliza Real Estate Price Prediction")


