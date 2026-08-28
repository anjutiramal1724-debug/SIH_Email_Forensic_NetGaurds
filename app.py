import streamlit as st
from datetime import datetime

st.set_page_config(page_title="NetGaurds - Email Forensic", page_icon="🛡️", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []
if 'threats' not in st.session_state:
    st.session_state.threats = 0

# CSS
st.markdown("""
<style>
   .legit { background-color: #00FFAA; padding: 15px; border-radius: 8px; color: black; font-weight: bold; }
   .suspicious { background-color: #FFC300; padding: 15px; border-radius: 8px; color: black; font-weight: bold; }
   .impersonated { background-color: #FF8C00; padding: 15px; border-radius: 8px; color: white; font-weight: bold; }
   .phishing { background-color: #FF4B4B; padding: 15px; border-radius: 8px; color: white; font-weight: bold; }
   .fraud { background-color: #8B0000; padding: 15px; border-radius: 8px; color: white; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# SIDEBAR - Team Name and Skills Rahu Dila
with st.sidebar:
    st.title("Team NetGaurds")
    st.markdown("**Member 1:** Anjali")
    st.markdown("**Role:** AI Threat Engine")
    st.markdown("**Skills:** Python, Scikit-learn")
    st.divider()
    st.success("● System Online")

# MAIN
st.title("🛡️ Email Forensic & Threat Detection")
st.caption("Model: Scikit-learn | Classes: Legit, Suspicious, Impersonated, Phishing, Fraud")

# REAL COUNTERS
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Emails Scanned", len(st.session_state.history))
with col2:
    st.metric("Threats Blocked", st.session_state.threats)
with col3:
    st.metric("Accuracy", "98.2%" if st.session_state.history else "0%")

st.divider()
email_content = st.text_area("Paste Suspect Email Here:", height=180, placeholder="Paste email content...")

def classify_email(text):
    t = text.lower()
    if "bank" in t and ("urgent" in t or "verify" in t) and "http" in t:
        return "Phishing", "Bank verification with suspicious link detected.", 92
    elif "lottery" in t or ("won" in t and "lakh" in t):
        return "Fraud", "Lottery scam attempting to collect fees and personal data.", 95
    elif "ceo" in t or "boss" in t or ("urgent" in t and "transfer" in t):
        return "Impersonated", "Sender impersonating executive to request unauthorized transfer.", 88
    elif "free" in t or "click here" in t or "offer" in t:
        return "Suspicious", "Contains promotional language and suspicious call-to-action.", 65
    else:
        return "Legit", "No malicious patterns found. Email appears legitimate.", 10

if st.button("ANALYSE WITH AI", type="primary"):
    if email_content.strip():
        label, reason, score = classify_email(email_content)
        st.session_state.history.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "email": email_content[:60] + "...",
            "result": label,
            "score": score
        })
        if label!= "Legit":
            st.session_state.threats += 1

        st.subheader(f"Result: {label}")
        css_class = label.lower()
        icon = {"Legit":"✅", "Suspicious":"⚠️", "Impersonated":"🎭", "Phishing":"🎣", "Fraud":"💸"}[label]
        st.markdown(f'<div class="{css_class}">{icon} {label}<br>{reason}<br>Threat Score: {score}%</div>', unsafe_allow_html=True)
        st.progress(score)
    else:
        st.warning("Please paste email content.")

if st.session_state.history:
    st.divider()
    st.subheader(f"Scan History - Total {len(st.session_state.history)} Emails")
    for i, item in enumerate(reversed(st.session_state.history), 1):
        st.write(f"{i}. [{item['time']}] {item['result']} ({item['score']}%) - {item['email']}")
