import os
from orchestrator import Orchestrator

def main():
    # Initialize the system
    system = Orchestrator()
    
    # Path to your local data
    data_path = r"P:\naive based sentiment project\data\raw_data.txt"

    print("=== [AGENTIC SYSTEM CHECK START] ===")

    # 1. Connection Check: Data Ingestion
    if not os.path.exists(data_path):
        print(f"❌ Connection Error: Data Agent cannot find the file at {data_path}")
        return
    else:
        print(f"✅ Data Agent: Found raw data at {data_path}")

    # 2. Connection Check: Training & Feature Extraction
    try:
        print("\n--- Phase 1: Booting up Agents ---")
        system.boot_up(data_path)
        print("✅ Feature Agent: Vocabulary built successfully.")
    except Exception as e:
        print(f"❌ Connection Error in Pipeline: {e}")
        return

    # 3. Connection Check: Inference & Strategy Loop
    print("\n--- Phase 2: Testing Agentic Loop ---")
    
    # Testing with a specific review to see the Strategy Agent's logic
    test_review = "The product quality is fine, but the shipping was slow."
    print(f"Input Review: '{test_review}'")
    
    try:
        # We pass a label to see if the Strategy Agent decides to 'Adapt'
        prediction = system.run_inference(test_review, true_label="negative")
        print(f"✅ Learning Agent Prediction: {prediction}")
        print("✅ Strategy Agent: Decision loop completed.")
    except Exception as e:
        print(f"❌ Connection Error in Inference: {e}")

    print("\n=== [SYSTEM FULLY CONNECTED] ===")

if __name__ == "__main__":
    main()