import pandas as pd
import streamlit as st
# reading CSV file
leaderboard = pd.read_csv("data1.csv")

# converting column data to list

username = leaderboard['Username'].tolist()
password = leaderboard['Password'].tolist()
points = leaderboard['Points'].tolist()

for i in range (len(username)-1):
    for j in range (len(username)-i-1):
        if points[j] < points[j + 1]:
            points[j], points[j + 1] = points[j + 1], points[j]
            username[j], username[j + 1] = username[j + 1], username[j]
            password[j], password[j + 1] = password[j + 1], password[j]
         

st.title("Leaderboard")

# Podium display for the top 3 positions
with st.container():
    for i in range(3):
        st.markdown(f"<h1 style='text-align: center; background-color: {'gold' if i == 0 else 'silver' if i == 1 else 'peru'}; color: {'black' if i == 0 else 'black'};'>{i + 1}</h1>", unsafe_allow_html=True)
        st.write(f"**Username:** {username[i]} | **Points:** {points[i]}")

# Display the next 10 users initially, showing only "username" and "points" columns
num_users_to_display = 10
st.markdown("<h2>Leaderboard (4th and below)</h2>", unsafe_allow_html=True)
for i in range(3, min(len(username), num_users_to_display + 3)):
    st.write(f"**Username:** {username[i]} | **Points:** {points[i]}")

# Add a "View More" button to show additional users
if len(username) > num_users_to_display + 3:
    view_more = st.button("View More")

# Display additional users if "View More" button is clicked
if view_more:
    remaining_users = len(username) - (num_users_to_display + 3)
    for i in range(num_users_to_display + 3, min(len(username), num_users_to_display + 3 + remaining_users)):
        st.write(f"**Username:** {username[i]} | **Points:** {points[i]}")
    if remaining_users <= 0:
        st.write("No more users to display.")