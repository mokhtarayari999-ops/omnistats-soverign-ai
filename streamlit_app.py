import streamlit as st
import requests
import numpy as np
import plotly.graph_objects as go
from scipy.stats import poisson
import time

# --- 🔑 NUCLEAR CONFIG ---
API_KEY = "757497fe293f4e39a291cc5c575c6dc3" 
BASE_URL = "https://api.football-data.org"

# 1. التصميم البصري الفائق (The Sovereign Dark UI)
st.set_page_config(page_title="OmniStats Sovereign Elite", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    
    .stApp { background: radial-gradient(circle at center, #111 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    
    .glass-panel {
        background: rgba(255, 255, 255, 0.01);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 35px;
        padding: 40px;
        backdrop-filter: blur(30px);
        box-shadow: 0 0 100px rgba(212, 175, 55, 0.05);
    }
    
    .glow-header { font-family: 'Orbitron', sans-serif; font-size: 4rem; text-align: center; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; margin:0; }
    
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37, #F2D388, #D4AF37);
        color: #000 !important; font-weight: 900; border-radius: 100px;
        height: 80px; border: none; font-size: 1.6rem; transition: 0.5s; width: 100%;
        box-shadow: 0 10px 40px rgba(212, 175, 55, 0.3);
    }
    .stButton>button:hover { transform: scale(1.03) translateY(-5px); box-shadow: 0 20px 60px rgba(212, 175, 55, 0.6); }
    
    .metric-card { background: rgba(212, 175, 55, 0.05); border-radius: 20px; padding: 20px; border: 1px solid rgba(212, 175, 55, 0.1); text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 2. محرك البيانات الاستخباراتي
def fetch_data(league_code):
    url = f"{BASE_URL}{league_code}/standings"
    headers = {'X-Auth-Token': API_KEY}
    try:
        res = requests.get(url, headers=headers)
        return res.json()['standings'][0]['table'] if res.status_code == 200 else None
    except: return None

# 3. خوارزمية التوقع الكمي (Quantum Prediction)
def analyze_deep(h_avg, a_avg):
    sims = 50000
    h_g = np.random.poisson(h_avg, sims)
    a_g = np.random.poisson(a_avg, sims)
    
    # حساب احتمالات النتائج الدقيقة
    scores = list(zip(h_g, a_g))
    best_score = max(set(scores), key=scores.count)
    
    h_win = (h_g > a_g).mean() * 100
    draw = (h_g == a_g).mean() * 100
    a_win = (a_g > h_g).mean() * 100
    return round(h_win, 1), round(draw, 1), round(a_win, 1), best_score

# 4. بناء لوحة التحكم الأسطورية
st.markdown("<p class='glow-header'>OMNISTATS</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; letter-spacing:15px; color:#555;'>THE QUANTUM SOVEREIGN v10.0</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    
    league = st.selectbox("🌍 اختر ساحة المعركة:", ["PL", "SA", "PD", "BL1", "CL"], 
                          format_func=lambda x: {"PL":"الدوري الإنجليزي الممتاز", "SA":"الدوري الإيطالي", "PD":"الدوري الإسباني", "BL1":"الدوري الألماني", "CL":"دوري أبطال أوروبا"}[x])
    
    table = fetch_data(league)
    
    if table:
        teams = [t['team']['name'] for t in table]
        col_left, col_vs, col_right = st.columns([2, 0.4, 2])
        
        with col_left:
            h_team = st.selectbox("الفريق المضيف:", teams, index=0)
            h_data = next(t for t in table if t['team']['name'] == h_team)
            h_avg = h_data['goalsFor'] / h_data['playedGames']
            st.markdown(f"<div class='metric-card'><p>الترتيب: {h_data['position']}</p><h3>{h_team}</h3><p>القوة الهجومية: {round(h_avg, 2)}</p></div>", unsafe_allow_html=True)

        with col_vs:
            st.markdown("<h1 style='text-align:center; margin-top:60px; opacity:0.2;'>VS</h1>", unsafe_allow_html=True)

        with col_right:
            a_team = st.selectbox("الضيف المتحدي:", teams, index=1)
            a_data = next(t for t in table if t['team']['name'] == a_team)
            a_avg = a_data['goalsFor'] / a_data['playedGames']
            st.markdown(f"<div class='metric-card'><p>الترتيب: {a_data['position']}</p><h3>{a_team}</h3><p>القوة الهجومية: {round(a_avg, 2)}</p></div>", unsafe_allow_html=True)

        st.write("<br>", unsafe_allow_html=True)
        
        if st.button("إطلاق المحاكاة الكمية 🧠⚡"):
            with st.spinner('يتم الآن تحليل 50,000 سيناريو للمواجهة...'):
                time.sleep(2)
                h_p, d_p, a_p, score = analyze_deep(h_avg, a_avg)
                
                # النتائج الرئيسية
                st.markdown("<hr style='border-color:rgba(212,175,55,0.1)'>", unsafe_allow_html=True)
                r1, r2, r3 = st.columns(3)
                r1.metric(f"فوز {h_team}", f"{h_p}%")
                r2.metric("احتمال التعادل", f"{d_p}%")
                r3.metric(f"فوز {a_team}", f"{a_p}%")
                
                # النتيجة المتوقعة (The Magic Score)
                st.markdown(f"""
                    <div style='background: linear-gradient(90deg, transparent, rgba(212,175,55,0.1), transparent); padding: 30px; border-radius: 50px; text-align: center; border: 1px solid #D4AF37; margin-top: 30px;'>
                        <h2 style='margin:0; color:#D4AF37;'>توقع النتيجة الدقيقة: <span style='color:white;'>{score[0]} - {score[1]}</span></h2>
                        <p style='color:#666; margin:0;'>بناءً على خوارزمية توزيع بويسون المتقدمة</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # الرادار التشارت (Visual Comparison)
                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(r=[h_avg*40, h_data['points'], h_data['goalDifference']], theta=['الهجوم','النقاط','فارق الأهداف'], fill='toself', name=h_team, line_color='#D4AF37'))
                fig.add_trace(go.Scatterpolar(r=[a_avg*40, a_data['points'], a_data['goalDifference']], theta=['الهجوم','النقاط','فارق الأهداف'], fill='toself', name=a_team, line_color='#fff'))
                fig.update_layout(polar=dict(bgcolor="rgba(0,0,0,0)", radialaxis=dict(visible=False)), paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#D4AF37"))
                st.plotly_chart(fig, use_container_width=True)
                
                st.balloons()
    else:
        st.error("⚠️ المحرك غير قادر على سحب البيانات. تأكد من استقرار الخوادم العالمية.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#222; margin-top:80px; font-family:Orbitron;'>OMNISTATS | SOVEREIGN ULTIMATE BUILD | v10.0</p>", unsafe_allow_html=True)
