import streamlit as st
from email_generator import generate_email


st.title("AI Email Generator")
st.session_state.setdefault("email_history", [])
st.session_state.setdefault("current_email", "")

purpose = st.text_area( "Enter purpose" )
tone = st.selectbox( "Select Tone", [ "Formal", "Friendly", "Professional" ] )
recipient = st.selectbox( "Recipient", [ "Manager", "Client", "Student" ] )

length = st.selectbox( "Email Length", [ "Short", "Medium", "Long" ] )
sender_name = st.text_input( "Enter your name (optional)" )

if st.button( "Generate Email" ):
    if purpose:
        output = generate_email(purpose, tone, recipient, sender_name, length)
        st.session_state["current_email"] = output
        st.session_state["email_history"].append(
            {
                "purpose": purpose,
                "tone": tone,
                "recipient": recipient,
                "length": length,
                "email": output,
            }
        )
    else:
        st.warning("Enter purpose")

if st.session_state["current_email"]:
    st.subheader("Generated Email")
    st.write(st.session_state["current_email"])

if st.session_state["email_history"]:
    st.subheader("Email History")
    for index, item in enumerate(reversed(st.session_state["email_history"]), start=1):
        with st.expander(f"Email {index}: {item['recipient']} · {item['tone']} · {item['length']}"):
            st.write(f"**Purpose:** {item['purpose']}")
            st.write(item["email"])

st.download_button(
    label="Download Email",
    data=st.session_state["current_email"],
    file_name="generated_email.txt",
    mime="text/plain",
    disabled=not st.session_state["current_email"],
)
