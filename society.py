import streamlit as st
import pywhatkit as kit
from datetime import datetime

# List of WhatsApp numbers
whatsapp_numbers = ["+1234567890"]  # Replace with actual numbers

def send_whatsapp_message(notice, recipient_number):
    """Send WhatsApp message using pywhatkit."""
    try:
        # Send message at the current time + 1 minute
        now = datetime.now()
        hour, minute = now.hour, now.minute + 1
        
        # Send message
        kit.sendwhatmsg(recipient_number, notice, hour, minute)
        return "Message sent successfully!"
    except Exception as e:
        return f"Failed to send message: {e}"

# Streamlit app
st.title("Housing Society Notice Board")

# Input notice
st.subheader("Post a Notice")
notice = st.text_area("Type the notice to be displayed:")

if st.button("Submit Notice"):
    if notice:
        st.success("Notice submitted successfully!")
        
        # Send notice to all WhatsApp numbers
        st.subheader("Sending to WhatsApp Numbers")
        for number in whatsapp_numbers:
            result = send_whatsapp_message(notice, number)
            st.write(f"{result} to {number}")
    else:
        st.error("Notice cannot be empty.")

# Add a new WhatsApp number
st.subheader("Add a WhatsApp Number")
new_number = st.text_input("Enter the new WhatsApp number (format: +1234567890):")

if st.button("Add Number"):
    if new_number.startswith("+"):
        whatsapp_numbers.append(new_number)
        st.success(f"Number {new_number} added successfully!")
    else:
        st.error("Invalid number format. Use format: +1234567890")

st.write("Current WhatsApp Numbers:")
for num in whatsapp_numbers:
    st.write(num)