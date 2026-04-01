import streamlit as st
import numpy as np
import time

# --- 🛰️ الإعدادات السيادية ---
st.set_page_config(page_title="ARABIC PRO", layout="wide", initial_sidebar_state="collapsed")

# --- 🎨 CSS التصميم الفولاذي (محمي تماماً) ---
st.markdown("""
<style>
    @import url('https://googleapis.com');
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .phantom-header { text-align: center; padding: 20px; border-bottom: 2px solid #D4AF37; margin-bottom: 20px; }
    
    /* بطاقة النتيجة المحمية */
    .result-card { background: rgba(255,255,255,0.02); border: 2px solid #D4AF37; border-radius: 20px; padding: 20px; text-align: center; margin-top: 20px; }
    .main-score { font-size: 5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 20px #D4AF37; margin: 0; }
    
    /* الحاويات الإحصائية */
    .stats-container { display: flex; justify-content: center; flex-wrap: wrap; gap: 8px; margin-top: 15px; }
    .stat-node { background: #111; border: 1px solid rgba(212,175,55,0.3); border-radius: 12px; padding: 12px; min-width: 90px; flex: 1; }
    .stat-node p { font-size: 0.7rem; color: #888; margin: 0; }
    .stat-node h3 { font-size: 1.1rem; color: #fff; margin: 3px 0 0 0; }

    .stNumberInput input, .stTextInput input { background: #0a0a0a !important; border: 1px solid #D4AF37 !important; color: #fff !important; text-align: center !important; }
    label { color: #D4AF37 !important; font-weight: bold !important; }
    
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #8A6D3B) !important; color: #000 !important; font-weight: 900 !important; border-radius: 15px !important; width: 100% !important; height: 3.5rem !important; font-size: 1.3rem !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='phantom-header'><h1 style='color:#D4AF37; margin:0;'>ARABIC PRO 🏆</h1></div>", unsafe_allow_html=True)

# --- واجهة المدخلات ---
c1, c2 = st.columns(2)
with c1:
    h_name = st.text_input("الفريق المضيف:", "نادي بارادو")
    h_pwr = st.number_input("قوة الهجوم (1-10):", 1.0, 10.0, 7.1)
    h_def = st.number_input("صلابة الدفاع (1-10):", 1.0, 10.0, 6.9)

with c2:
    a_name = st.text_input("الفريق الضيف:", "شباب بلوزداد")
    a_pwr = st.number_input("قوة الهجوم (1-10) :", 1.0, 10.0, 8.0)
    a_def = st.number_input("صلابة الدفاع (1-10) :", 1.0, 10.0, 8.6)

if st.button("🔱 إطلاق التحليل الشمولي"):
    with st.spinner('🎯 جاري معالجة البيانات...'):
        time.sleep(1)
        
        # محرك المحاكاة
        h_exp = max(0.2, (h_pwr * (11 - a_def)) / 25)
        a_exp = max(0.2, (a_pwr * (11 - h_def)) / 25)
        h_sim = np.random.poisson(h_exp, 100000)
        a_sim = np.random.poisson(a_exp, 100000)
        
        # الحسابات الإحصائية
        sc_h, sc_a = int(np.round(np.mean(h_sim))), int(np.round(np.mean(a_sim)))
        w_h = (h_sim > a_sim).mean() * 100
        dr = (h_sim == a_sim).mean() * 100
        w_a = (h_sim < a_sim).mean() * 100
        corn = int((h_pwr + a_pwr) * 0.75)
        cards = int((h_def + a_def) * 0.28)

        # ✅ البناء الفولاذي (نستخدم st.markdown لكل جزء على حدة لضمان عدم الانكسار)
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#888;'>توقع النتيجة</p><h1 class='main-score'>{sc_h} - {sc_a}</h1>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color:#fff;'>{h_name} 🆚 {a_name}</h2>", unsafe_allow_html=True)
        
        # توزيع الإحصائيات في حاويات مستقلة تماماً
        st.markdown(f"""
        <div class='stats-container'>
            <div class='stat-node'><p>فوز المضيف</p><h3>{w_h:.1f}%</h3></div>
            <div class='stat-node'><p>تعادل</p><h3>{dr:.1f}%</h3></div>
            <div class='stat-node'><p>فوز الضيف</p><h3>{w_a:.1f}%</h3></div>
        </div>
        <div class='stats-container'>
            <div class='stat-node' style='border-color:#D4AF37;'><p>🚩 ركنيات</p><h3>{corn}</h3></div>
            <div class='stat-node' style='border-color:#FFD700;'><p>🟨 بطاقات</p><h3>{cards}</h3></div>
        </div>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
        
