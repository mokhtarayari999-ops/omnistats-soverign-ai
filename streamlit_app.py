import streamlit as st
import numpy as np
import time

# --- 🛰️ الإعدادات الاحترافية ---
st.set_page_config(page_title="ARABIC PRO", layout="wide", initial_sidebar_state="collapsed")

# --- 🎨 CSS التصميم الإمبراطوري (نسخة مستقرة 100%) ---
st.markdown("""
<style>
    @import url('https://googleapis.com');
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .phantom-header { text-align: center; padding: 20px; border-bottom: 2px solid #D4AF37; margin-bottom: 20px; }
    .phantom-title { font-size: 2.2rem; font-weight: 900; letter-spacing: 2px; color: #D4AF37; }
    
    /* بطاقة النتيجة الاحترافية */
    .result-card { background: rgba(255,255,255,0.02); border: 2px solid #D4AF37; border-radius: 30px; padding: 30px; text-align: center; margin-top: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.8); }
    .main-score { font-size: 6rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; line-height: 1; margin: 10px 0; }
    
    /* شبكة البيانات */
    .stats-row { display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; margin-top: 20px; }
    .stat-item { background: #111; border: 1px solid rgba(212,175,55,0.3); border-radius: 15px; padding: 15px; min-width: 100px; flex: 1; }
    .stat-item p { font-size: 0.8rem; color: #888; margin: 0; }
    .stat-item h3 { font-size: 1.3rem; color: #fff; margin: 5px 0 0 0; }

    /* تحسين خانات الإدخال */
    .stNumberInput input, .stTextInput input { background: #0a0a0a !important; border: 1px solid #D4AF37 !important; color: #fff !important; text-align: center !important; border-radius: 12px !important; }
    label { color: #D4AF37 !important; font-weight: bold !important; }
    
    /* الزر الاحترافي */
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #8A6D3B) !important; color: #000 !important; font-weight: 900 !important; border-radius: 15px !important; border: none !important; padding: 15px !important; width: 100% !important; font-size: 1.4rem !important; transition: 0.3s !important; }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 10px 30px rgba(212,175,55,0.4); }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='phantom-header'><h1 class='phantom-title'>ARABIC PRO 🏆</h1></div>", unsafe_allow_html=True)

# --- واجهة مدخلات موازين القوى ---
c1, c2 = st.columns(2)
with c1:
    h_name = st.text_input("الفريق المضيف:", "نادي بارادو")
    h_pwr = st.number_input("قوة الهجوم (1-10):", 1.0, 10.0, 7.1)
    h_def = st.number_input("صلابة الدفاع (1-10):", 1.0, 10.0, 6.9)

with c2:
    a_name = st.text_input("الفريق الضيف:", "شباب بلوزداد")
    a_pwr = st.number_input("قوة الهجوم (1-10) :", 1.0, 10.0, 8.0)
    a_def = st.number_input("صلابة الدفاع (1-10) :", 1.0, 10.0, 8.6)

if st.button("🔱 إطلاق التحليل الاحترافي"):
    with st.spinner('🎯 جاري معالجة البيانات السيادية...'):
        time.sleep(1.5)
        
        # محرك المحاكاة الرياضي
        h_exp = max(0.2, (h_pwr * (11 - a_def)) / 25)
        a_exp = max(0.2, (a_pwr * (11 - h_def)) / 25)
        
        h_sim = np.random.poisson(h_exp, 100000)
        a_sim = np.random.poisson(a_exp, 100000)
        
        # النتائج النهائية
        score_h, score_a = int(np.round(np.mean(h_sim))), int(np.round(np.mean(a_sim)))
        win_h = (h_sim > a_sim).mean() * 100
        draw = (h_sim == a_sim).mean() * 100
        win_a = (h_sim < a_sim).mean() * 100
        
        corners = int((h_pwr + a_pwr) * 0.75)
        cards = int((h_def + a_def) * 0.28)

        # ✅ بناء القالب الاحترافي الموحد (لمنع ظهور الكود الخام)
        final_ui = f"""
        <div class='result-card'>
            <p style='color: #888; font-size: 1rem; margin:0;'>توقع النتيجة الشمولية</p>
            <div class='main-score'>{score_h} - {score_a}</div>
            <h2 style='color: white; margin-bottom: 20px;'>{h_name} <span style='color:#D4AF37;'>🆚</span> {a_name}</h2>
            
            <div class='stats-row'>
                <div class='stat-item'><p>فوز {h_name}</p><h3>{win_h:.1f}%</h3></div>
                <div class='stat-item'><p>التعادل</p><h3>{draw:.1f}%</h3></div>
                <div class='stat-item'><p>فوز {a_name}</p><h3>{win_a:.1f}%</h3></div>
            </div>
            
            <div class='stats-row' style='margin-top:15px; border-top: 1px solid rgba(212,175,55,0.1); padding-top:20px;'>
                <div class='stat-item' style='border-color: #D4AF37;'><p>🚩 الركنيات</p><h3>{corners}</h3></div>
                <div class='stat-item' style='border-color: #FFD700;'><p>🟨 بطاقات صفراء</p><h3>{cards}</h3></div>
            </div>
        </div>
        """
        st.markdown(final_ui, unsafe_allow_html=True)
        st.balloons()
    
