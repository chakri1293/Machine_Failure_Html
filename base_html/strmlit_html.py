import streamlit as st

def main():
    # Load your HTML content
    with open("base_html/index.html", "r") as f:
        html_content = f.read()

    # Display the HTML content
    st.write(html_content, unsafe_allow_html=True)

if __name__ == "__main__":
    main()