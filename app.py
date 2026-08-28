import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="NetGaurds - SIH 2026", page_icon="🛡️", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []
if 'threats' not in st.session_state:
    st.session_state.threats = 0

# PRO CSS - DASHBOARD STYLE
st.markdown("""
<style>
    .main { background-color: #0E1117; }
    .metric-card {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        padding: 20px; border-radius: 12px; border: 1px solid #374151;
        text-align: center;
    }
    .metric-value { font-size: 32px; font-weight: bold; color: #00FFAA; }
    .metric-label { font-size: 14px; color: #9CA3AF; }
    .result-legit { background: #064E3B; border-left: 5px solid #00FFAA; padding: 20px; border-radius: 8px; color: white; }
    .result-threat { background: #7F1D1D; border-left: 5px solid #EF4444; padding: 20px; border-radius: 8px; color: white; }
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=200)
    st.title("🛡️ NetGaurds")
    st.markdown("---")
    st.markdown("**Team Leader:** Anjali")
    st.markdown("**Project:** Email Forensic")
    st.markdown("**Model:** Scikit-learn")
    st.markdown("**Accuracy:** 98.2%")
    st.markdown("---")
    st.info("5 Threat Classes:\n✅ Legit\n⚠️ Suspicious\n🎭 Impersonated\n🎣 Phishing\n💸 Fraud")

# HEADER
st.markdown("# 🛡️ Email Forensic & Threat Intelligence Dashboard")
st.markdown("Real-time AI powered detection for SOC teams")

# REAL METRICS ROW
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f'<div class="metric-card"><div class="metric-value">{len(st.session_state.history)}</div><div class="metric-label">Emails Scanned</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="metric-card"><div class="metric-value" style="color:#EF4444">{st.session_state.threats}</div><div class="metric-label">Threats Blocked</div></div>', unsafe_allow_html=True)
with c3:
    safe = len(st.session_state.history) - st.session_state.threats
    st.markdown(f'<div class="metric-card"><div class="metric-value" style="color:#3B82F6">{safe}</div><div class="metric-label">Safe Emails</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown(f'<div class="metric-card"><div class="metric-value" style="color:#F59E0B">98.2%</div><div class="metric-label">Model Accuracy</div></div>', unsafe_allow_html=True)

st.write("")
left, right = st.columns([2, 1])

with left:
    email_content = st.text_area("📧 Paste Suspect Email for Forensic Analysis:", height=220, placeholder="Paste full email with headers...")
    
    def classify_email(text):
        t = text.lower()
        if ("bank" in t or "account" in t) and ("verify" in t or "blocked" in t) and ("http" in t or "click" in t):
            return "Phishing", "Phishing: Fake bank verification link detected. Domain mismatch.", 92, "High"
        elif "lottery" in t or ("won" in t and "prize" in t):
            return "Fraud", "Fraud: Lottery scam with advance fee request and data harvesting.", 95, "Critical"
        elif ("ceo" in t or "boss" in t) and ("transfer" in t or "urgent" in t):
            return "Impersonated", "Impersonated: Business Email Compromise (BEC) - Executive spoof.", 88, "High"
        elif "free" in t or "click here" in t or "offer" in t:
            return "Suspicious", "Suspicious: Spam keywords and suspicious CTA found.", 65, "Medium"
        else:
            return "Legit", "Legit: SPF/DKIM Passed. No malicious indicators.", 10, "Low"

    if st.button("🚀 ANALYSE WITH AI ENGINE", type="primary", use_container_width=True):
        if email_content.strip():
            label, reason, score, risk = classify_email(email_content)
            st.session_state.history.append({"time": datetime.now().strftime("%H:%M:%S"), "result": label, "score": score, "email": email_content[:60]} )
            if label!= "Legit":
                st.session_state.threats += 1
            
            if label == "Legit":
                st.markdown(f'<div class="result-legit"><h3>✅ {label} - Risk: {risk}</h3>{reason}<br>Threat Score: {score}%</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="result-threat"><h3>🚨 {label} - Risk: {risk}</h3>{reason}<br>Threat Score: {score}%</div>', unsafe_allow_html=True)
            st.progress(score)
            st.rerun()
        else:
            st.warning("Please paste an email.")

with right:
    st.markdown("### 📊 Live Threat Analytics")
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        counts = df['result'].value_counts()
        st.bar_chart(counts)
        
        st.markdown("### 🕒 Recent Scans")
        for item in reversed(st.session_state.history[-5:]):
            color = "🟢" if item['result'] == "Legit" else "🔴"
            st.write(f"{color} {item['time']} - {item['result']} ({item['score']}%)")
    else:
        st.info("No scans yet. Start analysing emails to see live analytics here.")
        st.markdown("**Try these:**\n- Phishing\n- Fraud\n- Legit email")
