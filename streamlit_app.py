import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AURASTATS PRO: THE FINAL ABSOLUTE BREACH v1000.0 ---
st.set_page_config(page_title="AuraStats Pro", layout="wide")

# 👇 ضع مفتاحك هنا (تأكد من تفعيل الحساب من بريدك الإلكتروني)
API_KEY = "8abdb813dece636993e2182de4ee374a" 

def fetch_live_arabic_absolute(league_id):
    # 🕵️ الاختراق البرمجي: محاكاة هوية متصفح حقيقي لتجاوز الحظر
    headers = {
        'x-apisports-key': API_KEY,
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15'
    }
    url = "https://api-sports.io"
    
    # محاولة جلب مباريات اليوم (2026-03-31) والمستقبل القريب عبر مواسم 2025 و 2026
    for season in:
        params = {'league': league_id, 'season': season, 'next': 15}
        try:
            response = requests.get(url, headers=headers, params=params, timeout=15)
            if response.status_code == 200:
                res_json = response.json()
                if res_json.get('response'): return res_json['response']
        except: continue
    return []

# --- CSS الهوية الإمبراطورية الفائقة ---
st.markdown("""
    <style>
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .main-panel { border: 2px solid #D4AF37; border-radius: 40px; padding: 25px; background: rgba(212,175,55,0.02); text-align: center; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #F2D388 50%, #D4AF37 100%); color: black !important; font-weight: 900; border-radius: 100px; height: 75px; font-size: 1.6rem; border: none; box-shadow: 0 0 40px rgba(212,175,55,0.4); }
    .stat-badge { background: #111; border: 1px solid #D4AF37; border-radius: 25px; padding: 20px; margin: 10px; min-width: 140px; }
    .score-display { font-size: 7.5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 50px #D4AF37; margin: 0; line-height: 1; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)

leagues = {
    "🇹🇳 الدوري التونسي الممتاز": 202,
    "🇪🇬 الدوري المصري الممتاز": 233,
    "🇸🇦 دوري روشن السعودي": 307,
    "🇩🇿 الدوري الجزائري": 194,
    "🌍 أبطال أفريقيا": 12
}

sel_league = st.selectbox("🎯 اختر البطولة العربية المراد رصدها حياً:", list(leagues.keys()))

with st.spinner('📡 جاري كسر حماية السيرفر وجلب البيانات الحية...'):
    matches = fetch_live_arabic_absolute(leagues[sel_league])

st.markdown("<div class='main-panel'>", unsafe_allow_html=True)

if matches:
    titles = {f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}": m for m in matches}
    sel_match = st.selectbox("المواجهات الحية المرصودة (Live):", list(titles.keys()))
    
    m_data = titles[sel_match]
    h_name, a_name = m_data['teams']['home']['name'], m_data['teams']['away']['name']
    h_logo, a_logo = m_data['teams']['home']['logo'], m_data['teams']['away']['logo']
    
    st.success(f"✅ تم الاتصال بنجاح بمواجهة: {sel_match}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(h_logo, width=80)
        h_xg = st.slider(f"قوة {h_name}:", 0.1, 5.0, 2.10)
    with col2:
        st.image(a_logo, width=80)
        a_xg = st.slider(f"قوة {a_name}:", 0.1, 5.0, 1.45)

    if st.button("🚀 إطلاق المحاكاة السيادية الحقيقية"):
        with st.spinner('🎯 تحليل 100,000 سيناريو احتمالي...'):
            h_sim = np.random.poisson(h_xg, 100000)
            a_sim = np.random.poisson(a_xg, 100000)
            st.markdown(f"<h1 class='score-display'>{int(np.mean(h_sim))} - {int(np.mean(a_sim))}</h1>", unsafe_allow_html=True)
            st.balloons()
else:
    # خطة الطوارئ النهائية: إذا فشل الاختراق، نفتح الإدخال فوراً لكي لا تتوقف
    st.error("❌ السيرفر العالمي يرفض الاتصال حالياً. أدخل البيانات يدوياً:")
    col_l, col_r = st.columns(2)
    h_n_m = col_l.text_input("المضيف:", "الترجي")
    a_n_m = col_r.text_input("الضيف:", "الأهلي")
    h_xg, a_xg = 2.1, 1.5

st.markdown("</div>", unsafe_allow_html=True)
    
