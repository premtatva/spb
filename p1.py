import streamlit as st
import time

# Configure the Streamlit page
st.set_page_config()

# Main title for the app
st.title("Score Tracking System For Sports")

# Dropdown to select the sport
sport_name = st.selectbox("Select The Sport:", ["Basketball", "Volleyball", "Soccer"])

# Basketball scorecard function
if sport_name == "Basketball":
    
    # Define function for basketball scorecard
    def basketball_scorecard():
        st.title("Basketball Scorecard")
        
        # Dropdown for quarters
        quater = st.selectbox("Quarter:", ["1", "2", "3", "4"])
        
        # Input fields for team names
        team1_name = st.text_input("Team 1 Name", "Team 1")
        team2_name = st.text_input("Team 2 Name", "Team 2")
        
        # Input fields for scores
        team1_score = st.number_input(team1_name + " Number of Baskets", value=0, step=1)
        team2_score = st.number_input(team2_name + " Number of Baskets", value=0, step=1)
        
        # Calculate the difference in scores
        total1_score = team1_score - team2_score
        total2_score = team2_score - team1_score
        
        # Display total scores
        st.write(team1_name + " Total Score: " + str(team1_score))
        st.write(team2_name + " Total Score: " + str(team2_score))
        
        # Determine and display leading team or tie based on quarter
        if quater in ["1", "2", "3"]:
            if team1_score > team2_score:
                st.subheader(team1_name + " leads by " + str(total1_score) + " Basket")
            elif team1_score < team2_score:
                st.subheader(team2_name + " leads by " + str(total2_score) + " Basket")
            elif team1_score == team2_score and team1_score != 0 and team2_score != 0:
                st.subheader("The Scores Are Equal")
                
        # Determine and display winning team or tie at the end of game
        if quater == "4":
            if team1_score > team2_score:
                st.subheader(team1_name + " Wins!!!")
            elif team1_score < team2_score:
                st.subheader(team2_name + " Wins!!!")
            elif team1_score == team2_score and team1_score != 0 and team2_score != 0:
                st.subheader("The Scores Are Equal")

    # Call basketball scorecard function
    basketball_scorecard()
    
    # Timer functionality for basketball game
    user_input = st.text_input("Enter Time Period Of The Game:", "0")
    ph = st.empty()
    N = int(user_input) * 60

    reset_button = st.button("Reset")
    start_button = st.button("Start The Game")
    
    if start_button:
        for secs in range(N, -1, -1):
            mm, ss = secs // 60, secs % 60
            if secs == 0:
                ph.subheader("Time out, End Of Quarter")
                break
            else:
                ph.header(f"Countdown: {mm:02d}:{ss:02d}")
                time.sleep(1)
            if reset_button:
                N = int(user_input) * 60
                reset_button = False

# Volleyball scorecard function
if sport_name == "Volleyball":
    
    # Define function for volleyball scorecard
    def volleyball_scorecard():
        st.title("Volleyball Scorecard")
        
        # Dropdown for sets
        sets = st.selectbox("Sets:", ["1", "2", "3", "4", "5"])
        
        # Input fields for team names
        team1_name = st.text_input("Team 1 Name", "Team 1")
        team2_name = st.text_input("Team 2 Name", "Team 2")
        
        # Input fields for number of sets won
        number1_sets = st.number_input("Number of sets won by team 1", value=0, step=1, max_value=5)
        number2_sets = st.number_input("Number of sets won by team 2", value=0, step=1, max_value=5)
        
        # Depending on selected set, adjust maximum points and input fields for scores
        if sets in "1234":
            st.subheader("Maximum Points in set = 25")
            team1_score = st.number_input(team1_name + " Score", value=0, step=1, max_value=25)
            team2_score = st.number_input(team2_name + " Score", value=0, step=1, max_value=25)
        elif sets == "5":
            st.subheader("Maximum Points = 15")
            team1_score = st.number_input(team1_name + " Score", value=0, step=1, max_value=15)
            team2_score = st.number_input(team2_name + " Score", value=0, step=1, max_value=15)
        
        # Display total scores
        st.write(team1_name + " Total Score: " + str(team1_score))
        st.write(team2_name + " Total Score: " + str(team2_score))
        
        # Calculate score difference
        total1_score = team1_score - team2_score
        total2_score = team2_score - team1_score
        
        # Display which team leads or if scores are equal
        if team1_score < 25 and team1_score > team2_score:
            st.subheader(team1_name + " Leads by " + str(total1_score) + " points")
        elif team2_score < 25 and team2_score > team1_score:
            st.subheader(team2_name + " Leads by " + str(total2_score) + " points")
        elif team1_score == 25:
            st.subheader(team1_name + " Wins the set!!!")
        elif team2_score == 25:
            st.subheader(team2_name + " Wins the set!!!")
        else:
            st.subheader("The Scores Are Equal.")
        
        # Determine and display match winner or tie
        if number1_sets > number2_sets:
            st.header("Team 1 Wins the match!!!")
        elif number2_sets > number1_sets:
            st.header("Team 2 Wins the match!!!")
        else:
            st.header("It's A Tie")

    # Call volleyball scorecard function
    volleyball_scorecard()

# Soccer scorecard function
if sport_name == "Soccer":
    
    # Define function for soccer scorecard
    def soccer_scorecard():
        st.title("Soccer Scorecard")
        st.markdown("Duration of Game: 90 mins")
        
        # Input fields for team names and scores
        team1_name = st.text_input("Team 1 Name", "Team 1")
        team2_name = st.text_input("Team 2 Name", "Team 2")
        team1_score = st.number_input(team1_name + " Number of Goals", value=0, step=1)
        team2_score = st.number_input(team2_name + " Number of Goals", value=0, step=1)
        
        # Display total scores
        st.write(team1_name + " Total Score: " + str(team1_score))
        st.write(team2_name + " Total Score: " + str(team2_score))
        
        # Function to handle timer and game end logic
        def main():
            st.title("Timer")
            
            # Initialize countdown timer in session state
            if 'countdown_seconds' not in st.session_state:
                st.session_state.countdown_seconds = 0
            
            # Input field for game duration
            user_input = st.text_input("Enter Time Period Of The Game (in minutes):", "90")
            
            # Convert input to seconds
            if user_input.isdigit():
                N = int(user_input) * 60
            else:
                N = 0
            
            # Buttons for reset and start
            reset_button = st.button("Reset")
            start_button = st.button("Start")
            
            # Start the timer when start button is pressed
            if start_button:
                st.session_state.countdown_seconds = N
            
            # Placeholder to display countdown
            countdown_placeholder = st.empty()
            
            # Countdown loop
            while st.session_state.countdown_seconds > 0:
                mm = st.session_state.countdown_seconds // 60
                ss = st.session_state.countdown_seconds % 60
                countdown_placeholder.subheader(f"Countdown: {mm:02d}:{ss:02d}")
                
                # Sleep for one second
                time.sleep(1)
                
                # Decrement countdown timer
                st.session_state.countdown_seconds -= 1
                
                # Game over condition
                if st.session_state.countdown_seconds == 0:
                    countdown_placeholder.header("Time out, Game Over")
                    if team1_score > team2_score:
                        countdown_placeholder.header(team1_name + " Wins!!!")
                    elif team2_score > team1_score:
                        countdown_placeholder.header(team2_name + " Wins!!!")
                    elif team2_score == team1_score:
                        countdown_placeholder.header("It's A Tie!")

        # Call main function
        if __name__ == "__main__":
            main()

    # Call soccer scorecard function
    soccer_scorecard()
