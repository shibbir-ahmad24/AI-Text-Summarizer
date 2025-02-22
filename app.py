import streamlit as st
from summary import summarizer

def main():
    # Load the custom CSS file for styling
    st.markdown("""
        <style>
            /* Importing Google Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');
            body {
                background: #f7f7f7;
                font-family: 'Roboto', sans-serif;
            }

            /* Header styling */
            .header {
                font-size: 2rem;
                font-weight: bold;
                color: #007bff;
                text-align: center;
                margin-bottom: 30px;
            }

            /* Card for results */
            .result-card {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
            }

            /* Button styles */
            .stButton>button {
                background-color: #007bff;
                color: white;
                font-size: 16px;
                padding: 12px 40px;
                border-radius: 5px;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.3s ease;
            }

            .stButton>button:hover {
                background-color: #0056b3;
                transform: scale(1.05);
            }

            /* Title for summary */
            .section-title {
                font-size: 1.6rem;
                font-weight: 600;
                color: #333;
            }

            /* Summary Text Formatting */
            .summary-text {
                background-color: #f8f9fa;
                border-radius: 8px;
                padding: 15px;
                font-size: 1rem;
                white-space: pre-wrap;
                word-wrap: break-word;
            }

            .footer {
                text-align: center;
                font-size: 0.9rem;
                color: #888;
                margin-top: 40px;
            }
        </style>
    """, unsafe_allow_html=True)

    # App Title
    st.markdown("<div class='header'>AI Text Summarizer</div>", unsafe_allow_html=True)
    st.write("Paste your text below and let the AI generate a concise summary for you.")

    # Text input area for raw text
    rawtext = st.text_area("Paste your text here...", height=200, placeholder="Enter your content...")

    # Submit button for generating the summary
    if st.button("Generate Summary"):
        if rawtext:
            with st.spinner('Generating summary...'):
                try:
                    summary, len_summ = summarizer(rawtext)

                    # Display the summary
                    st.markdown(f"<div class='section-title'>Summary</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='summary-text'>{summary}</div>", unsafe_allow_html=True)
                    st.markdown(f"<strong>Summary Length:</strong> {len_summ} words", unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please paste some text before generating a summary.")

    # Footer with contact information and links
    st.markdown("""
        <div class="footer">
            Developed by Shibbir Ahmad
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()