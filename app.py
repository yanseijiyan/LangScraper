# Streamlit integration for user interaction
import streamlit as st
from main import scrape_website, process_documents

st.title('Web Scraping and Summarization with Streamlit')

# Create a text area for user input of URLs
urls_input = st.text_area("Enter the URLs for scraping, separated by a new line:")

# Button to initiate the scraping and summarization process
if st.button('Start Scraping and Summarize'):
    if urls_input:
        # Split the input URLs into a list, removing whitespace
        urls = [url.strip() for url in urls_input.split('\n') if url.strip()]

        with st.spinner('Performing web scraping...'):
            # Scrape each URL using the scrape_website function
            documents = [scrape_website(url) for url in urls]
            valid_documents = [doc for doc in documents if doc is not None]

        if valid_documents:
            # Process the collected documents for summarization
            with st.spinner('Processing summarization...'):
                summary_result = process_documents(valid_documents)

            # Display the final summarization
            st.subheader('Final Summarization:')
            st.write(f'Generated from {len(valid_documents)} documents.')
            st.write(summary_result["output_text"])
            
        else:
            # Display an error message if no valid documents were collected
            st.error('Failed to scrape any of the provided URLs.')
    else:
        # Display an error message if the URL input is empty
        st.error('Please enter at least one URL.')