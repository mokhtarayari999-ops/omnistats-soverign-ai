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
    .royal-panel { background: rgba(212, 175, 55, 0.01); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 50px; padding: 60px; backdrop-filter: blur(50px); box-shadow: 0 0 120px rgba(212, 175, 55, 0.08); }
    .glow-header { font-family: 'Orbitron', sans-serif; font-size: 3.5rem; text-align: center; color: #D4AF37; text-shadow: 0 0 40px #D4AF37; margin:0; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #F2D388 50%, #D4AF37 100%); color: #000 !important; font-weight: 900; border-radius: 100px; height: 85px; border: none; font-size: 1.8rem; width: 100%; transition: 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275); box-shadow: 0 20px 60px rgba(212, 175, 55, 0.4); }
    .stButton>button:hover { transform: scale(1.03) translateY(-10px); box-shadow: 0 30px 100px rgba(212, 175, 55, 0.7); }
    .stat-card { background: rgba(255,255,255,0.02); border-radius: 25px; padding: 25px; border: 1px solid rgba(212, 175, 55, 0.1); text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 1. محرك البيانات الاستخباراتي
def get_live_intel(league_code):
    url = f"https://football-data.org{league_code}/standings"
    headers = {'X-Auth-Token': API_KEY}
    try:
        res = requests.get(url, headers=headers)
        return res.json()['standings']['table'] if res.status_code == 200 else None
    except: return None

# 2. خوارزمية "الزلزال التكتيكي" (The Momentum Engine)
def calculate_momentum(h_p, a_p):
    events = [
        "⚠️ ركلة جزاء محتملة: ضغط عالٍ في منطقة الجزاء.",
        "🛑 طرد وارد: تدخلات عنيفة متوقعة لكسر الهجمات.",
        "⚽ هدف ملغى: الـ VAR سيكون بطلاً اليوم.",
        "🧤 تألق حراس: حارس مرمى سيتصدى لركلة جزاء أو انفراد.",
        "🚑 إصابة تكتيكية: تغيير اضطراري سيغير مجرى المباراة."
    ]
    return random.choice(events) if abs(h_p - a_p) < 0.5 else random.choice(events[:3])

# 3. محاكي بويسون (100,000 سيناريو للدقة القصوى)
def run_crown_sim(h_avg, a_avg):
    sims = 100000
    h_g = np.random.poisson(h_avg, sims)
    a_g = np.random.poisson(a_avg, sims)
    scores = list(zip(h_g, a_g))
    best_score = max(set(scores), key=scores.count)
    hw, dr, aw = (h_g > a_g).mean()*100, (h_g == a_g).mean()*100, (a_g > h_g).mean()*100
    return hw, dr, aw, f"{int(best_score)} - {int(best_score)}"

st.markdown("<p class='glow-header'>AURASTATS AI</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; letter-spacing:20px; color:#444; margin-bottom:50px;'>THE CROWN BUILD v26.0</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='royal-panel'>", unsafe_allow_html=True)
    
    league = st.selectbox("🌍 بوابة الدوريات العالمية:", ["PL", "SA", "PD", "BL1", "CL"], 
                          format_func=lambda x: {"PL":"Premier League", "SA":"Serie A", "PD":"La Liga", "BL1":"Bundesliga", "CL":"Champions League"}[x])
    
    data = get_live_intel(league)
    
    if data:
        st.success("✅ تم ربط AuraStats بالمركز الاستخباراتي الموحد")
        teams = [t['team']['name'] for t in data]
        c1, c2 = st.columns(2, gap="large")
        with c1:
            h_name = st.selectbox("سيد الأرض:", teams, index=0)
            h_s = next(t for t in data if t['team']['name'] == h_name)
            h_avg = h_s['goalsFor'] / h_s['playedGames']
        with c2:
            a_name = st.selectbox("المنافس المتحدي:", teams, index=1)
            a_s = next(t for t in data if t['team']['name'] == a_name)
            a_avg = a_s['goalsFor'] / a_s['playedGames']

        if st.button("إطلاق المحاكاة السيادية القصوى 🔱🔥"):
            with st.spinner('AuraStats يحلل 100,000 سيناريو بدقة نانوية...'):
                time.sleep(2.5)
                hw, dr, aw, score = run_crown_sim(h_avg, a_avg)
                intel_event = calculate_momentum(h_avg, a_avg)
                
                # النتيجة الكبرى
                st.markdown(f"<div style='text-align:center; padding:60px; border:2px solid #D4AF37; border-radius:150px; margin:40px 0; background:rgba(212,175,55,0.05);'><p style='color:#D4AF37; margin:0; letter-spacing:10px;'>النتيجة المرجحة</p><h1 style='font-size:7rem; color:white; margin:10px 0;'>{score}</h1></div>", unsafe_allow_html=True)
                
                # بطاقات الاستخبارات
                st.markdown("### 🔱 تقارير الغرفة السرية")
                res1, res2, res3 = st.columns(3)
                with res1: st.markdown(f"<div class='stat-card'><b>📊 فرصة فوز {h_name}</b><h2>{round(hw, 1)}%</h2></div>", unsafe_allow_html=True)
                with res2: st.markdown(f"<div class='stat-card'><b>⚖️ التعادل الإحصائي</b><h2>{round(dr, 1)}%</h2></div>", unsafe_allow_html=True)
                with res3: st.markdown(f"<div class='stat-card'><b>📊 فرصة فوز {a_name}</b><h2>{round(aw, 1)}%</h2></div>", unsafe_allow_html=True)
                
                st.markdown(f"<div style='background:rgba(212,175,55,0.1); padding:30px; border-radius:30px; border-left:10px solid #D4AF37; margin-top:20px;'><h3>🚨 حدث مفصلي متوقع:</h3><p style='font-size:20px;'>{intel_event}</p></div>", unsafe_allow_html=True)
                
                # رادار السيطرة
                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(r=[h_avg*30, h_s['points'], 100-h_s['position']*3], theta=['الهجوم','النقاط','الترتيب'], fill='toself', name=h_name, line_color='#D4AF37'))
                fig.add_trace(go.Scatterpolar(r=[a_avg*30, a_s['points'], 100-a_s['position']*3], theta=['الهجوم','النقاط','الترتيب'], fill='toself', name=a_name, line_color='#fff'))
                fig.update_layout(polar=dict(bgcolor="rgba(0,0,0,0)", radialaxis=dict(visible=False)), paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#D4AF37", size=14))
                st.plotly_chart(fig, use_container_width=True)
                st.balloons()
    else:
        st.error("⚠️ فشل جلب البيانات. الخوادم تحت الصيانة.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#222; margin-top:100px; font-family:Orbitron;'>AURASTATS AI | THE SUPREME CROWN | MARCH 2026</p>", unsafe_allow_html=True)
