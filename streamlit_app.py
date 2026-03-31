import streamlit as st
import requests
import numpy as np
import plotly.graph_objects as go
import random
import time

# --- 👑 THE GLOBAL COMMAND CONFIG ---
API_KEY = "757497fe293f4e39a291cc5c575c6dc3"

st.set_page_config(page_title="AuraStats AI | Global Sovereign", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background: radial-gradient(circle at center, #0a0a0a 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .supreme-panel { background: rgba(212, 175, 55, 0.015); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 45px; padding: 40px; backdrop-filter: blur(40px); }
    .glow-header { font-family: 'Orbitron', sans-serif; font-size: 3rem; text-align: center; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #F2D388 50%, #D4AF37 100%); color: #000 !important; font-weight: 900; border-radius: 100px; height: 80px; border: none; font-size: 1.8rem; width: 100%; transition: 0.5s; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 20px 60px rgba(212, 175, 55, 0.5); }
    .input-card { background: rgba(255,255,255,0.03); border-radius: 20px; padding: 25px; border-left: 5px solid #D4AF37; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 1. محرك البيانات الهجين
def get_league_data(league_code):
    url = f"https://football-data.org{league_code}/standings"
    headers = {'X-Auth-Token': API_KEY}
    try:
        res = requests.get(url, headers=headers, timeout=8)
        if res.status_code == 200: return res.json()['standings'][0]['table'], "LIVE"
        return None, "OFFLINE"
    except: return None, "OFFLINE"

# 2. محاكي بويسون (150,000 سيناريو)
def run_supreme_sim(h_avg, a_avg):
    sims = 150000
    h_g = np.random.poisson(h_avg, sims)
    a_g = np.random.poisson(a_avg, sims)
    scores = list(zip(h_g, a_g))
    best_score = max(set(scores), key=scores.count)
    return (h_g > a_g).mean()*100, (h_g == a_g).mean()*100, (a_g > h_g).mean()*100, f"{int(best_score)} - {int(best_score)}"

st.markdown("<p class='glow-header'>AURASTATS AI</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444; letter-spacing:15px; margin-bottom:40px;'>GLOBAL SOVEREIGN COMMAND v29.0</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='supreme-panel'>", unsafe_allow_html=True)
    
    # اختيار وضع العمل لكسر حاجز الدوريات المعروفة
    op_mode = st.radio("🛠️ اختيار نطاق الاستخبارات:", ["البطولات الكبرى (Auto-Fetch)", "النطاق العالمي المفتوح (Custom)"], horizontal=True)
    
    if op_mode == "البطولات الكبرى (Auto-Fetch)":
        league = st.selectbox("🌍 اختر المسرح:", ["PL", "PD", "SA", "BL1", "CL"], format_func=lambda x: {"PL":"EPL", "PD":"La Liga", "SA":"Serie A", "BL1":"Bundesliga", "CL":"Champions League"}[x])
        data, status = get_league_data(league)
        if data:
            st.caption(f"🔱 الحالة: **{status} Mode**")
            teams_map = {t['team']['name']: t for t in data}
            col_h, col_a = st.columns(2, gap="large")
            with col_h:
                h_name = st.selectbox("المضيف:", list(teams_map.keys()), index=0)
                h_base_xg = teams_map[h_name]['goalsFor'] / teams_map[h_name]['playedGames']
                h_final_xg = st.slider(f"تعديل xG لـ {h_name}:", 0.1, 5.0, float(round(h_base_xg, 2)))
            with col_a:
                a_name = st.selectbox("المنافس:", list(teams_map.keys()), index=1)
                a_base_xg = teams_map[a_name]['goalsFor'] / teams_map[a_name]['playedGames']
                a_final_xg = st.slider(f"تعديل xG لـ {a_name}:", 0.1, 5.0, float(round(a_base_xg, 2)))
        else:
            st.error("⚠️ فشل جلب البيانات. استخدم الوضع المفتوح للمتابعة.")
            h_name, a_name, h_final_xg, a_final_xg = None, None, 0, 0
    else:
        st.info("🎯 وضع النطاق العالمي: أدخل بيانات أي مباراة في العالم")
        col_h, col_a = st.columns(2, gap="large")
        with col_h:
            h_name = st.text_input("اسم الفريق المضيف (مثلاً: الترجي):", "Esperance")
            h_final_xg = st.number_input(f"معدل أهداف {h_name} (xG):", 0.1, 5.0, 1.8)
        with col_a:
            a_name = st.text_input("اسم الفريق المنافس (مثلاً: الأهلي):", "Al Ahly")
            a_final_xg = st.number_input(f"معدل أهداف {a_name} (xG):", 0.1, 5.0, 1.5)

    if h_name and a_name:
        if st.button("إطلاق المحاكاة السيادية العليا 🔱🔥"):
            with st.spinner('AuraStats يحلل 150,000 سيناريو احتمالي...'):
                time.sleep(1.5)
                hw, dr, aw, score = run_supreme_sim(h_final_xg, a_final_xg)
                st.markdown(f"<div style='text-align:center; padding:40px; border:2px solid #D4AF37; border-radius:100px; margin:30px 0; background:rgba(212,175,55,0.05);'><h1 style='font-size:6rem; color:white; margin:0;'>{score}</h1></div>", unsafe_allow_html=True)
                r1, r2, r3 = st.columns(3)
                r1.metric(f"فوز {h_name}", f"{round(hw, 1)}%")
                r2.metric("التعادل", f"{round(dr, 1)}%")
                r3.metric(f"فوز {a_name}", f"{round(aw, 1)}%")
                st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)
            
