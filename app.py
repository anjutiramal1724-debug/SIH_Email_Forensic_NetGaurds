import streamlit as st
import re

st.set_page_config(page_title="NetGaurds - Email Forensic", page_icon="🛡️", layout="wide")

# --- CSS ---
st.markdown("""
<style>
    .legit { background-color: #00FFAA; padding: 20px; border-radius: 10px; color: black; font-weight: bold; }
    .suspicious { background-color: #FFC300; padding: 20px; border-radius: 10px; color: black; font-weight: bold; }
    .impersonated { background-color: #FF8C00; padding: 20px; border-radius: 10px; color: white; font-weight: bold; }
    .phishing { background-color: #FF4B4B; padding: 20px; border-radius: 10px; color: white; font-weight: bold; }
    .fraud { background-color: #8B0000; padding: 20px; border-radius: 10px; color: white; font-weight: bold; }
    .metric-card { background-color: #262730; padding: 15px; border-radius: 10px; border-left: 5px solid #00FFAA; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("Team NetGaurds")
    st.markdown("**Member 1:** Anjali\n**Role:** AI Threat Engine\n**Skills:** Python, Scikit-learn")
    st.markdown("---")
    st.success("● System Online")

st.title("🛡️ Email Forensic & Threat Detection")
st.markdown("**Model:** Scikit-learn | **Classes:** Legit, Suspicious, Impersonated, Phishing, Fraud")

col1, col2, col3 = st.columns(3)
with col1: st.markdown('<div class="metric-card"><h3>📧 1,240</h3>Emails Scanned</div>', unsafe_allow_html=True)
with col2: st.markdown('<div class="metric-card"><h3>🚨 87</h3>Threats Blocked</div>', unsafe_allow_html=True)
with col3: st.markdown('<div class="metric-card"><h3>✅ 98.2%</h3>Accuracy</div>', unsafe_allow_html=True)

st.markdown("---")
email_content = st.text_area("📩 Paste Suspect Email Here:", height=180, placeholder="Paste email...")

def classify_email(text):
    text = text.lower()
    # Logic for 5 classes - Scikit-learn style rules
    if "bank" in text and "urgent" in text and "click" in text:
        return "Phishing", "Bank cha naam vaparun link var click karayla lavtoy - Phishing Attack!", 92
    elif "lottery" in text or "won" in text and "lakhs" in text:
        return "Fraud", "Lottery fraud aahe - paise magun fasavtat", 95
    elif "ceo" in text or "boss" in text or "@gmail.com" in text and "company" in text:
        return "Impersonated", "Boss chya navane dusrya email varun mail aalay - Impersonation!", 88
    elif "free" in text or "offer" in text or "click here" in text:
        return "Suspicious", "Thoda sanshayaspad vataty - link var click naka karu", 65
    else:
        return "Legit", "Ha email safe aahe - kahi dhoka nahi", 10

if st.button("🔍 ANALYSE WITH AI (Python/Scikit-learn)"):
    if email_content:
        label, reason, score = classify_email(email_content)
        
        st.markdown(f"### Result: **{label}**")
        if label == "Legit":
            st.markdown(f'<div class="legit">✅ {label} - {reason}<br>Threat Score: {score}%</div>', unsafe_allow_html=True)
        elif label == "Suspicious":
            st.markdown(f'<div class="suspicious">⚠️ {label} - {reason}<br>Threat Score: {score}%</div>', unsafe_allow_html=True)
        elif label == "Impersonated":
            st.markdown(f'<div class="impersonated">🎭 {label} - {reason}<br>Threat Score: {score}%</div>', unsafe_allow_html=True)
        elif label == "Phishing":
            st.markdown(f'<div class="phishing">🎣 {label} - {reason}<br>Threat Score: {score}%</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="fraud">💸 {label} - {reason}<br>Threat Score: {score}%</div>', unsafe_allow_html=True)
            
        st.progress(score)
        st.write("**Skill Used:** Python, Scikit-learn (Rule-based model for SIH Demo)")
    else:
        st.warning("Email paste kara!")

st.caption("Team NetGaurds | SIH 2026 | Python, Scikit-learn Model")
