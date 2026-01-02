import streamlit as st
import os
from orchestrator import AgenticOrchestrator

st.set_page_config(page_title="Agentic Sentiment System", layout="wide")

def main():
    st.title("🤖 Agentic Sentiment Analysis System")
    
    st.sidebar.header("System Monitoring")
    status_placeholder = st.sidebar.empty()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Upload Training/Data File")
        uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])
    with col2:
        st.subheader("Test a Sentence")
        user_sentence = st.text_input("Enter a sentence to predict:")

    if st.button("🚀 Run Agentic Pipeline"):
        if not (uploaded_file or user_sentence):
            st.warning("Please provide input.")
            return

        with st.status("Agents are working...", expanded=True):
            orchestrator = AgenticOrchestrator()
            # FIX: Pass the file object directly
            result = orchestrator.run_logic(uploaded_file, user_sentence)

        st.success(f"**Final Prediction:** {result['prediction']}")
        
        with st.expander("View Agentic Decision Logs"):
            st.json({
                "Confidence Score": result.get('confidence', 0),
                "Strategy Agent Decision": result.get('strategy_log', 'N/A'),
                "Vocab Size": result.get('vocab_size', 0)
            })

if __name__ == "__main__":
    main()