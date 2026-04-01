import streamlit as st
import numpy as np
import time
import plotly.graph_objects as go

# --- 🛰️ إعدادات المحرك السيادي ---
st.set_page_config(page_title="ARABIC PRO | PHANTOM", layout="wide", initial_sidebar_state="collapsed")

# --- 🎨 CSS التصميم الخيالي (زجاجي، ذهبي، خطوط متوسطة) ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp { background: radial-gradient(circle, #0f0f0f 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    
    /* رأس الصفحة الأنيق */
    .phantom-header { text-align: center; padding: 30px 10px; border-bottom: 1px solid rgba(212,175,55,0.3); margin-bottom: 25px; }
    .phantom-title { font-size: 2.5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 15px rgba(212,175,55,0.5); margin: 0; }
    
    /* بطاقة النتيجة الزجاجية */
    .glass-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(212,175,55,0.2); border-radius: 25px; padding: 25px; text-align: center; backdrop-filter: blur(10px); box-shadow: 0 15px 35px rgba(0,0,0,0.5); margin-top: 20px; }
    .score-text { font-size: 5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 20px #D4AF37; margin: 10px 0; line-height: 1.2; }
    
    /* صناديق الإحصائيات المتوسطة */
    .stat-grid { display: flex; justify-content: space-around; flex-wrap: wrap; gap: 10px; margin-top: 20px; }
    .stat-pill { background: rgba(0,0,0,0.6); border: 1px solid #D4AF37; border-radius: 15px; padding: 12px; min-width: 100px; flex: 1; }
    .stat-pill p { font-size: 0.8rem; color: #888; margin: 0; }
    .stat-pill h3 { font-size: 1.2rem; color: #fff; margin: 5px 0 0 0; }
    
    /* الزر الخيالي المتوهج */
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #8A6D3B) !important; color: #000 !important; font-weight: 900 !important; border-radius: 15px !important; border: none !important; padding: 12px !important; width: 100% !important; font-size: 1.2rem !important; transition: 0.3s !important; box-shadow: 0 5px 15px rgba(212,175,55,0.3) !important; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 8px 25px rgba(212,175,55,0.5) !important; }
    
    /* تحسين المدخلات (حجم متوسط) */
    .stTextInput>div>div>input { background: #0a0a0a !important; border: 1px solid #D4AF37 !important; color: #fff !important; font-size: 1.1rem !important; border-radius: 12px !important; text-align: center !important; }
    label { color: #D4AF37 !important; font-weight: bold !important; font-size: 1rem !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 🏟️ واجهة الخيال ---
st.markdown("<div class='phantom-header'><h1 class='phantom-title'>ARABIC PRO</h1><p style='color:#666;'>نظام المحاكاة الخيالي - إصدار 2026</p></div>", unsafe_allow_html=True)

# مدخلات متوازنة الحجم
col1, col2 = st.columns(2)
with col1:
    h_name = st.text_input("اسم المستضيف:", "مانشستر سيتي")
    h_pwr = st.slider("القوة الهجومية:", 1.0, 10.0, 7.5)
    h_def = st.slider("الصلابة الدفاعية:", 1.0, 10.0, 8.0)

with col2:
    a_name = st.text_input("اسم الضيف:", "ريال مدريد")
    a_pwr = st.slider("القوة الهجومية :", 1.0, 10.0, 7.0)
    a_def = st.slider("الصلابة الدفاعية :", 1.0, 10.0, 7.8)

st.markdown("<br>", unsafe_allow_html=True)

# --- 🚀 محرك المحاكاة الفانتوم ---
if st.button("🔱 بـدء المحاكاة الخرافية"):
    with st.spinner('⏳ جاري تحليل موازين القوى...'):
        time.sleep(2)
        
        # معادلة المحاكاة (متوسط الأهداف المتوقع)
        h_idx = max(0.2, (h_pwr * (11 - a_def)) / 25)
        a_idx = max(0.2, (a_pwr * (11 - h_def)) / 25)
        
        # محاكاة Poisson
        h_sim = np.random.poisson(h_idx, 100000)
        a_sim = np.random.poisson(a_idx, 100000)
        
        score_h = int(np.round(np.mean(h_sim)))
        score_a = int(np.round(np.mean(a_sim)))
        win_h = (h_sim > a_sim).mean() * 100
        draw = (h_sim == a_sim).mean() * 100
        win_a = (h_sim < a_sim).mean() * 100
        
        st.markdown(f"""
            <div class='glass-card'>
                <p style='color: #888; font-size: 0.9rem; margin:0;'>النتيجة المتوقعة</p>
                <div class='score-text'>{score_h} - {score_a}</div>
                <h2 style='color: #fff; font-size: 1.5rem;'>{h_name} <span style='color:#D4AF37;'>❌</span> {a_name}</h2>
                <div class='stat-grid'>
                    <div class='stat-pill'><p>فوز {h_name}</p><h3>{win_h:.1f}%</h3></div>
                    <div class='stat-pill'><p>تعادل</p><h3>{draw:.1f}%</h3></div>
                    <div class='stat-pill'><p>فوز {a_name}</p><h3>{win_a:.1f}%</h3></div>
                </div>
                <div class='stat-grid'>
                    <div class='stat-pill'><p>ركنيات</p><h3>{int((h_idx+a_idx)*4)}</h3></div>
                    <div class='stat-pill'><p>بطاقات</p><h3>{int((h_def+a_def)*0.2)}</h3></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.markdown("<p style='text-align: center; color: #333; margin-top: 40px; font-size: 0.8rem;'>ARABIC PRO | PHANTOM SYSTEM 2026</p>", unsafe_allow_html=True)
