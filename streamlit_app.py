import streamlit as st
import requests
import numpy as np
import plotly.graph_objects as go
import time

# --- 🔑 NUCLEAR CONFIG ---
API_KEY = "757497fe293f4e39a291cc5c575c6dc3"

st.set_page_config(page_title="OmniStats Sovereign Pro", layout="wide", page_icon="🔱")

# التنسيق البصري الفائق
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    .stApp { background: radial-gradient(circle at center, #111 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .glass-panel { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 35px; padding: 30px; backdrop-filter: blur(20px); }
    .glow-header { font-family: 'Orbitron', sans-serif; font-size: 2.5rem; text-align: center; color: #D4AF37; text-shadow: 0 0 20px #D4AF37; }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #F2D388, #D4AF37); color: #000 !important; font-weight: 900; border-radius: 100px; height: 60px; border: none; font-size: 1.4rem; transition: 0.5s; width: 100%; box-shadow: 0 10px 40px rgba(212, 175, 55, 0.3); }
    </style>
    """, unsafe_allow_html=True)

# محرك جلب البيانات (مع فحص أمني مكثف)
def fetch_real_data(league_code):
    url = f"https://api.football-data.org{league_code}/standings"
    headers = {'X-Auth-Token': API_KEY}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            return res.json()['standings'][0]['table'], "OK"
        return None, f"Status {res.status_code}"
    except:
        return None, "Offline"

# خوارزمية المحاكاة (50,000 سيناريو)
def simulate_match(h_avg, a_avg):
    sims = 50000
    h_g = np.random.poisson(h_avg, sims)
    a_g = np.random.poisson(a_avg, sims)
    scores = list(zip(h_g, a_g))
    best_score = max(set(scores), key=scores.count)
    return (h_g > a_g).mean()*100, (h_g == a_g).mean()*100, (a_g > h_g).mean()*100, best_score

st.markdown("<p class='glow-header'>OMNISTATS CORE</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    
    mode = st.radio("🛠️ وضع التشغيل:", ["البيانات المباشرة (Global)", "التحليل اليدوي (Pro)"], horizontal=True)
    
    if mode == "البيانات المباشرة (Global)":
        league = st.selectbox("🌍 اختر الدوري:", ["PL", "BL1", "SA", "PD", "CL"], 
                              format_func=lambda x: {"PL":"إنجلترا", "BL1":"ألمانيا", "SA":"إيطاليا", "PD":"إسبانيا", "CL":"أبطال أوروبا"}[x])
        table, status = fetch_real_data(league)
        
        if table:
            st.success("✅ تم تحديث البيانات الحقيقية!")
            teams = [t['team']['name'] for t in table]
            c1, c2 = st.columns(2)
            with c1:
                h_team = st.selectbox("صاحب الأرض:", teams, index=0)
                h_d = next(t for t in table if t['team']['name'] == h_team)
                h_avg = h_d['goalsFor'] / h_d['playedGames']
            with c2:
                a_team = st.selectbox("الضيف المتحدي:", teams, index=1)
                a_d = next(t for t in table if t['team']['name'] == a_team)
                a_avg = a_d['goalsFor'] / a_d['playedGames']
        else:
            st.warning(f"⚠️ الخادم العالمي لا يستجيب حالياً ({status}). استخدم 'التحليل اليدوي' للمتابعة.")
            h_team, a_team, h_avg, a_avg = None, None, 0, 0
    else:
        st.info("💡 وضع التحليل اليدوي المتقدم")
        c1, c2 = st.columns(2)
        with c1:
            h_team = st.text_input("اسم الفريق المضيف:", "الترجي")
            h_avg = st.slider("القوة الهجومية (معدل أهداف):", 0.5, 4.0, 2.0, key="h")
        with c2:
            a_team = st.text_input("اسم الفريق الضيف:", "الإفريقي")
            a_avg = st.slider("القوة الهجومية (معدل أهداف):", 0.5, 4.0, 1.5, key="a")

    if h_team and a_team:
        if st.button("إطلاق المحاكاة السيادية 🧠⚡"):
            with st.spinner('تحليل 50,000 سيناريو...'):
                time.sleep(1.5)
                h_p, d_p, a_p, score = simulate_match(h_avg, a_avg)
                st.markdown("<br><hr style='opacity:0.2'><br>", unsafe_allow_html=True)
                r1, r2, r3 = st.columns(3)
                r1.metric(f"فوز {h_team}", f"{round(h_p, 1)}%")
                r2.metric("التعادل", f"{round(d_p, 1)}%")
                r3.metric(f"فوز {a_team}", f"{round(a_p, 1)}%")
                st.markdown(f"<div style='text-align:center; padding:20px; border:1px solid #D4AF37; border-radius:50px; margin-top:20px;'><h2>النتيجة الأكثر توقعاً: {score[0]} - {score[1]}</h2></div>", unsafe_allow_html=True)
                st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)
