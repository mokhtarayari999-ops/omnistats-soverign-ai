import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AURASTATS ARABIC PRO v350.0 ---
st.set_page_config(page_title="AuraStats Arabic Pro", layout="wide")

# 👇 ضع مفتاح الـ API الخاص بك هنا (من موقع api-football.com) لفتح البيانات الحقيقية
API_KEY = "8abdb813dece636993e2182de4ee374a" 

def get_real_arabic_fixtures(league_id):
    headers = {'x-apisports-key': API_KEY}
    url = "https://api-sports.io"
    # جلب مباريات الموسم الحالي 2025/2026
    params = {'league': league_id, 'season': 2025, 'next': 10}
    try:
        res = requests.get(url, headers=headers, params=params, timeout=10).json()
        return res.get('response', [])
    except: return []

# --- التصميم الإمبراطوري (تطابق مع صورتك) ---
st.markdown("""
    <style>
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .main-card { border: 2px solid #D4AF37; border-radius: 40px; padding: 25px; background: rgba(212,175,55,0.02); text-align: center; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37, #F2D388); color: black !important; font-weight: 900; border-radius: 100px; height: 70px; font-size: 1.5rem; width: 100%; border: none; }
    .stat-badge { background: #111; border: 1px solid #D4AF37; border-radius: 20px; padding: 15px; margin: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS ARABIC 🏆</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888;'>محرك التوقعات الحقيقي للدوريات العربية والركنيات</p>", unsafe_allow_html=True)

# معرفات الدوريات العربية الحقيقية (Real IDs)
leagues = {
    "🇹🇳 الدوري التونسي الممتاز": 202,
    "🇪🇬 الدوري المصري الممتاز": 233,
    "🇸🇦 دوري روشن السعودي": 307,
    "🇲🇦 الدوري المغربي المحترف": 200,
    "🌍 أبطال أفريقيا": 12
}

sel_league_name = st.selectbox("🎯 اختر البطولة العربية الحية:", list(leagues.keys()))
league_id = leagues[sel_league_name]

# جلب البيانات الحقيقية
with st.spinner('📡 جاري رصد الملاعب العربية...'):
    matches = get_real_arabic_fixtures(league_id)

st.markdown("<div class='main-card'>", unsafe_allow_html=True)

if matches:
    titles = {f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}": m for m in matches}
    sel_match = st.selectbox("المباريات المجدولة حقيقياً:", list(titles.keys()))
    
    match_data = titles[sel_match]
    h_name = match_data['teams']['home']['name']
    a_name = match_data['teams']['away']['name']
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(match_data['teams']['home']['logo'], width=80)
        h_xg = st.slider(f"قوة {h_name}:", 0.5, 5.0, 2.23) # القيمة التي في صورتك
    with col2:
        st.image(match_data['teams']['away']['logo'], width=80)
        a_xg = st.slider(f"قوة {a_name}:", 0.5, 5.0, 1.85)

    if st.button("🚀 إطلاق المحاكاة السيادية الحقيقية"):
        h_sim = np.random.poisson(h_xg, 100000)
        a_sim = np.random.poisson(a_xg, 100000)
        
        score_h, score_a = int(np.mean(h_sim)), int(np.mean(a_sim))
        corners = int((h_xg + a_xg) * 3.8) # توقع الركنيات
        win_p = (h_sim > a_sim).mean() * 100

        st.markdown(f"""
            <div style='margin-top:20px;'>
                <h1 style='font-size:5rem; color:#D4AF37;'>{score_h} - {score_a}</h1>
                <div style='display:flex; justify-content:space-around;'>
                    <div class='stat-badge'><p>🚩 ركنيات</p><h2>{corners}</h2></div>
                    <div class='stat-badge'><p>📊 فوز {h_name}</p><h2>{win_p:.1f}%</h2></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
else:
    st.error("📡 السيرفر العالمي لم يرسل مباريات اليوم حالياً. استخدم 'الوضع اليدوي' أسفل الشاشة.")
    # وضع يدوي احتياطي (نفس صورتك)
    h_manual = st.text_input("الفريق المضيف:", "الترجي")
    a_manual = st.text_input("الفريق الضيف:", "النادي الافريقي")

st.markdown("</div>", unsafe_allow_html=True)
