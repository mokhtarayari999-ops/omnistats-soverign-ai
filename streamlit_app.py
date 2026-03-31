import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AuraStats AI: The Sovereign Global Engine v43.0 ---
st.set_page_config(page_title="AuraStats AI | Immortal", layout="wide", page_icon="🔱")

# 👇 ضع مفتاح الـ API الخاص بك هنا بدقة (تأكد أنه بين العلامتين " ")
API_KEY = "c2f6d97fe715446c4be7f30600191daa" 

# دالة جلب البيانات الذكية (تحاول في أكثر من موسم لضمان النتائج)
def get_matches_smart(league_id):
    headers = {'x-apisports-key': API_KEY}
    url = "https://api-sports.io"
    
    # المحاولة الأولى: موسم 2025 (الموسم الحالي لعام 2026)
    params = {'league': league_id, 'season': 2025, 'next': 15}
    try:
        res = requests.get(url, headers=headers, params=params, timeout=10).json()
        if res.get('response'):
            return res['response']
        
        # المحاولة الثانية: إذا لم نجد مباريات، نجرب موسم 2024
        params['season'] = 2024
        res_alt = requests.get(url, headers=headers, params=params, timeout=10).json()
        return res_alt.get('response', [])
    except:
        return []

# --- تصميم الواجهة الفخمة ---
st.markdown("""
    <style>
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .main-panel { border: 2px solid #D4AF37; border-radius: 30px; padding: 25px; background: rgba(212,175,55,0.02); }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #F2D388); color: black !important; font-weight: bold; border-radius: 50px; height: 60px; width: 100%; border:none; font-size: 1.3rem; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS AI 🏆</h1>", unsafe_allow_html=True)

# بوابة التحكم
mode = st.radio("🔱 بوابة التحكم السيادي:", ["🌐 آلي (API)", "✍️ يدوي (Manual)"], horizontal=True)

st.markdown("<div class='main-panel'>", unsafe_allow_html=True)

if mode == "🌐 آلي (API)":
    leagues = {
        "دوري أبطال أوروبا 🇪🇺": 2,
        "الدوري الإنجليزي الممتاز 🏴󠁧󠁢󠁥󠁮󠁧󠁿": 39,
        "الدوري الإسباني 🇪🇸": 140,
        "الدوري التونسي الممتاز 🇹🇳": 202,
        "الدوري السعودي (روشن) 🇸🇦": 307
    }
    sel_league_name = st.selectbox("اختر البطولة العالمية:", list(leagues.keys()))
    league_id = leagues[sel_league_name]
    
    with st.spinner('📡 جاري الاتصال بالسيرفرات العالمية...'):
        matches = get_matches_smart(league_id)
    
    if matches:
        match_options = {f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}": m for m in matches}
        selected_match_label = st.selectbox("اختر المباراة القادمة:", list(match_options.keys()))
        
        match_data = match_options[selected_match_label]
        h_name = match_data['teams']['home']['name']
        a_name = match_data['teams']['away']['name']
        # قيم xG تقديرية ذكية (يمكنك تعديلها يدوياً إذا أردت دقة أكبر)
        h_xg = st.slider(f"قوة {h_name} (xG):", 0.5, 4.0, 1.95)
        a_xg = st.slider(f"قوة {a_name} (xG):", 0.5, 4.0, 1.40)
    else:
        st.error("⚠️ لم نجد مباريات مجدولة حالياً. تأكد من تفعيل المفتاح أو جرب 'الوضع اليدوي'.")
        h_xg = 0

else:
    # الوضع اليدوي المفضل لديك (تخصيص كامل)
    col1, col2 = st.columns(2)
    with col1:
        h_name = st.text_input("الفريق المضيف:", "الترجي")
        h_xg = st.number_input(f"قوة {h_name} (xG):", value=1.80)
    with col2:
        a_name = st.text_input("الضيف المتحدي:", "الأهلي")
        a_xg = st.number_input(f"قوة {a_name} (xG):", value=1.50)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 إطلاق المحاكاة السيادية العليا"):
    if h_xg > 0:
        with st.spinner('AuraStats يحلل 100,000 سيناريو بويسون...'):
            time.sleep(1.2)
            # محرك المحاكاة الاحتمالية
            h_sim = np.random.poisson(h_xg, 100000)
            a_sim = np.random.poisson(a_xg, 100000)
            
            # حساب النتيجة الأكثر تكراراً (Mode)
            res = list(zip(h_sim, a_sim))
            final_score = max(set(res), key=res.count)
            
            st.markdown(f"""
                <div style='text-align:center; padding:30px; border:2px solid #D4AF37; border-radius:100px; margin-top:20px; background:rgba(212,175,55,0.05);'>
                    <p style='color:#D4AF37; margin:0;'>النتيجة المتوقعة</p>
                    <h1 style='font-size:6rem; color:white; margin:0;'>{final_score[0]} - {final_score[1]}</h1>
                    <p style='font-size:1.2rem;'>مبنية على تحليل 100 ألف احتمال</p>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
    else:
        st.warning("⚠️ يرجى اختيار مباراة أو إدخال بيانات القوة أولاً.")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444; margin-top:50px;'>AURASTATS AI | v43.0 IMMORTAL EDITION</p>", unsafe_allow_html=True)
