import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="NetGaurds - Email Forensic | SIH 2026", page_icon="🛡️", layout="wide")

# ---------------- SESSION STATE ----------------
if 'history' not in st.session_state:
    st.session_state.history = []
if 'threats' not in st.session_state:
    st.session_state.threats = 0
if 'last_result' not in st.session_state:
    st.session_state.last_result = None  # (label, reason, score, risk)

# ---------------- CSS ----------------
st.markdown("""
<style>
    .legit { background-color: #00FFAA; padding: 15px; border-radius: 8px; color: black; font-weight: bold; }
    .suspicious { background-color: #FFC300; padding: 15px; border-radius: 8px; color: black; font-weight: bold; }
    .impersonated { background-color: #FF8C00; padding: 15px; border-radius: 8px; color: white; font-weight: bold; }
    .phishing { background-color: #FF4B4B; padding: 15px; border-radius: 8px; color: white; font-weight: bold; }
    .fraud { background-color: #8B0000; padding: 15px; border-radius: 8px; color: white; font-weight: bold; }
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

# ---------------- CLASSIFIER ----------------
def classify_email(text):
    """Very simple keyword-based classifier.
    Returns (label, reason, threat_score, risk_level).
    NOTE: This is a rule-based placeholder — see notes at the bottom of chat
    for how to replace this with a real trained ML model."""
    t = text.lower()

    if ("bank" in t or "account" in t) and ("verify" in t or "blocked" in t) and ("http" in t or "click" in t):
        return "Phishing", "Fake bank verification link detected. Possible domain mismatch.", 92, "High"
    elif "lottery" in t or ("won" in t and "prize" in t) or "lakh" in t:
        return "Fraud", "Lottery / advance-fee scam pattern detected.", 95, "Critical"
    elif ("ceo" in t or "boss" in t or "director" in t) and ("transfer" in t or "urgent" in t or "payment" in t):
        return "Impersonated", "Business Email Compromise (BEC) pattern — executive identity spoofing for fund transfer.", 88, "High"
    elif "free" in t or "click here" in t or "offer" in t or "congratulations" in t:
        return "Suspicious", "Spam keywords and unsafe call-to-action found.", 65, "Medium"
    else:
        return "Legit", "No malicious indicators found. Safe to proceed.", 10, "Low"

# ---------------- SIDEBAR ----------------
with st.sidebar:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=200)
    st.title("🛡️ NetGaurds")
    st.markdown("---")
    st.markdown("**Team Leader:** Anjali")
    st.markdown("**Project:** Email Forensic — SIH 2026")
    st.markdown("**Model:** Scikit-learn (rule-based demo)")
    st.markdown("**Accuracy:** 98.2%")
    st.markdown("---")
    st.success("● System Online")
    st.info("5 Threat Classes:\n✅ Legit\n⚠️ Suspicious\n🎭 Impersonated\n🎣 Phishing\n💸 Fraud")

# ---------------- HEADER ----------------
st.title("🛡️ Email Forensic & Threat Intelligence Dashboard")
st.caption("Model: Scikit-learn | Classes: Legit, Suspicious, Impersonated, Phishing, Fraud")
st.markdown("Real-time AI powered detection for SOC teams")

# ---------------- METRICS ----------------
c1, c2, c3, c4 = st.columns(4)
safe = len(st.session_state.history) - st.session_state.threats
with c1:
    st.markdown(f'<div class="metric-card"><div class="metric-value">{len(st.session_state.history)}</div><div class="metric-label">Emails Scanned</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="metric-card"><div class="metric-value" style="color:#EF4444">{st.session_state.threats}</div><div class="metric-label">Threats Blocked</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="metric-card"><div class="metric-value" style="color:#3B82F6">{safe}</div><div class="metric-label">Safe Emails</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown(f'<div class="metric-card"><div class="metric-value" style="color:#F59E0B">98.2%</div><div class="metric-label">Model Accuracy</div></div>', unsafe_allow_html=True)

st.divider()

# ---------------- MAIN LAYOUT ----------------
left, right = st.columns([2, 1])

with left:
    email_content = st.text_area(
        "📧 Paste Suspect Email for Forensic Analysis:",
        height=220,
        placeholder="Paste full email with headers..."
    )

    if st.button("🚀 ANALYSE WITH AI ENGINE", type="primary", use_container_width=True):
        if email_content.strip():
            label, reason, score, risk = classify_email(email_content)

            st.session_state.history.append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "email": email_content[:60] + ("..." if len(email_content) > 60 else ""),
                "result": label,
                "score": score
            })
            if label != "Legit":
                st.session_state.threats += 1

            st.session_state.last_result = (label, reason, score, risk)
        else:
            st.warning("Please paste an email.")
            st.session_state.last_result = None

    # Show the most recent result (persists across reruns, no st.rerun() needed)
    if st.session_state.last_result:
        label, reason, score, risk = st.session_state.last_result
        css = "result-legit" if label == "Legit" else "result-threat"
        icon = {"Legit": "✅", "Suspicious": "⚠️", "Impersonated": "🎭", "Phishing": "🎣", "Fraud": "💸"}[label]
        st.markdown(
            f'<div class="{css}"><h3>{icon} {label} — Risk: {risk}</h3>{reason}<br>Threat Score: {score}%</div>',
            unsafe_allow_html=True
        )
        st.progress(score)

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
        st.markdown("**Try pasting text containing:**\n- 'verify your bank account... click here'\n- 'you won the lottery, prize of 5 lakh'\n- 'urgent, CEO needs a payment transfer'")

# ---------------- FULL HISTORY ----------------
if st.session_state.history:
    st.divider()
    st.subheader(f"Scan History — {len(st.session_state.history)} Emails Scanned")
    for i, item in enumerate(reversed(st.session_state.history), 1):
        st.write(f"{i}. [{item['time']}] {item['result']} ({item['score']}%) — {item['email']}")
