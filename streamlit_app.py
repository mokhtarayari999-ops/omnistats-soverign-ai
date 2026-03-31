import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AuraStats AI: Global Engine v38.0 ---
st.set_page_config(page_title="AuraStats AI", layout="wide")

# 👇 ضع مفتاح الـ API الخاص بك بين العلامتين " " في السطر التالي:
API_KEY ="c2f6d97fe715446c4be7f30600191daa" 

# --- وظائف النظام ---
def get_data(league_id):
    headers = {'x-apisports-key': API_KEY}
    url = f"https://api-sports.io{league_id}&season=2023&next=10"
    try:
        res = requests.get(url, headers=headers, timeout=5).json()
        return res.get('response', [])
    except: return []

# --- تصميم الواجهة (نفس الهوية التي تحبها) ---
st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS AI 🏆</h1>", unsafe_allow_html=True)

mode = st.radio("تحكم بالنظام:", ["🌐 آلي (API)", "✍️ يدوي"], horizontal=True)

if mode == "🌐 آلي (API)":
    leagues = {"أبطال أوروبا": 2, "الدوري الإنجليزي": 39, "الدوري التونسي": 202}
    sel_league = st.selectbox("اختر البطولة:", list(leagues.keys()))
    matches = get_data(leagues[sel_league])
    
    if matches:
        match_names = [f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}" for m in matches]
        sel_match = st.selectbox("اختر المباراة:", match_names)
        st.success(f"✅ جاهز لتحليل: {sel_match}")
        h_xg, a_xg = 2.1, 1.5 # قيم افتراضية للتحليل الآلي
    else:
        st.error("⚠️ تأكد من وضع المفتاح الصحيح في الكود أعلاه")
        h_xg, a_xg = 1.0, 1.0
else:
    c1, c2 = st.columns(2)
    h_xg = c1.number_input("xG المضيف:", value=1.8)
    a_xg = c2.number_input("xG الضيف:", value=1.5)

if st.button("🚀 إطلاق المحاكاة السيادية"):
    st.balloons()
    st.write("📊 جاري المعالجة...")
                          
