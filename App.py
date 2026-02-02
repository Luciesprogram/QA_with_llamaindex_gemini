import streamlit as st
import os
from QA_pdf.data_ingestion import load_data
from QA_pdf.embeddings import loading_gemini_embedding
from QA_pdf.model_api import load_gemini_model
from logger import logging

st.set_page_config(page_title="QA with Documents")

# -----------------------------
# Cache query engine per session
# -----------------------------
@st.cache_resource(show_spinner=False)
def build_query_engine(upload_file):
    documents = load_data(upload_file)
    model = load_gemini_model()
    return loading_gemini_embedding(model, documents)

def main():
    st.header("QA with Document (RAG System)")

    # -------- STEP 1: API KEY FORM --------
    with st.form("api_key_form"):
        api_key = st.text_input(
            "Enter your Gemini API Key",
            type="password",
            placeholder="AIza...",max_chars=39
        )
        submitted = st.form_submit_button("Submit API Key")

    if submitted:
        if not api_key:
            st.error("API key cannot be empty")
            return

        # Store key for this session
        st.session_state["GEMINI_API_KEY"] = api_key
        os.environ["GEMINI_API_KEY"] = api_key

        logging.info("Gemini API key stored in environment for session")
        st.success("API key saved. You can now upload a document.")

    # Stop until key is available
    if "GEMINI_API_KEY" not in st.session_state:
        st.info("Please submit your Gemini API key to continue.")
        return

    # -------- STEP 2: FILE UPLOAD --------
    upload_file = st.file_uploader(
        "Upload PDF",
        type=["pdf", "txt"],
        max_upload_size=10
    )

    if upload_file:
        with st.spinner("Processing document..."):
            query_engine = build_query_engine(upload_file)

        # -------- STEP 3: QUESTION --------
        question = st.text_input("Ask your question")

        if st.button("Submit Question") and question:
            with st.spinner("Generating answer..."):
                response = query_engine.query(question)
                st.write(response.response)

if __name__ == "__main__":
    main()
