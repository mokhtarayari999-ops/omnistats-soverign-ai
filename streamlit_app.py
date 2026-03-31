import streamlit as st
import numpy as np
import time

# --- 🔱 AURASTATS ARABIC EMPIRE v320.0 ---
st.set_page_config(page_title="AuraStats Arabic Empire", layout="wide", page_icon="🔱")

# التصميم الإمبراطوري (ذهبي وأسود)
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #0a0a0a 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .main-card { border: 2px solid #D4AF37; border-radius: 40px; padding: 30px; background: rgba(212,175,55,0.03); text-align: center; }
    .stat-badge { background: #111; border: 1px solid #D4AF37; border-radius: 15px; padding: 10px; margin: 10px; }
    .score-display { font-size: 6rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #F2D388 50%, #D4AF37 100%); color: #000 !important; font-weight: 900; border-radius: 100px; height: 70px; font-size: 1.5rem; width: 100%; transition: 0.5s; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37; font-size:3rem;'>AURASTATS ARABIC 🏆</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888;'>محرك التوقعات للدوريات العربية والركنيات</p>", unsafe_allow_html=True)

# --- واجهة اختيار الدوري العربي ---
leagues = ["🇹🇳 الدوري التونسي", "🇪🇬 الدوري المصري", "🇸🇦 الدوري السعودي", "🇲🇦 الدوري المغربي", "🌍 أبطال أفريقيا"]
sel_league = st.selectbox("🎯 اختر البطولة العربية:", leagues)

st.markdown("<div class='main-card'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    h_name = st.text_input("الفريق المضيف (Home):", value="الترجي")
    h_xg = st.slider(f"قوة هجوم {h_name}:", 0.5, 5.0, 1.8)
with col2:
    a_name = st.text_input("الفريق الضيف (Away):", value="الأهلي")
    a_xg = st.slider(f"قوة هجوم {a_name}:", 0.5, 5.0, 1.5)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 إطلاق المحاكاة السيادية العربية"):
    with st.spinner('🎯 جاري تحليل 100,000 سيناريو احتمالي...'):
        time.sleep(1.2)
        
        # محرك بويسون للتوقعات
        h_sim = np.random.poisson(h_xg, 100000)
        a_sim = np.random.poisson(a_xg, 100000)
        
        # حساب النتائج
        score_h, score_a = int(np.mean(h_sim)), int(np.mean(a_sim))
        win_prob = (h_sim > a_sim).mean() * 100
        
        # خوارزمية توقع الركنيات (بناءً على الـ xG والضغط الهجومي)
        total_xg = h_xg + a_xg
        corners = int(total_xg * 3.7) # معادلة الركنيات المتوقعة
        
        # عرض النتائج الشاملة
        st.markdown(f"""
            <div style='margin-top:20px;'>
                <p style='color:#D4AF37; font-size:1.5rem;'>النتيجة المتوقعة</p>
                <h1 class='score-display'>{score_h} - {score_a}</h1>
                <h2 style='color:white;'>{h_name} vs {a_name}</h2>
                <hr style='border:1px solid #D4AF37; opacity:0.3; margin:30px 0;'>
                <div style='display:flex; justify-content:space-around; flex-wrap:wrap;'>
                    <div class='stat-badge'>
                        <p style='color:#D4AF37; margin:0;'>🚩 ركنيات متوقعة</p>
                        <h2 style='color:white; margin:0;'>{corners}</h2>
                    </div>
                    <div class='stat-badge'>
                        <p style='color:#D4AF37; margin:0;'>📊 نسبة الفوز ({h_name})</p>
                        <h2 style='color:white; margin:0;'>{win_prob:.1f}%</h2>
                    </div>
                    <div class='stat-badge'>
                        <p style='color:#D4AF37; margin:0;'>🔥 مستوى الإثارة</p>
                        <h2 style='color:white; margin:0;'>{"عالي" if total_xg > 3 else "متوسط"}</h2>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#333; margin-top:50px;'>AURASTATS AI | ARABIC EDITION v320.0</p>", unsafe_allow_html=True)
    
