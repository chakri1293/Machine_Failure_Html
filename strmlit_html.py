import streamlit as st
import os

def main():
    # Print current working directory
    st.write("Current Working Directory:", os.getcwd())

    # List contents of the "assets" folder
    assets_folder = "assets"
    st.write("Contents of 'assets' folder:", os.listdir(assets_folder))

    # Load your HTML content
    with open("index.html", "r") as f:
        html_content = f.read()

    # Display the HTML content
    st.write(html_content, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
