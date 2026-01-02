from agents.data_agent import DataAgent
from agents.cleaning_agent import CleaningAgent
from agents.learning_agent import LearningAgent

def run_agentic_pipeline(uploaded_file, user_sentence):
    # 1. DATA AGENT: Save and Extract
    da = DataAgent()
    raw_text = da.handle_upload(uploaded_file)
    
    # 2. CLEANING AGENT: Process
    ca = CleaningAgent()
    clean_text = ca.clean(raw_text)
    
    # 3. LEARNING AGENT: Update & Predict
    la = LearningAgent()
    
    # If the file had labels, we train:
    # la.train_incremental(clean_text, label)
    
    # Predict the sentiment of the specific sentence
    prediction = la.predict(ca.clean(user_sentence))
    
    return prediction