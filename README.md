# AI Text Summarizer

## **Overview**

The **AI Text Summarizer** is a Streamlit-based web app that utilizes advanced AI models for **abstractive text summarization**. The app allows users to input a document or article, and the model will generate a concise summary that retains the main ideas. This tool is ideal for quickly digesting long content without losing important details.

## **Key Features**

- **Text Input:** Input text directly or paste documents in supported formats.
- **Automatic Summarization:** The app uses a pre-trained **BART** model to analyze and generate a summary of the input text.
- **Customizable Summary Length:** The summary length can be adjusted based on user preferences.
- **Word Count Display:** The app displays the summary word count quickly.
- **Real-Time Summarization:** Instant summaries are generated after submitting the text.

## **How the AI Summarizer Works**

The **BART** (Bidirectional and Auto-Regressive Transformers) model is used for **abstractive summarization**. Here’s how it works:

- **Tokenization:** The input text is tokenized using the BART tokenizer.
- **Text Encoding:** The model encodes the text and generates a summary based on its learned understanding of language.
- **Decoding and Summary Generation:** The BART model generates a concise version of the input, ensuring key points are retained while reducing the length.
- **Summary Output:** The generated summary is decoded, and the length is displayed for comparison.

## **Tech Stack**

- **Python:** The core functionality of the app is built using Python.
- **Streamlit:** A fast, interactive framework for building web apps.
- **Hugging Face Transformers Library:** Uses **BART** for summarization.
- **SpaCy:** Used for text processing and analysis.

## **Installation Guide**

To set up the AI Text Summarizer app locally, follow these steps:

1. **Clone the Repository:**
   
   ``
   git clone https://github.com/shibbir-ahmad24/AI-Text-Summarizer.git
   ``

3. **Install Dependencies:**

   Set up your Python environment and install the required dependencies:

   ``
   pip install textstat spacy
   ``
   
   ``
   pip install transformers torch
   ``

5. **Download the SpaCy Model:**

   Download the SpaCy language model for processing:

   ``
   python -m spacy download en_core_web_sm
   ``

7. **Run the App:**

   Start the Streamlit development server:

   ``
   streamlit run app.py
   ``

9. **Access the App:**

   Open your web browser and go to the following URL:

   ``
   http://127.0.0.1:8501/
   ``

## **Usage Instructions**

- Input Text: Paste your text into the input box in the app.
- Generate Summary: Click the "Generate Summary" button to get a concise summary.
- View Word Count: The app will display the word count for both the original text and the generated summary.
- Share: If needed, you can copy and share the summary directly.
- Experiment: Try different input lengths and summaries to explore how the model condenses content.

## **Contributions**

Contributions are welcome! If you'd like to improve the project, feel free to fork the repository, create a new branch, and submit a pull request. You can also report issues or suggest features in the "Issues" section.

## **Acknowledgements**

Special thanks to the open-source community for providing invaluable resources like the BART model from Hugging Face and Streamlit for web app development. This project wouldn’t have been possible without these tools.

## **Future Enhancements**

- **Multi-Language Support:** Expand the app to support summarization in other languages.
- **User Accounts:** Add user authentication to save summaries for future reference.
- **API Integration:** Build an API that allows other applications to integrate the summarization feature.
- **Abstractive Summarization Enhancements:** Explore additional models and techniques for even more accurate and nuanced summaries.

## **Conclusion**

The AI Text Summarizer app is a powerful tool for anyone who needs quick, accurate summaries of long documents. Powered by the BART model, this app provides high-quality text summaries in a user-friendly interface. Whether you’re dealing with academic papers, articles, or any other lengthy content, this app simplifies the process and helps you get to the key points faster.

## **APP UI**

![p1](https://github.com/shibbir-ahmad24/AI-Text-Summarizer/blob/main/Figures/Output1.png)

![p2](https://github.com/shibbir-ahmad24/AI-Text-Summarizer/blob/main/Figures/Output2.png)
