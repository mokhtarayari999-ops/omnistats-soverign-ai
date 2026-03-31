import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random
import time
import re

# --- 🔱 AuraStats AI: THE IMMORTAL ENGINE v33.0 ---
st.set_page_config(page_title="AuraStats AI | Immortal", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background: radial-gradient(circle at top, #0d0d0d 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .supreme-panel { background: rgba(212, 175, 55, 0.01); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 45px; padding: 40px; backdrop-filter: blur(50px); }
    .glow-header { font-family: 'Orbitron', sans-serif; font-size: 3rem; text-align: center; color: #D4AF37; text-shadow: 0 0 40px #D4AF37; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #F2D388 50%, #D4AF37 100%); color: #000 !important; font-weight: 900; border-radius: 100px; height: 75px; border: none; font-size: 1.6rem; width: 100%; transition: 0.5s; }
    .prediction-card { background: rgba(255,255,255,0.02); border-radius: 25px; padding: 25px; border: 1px solid rgba(212, 175, 55, 0.1); text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# دالة التنظيف الذري للبيانات (The Bulletproof Cleaner)
def clean_numeric_input(value):
    try:
        # إزالة كل المسافات والرموز غير الرقمية باستثناء النقطة والفاصلة
        cleaned = re.sub(r'[^\d.,]', '', str(value))
        # تحويل الفاصلة إلى نقطة
        cleaned = cleaned.replace(',', '.')
        return float(cleaned)
    except:
        return None

# محرك بويسون والسيناريوهات
def run_quantum_sim(h_val, a_val):
    h_avg = clean_numeric_input(h_val)
    a_avg = clean_numeric_input(a_val)
    
    if h_avg is not None and a_avg is not None:
        sims = 100000
        h_g = np.random.poisson(h_avg, sims)
        a_g = np.random.poisson(a_avg, sims)
        scores = list(zip(h_g, a_g))
        best = max(set(scores), key=scores.count)
        hw, dr, aw = (h_g > a_g).mean()*100, (h_g == a_g).mean()*100, (a_g > h_g).mean()*100
        return round(hw, 1), round(dr, 1), round(aw, 1), f"{int(best[0])} - {int(best[1])}", h_avg, a_avg
    return None

st.markdown("<p class='glow-header'>AURASTATS AI</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='supreme-panel'>", unsafe_allow_html=True)
    
    st.info("🎯 وضع التحليل الشامل (Sovereign Expansion)")
    c1, c2 = st.columns(2)
    with c1:
        h_name = st.text_input("الفريق المضيف (Home):", "الترجي")
        h_input = st.text_input(f"قوة {h_name} (xG):", "1.80")
    with c2:
        a_name = st.text_input("الضيف المتحدي (Away):", "الأهلي")
        a_input = st.text_input(f"قوة {a_name} (xG):", "1.50")

    if st.button("إطلاق المحاكاة السيادية العليا 🔱🔥"):
        with st.spinner('AuraStats يطهر البيانات ويحلل 100,000 سيناريو...'):
            time.sleep(1.5)
            results = run_quantum_sim(h_input, a_input)
            
            if results:
                hw, dr, aw, score_txt, h_fix, a_fix = results
                
                # عرض النتيجة الرئيسية
                st.markdown(f"<div style='text-align:center; padding:50px; border:2px solid #D4AF37; border-radius:150px; margin:40px 0; background:rgba(212,175,55,0.05);'><h1 style='font-size:7rem; color:white; margin:0;'>{score_txt}</h1></div>", unsafe_allow_html=True)
                
                # عرض تفاصيل إضافية
                res_c1, res_c2, res_c3 = st.columns(3)
                with res_c1: st.markdown(f"<div class='prediction-card'><b>🚩 ركنيات متوقعة</b><h2>{int((h_fix+a_fix)*3.5)}</h2></div>", unsafe_allow_html=True)
                with res_c2: st.markdown(f"<div class='prediction-card'><b>⚽ الهداف المرجح</b><h3>مهاجم {h_name}</h3></div>", unsafe_allow_html=True)
                with res_c3: st.markdown(f"<div class='prediction-card'><b>📊 فرصة الفوز</b><h2>{hw}%</h2></div>", unsafe_allow_html=True)
                
                st.balloons()
            else:
                st.error("⚠️ يرجى التأكد من كتابة الأرقام بشكل صحيح (مثال: 1.50)")

    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#222; margin-top:80px;'>AURASTATS AI | v33.0 IMMORTAL</p>", unsafe_allow_html=True)
