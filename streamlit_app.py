import streamlit as st
import requests
import numpy as np
import plotly.graph_objects as go
import random
import time

# --- 👑 THE ROYAL CONFIG ---
API_KEY = "757497fe293f4e39a291cc5c575c6dc3"

st.set_page_config(page_title="AuraStats AI | The Crown", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background: radial-gradient(circle at top, #0d0d0d 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .royal-panel { background: rgba(212, 175, 55, 0.01); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 50px; padding: 40px; backdrop-filter: blur(50px); }
    .glow-header { font-family: 'Orbitron', sans-serif; font-size: 3rem; text-align: center; color: #D4AF37; text-shadow: 0 0 40px #D4AF37; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #F2D388 50%, #D4AF37 100%); color: #000 !important; font-weight: 900; border-radius: 100px; height: 75px; border: none; font-size: 1.5rem; width: 100%; transition: 0.5s; }
    .stat-card { background: rgba(255,255,255,0.02); border-radius: 25px; padding: 20px; border: 1px solid rgba(212, 175, 55, 0.1); text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# محرك جلب البيانات الذكي
def get_intel(league):
    url = f"https://football-data.org{league}/standings"
    headers = {'X-Auth-Token': API_KEY}
    try:
        res = requests.get(url, headers=headers, timeout=8)
        if res.status_code == 200: return res.json()['standings'][0]['table'], "OK"
        return None, f"Status {res.status_code}"
    except: return None, "Offline"

# محاكي بويسون السيادي
def run_crown_sim(h_avg, a_avg):
    sims = 100000
    h_g = np.random.poisson(h_avg, sims)
    a_g = np.random.poisson(a_avg, sims)
    scores = list(zip(h_g, a_g))
    best_score = max(set(scores), key=scores.count)
    return (h_g > a_g).mean()*100, (h_g == a_g).mean()*100, (a_g > h_g).mean()*100, f"{int(best_score)} - {int(best_score)}"

st.markdown("<p class='glow-header'>AURASTATS AI</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='royal-panel'>", unsafe_allow_html=True)
    
    op_mode = st.radio("🛠️ وضع المحرك:", ["الذكاء العالمي (Global)", "التحليل الاستراتيجي (Manual)"], horizontal=True)
    
    if op_mode == "الذكاء العالمي (Global)":
        league = st.selectbox("🌍 بوابة الدوريات:", ["PL", "SA", "PD", "BL1", "CL"], 
                              format_func=lambda x: {"PL":"Premier League", "SA":"Serie A", "PD":"La Liga", "BL1":"Bundesliga", "CL":"Champions League"}[x])
        data, status = get_intel(league)
        if data:
            st.success("✅ متصل بالبيانات الحقيقية")
            teams = [t['team']['name'] for t in data]
            c1, c2 = st.columns(2)
            with c1:
                h_name = st.selectbox("المضيف:", teams)
                h_t = next(t for t in data if t['team']['name'] == h_name)
                h_avg = h_t['goalsFor'] / h_t['playedGames']
            with c2:
                a_name = st.selectbox("الضيف:", teams, index=1)
                a_t = next(t for t in data if t['team']['name'] == a_name)
                a_avg = a_t['goalsFor'] / a_t['playedGames']
        else:
            st.warning(f"⚠️ الخادم العالمي لا يستجيب ({status}). استخدم 'التحليل الاستراتيجي' للمتابعة فوراً.")
            h_name, a_name, h_avg, a_avg = None, None, 0, 0
    else:
        st.info("🎯 وضع التحليل اليدوي المتقدم (Sovereign Mode)")
        c1, c2 = st.columns(2)
        with c1:
            h_name = st.text_input("فريق الأرض:", "أرسنال")
            h_avg = st.slider("قوة الهجوم (xG):", 0.5, 4.5, 2.1, key="h")
        with c2:
            a_name = st.text_input("فريق الضيف:", "مانشستر سيتي")
            a_avg = st.slider("قوة الهجوم (xG):", 0.5, 4.5, 1.9, key="a")

    if h_name and a_name:
        if st.button("إطلاق المحاكاة السيادية 🔱🔥"):
            with st.spinner('AuraStats يحلل 100,000 سيناريو...'):
                time.sleep(1.5)
                hw, dr, aw, score = run_crown_sim(h_avg, a_avg)
                st.markdown(f"<div style='text-align:center; padding:40px; border:2px solid #D4AF37; border-radius:100px; margin:30px 0; background:rgba(212,175,55,0.05);'><h1 style='font-size:5rem; color:white; margin:0;'>{score}</h1></div>", unsafe_allow_html=True)
                r1, r2, r3 = st.columns(3)
                r1.metric(f"فوز {h_name}", f"{round(hw, 1)}%")
                r2.metric("التعادل", f"{round(dr, 1)}%")
                r3.metric(f"فوز {a_name}", f"{round(aw, 1)}%")
                st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#222; margin-top:50px;'>AURASTATS AI | THE CROWN BUILD v26.1</p>", unsafe_allow_html=True)
    
