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
=======
=======
import streamlit as st
>>>>>>> 5e1ed3e (made the app.py)
import os
import time
# Assuming these exist based on your snippet
# from orchestrator import run_agentic_pipeline 

# 1. Page Configuration
st.set_page_config(
    page_title="Sentiment AI | Agentic System", 
    page_icon="🧠", 
    layout="wide"
)

# 2. Custom Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #3e4452; }
    .agent-card { border-left: 5px solid #00ffcc; padding-left: 15px; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

def main():
<<<<<<< HEAD
    # Initialize the systeml
    system = Orchestrator()
    
    # Path to your local data
    data_path = r"data\raw_data.txt"
=======
    # Header Section
    col_head, col_logo = st.columns([4, 1])
    with col_head:
        st.title("🧠 Agentic Sentiment Intelligence")
        st.caption("Multi-agent system for deep linguistic analysis and sentiment scoring.")
    
    st.divider()
>>>>>>> 5e1ed3e (made the app.py)

    # 3. Sidebar Monitoring & Config
    with st.sidebar:
        st.header("⚙️ System Control")
        st.info("Status: **System Operational**")
        confidence_threshold = st.slider("Confidence Threshold", 0.0, 1.0, 0.7)
        st.divider()
        if st.button("🧹 Clear Cache & Logs"):
            st.rerun()

    # 4. Input Layout
    col_input, col_viz = st.columns([1, 1])

    with col_input:
        st.subheader("📥 Data Input")
        uploaded_file = st.file_uploader("Upload Document (PDF/TXT)", type=["pdf", "txt"])
        user_sentence = st.text_area("Or enter text manually:", placeholder="Type something like 'The service was incredible'...")

    # 5. Execution Logic
    if st.button("🚀 Execute Agentic Pipeline", use_container_width=True):
        if not (uploaded_file or user_sentence):
            st.error("⚠️ Action Required: Please provide a file or text input.")
        else:
            with st.status("🤖 Agents Coordinating...", expanded=True) as status:
                st.write("🔍 **Data Agent**: Pre-processing and cleaning input...")
                time.sleep(1) # Simulating agent work
                
                st.write("⚖️ **Sentiment Agent**: Running inference models...")
                time.sleep(1)
                
                # Mocking the result for the UI demo. 
                # In production, replace with: result = run_agentic_pipeline(uploaded_file, user_sentence)
                result = {
                    "prediction": "Positive",
                    "confidence": 0.94,
                    "data_agent_logs": "Extracted 45 words. No noise detected.",
                    "sentiment_agent_logs": "High-polarity keywords identified: 'incredible', 'service'.",
                    "orchestrator_logs": "Consensus reached between agents."
                }
                
                status.update(label="✅ Analysis Complete!", state="complete", expanded=False)

<<<<<<< HEAD
    print("\n=== [SYSTEM FULLY CONNECTED] ===")
>>>>>>> 5644ccd ()
=======
            # 6. Results Visualization
            st.divider()
            res_col1, res_col2, res_col3 = st.columns(3)
            
            with res_col1:
                st.metric("Final Sentiment", result["prediction"])
            with res_col2:
                st.metric("Confidence Score", f"{result['confidence']*100:.1f}%")
            with res_col3:
                sentiment_color = "🟢" if result["prediction"] == "Positive" else "🔴"
                st.write(f"### Status: {sentiment_color}")

            # 7. Agentic Transparency (The Logs)
            with st.expander("🛠️ View Internal Agent Decision Logs", expanded=True):
                tab1, tab2, tab3 = st.tabs(["Data Agent", "Sentiment Agent", "Orchestrator"])
                
                with tab1:
                    st.code(result["data_agent_logs"])
                with tab2:
                    st.code(result["sentiment_agent_logs"])
                with tab3:
                    st.info(result["orchestrator_logs"])
>>>>>>> 5e1ed3e (made the app.py)

if __name__ == "__main__":
    main()