import streamlit as st
import numpy as np
import time
import plotly.graph_objects as go

# --- 🛰️ إعدادات النواة المركزية ---
st.set_page_config(page_title="ARABIC PRO | THE BEAST", layout="wide", initial_sidebar_state="collapsed")

# --- 🎨 CSS التصميم الوحشي (الذهب المتفجر والأسود العميق) ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    
    /* رأس الصفحة المتوحش */
    .beast-header { text-align: center; padding: 60px 20px; border-bottom: 4px solid #D4AF37; background: linear-gradient(180deg, #111 0%, #000 100%); box-shadow: 0 10px 50px rgba(212,175,55,0.2); margin-bottom: 50px; }
    .beast-title { font-family: 'Orbitron', sans-serif; font-size: 5rem; letter-spacing: 10px; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; margin: 0; }
    
    /* بطاقة النتائج المرعبة */
    .beast-card { background: #080808; border: 2px solid #D4AF37; border-radius: 50px; padding: 60px; text-align: center; position: relative; overflow: hidden; box-shadow: 0 0 100px rgba(212,175,55,0.1); }
    .beast-card::before { content: 'LIVE ANALYSIS'; position: absolute; top: 20px; left: 50%; transform: translateX(-50%); color: #ff0000; font-weight: 900; letter-spacing: 5px; font-size: 0.8rem; animation: blink 1s infinite; }
    
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.2; } 100% { opacity: 1; } }
    
    .beast-score { font-family: 'Orbitron', sans-serif; font-size: 11rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 60px #D4AF37; line-height: 1; margin: 30px 0; }
    
    /* صناديق الإحصائيات الذكية */
    .stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px; margin-top: 40px; }
    .stat-node { background: #111; border: 1px solid rgba(212,175,55,0.3); border-radius: 20px; padding: 25px; transition: 0.5s; }
    .stat-node:hover { border-color: #D4AF37; transform: translateY(-10px); box-shadow: 0 10px 30px rgba(212,175,55,0.2); }
    
    /* الزر القاتل */
    .stButton>button { background: #D4AF37 !important; color: #000 !important; font-family: 'Orbitron', sans-serif !important; font-size: 2rem !important; font-weight: 900 !important; border-radius: 0 !important; border: 2px solid #D4AF37 !important; padding: 30px !important; width: 100% !important; transition: 0.4s !important; text-transform: uppercase; }
    .stButton>button:hover { background: #000 !important; color: #D4AF37 !important; box-shadow: 0 0 50px #D4AF37 !important; }
    
    /* تحسين المدخلات */
    input { background: #000 !important; border: 2px solid #D4AF37 !important; color: #fff !important; font-size: 1.8rem !important; text-align: center !important; height: 70px !important; border-radius: 0 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 🏛️ واجهة الوحش ---
st.markdown("<div class='beast-header'><h1 class='beast-title'>ARABIC PRO</h1><p style='letter-spacing: 5px; color:#888;'>SUPREME BEAST ENGINE v25.0</p></div>", unsafe_allow_html=True)

# مدخلات القوة
col1, col2 = st.columns(2)
with col1:
    h_name = st.text_input("NAME", "MAN CITY", key="h_name").upper()
    h_pwr = st.slider("ATTACK POWER", 0.1, 10.0, 7.5, key="h_pwr")
    h_def = st.slider("DEFENSE WALL", 0.1, 10.0, 8.0, key="h_def")

with col2:
    a_name = st.text_input("NAME ", "REAL MADRID", key="a_name").upper()
    a_pwr = st.slider("ATTACK POWER ", 0.1, 10.0, 6.8, key="a_pwr")
    a_def = st.slider("DEFENSE WALL ", 0.1, 10.0, 7.5, key="a_def")

st.markdown("<br><br>", unsafe_allow_html=True)

# --- 🚀 محرك المحاكاة الكاسر ---
if st.button("EXECUTE SIMULATION"):
    with st.spinner('☣️ ANALYZING MILLIONS OF DATA POINTS...'):
        time.sleep(3) # الانتظار لزيادة الحماس
        
        # معادلة "الوحش" السرية (تعديل xG بناءً على التضاد بين الهجوم والدفاع)
        h_idx = max(0.1, (h_pwr * (11 - a_def)) / 25)
        a_idx = max(0.1, (a_pwr * (11 - h_def)) / 25)
        
        # محاكاة مونت كارلو (مليون سيناريو لـ "الوحش")
        h_sim = np.random.poisson(h_idx, 1000000)
        a_sim = np.random.poisson(a_idx, 1000000)
        
        score_h = int(np.round(np.mean(h_sim)))
        score_a = int(np.round(np.mean(a_sim)))
        win_h = (h_sim > a_sim).mean() * 100
        draw = (h_sim == a_sim).mean() * 100
        win_a = (h_sim < a_sim).mean() * 100
        
        # رادارات إحصائية
        total_goals = (h_sim + a_sim).mean()
        danger_index = (h_idx + a_idx) * 10 # مؤشر الخطورة

        st.markdown(f"""
            <div class='beast-card'>
                <p style='color: #444; letter-spacing: 10px; margin:0;'>EXPECTED SUPREMACY</p>
                <div class='beast-score'>{score_h} - {score_a}</div>
                <h1 style='color: white; font-size: 3.5rem; font-family: Orbitron;'>{h_name} <span style='color:#D4AF37;'>X</span> {a_name}</h1>
                <div class='stat-grid'>
                    <div class='stat-node'><p style='color:#D4AF37;'>VICTORY {h_name}</p><h2>{win_h:.1f}%</h2></div>
                    <div class='stat-node'><p style='color:#888;'>DRAW PROB</p><h2>{draw:.1f}%</h2></div>
                    <div class='stat-node'><p style='color:#D4AF37;'>VICTORY {a_name}</p><h2>{win_a:.1f}%</h2></div>
                </div>
                <div class='stat-grid'>
                    <div class='stat-node'><p style='color:#ff0000;'>DANGER INDEX</p><h2>{danger_index:.1f}/20</h2></div>
                    <div class='stat-node'><p style='color:#D4AF37;'>TOTAL GOALS</p><h2>{total_goals:.2f}</h2></div>
                    <div class='stat-node'><p style='color:#D4AF37;'>CORNERS EXP</p><h2>{int(danger_index * 0.8)}</h2></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # رسم بياني احترافي للوحش
        labels = [h_name, 'DRAW', a_name]
        values = [win_h, draw, win_a]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.7, marker_colors=['#D4AF37', '#222', '#8A6D3B'])])
        fig.update_layout(showlegend=False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=0, b=0, l=0, r=0), height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        st.balloons()

st.markdown("<p style='text-align: center; color: #222; margin-top: 100px; font-family: Orbitron;'>UNSTOPPABLE BEAST SYSTEM 2026</p>", unsafe_allow_html=True)
