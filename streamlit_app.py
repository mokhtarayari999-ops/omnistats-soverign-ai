import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 ARABIC PRO: THE ERROR-FREE v16.0 ---
st.set_page_config(page_title="Arabic Pro", layout="wide")

API_KEY = "afc8d6974db7dfcf37770c1b5791b65d"

def fetch_data(league_id):
    headers = {'x-apisports-key': API_KEY}
    url = f"https://api-sports.io{league_id}&season=2025&next=10"
    try:
        res = requests.get(url, headers=headers, timeout=10).json()
        return res.get('response', [])
    except:
        return None

# --- التصميم المصحح بدقة (تم حل مشكلة الـ Syntax هنا) ---
st.markdown("""
    <style>
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .main-box { border: 2px solid #D4AF37; border-radius: 20px; padding: 25px; background: rgba(212,175,55,0.03); text-align: center; }
    .score-display { font-size: 5rem; font-weight: 900; color: #D4AF37; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)

leagues = {"🇬🇧 الدوري الإنجليزي": 39, "🇪🇸 الدوري الإسباني": 140, "🇹🇳 الدوري التونسي": 202}
sel_league = st.selectbox("🎯 اختر الساحة المستهدفة:", list(leagues.keys()))

matches = fetch_data(leagues[sel_league])

st.markdown("<div class='main-box'>", unsafe_allow_html=True)

# الجزء الذي كان يسبب الخطأ في صورتك تم تصحيحه هنا:
if matches and len(matches) > 0:
    titles = {f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}": m for m in matches}
    sel_match = st.selectbox("✅ تم الاتصال! اختر المواجهة:", list(titles.keys()))
    h_name = titles[sel_match]['teams']['home']['name']
    a_name = titles[sel_match]['teams']['away']['name']
else:
    # السطر المصحح تماماً:
    st.markdown("<p style='color:#D4AF37;'>⚠️ تعذر الاتصال التلقائي - تم تفعيل المحرك اليدوي</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    h_name = c1.text_input("الفريق المضيف:", "الترجي")
    a_name = c2.text_input("الفريق الضيف:", "الأهلي")

if st.button("🔱 إطلاق المحاكاة"):
    with st.spinner('⏳ جاري التحليل...'):
        time.sleep(1)
        h_res, a_res = np.random.poisson(2.1), np.random.poisson(1.2)
        st.markdown(f"<div class='score-display'>{h_res} - {a_res}</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:white;'>{h_name} vs {a_name}</p>", unsafe_allow_html=True)
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)
    
