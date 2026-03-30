import streamlit as st
import requests
import numpy as np
import plotly.graph_objects as go
import time

# --- 🔑 ضع مفتاحك الحقيقي هنا بين علامتي التنصيص ---
API_KEY = "757497fe293f4e39a291cc5c575c6dc3" 

# 1. التكوين البصري الفاخر
st.set_page_config(page_title="OmniStats Sovereign AI", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    .stApp { background: radial-gradient(circle at center, #111 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .sovereign-panel { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 30px; padding: 35px; backdrop-filter: blur(20px); box-shadow: 0 0 50px rgba(212, 175, 55, 0.1); }
    .glow-title { font-family: 'Orbitron', sans-serif; font-size: 3.5rem; text-align: center; color: #D4AF37; text-shadow: 0 0 20px #D4AF37; margin-bottom: 0px; }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #F2D388, #D4AF37); color: #000 !important; font-weight: 900; border-radius: 100px; height: 65px; border: none; font-size: 1.3rem; transition: 0.5s; width: 100%; }
    .stButton>button:hover { transform: scale(1.03); box-shadow: 0 15px 30px rgba(212, 175, 55, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# 2. وظيفة جلب البيانات الحقيقية
def get_league_standings(league_code):
    url = f"https://api.football-data.org{league_code}/standings"
    headers = {'X-Auth-Token': API_KEY}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['standings'][0]['table']
        return None
    except:
        return None

# 3. محاكاة مونت كارلو الذكية
def simulate_match(h_avg, a_avg):
    sims = 10000
    h_goals = np.random.poisson(h_avg, sims)
    a_goals = np.random.poisson(a_avg, sims)
    h_win = (h_goals > a_goals).mean() * 100
    draw = (h_goals == a_goals).mean() * 100
    a_win = (a_goals > h_goals).mean() * 100
    return round(h_win, 1), round(draw, 1), round(a_win, 1)

# 4. بناء المسرح
st.markdown("<p class='glow-title'>OMNISTATS</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; letter-spacing:10px; color:#888; margin-bottom:40px;'>SOVEREIGN INTELLIGENCE v8.0</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='sovereign-panel'>", unsafe_allow_html=True)
    
    # اختيار الدوري
    league_choice = st.selectbox("🌍 اختر الدوري الحقيقي:", ["PL", "SA", "PD", "BL1", "CL"], 
                                 format_func=lambda x: {"PL":"الدوري الإنجليزي", "SA":"الدوري الإيطالي", "PD":"الدوري الإسباني", "BL1":"الدوري الألماني", "CL":"دوري أبطال أوروبا"}[x])
    
    table = get_league_standings(league_choice)
    
    if table:
        teams = [t['team']['name'] for t in table]
        col_h, vs, col_a = st.columns([2, 0.5, 2])
        
        with col_h:
            h_team = st.selectbox("الفريق المضيف:", teams, index=0)
            h_data = next(t for t in table if t['team']['name'] == h_team)
            h_score_avg = h_data['goalsFor'] / h_data['playedGames']
            st.info(f"قوة الهجوم الحالية: {round(h_score_avg, 2)}")

        with vs:
            st.markdown("<h1 style='text-align:center; margin-top:40px; opacity:0.2;'>VS</h1>", unsafe_allow_html=True)

        with col_a:
            a_team = st.selectbox("الضيف المتحدي:", teams, index=1)
            a_data = next(t for t in table if t['team']['name'] == a_team)
            a_score_avg = a_data['goalsFor'] / a_data['playedGames']
            st.info(f"قوة الهجوم الحالية: {round(a_score_avg, 2)}")

        if st.button("إطلاق المحاكاة السيادية (10,000 سيناريو) ⚡"):
            with st.spinner('جارِ تحليل البيانات الميدانية...'):
                time.sleep(1.5)
                h_p, d_p, a_p = simulate_match(h_score_avg, a_score_avg)
                
                st.markdown("<br><hr style='opacity:0.1'><br>", unsafe_allow_html=True)
                r1, r2, r3 = st.columns(3)
                r1.metric(f"فوز {h_team}", f"{h_p}%")
                r2.metric("التعادل", f"{d_p}%")
                r3.metric(f"فوز {a_team}", f"{a_p}%")
                st.balloons()
    else:
        st.warning("🔄 جارِ الاتصال بالبيانات.. تأكد من صحة المفتاح API.")

    st.markdown("</div>", unsafe_allow_html=True)
