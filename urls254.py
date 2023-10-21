import streamlit as st
import requests

def filter_urls(urls):
    valid_urls = []
    invalid_urls = []

    for url in urls:
        try:
            response = requests.head(url)
            if response.status_code == 200:
                valid_urls.append(url)
            else:
                invalid_urls.append(url)
        except requests.exceptions.RequestException:
            invalid_urls.append(url)

    return valid_urls, invalid_urls

st.title("URL Filtering App")

# Input for URLs
user_input = st.text_area("Enter a list of URLs (one per line):", height=200)

# Split the input into a list of URLs
user_input = user_input.strip()
urls = user_input.split("\n")

if st.button("Filter URLs"):
    valid_urls, invalid_urls = filter_urls(urls)

    # Display valid URLs
    if valid_urls:
        st.subheader("Valid URLs:")
        st.text("\n".join(valid_urls))
    else:
        st.write("No valid URLs found.")

    # Display invalid URLs
    if invalid_urls:
        st.subheader("Invalid URLs:")
        st.text("\n".join(invalid_urls))
    else:
        st.write("No invalid URLs found.")
