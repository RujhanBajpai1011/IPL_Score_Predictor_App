import streamlit as st
import numpy as np
import pickle
import os

st.set_page_config(page_title="IPL Score Prediction", layout="centered")

st.title("IPL score Prediction App")

menu=st.sidebar.selectbox("Choose a section",["🏠Home", "📝 Input Match Details", "📈Show Prediction", 
                          "🔍Explore DataSet"])

if menu=="🏠Home":
    st.subheader("Welcome To IPL Score Prediction App !")

    st.markdown(""" 
    This App predicts the final score of an IPL match based on current match conditions such as :
    - Batting Team
    - Bowling Team
    - Overs Completed 
    - Runs and Wickets So far
    - Recent over performance

    The Back end uses Machine Learning Algorithm To make accurate Score Predictions
    """)

if menu==("📝 Input Match Details"):
    st.markdown("Enter Match Details")
    Teams= ("Chennai Super Kings",
            "Delhi Daredevils",
            "Kings XI Punjab",
            "Kolkata Knight Riders",
            "Mumbai Indians",
            "Rajasthan Royals",
            "Royal Challengers Bangalore",
            "Sunrisers Hyderabad")

    cities=("Ahmedabad",
            "Bangalore",
            "Chennai",
            "Delhi",
            "Hyderabad",
            "Jaipur",
            "Kolkata",
            "Lucknow", 
            "Mumbai",
            "Pune",
            "Raipur",
            "Ranchi",
            "Visakhapatnam",
            "Dharamsala",
            "Indore",
            "Abu Dhabi",
            "Dubai",
            "Sharjah")
    st.session_state.batting_team= st.selectbox("Select The Batting Team", Teams)
    st.session_state.bowling_team= st.selectbox("Select The Boeling Team", Teams)
    st.session_state.city= st.selectbox("Select Match City", cities)

    if st.session_state.batting_team == st.session_state.bowling_team:
        st.error("⚠️ Batting Team and Bowling Teams can not be same . Please select different teams.")
    else:
        st.success("✅ Teams selected successfully.")

        st.session_state.overs=st.slider("Overs Completed" , min_value=5.1 , max_value=20.0, step=0.1)
        st.session_state.runs=st.number_input("Current Runs", min_value=0, max_value=354, step=1)
        st.session_state.wickets=st.slider("Wickets fallen", 0, 9)
        st.session_state.runs_last_5=st.number_input("Runs scored in last 5 overs", min_value=0, max_value=st.session_state.runs)
        st.session_state.wickets_last_5=st.number_input("Wickets lost in last 5 overs", min_value=0, max_value=st.session_state.wickets)

if menu == "📈Show Prediction":
    if "batting_team" in st.session_state and "bowling_team" in st.session_state:
        if st.session_state.batting_team == st.session_state.bowling_team:
            st.error("Batting Team and Bowling Teams are Same. Please Change The Teams")
        else:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))

            filename = os.path.join(BASE_DIR, 'ml_model.pkl')
            # with open(filename, 'rb') as f:
            #     model = pickle.load(f)
            model = pickle.load(open(filename, 'rb'))


            # Encode batting team
            team_encoding = {
                'Chennai Super Kings': [1,0,0,0,0,0,0,0],
                'Delhi Daredevils': [0,1,0,0,0,0,0,0],
                'Kings XI Punjab': [0,0,1,0,0,0,0,0],
                'Kolkata Knight Riders': [0,0,0,1,0,0,0,0],
                'Mumbai Indians': [0,0,0,0,1,0,0,0],
                'Rajasthan Royals': [0,0,0,0,0,1,0,0],
                'Royal Challengers Bangalore': [0,0,0,0,0,0,1,0],
                'Sunrisers Hyderabad': [0,0,0,0,0,0,0,1]
            }

            if st.button("Predicted Final Score"):
                bat_vector = team_encoding[st.session_state.batting_team]
                bowl_vector = team_encoding[st.session_state.bowling_team]

                features = bat_vector + bowl_vector + [
                    st.session_state.runs,
                    st.session_state.wickets,
                    st.session_state.overs,
                    st.session_state.runs_last_5,
                    st.session_state.wickets_last_5
                ]

                input_array = np.array([features])
                prediction = model.predict(input_array)[0]
                st.success(f"Predicted Final Score: {int(prediction)-5} to {int(prediction)+5} Runs")
    else:
        st.warning("⚠️Please enter Details under 'Input Match Details'.")
