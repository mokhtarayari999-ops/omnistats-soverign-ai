import streamlit as st
import numpy as np
import time

# --- 👑 AuraStats Supreme v31.0 ---
st.set_page_config(page_title="AuraStats AI | Immortal", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background: radial-gradient(circle at center, #0a0a0a 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .supreme-panel { background: rgba(212, 175, 55, 0.01); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 40px; padding: 30px; backdrop-filter: blur(40px); }
    .glow-header { font-family: 'Orbitron', sans-serif; font-size: 2.5rem; text-align: center; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #F2D388 50%, #D4AF37 100%); color: #000 !important; font-weight: 900; border-radius: 100px; height: 70px; border: none; font-size: 1.5rem; width: 100%; transition: 0.5s; }
    </style>
    """, unsafe_allow_html=True)

# محاكي بويسون (مصحح للتعامل مع أي مدخلات)
def run_quantum_sim(h_val, a_val):
    try:
        # تحويل المدخلات إلى أرقام عشرية صحيحة (علاج مشكلة الفاصلة)
        h_avg = float(str(h_val).replace(',', '.'))
        a_avg = float(str(a_val).replace(',', '.'))
        
        sims = 150000
        h_g = np.random.poisson(h_avg, sims)
        a_g = np.random.poisson(a_avg, sims)
        
        hw = (h_g > a_g).mean() * 100
        dr = (h_g == a_g).mean() * 100
        aw = (a_g > h_g).mean() * 100
        
        scores = list(zip(h_g, a_g))
        best = max(set(scores), key=scores.count)
        return round(hw, 1), round(dr, 1), round(aw, 1), f"{int(best[0])} - {int(best[1])}"
    except:
        return 0, 0, 0, "Error"

st.markdown("<p class='glow-header'>AURASTATS AI</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='supreme-panel'>", unsafe_allow_html=True)
    
    st.info("🎯 وضع التحليل اليدوي المفتوح")
    c1, c2 = st.columns(2)
    with c1:
        h_name = st.text_input("اسم الفريق المضيف:", "الترجي")
        h_input = st.text_input(f"معدل أهداف {h_name} (xG):", "1.8")
    with c2:
        a_name = st.text_input("اسم الفريق الضيف:", "الأهلي")
        a_input = st.text_input(f"معدل أهداف {a_name} (xG):", "1.5")

    if st.button("إطلاق المحاكاة السيادية العليا 🔱🔥"):
        with st.spinner('AuraStats يعالج البيانات...'):
            time.sleep(1)
            hw, dr, aw, score = run_quantum_sim(h_input, a_input)
            
            if score != "Error":
                st.markdown(f"<div style='text-align:center; padding:40px; border:2px solid #D4AF37; border-radius:100px; margin:30px 0; background:rgba(212,175,55,0.05);'><h1 style='font-size:5rem; color:white; margin:0;'>{score}</h1></div>", unsafe_allow_html=True)
                r1, r2, r3 = st.columns(3)
                r1.metric(f"فوز {h_name}", f"{hw}%")
                r2.metric("التعادل", f"{dr}%")
                r3.metric(f"فوز {a_name}", f"{aw}%")
                st.balloons()
            else:
                st.error("⚠️ يرجى إدخال أرقام صحيحة في خانات الـ xG.")

    st.markdown("</div>", unsafe_allow_html=True)
        
