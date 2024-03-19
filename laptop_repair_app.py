import streamlit as st
from datetime import datetime, timedelta

# Streamlit app title
st.title('Laptop Repair Date Calculator')

# Function to calculate repair date
def calculate_repair_date(current_date):
    repair_date = current_date + timedelta(days=25)
    return repair_date

# Default current date
current_date = datetime.today()

# User input for current date
current_date_input = st.date_input('Enter Current Date', current_date)

# Calculate repair date
repair_date = calculate_repair_date(current_date_input)

# Show repair date
st.write(f"Your laptop is scheduled for repair on: {repair_date.strftime('%Y-%m-%d')}")

# Check if repair date has arrived
if current_date_input >= repair_date:
    st.write("Your laptop is being repaired.")
