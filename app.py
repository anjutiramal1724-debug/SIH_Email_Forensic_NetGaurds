import streamlit as st
from modules.advanced_features import extract_features

st.set_page_config(page_title="NetGaurds Forensic", page_icon="🛡️")
st.title("🛡️ NetGaurds - Email Forensic Dashboard")
st.caption("For Cybercrime Police | SIH 2025 | Team NetGaurds")

email = st.text_area("Suspicious Email Paste Kar:", height=150, placeholder="Paste email content here...")

if st.button("🔍 Analyze Threat"):
    if email:
        f = extract_features(email)
        score = min(sum(f.values())*12, 95)
        
        c1, c2 = st.columns(2)
        c1.metric("Fraud Score", f"{score}%")
        if score > 70:
            c2.error("🚨 HIGH RISK FRAUD")
        elif score > 35:
            c2.warning("⚠️ SUSPICIOUS")
        else:
            c2.success("✅ SAFE")
            
        st.write("### Detected Features:")
        st.json(f)
    else:
        st.warning("Email tak pehle!")

st.sidebar.markdown("**Member 1:** Anjali\n**Role:** AI Threat Engine")
