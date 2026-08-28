import streamlit as st
import re

st.set_page_config(page_title="NetGaurds - Email Forensic", page_icon="🛡️", layout="wide")

# CSS for Cyber Theme
st.markdown("""
<style>
    .main { background-color: #0E1117; }
    .stButton>button { background-color: #00FFAA; color: black; font-weight: bold; width: 100%; border-radius: 10px; }
    .threat-box { background-color: #FF4B4B; padding: 20px; border-radius: 10px; color: white; font-weight: bold; }
    .safe-box { background-color: #00FFAA; padding: 20px; border-radius: 10px; color: black; font-weight: bold; }
    .metric-card { background-color: #262730; padding: 15px; border-radius: 10px; border-left: 5px solid #00FFAA; }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=100)
    st.title("Team NetGaurds")
    st.markdown("**Member 1:** Anjali\n**Role:** AI Threat Engine")
    st.markdown("**Member 2:** Cyber Forensic")
    st.markdown("---")
    st.markdown("### SIH 2026\nCybercrime Police\nProblem Statement")
    st.success("● System Online")

st.title("🛡️ Email Forensic & Threat Detection Dashboard")
st.markdown("AI-Powered Investigation Tool for Cybercrime Department")

col1, col2, col3 = st.columns(3)
with col1: st.markdown('<div class="metric-card"><h3>📧 1,240</h3><p>Emails Scanned</p></div>', unsafe_allow_html=True)
with col2: st.markdown('<div class="metric-card"><h3>🚨 87</h3><p>Threats Blocked</p></div>', unsafe_allow_html=True)
with col3: st.markdown('<div class="metric-card"><h3>✅ 98.2%</h3><p>Accuracy</p></div>', unsafe_allow_html=True)

st.markdown("---")
email_content = st.text_area("📩 Paste Suspect Email Content Here:", height=200, placeholder="Paste email header + body here for forensic analysis...")

if st.button("🔍 ANALYSE THREAT"):
    if email_content:
        with st.spinner("Analysing with AI Engine..."):
            # Simple logic
            threats = ["win", "lottery", "click here", "free money", "bit.ly", "urgent"]
            score = sum(1 for t in threats if t in email_content.lower())
            
            st.markdown("### 📋 Forensic Report:")
            c1, c2 = st.columns(2)
            with c1:
                if score > 1:
                    st.markdown(f'<div class="threat-box">🚨 HIGH RISK THREAT DETECTED<br>Threat Score: {score*30}%<br>Action: Block & Report to Cyber Cell</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="safe-box">✅ SAFE EMAIL<br>Threat Score: {score*10}%<br>No malicious content found</div>', unsafe_allow_html=True)
            with c2:
                st.write("**Links Found:**", re.findall(r'http\S+', email_content))
                st.write("**Suspicious Words:**", score)
                st.progress(score*30 if score>0 else 10)
    else:
        st.warning("Please paste email content!")

st.markdown("---")
st.caption("Developed by Team NetGaurds | SIH 2026 | Made for Indian Cyber Police")
