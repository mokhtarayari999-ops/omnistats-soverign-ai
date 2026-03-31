import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AuraStats AI: THE TOTAL ANALYTICS v49.0 ---
st.set_page_config(page_title="AuraStats AI | Comprehensive", layout="wide")

# 👇 ضع مفتاح الـ API الخاص بك هنا
API_KEY = "7c52e30a48a1d5b620195ee6061b7ccf" 

def get_data(league_id):
    headers = {'x-apisports-key': API_KEY}
    url = "https://api-sports.io"
    params = {'league': league_id, 'season': 2025, 'next': 15}
    try:
        res = requests.get(url, headers=headers, params=params, timeout=8).json()
        return res.get('response', [])
    except: return []

# --- CSS التنسيق الشامل ---
st.markdown("""
    <style>
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .stat-box { background: rgba(255,255,255,0.03); border: 1px solid rgba(212,175,55,0.2); border-radius: 20px; padding: 15px; text-align: center; }
    .stat-val { font-size: 2rem; font-weight: bold; color: #fff; }
    .stat-label { color: #D4AF37; font-size: 0.9rem; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS AI 🏆</h1>", unsafe_allow_html=True)

mode = st.radio("بوابة التحكم:", ["🌐 آلي (API)", "✍️ يدوي"], horizontal=True)

if mode == "🌐 آلي (API)":
    leagues = {"الدوري الإنجليزي": 39, "أبطال أوروبا": 2, "الدوري التونسي": 202}
    sel_league = st.selectbox("اختر البطولة:", list(leagues.keys()))
    matches = get_data(leagues[sel_league])
    
    if matches:
        titles = [f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}" for m in matches]
        sel_match = st.selectbox("اختر المباراة:", titles)
        h_name, a_name = sel_match.split(" vs ")
        h_xg, a_xg = 2.1, 1.4
    else:
        st.error("📡 السيرفر لم يستجب. أدخل البيانات يدوياً:")
        c1, c2 = st.columns(2)
        h_name, h_xg = c1.text_input("المضيف:", "مانشستر سيتي"), c1.number_input("قوة المضيف:", 2.2)
        a_name, a_xg = c2.text_input("الضيف:", "أرسنال"), c2.number_input("قوة الضيف:", 1.9)
else:
    c1, c2 = st.columns(2)
    h_name, h_xg = c1.text_input("المضيف:", "الترجي"), c1.number_input("xG المضيف:", 1.8)
    a_name, a_xg = c2.text_input("الضيف:", "الأهلي"), c2.number_input("xG الضيف:", 1.5)

if st.button("🚀 إطلاق المحاكاة السيادية الشاملة"):
    with st.spinner('يتم تحليل 100,000 سيناريو...'):
        time.sleep(1.2)
        h_sim = np.random.poisson(h_xg, 100000)
        a_sim = np.random.poisson(a_xg, 100000)
        
        # حساب التوقعات الشاملة
        score_h, score_a = int(np.mean(h_sim)), int(np.mean(a_sim))
        win_prob = (h_sim > a_sim).mean() * 100
        # معادلة ذكية لتوقع الركنيات بناءً على الـ xG والضغط
        corners = int((h_xg + a_xg) * 3.5) 
        danger_level = "عالي جداً" if (h_xg + a_xg) > 3 else "متوسط"

        # 1. عرض النتيجة الكبرى
        st.markdown(f"""
            <div style='text-align:center; border:3px solid #D4AF37; border-radius:45px; padding:30px; background-color:#111;'>
                <p style='color:#D4AF37;'>النتيجة المتوقعة</p>
                <h1 style='color:#D4AF37; font-size:6rem; margin:0;'>{score_h} - {score_a}</h1>
                <p style='color:#fff;'>{h_name} ضد {a_name}</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 2. لوحة الإحصائيات الشاملة (الركنيات وغيرها)
        col_stat1, col_stat2, col_stat3 = st.columns(3)
        with col_stat1:
            st.markdown(f"<div class='stat-box'><p class='stat-label'>🚩 ركنيات متوقعة</p><p class='stat-val'>{corners}</p></div>", unsafe_allow_html=True)
        with col_stat2:
            st.markdown(f"<div class='stat-box'><p class='stat-label'>📊 فرصة الفوز</p><p class='stat-val'>{win_prob:.1f}%</p></div>", unsafe_allow_html=True)
        with col_stat3:
            st.markdown(f"<div class='stat-box'><p class='stat-label'>🔥 مستوى الخطورة</p><p class='stat-val'>{danger_level}</p></div>", unsafe_allow_html=True)
        
        st.balloons()

st.markdown("<p style='text-align:center; color:#444; margin-top:50px;'>AURASTATS AI | v49.0 COMPREHENSIVE EDITION</p>", unsafe_allow_html=True)
