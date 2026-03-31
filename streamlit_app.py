import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AURASTATS ARABIC PRO: LIVE SYNC v950.0 ---
st.set_page_config(page_title="AuraStats Arabic Pro", layout="wide", page_icon="🔱")

# 👇 ضع مفتاحك هنا (من موقع api-football.com) لتحديث البيانات حياً
API_KEY = "8abdb813dece636993e2182de4ee374a" 

# --- دالة التحديث الحي (Live Data Sync) ---
def get_live_empire_data(league_id):
    headers = {'x-apisports-key': API_KEY}
    url = "https://api-sports.io"
    # رصد مباريات اليوم 31 مارس 2026 والمباريات الـ 10 القادمة
    params = {'league': league_id, 'season': 2025, 'next': 10}
    try:
        res = requests.get(url, headers=headers, params=params, timeout=10).json()
        return res.get('response', [])
    except: return []

# --- CSS الهوية الإمبراطورية الفائقة ---
st.markdown("""
    <style>
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .main-panel { border: 2px solid #D4AF37; border-radius: 45px; padding: 25px; background: rgba(212,175,55,0.02); text-align: center; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #F2D388 50%, #D4AF37 100%); color: black !important; font-weight: 900; border-radius: 100px; height: 75px; font-size: 1.6rem; border: none; box-shadow: 0 0 40px rgba(212,175,55,0.4); }
    .stat-badge { background: #111; border: 1px solid #D4AF37; border-radius: 25px; padding: 20px; margin: 10px; min-width: 140px; }
    .score-display { font-size: 7.5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 50px #D4AF37; margin: 0; line-height: 1; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37; font-size:3.8rem; margin-bottom:0;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)

# 🌍 مصفوفة الدوريات العربية والخليجية (مع الرموز البرمجية للـ API)
leagues_api = {
    "🇹🇳 الدوري التونسي الممتاز": 202,
    "🇪🇬 الدوري المصري الممتاز": 233,
    "🇸🇦 دوري روشن السعودي": 307,
    "🇶🇦 دوري نجوم قطر": 305,
    "🇲🇦 الدوري المغربي": 200,
    "🇦🇪 الدوري الإماراتي": 301,
    "🇩🇿 الدوري الجزائري": 194,
    "🇴🇲 دوري عمانتل": 313,
    "🌍 دوري أبطال أفريقيا": 12
}

sel_league_name = st.selectbox("🎯 اختر البطولة المراد تحديث بياناتها حياً:", list(leagues_api.keys()))
league_id = leagues_api[sel_league_name]

# --- عملية التحديث التلقائي ---
with st.spinner('📡 جاري رصد الملاعب وتحديث البيانات اللحظية لعام 2026...'):
    live_matches = get_live_empire_data(league_id)

st.markdown("<div class='main-panel'>", unsafe_allow_html=True)

if live_matches:
    # عرض المباريات الحقيقية المحدثة
    match_options = {f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}": m for m in live_matches}
    selected_match_label = st.selectbox("المباريات الحقيقية المرصودة (Live):", list(match_options.keys()))
    
    m_data = match_options[selected_match_label]
    h_name = m_data['teams']['home']['name']
    a_name = m_data['teams']['away']['name']
    h_logo = m_data['teams']['home']['logo']
    a_logo = m_data['teams']['away']['logo']
    
    st.success(f"✅ تم تحديث بيانات {sel_league_name} بنجاح!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(h_logo, width=80)
        h_xg = st.slider(f"قوة {h_name}:", 0.5, 5.0, 2.10)
    with col2:
        st.image(a_logo, width=80)
        a_xg = st.slider(f"قوة {a_name}:", 0.5, 5.0, 1.45)

    if st.button("🚀 إطلاق المحاكاة السيادية الحقيقية"):
        with st.spinner('🎯 تحليل 100,000 سيناريو احتمالي...'):
            h_sim = np.random.poisson(h_xg, 100000)
            a_sim = np.random.poisson(a_xg, 100000)
            score_h, score_a = int(np.mean(h_sim)), int(np.mean(a_sim))
            corners = int((h_xg + a_xg) * 3.8)
            win_p = (h_sim > a_sim).mean() * 100

            st.markdown(f"<h1 class='score-display'>{score_h} - {score_a}</h1>", unsafe_allow_html=True)
            st.markdown(f"""
                <div style='display:flex; justify-content:center; flex-wrap:wrap;'>
                    <div class='stat-badge'><p>🚩 ركنيات</p><h2>{corners}</h2></div>
                    <div class='stat-badge'><p>📈 فوز {h_name}</p><h2>{win_p:.1f}%</h2></div>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
else:
    # وضع الطوارئ في حال تعذر الاتصال بالسيرفر
    st.error("⚠️ السيرفر العالمي لم يرسل بيانات اليوم بعد. استخدم الوضع اليدوي أدناه:")
    h_manual = st.text_input("المضيف يدوياً:", "الترجي")
    a_manual = st.text_input("الضيف يدوياً:", "الأهلي")
    st.info("💡 بمجرد عودة السيرفر للعمل، ستظهر الفرق الحقيقية هنا تلقائياً.")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#333; margin-top:50px;'>AURASTATS AI | v950.0 LIVE SYNC EDITION</p>", unsafe_allow_html=True)
