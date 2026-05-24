import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="MedAgent AI Portal",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. Inject Custom CSS for specific element styling (Greens & Greys)
st.markdown("""
    <style>
    /* Styling the main header */
    .main-header {
        color: #2ECC71;
        font-weight: 700;
        font-size: 2.2rem;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        color: #A0A0A0;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    /* Pulse indicator for connection status */
    .status-indicator {
        background-color: #1E1E1E;
        padding: 10px 15px;
        border-radius: 8px;
        border-left: 4px solid #2ECC71;
        color: #E0E0E0;
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar (Grey/Black background configured by theme)
with st.sidebar:
    st.markdown("<h2 style='color: #2ECC71;'>System Controls</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Context selectors for a medical app
    st.subheader("Patient Context")
    patient_id = st.text_input("Patient ID / Session Reference", value="PT-8832", help="Unique identifier for backend retrieval")
    scope = st.selectbox("Clinical Scope", ["General Consultation", "Lab Report Analysis", "Prescription Cross-Check"])
    
    st.markdown("---")
    # Quick status check
    st.markdown('<div class="status-indicator">● Backend Connected: FastAPI Secure Port</div>', unsafe_allow_html=True)

# 4. Main Interface Layout
st.markdown('<div class="main-header">🩺 MedAgent AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Clinical Decision Support & Analysis Portal</div>', unsafe_allow_html=True)

# 5. Initialize Chat History in Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to the clinical portal. How can I assist you with patient data or medical query analysis today?"}
    ]

# 6. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 7. Handle User Input
if user_prompt := st.chat_input("Type your medical query or drop patient vitals here..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    # Add user message to session history
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    
    # Display assistant response container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # --- PLACEHOLDER FOR BACKEND INTEGRATION ---
        # Right now, this simulates a response. Later, you will replace this block 
        # with a request to your FastAPI backend server.
        simulated_backend_reply = f"Acknowledged. Processing your request under scope '{scope}' for patient '{patient_id}'. (Backend link ready for connection)."
        
        # Simulate a typing effect (Streaming UI)
        for chunk in simulated_backend_reply.split(" "):
            full_response += chunk + " "
            time.sleep(0.08)
            # Add a blinking cursor to simulate real-time generation
            message_placeholder.markdown(full_response + "▌")
            
        message_placeholder.markdown(full_response)
        # --------------------------------------------
        
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})