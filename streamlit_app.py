import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# 1. إعدادات الفخامة المطلقة
st.set_page_config(page_title="OmniStats Sovereign Pro", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    .stApp { background: radial-gradient(circle at center, #111 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .glass-panel { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 35px; padding: 40px; backdrop-filter: blur(25px); }
    .glow-header { font-family: 'Orbitron', sans-serif; font-size: 2.5rem; text-align: center; color: #D4AF37; text-shadow: 0 0 20px #D4AF37; }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #F2D388, #D4AF37); color: #000 !important; font-weight: 900; border-radius: 100px; height: 60px; border: none; font-size: 1.4rem; transition: 0.5s; width: 100%; box-shadow: 0 10px 40px rgba(212, 175, 55, 0.3); }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 20px 60px rgba(212, 175, 55, 0.6); }
    .metric-box { background: rgba(212, 175, 55, 0.05); border-radius: 20px; padding: 20px; border: 1px solid rgba(212, 175, 55, 0.1); text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 2. محرك المحاكاة الكمي (50,000 سيناريو)
def simulate_sovereign(h_avg, a_avg):
    sims = 50000
    h_g = np.random.poisson(h_avg, sims)
    a_g = np.random.poisson(a_avg, sims)
    scores = list(zip(h_g, a_g))
    best_score = max(set(scores), key=scores.count)
    return (h_g > a_g).mean()*100, (h_g == a_g).mean()*100, (a_g > h_g).mean()*100, best_score

# 3. واجهة المستخدم
st.markdown("<p class='glow-header'>OMNISTATS CORE</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>مركز التحليل الاستراتيجي 🧠</h3>", unsafe_allow_html=True)
    
    col_h, col_a = st.columns(2)
    with col_h:
        home = st.text_input("الفريق المضيف:", "أرسنال")
        h_power = st.slider("قوة الهجوم (أهداف متوقعة):", 0.5, 5.0, 2.2, key="h")
    with col_a:
        away = st.text_input("الفريق الضيف:", "مانشستر سيتي")
        away_power = st.slider("قوة الهجوم (أهداف متوقعة):", 0.5, 5.0, 1.8, key="a")

    if st.button("إطلاق المحاكاة السيادية ⚡"):
        with st.spinner('يتم الآن معالجة 50,000 سيناريو...'):
            time.sleep(1.2)
            h_p, d_p, a_p, score = simulate_sovereign(h_power, away_power)
            
            st.markdown("<br><hr style='opacity:0.2'><br>", unsafe_allow_html=True)
            r1, r2, r3 = st.columns(3)
            with r1: st.markdown(f"<div class='metric-box'><p>فوز {home}</p><h2>{round(h_p, 1)}%</h2></div>", unsafe_allow_html=True)
            with r2: st.markdown(f"<div class='metric-box'><p>التعادل</p><h2>{round(d_p, 1)}%</h2></div>", unsafe_allow_html=True)
            with r3: st.markdown(f"<div class='metric-box'><p>فوز {away}</p><h2>{round(a_p, 1)}%</h2></div>", unsafe_allow_html=True)
            
            st.markdown(f"<div style='text-align:center; padding:25px; border:1px solid #D4AF37; border-radius:50px; margin-top:30px;'><h2>النتيجة المتوقعة: <span style='color:white;'>{score[0]} - {score[1]}</span></h2></div>", unsafe_allow_html=True)
            
            # رادار القوة الذهبي
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(r=[h_power*20, 80, 70], theta=['الهجوم','الدفاع','الاستحواذ'], fill='toself', name=home, line_color='#D4AF37'))
            fig.add_trace(go.Scatterpolar(r=[away_power*20, 75, 85], theta=['الهجوم','الدفاع','الاستحواذ'], fill='toself', name=away, line_color='#fff'))
            fig.update_layout(polar=dict(bgcolor="rgba(0,0,0,0)", radialaxis=dict(visible=False)), paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#D4AF37"))
            st.plotly_chart(fig, use_container_width=True)
            st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#222; margin-top:50px;'>OMNISTATS | INDEPENDENT BUILD v14.0</p>", unsafe_allow_html=True)
    
