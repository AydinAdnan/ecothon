import streamlit as st

def login_page():
    st.title("Login")
    st.header("Welcome to the Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            # Add your login logic here
            st.success("Logged in successfully!")
        else:
            st.warning("Please enter a username and password.")

    if st.button("Register"):
        st.session_state["page"] = "register"

def register_page():
    st.title("Register Page")
    st.header("Welcome to the Register Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if username and password:
            # Add your registration logic here
            st.success("Registered successfully!")
        else:
            st.warning("Please enter a username and password.")

    if st.button("Go back to Login"):
        st.session_state["page"] = "login"

def main():
    if "page" not in st.session_state:
        st.session_state["page"] = "login"

    if st.session_state["page"] == "login":
        login_page()
    elif st.session_state["page"] == "register":
        register_page()

if __name__ == "__main__":
    main()