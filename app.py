import streamlit as st
import os
import time
from orchestrator import AgenticOrchestrator

# 1. Page Configuration
st.set_page_config(
    page_title="Sentiment AI | Agentic System", 
    page_icon="🧠", 
    layout="wide"
)

# 2. Custom Styling for a Professional Look
st.markdown("""
    <style>
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #3e4452; }
    </style>
    """, unsafe_allow_html=True)

def main():
    with st.sidebar:
        st.header("⚙️ System Control")
        # --- ADD TEAM NAMES HERE ---
        st.subheader("👥 Project Team")
        st.markdown("""
        * **Namrata Pathak**
        * **Soham Guha**
        """)
        st.divider()
    
    # Header Section
    col_head, col_logo = st.columns([4, 1])
    with col_head:
        st.title("🧠 Agentic Sentiment Intelligence")
        st.caption("Multi-agent system for deep linguistic analysis and sentiment scoring.")
    
    st.divider()

    # 3. Sidebar Monitoring & Config
    with st.sidebar:
        st.header("⚙️ System Control")
        st.info("Status: **System Operational**")
        # This threshold can be passed to the Strategy Agent later
        confidence_threshold = st.slider("Confidence Threshold", 0.0, 1.0, 0.7)
        st.divider()
        if st.button("🧹 Clear Session"):
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
                # Initialize your actual Orchestrator
                orchestrator = AgenticOrchestrator()
                
                st.write("🔍 **Data Agent**: Pre-processing and cleaning input...")
                # The orchestrator handles the file and text internally now
                result = orchestrator.run_logic(uploaded_file, user_sentence)
                
                time.sleep(0.5) # Brief pause for UI smoothness
                status.update(label="✅ Analysis Complete!", state="complete", expanded=False)

            # 6. Results Visualization
            st.divider()
            res_col1, res_col2, res_col3 = st.columns(3)
            
            with res_col1:
                st.metric("Final Sentiment", result["prediction"].upper())
            with res_col2:
                # Format confidence as a percentage
                st.metric("Confidence Score", f"{result['confidence']*100:.1f}%")
            with res_col3:
                sentiment_color = "🟢" if result["prediction"].lower() == "pos" else "🔴"
                st.write(f"### Status: {sentiment_color}")

            # 7. Agentic Transparency (The Logs)
            with st.expander("🛠️ View Internal Agent Decision Logs", expanded=True):
                st.json({
                    "Strategy Agent Decision": result.get('strategy_log'),
                    "Vocabulary Size": result.get('vocab_size'),
                    "Raw Confidence Value": result.get('confidence')
                })

if __name__ == "__main__":
    # Ensure directories exist
    for folder in ["data/raw", "data/processed", "data/models"]:
        os.makedirs(folder, exist_ok=True)
    main()