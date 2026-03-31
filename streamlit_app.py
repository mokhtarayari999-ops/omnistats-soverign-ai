import streamlit as st
import requests
import numpy as np
import plotly.graph_objects as go
import time

# --- 👑 THE IMMORTAL CONFIG ---
API_KEY = "757497fe293f4e39a291cc5c575c6dc3"

st.set_page_config(page_title="AuraStats AI | Immortal Sovereign", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background: radial-gradient(circle at center, #0a0a0a 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .supreme-panel { background: rgba(212, 175, 55, 0.01); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 40px; padding: 30px; backdrop-filter: blur(40px); }
    .glow-header { font-family: 'Orbitron', sans-serif; font-size: 2.5rem; text-align: center; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #F2D388 50%, #D4AF37 100%); color: #000 !important; font-weight: 900; border-radius: 100px; height: 70px; border: none; font-size: 1.5rem; width: 100%; transition: 0.5s; }
    /* إخفاء الأخطاء المزعجة وجعل الواجهة نظيفة */
    .stAlert { background-color: rgba(212, 175, 55, 0.1) !important; color: #D4AF37 !important; border: 1px solid #D4AF37 !important; }
    </style>
    """, unsafe_allow_html=True)

# دالة جلب البيانات الذكية (المحصنة)
def get_intel_safe(league_code):
    url = f"https://football-data.org{league_code}/standings"
    headers = {'X-Auth-Token': API_KEY}
    try:
        res = requests.get(url, headers=headers, timeout=5)
        if res.status_code == 200: return res.json()['standings']['table'], "LIVE"
        return None, "DATABASE"
    except: return None, "DATABASE"

# محاكي بويسون (150,000 سيناريو)
def run_quantum_sim(h_avg, a_avg):
    sims = 150000
    h_g = np.random.poisson(h_avg, sims)
    a_g = np.random.poisson(a_avg, sims)
    scores = list(zip(h_g, a_g))
    best_score = max(set(scores), key=scores.count)
    return (h_g > a_g).mean()*100, (h_g == a_g).mean()*100, (a_g > h_g).mean()*100, f"{int(best_score)} - {int(best_score)}"

st.markdown("<p class='glow-header'>AURASTATS AI</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444; letter-spacing:10px;'>IMMORTAL SOVEREIGN v30.0</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='supreme-panel'>", unsafe_allow_html=True)
    
    # اختيار الوضع
    choice = st.radio("🛠️ اختيار المحرك:", ["الذكاء العالمي (آلي)", "النطاق المفتوح (يدوي)"], horizontal=True)
    
    data = None
    if choice == "الذكاء العالمي (آلي)":
        league = st.selectbox("🌍 اختر المسرح:", ["PL", "PD", "SA", "BL1", "CL"], format_func=lambda x: {"PL":"EPL", "PD":"La Liga", "SA":"Serie A", "BL1":"Bundesliga", "CL":"Champions League"}[x])
        data, status = get_intel_safe(league)
        
        if data:
            st.success("✅ متصل بالبيانات الحقيقية")
            teams = [t['team']['name'] for t in data]
            c1, c2 = st.columns(2)
            with c1:
                h_name = st.selectbox("المضيف:", teams, index=0)
                h_t = next(t for t in data if t['team']['name'] == h_name)
                h_final_xg = st.slider(f"xG لـ {h_name}:", 0.1, 5.0, float(round(h_t['goalsFor']/h_t['playedGames'], 2)))
            with c2:
                a_name = st.selectbox("المنافس:", teams, index=1)
                a_t = next(t for t in data if t['team']['name'] == a_name)
                a_final_xg = st.slider(f"xG لـ {a_name}:", 0.1, 5.0, float(round(a_t['goalsFor']/a_t['playedGames'], 2)))
        else:
            st.warning("⚠️ الخادم العالمي مشغول. سيتم تحويلك للوضع اليدوي الفاخر فوراً...")
            choice = "النطاق المفتوح (يدوي)"
            time.sleep(1)
            st.rerun()

    if choice == "النطاق المفتوح (يدوي)":
        st.info("🎯 وضع النطاق العالمي المفتوح (شامل لجميع البطولات)")
        col_h, col_a = st.columns(2)
        with col_h:
            h_name = st.text_input("اسم الفريق الأول:", "الترجي")
            h_final_xg = st.number_input(f"معدل أهداف {h_name}:", 0.1, 5.0, 1.8)
        with col_a:
            a_name = st.text_input("اسم الفريق الثاني:", "الأهلي")
            a_final_xg = st.number_input(f"معدل أهداف {a_name}:", 0.1, 5.0, 1.5)

    if h_name and a_name:
        if st.button("إطلاق المحاكاة السيادية العليا 🔱🔥"):
            with st.spinner('AuraStats يحلل 150,000 سيناريو...'):
                time.sleep(1.5)
                hw, dr, aw, score = run_quantum_sim(h_final_xg, a_final_xg)
                st.markdown(f"<div style='text-align:center; padding:40px; border:2px solid #D4AF37; border-radius:100px; margin:30px 0; background:rgba(212,175,55,0.05);'><h1 style='font-size:6rem; color:white; margin:0;'>{score}</h1></div>", unsafe_allow_html=True)
                r1, r2, r3 = st.columns(3)
                r1.metric(f"فوز {h_name}", f"{round(hw, 1)}%")
                r2.metric("التعادل", f"{round(dr, 1)}%")
                r3.metric(f"فوز {a_name}", f"{round(aw, 1)}%")
                st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)
    
