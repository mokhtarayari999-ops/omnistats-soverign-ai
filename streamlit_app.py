import streamlit as st
import numpy as np
import time

# --- 🔱 ARABIC PRO: THE SOVEREIGN MANUAL v23.0 ---
st.set_page_config(page_title="Arabic Pro | الإمبراطورية", layout="wide")

# --- CSS التصميم الذهبي المتوهج ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    
    .header-box { text-align: center; padding: 40px; border-bottom: 2px solid #D4AF37; margin-bottom: 40px; background: rgba(212,175,55,0.02); }
    
    .result-card { background: rgba(255,255,255,0.02); border: 2px solid #D4AF37; border-radius: 40px; padding: 50px; text-align: center; box-shadow: 0 0 60px rgba(212,175,55,0.1); margin-top: 20px; }
    
    .score-big { font-size: 8.5rem; font-weight: 900; color: #D4AF37; text-shadow: 5px 5px 30px #000; line-height: 1; margin: 25px 0; }
    
    .stat-badge { background: #111; border: 1px solid #D4AF37; border-radius: 20px; padding: 25px; margin: 15px; flex: 1; text-align: center; min-width: 180px; transition: 0.4s; }
    .stat-badge:hover { transform: scale(1.05); background: #1a1a1a; box-shadow: 0 0 20px rgba(212,175,55,0.2); }
    
    .stButton>button { background: linear-gradient(90deg, #D4AF37 0%, #8A6D3B 100%) !important; color: black !important; font-weight: 900 !important; border-radius: 40px !important; padding: 20px !important; border: none !important; width: 100% !important; font-size: 1.8rem !important; transition: 0.3s; }
    .stButton>button:hover { transform: translateY(-5px); box-shadow: 0 10px 30px rgba(212,175,55,0.4); }
    
    input { background-color: #0c0c0c !important; color: white !important; border: 1px solid #D4AF37 !important; border-radius: 15px !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='header-box'><h1>ARABIC PRO 🏆</h1><p style='color:#888; font-size:1.2rem;'>غرفة المحاكاة الشمولية - الإصدار اليدوي السيادي 2026</p></div>", unsafe_allow_html=True)

# --- واجهة إدخال موازين القوى ---
col_h, col_a = st.columns(2)

with col_h:
    st.markdown("### 🏟️ الفريق المضيف")
    h_name = st.text_input("اسم الفريق:", "مانشستر سيتي")
    h_xg = st.slider("قوة الهجوم (0.5 - 5.0):", 0.5, 5.0, 2.4)

with col_a:
    st.markdown("### ✈️ الفريق الضيف")
    a_name = st.text_input("اسم الفريق :", "ريال مدريد")
    a_xg = st.slider("قوة الهجوم (0.5 - 5.0) :", 0.5, 5.0, 1.6)

st.markdown("<br>", unsafe_allow_html=True)

# --- محرك المحاكاة العبقري ---
if st.button("🔱 إطلاق المحاكاة المليونية"):
    with st.spinner('🎯 جاري تحليل 100,000 سيناريو احتمالي...'):
        time.sleep(2) # تأثير درامي احترافي
        
        # محاكاة توزيع Poisson
        h_sim = np.random.poisson(h_xg, 100000)
        a_sim = np.random.poisson(a_xg, 100000)
        
        score_h = int(np.round(np.mean(h_sim)))
        score_a = int(np.round(np.mean(a_sim)))
        win_p = (h_sim > a_sim).mean() * 100
        draw_p = (h_sim == a_sim).mean() * 100
        corners = int((h_xg + a_xg) * 3.9)
        cards = int((h_xg + a_xg) * 1.7)

        # عرض النتيجة الإمبراطورية
        st.markdown(f"""
            <div class='result-card'>
                <p style='font-size: 1.5rem; color: #888; margin-bottom: 0;'>النتيجة المتوقعة الشمولية</p>
                <div class='score-big'>{score_h} - {score_a}</div>
                <h2 style='color: white; font-size: 2.5rem;'>{h_name} <span style='color: #D4AF37;'>VS</span> {a_name}</h2>
                <hr style='border: 1px solid rgba(212,175,55,0.1); margin: 40px 0;'>
                <div style='display: flex; justify-content: space-around; flex-wrap: wrap;'>
                    <div class='stat-badge'><p style='color: #D4AF37; margin:0;'>📈 احتمالية الفوز</p><h2 style='color:white;'>{win_p:.1f}%</h2></div>
                    <div class='stat-badge'><p style='color: #D4AF37; margin:0;'>🤝 التعادل</p><h2 style='color:white;'>{draw_p:.1f}%</h2></div>
                    <div class='stat-badge'><p style='color: #D4AF37; margin:0;'>🚩 ركنيات</p><h2 style='color:white;'>{corners}</h2></div>
                    <div class='stat-badge'><p style='color: #D4AF37; margin:0;'>🟨 بطاقات</p><h2 style='color:white;'>{cards}</h2></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.markdown("<p style='text-align: center; color: #333; margin-top: 60px;'>ARABIC PRO: INDEPENDENT OPERATIONS 2026</p>", unsafe_allow_html=True)
        
