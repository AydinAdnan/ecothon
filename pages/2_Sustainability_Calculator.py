import streamlit as st
import pandas as pd

def main():
    st.title('Points Deduction System')

    # Load the points data from the CSV file
    points_data = pd.read_csv('data1.csv')

    # Get user input for the category
    category = st.selectbox('Select your category', ['Vehicle Emission', 'Water Consumption', 'Electricity Consumption'])

    if category == 'Vehicle Emission':
        # Get user input for the mode of transportation
        transport_mode = st.selectbox('Select your mode of transportation', ['Car', 'Bus/Train', 'Walk/Cycle'])

        # Deduct points based on the mode of transportation
        if transport_mode == 'Car':
            st.header('Car: Highest Points Deduction')
            car_kms = st.number_input("Enter kms driven : ")

            st.write('A comprehensive exploration into the section pertaining to private cars reveals why this choice incurs the most substantial points deduction. Data-driven insights underscore the profound environmental ramifications associated with personal vehicle usage.')
            points_data['Points'] -= 3*car_kms  # Assume 3 points are deducted for using a car
        elif transport_mode == 'Bus/Train':
            st.header('Bus/Train: Moderate Points Deduction')
            st.write('In this section, we illuminate the rationale behind assigning a moderate points deduction for the utilization of public transportation options. It elucidates how these choices embody a more sustainable alternative to private cars.')
            bus_kms = st.number_input("Enter kms driven : ")

            points_data['Points'] -= 2*bus_kms  # Assume 2 points are deducted for using a bus or train
        else:
            st.header('Walk/Cycle: No Points Deduction')
            st.write('The resplendent segment dedicated to sustainable alternatives elucidates the absence of points deduction when users opt for environmentally responsible modes of commuting, namely walking or cycling.')
            # No points are deducted for walking or cycling

    elif category == 'Water Consumption':
        # Get user input for the water usage
        water_usage = st.number_input('Enter your water usage')
        # Subtract the water usage from 50 and add the result to the points
        points_data['Points'] += 50 - water_usage

    else:  # Electricity Consumption
        # Get user input for the Kwh usage
        kwh_usage = st.number_input('Enter your Kwh usage')
        # Subtract the Kwh usage from 800 and add the result to the points
        points_data['Points'] += 800 - kwh_usage

    # Save the updated points data back to the CSV file
    points_data.to_csv('data1.csv', index=False)

    st.write('Your current points:', points_data['Points'].sum())

if __name__ == "__main__":
    main()
