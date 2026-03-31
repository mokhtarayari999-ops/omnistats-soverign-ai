import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random
import time

# --- 🔱 AuraStats AI: THE ULTIMATE COMMAND v32.0 ---
st.set_page_config(page_title="AuraStats AI | The Sovereign", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background: radial-gradient(circle at top, #0d0d0d 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .supreme-panel { background: rgba(212, 175, 55, 0.01); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 45px; padding: 40px; backdrop-filter: blur(50px); }
    .glow-header { font-family: 'Orbitron', sans-serif; font-size: 3rem; text-align: center; color: #D4AF37; text-shadow: 0 0 40px #D4AF37; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #F2D388 50%, #D4AF37 100%); color: #000 !important; font-weight: 900; border-radius: 100px; height: 75px; border: none; font-size: 1.6rem; width: 100%; transition: 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
    .stButton>button:hover { transform: scale(1.03) translateY(-8px); box-shadow: 0 30px 80px rgba(212, 175, 55, 0.6); }
    .prediction-card { background: rgba(255,255,255,0.02); border-radius: 25px; padding: 25px; border: 1px solid rgba(212, 175, 55, 0.1); text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 1. محرك "السيناريو والركنيات واللاعبين" الذكي
def get_detailed_intel(h_name, a_name, h_xg, a_xg):
    # محاكاة الركنيات
    h_cor = int(h_xg * 3.2 + random.randint(1, 4))
    a_cor = int(a_xg * 3.2 + random.randint(0, 3))
    
    # اختيار الهداف المحتمل (تلقائي)
    scorers = ["المهاجم الصريح", "صانع الألعاب", "الجناح الطائر", "رأسية من مدافع"]
    h_scorer = random.choice(scorers)
    a_scorer = random.choice(scorers)
    
    # سيناريوهات المباراة
    scenarios = [
        "🔥 ريمونتادا متوقعة في الشوط الثاني.",
        "🛡️ جدار دفاعي صلب سيصعب المباراة.",
        "⚡ أهداف مبكرة ستغير مجرى التكتيك.",
        "⚖️ صراع بدني كبير في وسط الميدان."
    ]
    return h_cor, a_cor, h_scorer, a_scorer, random.choice(scenarios)

# 2. محاكي بويسون (100,000 سيناريو - مع إصلاح الفواصل)
def run_quantum_sim(h_val, a_val):
    try:
        # إصلاح ذكي: تحويل الفاصلة العربية/الفرنسية (,) إلى نقطة برمجية (.)
        h_avg = float(str(h_val).replace(',', '.'))
        a_avg = float(str(a_val).replace(',', '.'))
        
        sims = 100000
        h_g = np.random.poisson(h_avg, sims)
        a_g = np.random.poisson(a_avg, sims)
        
        scores = list(zip(h_g, a_g))
        best = max(set(scores), key=scores.count)
        
        hw = (h_g > a_g).mean() * 100
        dr = (h_g == a_g).mean() * 100
        aw = (a_g > h_g).mean() * 100
        
        return round(hw, 1), round(dr, 1), round(aw, 1), f"{int(best)} - {int(best)}", h_avg, a_avg
    except:
        return None

st.markdown("<p class='glow-header'>AURASTATS AI</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444; letter-spacing:15px; margin-bottom:40px;'>THE CROWN BUILD v32.0</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='supreme-panel'>", unsafe_allow_html=True)
    
    st.info("🎯 وضع التحليل الشامل (Manual Expansion)")
    c1, c2 = st.columns(2)
    with c1:
        h_name = st.text_input("الفريق المضيف (Home):", "الترجي")
        h_input = st.text_input(f"قوة {h_name} (xG):", "2.1")
    with c2:
        a_name = st.text_input("الضيف المتحدي (Away):", "الأهلي")
        a_input = st.text_input(f"قوة {a_name} (xG):", "1.5")

    if st.button("إطلاق المحاكاة السيادية العليا 🔱🔥"):
        with st.spinner('AuraStats يحلل 100,000 سيناريو وتفاصيل المباراة...'):
            time.sleep(2)
            results = run_quantum_sim(h_input, a_input)
            
            if results:
                hw, dr, aw, score_txt, h_fix, a_fix = results
                h_cor, a_cor, h_sco, a_sco, scenario = get_detailed_intel(h_name, a_name, h_fix, a_fix)
                
                # النتيجة الرئيسية
                st.markdown(f"<div style='text-align:center; padding:50px; border:2px solid #D4AF37; border-radius:150px; margin:40px 0; background:rgba(212,175,55,0.05);'><p style='color:#D4AF37; margin:0; letter-spacing:10px;'>النتيجة المتوقعة</p><h1 style='font-size:7rem; color:white; margin:15px 0;'>{score_txt}</h1></div>", unsafe_allow_html=True)
                
                # تفاصيل المباراة (العودة القوية)
                st.markdown("### 🔱 التوقعات الاستخباراتية الشاملة")
                r1, r2, r3 = st.columns(3)
                with r1:
                    st.markdown(f"<div class='prediction-card'><b>🚩 إجمالي الركنيات</b><h2 style='color:white;'>{h_cor + a_cor}</h2><p>متوقع لـ {h_name}: {h_cor}</p></div>", unsafe_allow_html=True)
                with r2:
                    st.markdown(f"<div class='prediction-card'><b>⚽ الهداف المحتمل</b><h3 style='color:white;'>{h_sco}</h3><p>مرشح من فريق {h_name}</p></div>", unsafe_allow_html=True)
                with r3:
                    st.markdown(f"<div class='prediction-card'><b>🟨 الإنذارات</b><h2 style='color:white;'>{random.randint(3, 7)}</h2><p>مستوى الحدة: مرتفع</p></div>", unsafe_allow_html=True)
                
                # السيناريو التكتيكي
                st.markdown(f"<div style='background:rgba(212,175,55,0.1); padding:25px; border-radius:25px; border-left:10px solid #D4AF37; margin-bottom:40px;'><b>📌 السيناريو المتوقع:</b><p style='font-size:20px; margin-top:10px;'>{scenario}</p></div>", unsafe_allow_html=True)
                
                # نسب الفوز
                st.write("---")
                m1, m2, m3 = st.columns(3)
                m1.metric(f"فوز {h_name}", f"{hw}%")
                m2.metric("التعادل", f"{dr}%")
                m3.metric(f"فوز {a_name}", f"{aw}%")
                
                st.balloons()
            else:
                st.error("⚠️ يرجى التأكد من إدخال أرقام صحيحة في خانات الـ xG.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#222; margin-top:80px; font-family:Orbitron;'>AURASTATS AI | THE SUPREME CROWN | v32.0 FINAL</p>", unsafe_allow_html=True)
    
