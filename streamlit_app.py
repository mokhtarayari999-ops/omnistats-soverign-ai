import streamlit as st
import numpy as np
import time

# --- 🛰️ إعدادات المحرك السيادي ---
st.set_page_config(page_title="ARABIC PRO | ANALYST", layout="wide", initial_sidebar_state="collapsed")

# --- 🎨 CSS التصميم الرقمي الشامل ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background: radial-gradient(circle, #0f0f0f 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .phantom-header { text-align: center; padding: 25px 10px; border-bottom: 1px solid rgba(212,175,55,0.2); margin-bottom: 20px; }
    .phantom-title { font-size: 2.2rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 15px rgba(212,175,55,0.4); margin: 0; }
    .glass-card { background: rgba(255,255,255,0.02); border: 1px solid rgba(212,175,55,0.2); border-radius: 25px; padding: 30px; text-align: center; backdrop-filter: blur(15px); box-shadow: 0 20px 40px rgba(0,0,0,0.6); margin-top: 15px; }
    .score-text { font-size: 5.5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 25px #D4AF37; margin: 5px 0; line-height: 1.1; }
    .stNumberInput div div input { background: #0a0a0a !important; border: 1px solid #D4AF37 !important; color: #fff !important; font-size: 1.3rem !important; border-radius: 12px !important; text-align: center !important; height: 50px !important; }
    .stTextInput div div input { background: #0a0a0a !important; border: 1px solid #D4AF37 !important; color: #fff !important; font-size: 1.1rem !important; border-radius: 12px !important; text-align: center !important; }
    label { color: #D4AF37 !important; font-weight: bold !important; font-size: 0.9rem !important; margin-bottom: 5px !important; }
    .stat-grid { display: flex; justify-content: space-around; flex-wrap: wrap; gap: 8px; margin-top: 15px; }
    .stat-pill { background: rgba(0,0,0,0.7); border: 1px solid rgba(212,175,55,0.4); border-radius: 15px; padding: 10px; min-width: 90px; flex: 1; }
    .stat-pill p { font-size: 0.75rem; color: #888; margin: 0; }
    .stat-pill h3 { font-size: 1.1rem; color: #fff; margin: 3px 0 0 0; }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #8A6D3B) !important; color: #000 !important; font-weight: 900 !important; border-radius: 15px !important; border: none !important; padding: 15px !important; width: 100% !important; font-size: 1.3rem !important; margin-top: 10px !important; box-shadow: 0 5px 20px rgba(212,175,55,0.3) !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='phantom-header'><h1 class='phantom-title'>ARABIC PRO</h1><p style='color:#555;'>المحلل الرياضي الشامل - إصدار 2026</p></div>", unsafe_allow_html=True)

# --- واجهة الإدخال الرقمي ---
c1, c2 = st.columns(2)

with c1:
    st.markdown("### 🏟️ المضيف")
    h_name = st.text_input("اسم الفريق:", "نادي بارادو")
    h_pwr = st.number_input("القوة الهجومية (1-10):", 1.0, 10.0, 7.1, 0.1)
    h_def = st.number_input("الصلابة الدفاعية (1-10):", 1.0, 10.0, 6.9, 0.1)

with c2:
    st.markdown("### ✈️ الضيف")
    a_name = st.text_input("اسم الفريق :", "شباب بلوزداد")
    a_pwr = st.number_input("القوة الهجومية (1-10) :", 1.0, 10.0, 8.0, 0.1)
    a_def = st.number_input("الصلابة الدفاعية (1-10) :", 1.0, 10.0, 8.6, 0.1)

st.markdown("<br>", unsafe_allow_html=True)

# --- محرك المحاكاة والتحليل الشامل ---
if st.button("🔱 بـدء التحليل والتكهن"):
    with st.spinner('⏳ جاري حساب موازين القوى وتوقع السيناريوهات...'):
        time.sleep(1.8)
        
        # معادلة الأهداف (Poisson)
        h_idx = max(0.2, (h_pwr * (11 - a_def)) / 25)
        a_idx = max(0.2, (a_pwr * (11 - h_def)) / 25)
        
        h_sim = np.random.poisson(h_idx, 100000)
        a_sim = np.random.poisson(a_idx, 100000)
        
        score_h = int(np.round(np.mean(h_sim)))
        score_a = int(np.round(np.mean(a_sim)))
        win_h = (h_sim > a_sim).mean() * 100
        draw = (h_sim == a_sim).mean() * 100
        win_a = (h_sim < a_sim).mean() * 100
        
        # 🚩 التكهن بالركنيات (بناءً على القوة الهجومية الكلية)
        corners_exp = int((h_pwr + a_pwr) * 0.75)
        
        # 🟨 التكهن بالأوراق الصفراء (بناءً على الصلابة الدفاعية - كلما زاد الدفاع زاد الالتحام)
        cards_exp = int((h_def + a_def) * 0.28)

        st.markdown(f"""
            <div class='glass-card'>
                <p style='color: #888; font-size: 0.9rem;'>النتيجة المتوقعة للمباراة</p>
                <div class='score-text'>{score_h} - {score_a}</div>
                <h2 style='color: #fff; font-size: 1.4rem;'>{h_name} <span style='color:#D4AF37;'>❌</span> {a_name}</h2>
                
                <div class='stat-grid'>
                    <div class='stat-pill'><p>فوز {h_name}</p><h3>{win_h:.1f}%</h3></div>
                    <div class='stat-pill'><p>التعادل</p><h3>{draw:.1f}%</h3></div>
                    <div class='stat-pill'><p>فوز {a_name}</p><h3>{win_a:.1f}%</h3></div>
                </div>
                
                <div class='stat-grid' style='margin-top:20px; border-top:1px solid rgba(212,175,55,0.1); padding-top:15px;'>
                    <div class='stat-pill' style='border-color: #D4AF37;'><p>🚩 الركنيات</p><h3>{corners_exp}</h3></div>
                    <div class='stat-pill' style='border-color: #FFD700;'><p>🟨 أوراق صفراء</p><h3>{cards_exp}</h3></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.markdown("<p style='text-align: center; color: #222; margin-top: 40px; font-size: 0.7rem;'>ARABIC PRO | THE TOTAL ANALYST 2026</p>", unsafe_allow_html=True)
