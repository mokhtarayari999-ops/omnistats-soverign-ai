import streamlit as st
import numpy as np
import time

# --- 🛰️ إعدادات المحرك السيادي ---
st.set_page_config(page_title="ARABIC PRO", layout="wide", initial_sidebar_state="collapsed")

# --- 🎨 CSS التصميم الرقمي (تم تحسينه للهواتف) ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .phantom-header { text-align: center; padding: 20px 10px; border-bottom: 1px solid rgba(212,175,55,0.2); }
    .phantom-title { font-size: 2rem; font-weight: 900; color: #D4AF37; margin: 0; }
    
    /* بطاقة النتيجة الزجاجية - نسخة الهواتف */
    .glass-card { background: rgba(255,255,255,0.02); border: 1px solid #D4AF37; border-radius: 20px; padding: 20px; text-align: center; margin-top: 15px; }
    .score-text { font-size: 4.5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 20px #D4AF37; margin: 0; }
    
    /* تحسين الخانات الرقمية */
    .stNumberInput input { background: #0a0a0a !important; border: 1px solid #D4AF37 !important; color: #fff !important; text-align: center !important; }
    .stTextInput input { background: #0a0a0a !important; border: 1px solid #D4AF37 !important; color: #fff !important; text-align: center !important; }
    
    /* شبكة الإحصائيات - منع ظهور الكود الخام */
    .stat-container { display: flex; justify-content: space-around; flex-wrap: wrap; gap: 10px; margin-top: 20px; }
    .stat-pill { background: #111; border: 1px solid #D4AF37; border-radius: 12px; padding: 10px; flex: 1; min-width: 90px; }
    .stat-pill p { font-size: 0.7rem; color: #888; margin: 0; }
    .stat-pill h3 { font-size: 1.1rem; color: #fff; margin: 5px 0 0 0; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='phantom-header'><h1 class='phantom-title'>ARABIC PRO</h1></div>", unsafe_allow_html=True)

# --- واجهة الإدخال ---
c1, c2 = st.columns(2)
with c1:
    h_name = st.text_input("الفريق المضيف:", "نادي بارادو")
    h_pwr = st.number_input("هجوم المضيف:", 1.0, 10.0, 7.1)
    h_def = st.number_input("دفاع المضيف:", 1.0, 10.0, 6.9)

with c2:
    a_name = st.text_input("الفريق الضيف:", "شباب بلوزداد")
    a_pwr = st.number_input("هجوم الضيف:", 1.0, 10.0, 8.0)
    a_def = st.number_input("دفاع الضيف:", 1.0, 10.0, 8.6)

if st.button("🔱 بـدء التحليل الشامل"):
    with st.spinner('⏳ جاري التحليل...'):
        time.sleep(1.5)
        
        # المعادلات الرياضية
        h_idx = max(0.2, (h_pwr * (11 - a_def)) / 25)
        a_idx = max(0.2, (a_pwr * (11 - h_def)) / 25)
        h_sim = np.random.poisson(h_idx, 100000)
        a_sim = np.random.poisson(a_idx, 100000)
        
        win_h = (h_sim > a_sim).mean() * 100
        draw = (h_sim == a_sim).mean() * 100
        win_a = (h_sim < a_sim).mean() * 100
        corners = int((h_pwr + a_pwr) * 0.75)
        cards = int((h_def + a_def) * 0.28)

        # ✅ عرض النتيجة (تم تصحيح هذا الجزء لمنع ظهور الكود الخام)
        result_html = f"""
        <div class='glass-card'>
            <p style='color: #888;'>توقع النتيجة النهائية</p>
            <h1 class='score-text'>{int(np.mean(h_sim))} - {int(np.mean(a_sim))}</h1>
            <h2 style='color: #fff; font-size: 1.3rem;'>{h_name} <span style='color:#D4AF37;'>❌</span> {a_name}</h2>
            
            <div class='stat-container'>
                <div class='stat-pill'><p>فوز المضيف</p><h3>{win_h:.1f}%</h3></div>
                <div class='stat-pill'><p>التعادل</p><h3>{draw:.1f}%</h3></div>
                <div class='stat-pill'><p>فوز الضيف</p><h3>{win_a:.1f}%</h3></div>
            </div>
            
            <div class='stat-container' style='margin-top:15px;'>
                <div class='stat-pill' style='border-color: #D4AF37;'><p>🚩 الركنيات</p><h3>{corners}</h3></div>
                <div class='stat-pill' style='border-color: #FFD700;'><p>🟨 بطاقات</p><h3>{cards}</h3></div>
            </div>
        </div>
        """
        st.markdown(result_html, unsafe_allow_html=True)
        st.balloons()
    
