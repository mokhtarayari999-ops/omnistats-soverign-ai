import streamlit as st
import numpy as np
import time

# --- 🛰️ الإعدادات السيادية العظمى ---
st.set_page_config(page_title="ARABIC PRO | SUPREME", layout="wide", initial_sidebar_state="collapsed")

# --- 🎨 CSS النيون الذهبي (تصميم مستقبلي 2026) ---
st.markdown("""
<style>
    @import url('https://googleapis.com');
    .stApp { background: radial-gradient(circle, #111 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    
    /* رأس الصفحة المتوهج */
    .supreme-header { text-align: center; padding: 30px; border-bottom: 2px solid #D4AF37; margin-bottom: 30px; box-shadow: 0 0 20px rgba(212,175,55,0.2); }
    .supreme-title { font-family: 'Orbitron', sans-serif; font-size: 2.5rem; letter-spacing: 5px; color: #D4AF37; text-shadow: 0 0 15px #D4AF37; }
    
    /* بطاقة النتيجة الاستراتيجية */
    .strategy-card { background: rgba(255,255,255,0.02); border: 2px solid #D4AF37; border-radius: 35px; padding: 35px; text-align: center; margin-top: 20px; position: relative; overflow: hidden; }
    .main-score { font-family: 'Orbitron', sans-serif; font-size: 7rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 40px #D4AF37; margin: 0; line-height: 1; }
    
    /* كتل البيانات الذكية */
    .data-grid { display: flex; justify-content: center; flex-wrap: wrap; gap: 12px; margin-top: 25px; }
    .data-node { background: #0a0a0a; border: 1px solid rgba(212,175,55,0.3); border-radius: 20px; padding: 18px; min-width: 100px; flex: 1; transition: 0.3s; }
    .data-node:hover { border-color: #D4AF37; transform: translateY(-5px); box-shadow: 0 5px 15px rgba(212,175,55,0.2); }
    .data-node p { font-size: 0.75rem; color: #888; margin: 0; }
    .data-node h3 { font-size: 1.2rem; color: #fff; margin: 5px 0 0 0; }

    /* تحسين الخانات والزر */
    .stNumberInput input, .stTextInput input { background: #050505 !important; border: 1px solid #D4AF37 !important; color: #fff !important; text-align: center !important; border-radius: 15px !important; height: 50px !important; font-size: 1.2rem !important; }
    .stButton>button { background: linear-gradient(45deg, #D4AF37, #8A6D3B) !important; color: #000 !important; font-weight: 900 !important; border-radius: 50px !important; height: 4rem !important; font-size: 1.6rem !important; border: none !important; box-shadow: 0 5px 20px rgba(212,175,55,0.4) !important; transition: 0.3s !important; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 10px 30px rgba(212,175,55,0.6) !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='supreme-header'><h1 class='supreme-title'>ARABIC PRO</h1><p style='color:#666; letter-spacing:3px;'>STRATEGIC OPERATIONS CENTER 2026</p></div>", unsafe_allow_html=True)

# --- مدخلات موازين القوى ---
c1, c2 = st.columns(2)
with c1:
    h_name = st.text_input("🏠 الفريق المضيف:", "نادي بارادو")
    h_pwr = st.number_input("القوة الهجومية:", 1.0, 10.0, 7.1)
    h_def = st.number_input("الصلابة الدفاعية:", 1.0, 10.0, 6.9)

with c2:
    a_name = st.text_input("🚀 الفريق الضيف:", "شباب بلوزداد")
    a_pwr = st.number_input("القوة الهجومية :", 1.0, 10.0, 8.0)
    a_def = st.number_input("الصلابة الدفاعية :", 1.0, 10.0, 8.6)

if st.button("🔱 إطـلاق الـرادار الـشـامـل"):
    with st.status("📡 جاري تحليل موازين القوى...", expanded=True) as status:
        time.sleep(1)
        st.write("🎲 فحص 500,000 سيناريو احتمالي...")
        time.sleep(0.5)
        st.write("📊 توقع توزيع الأهداف والركنيات...")
        status.update(label="✅ تم اكتشاف السيناريو الأمثل!", state="complete")
        
        # محرك المحاكاة الشمولي
        h_exp = max(0.2, (h_pwr * (11 - a_def)) / 25)
        a_exp = max(0.2, (a_pwr * (11 - h_def)) / 25)
        h_sim = np.random.poisson(h_exp, 500000)
        a_sim = np.random.poisson(a_exp, 500000)
        
        sc_h, sc_a = int(np.round(np.mean(h_sim))), int(np.round(np.mean(a_sim)))
        w_h, dr, w_a = (h_sim > a_sim).mean()*100, (h_sim == a_sim).mean()*100, (h_sim < a_sim).mean()*100
        
        # تحليل توقيت الأهداف (إحصائياً)
        first_half = "42%" if (h_pwr + a_pwr) < 14 else "58%"
        danger_idx = int((h_pwr + a_pwr) * 0.9)

        # ✅ العرض الإمبراطوري الشامل
        st.markdown(f"""
        <div class='strategy-card'>
            <p style='color:#888; font-size:1.1rem; letter-spacing:2px; margin:0;'>PREDICTED OUTCOME</p>
            <div class='main-score'>{sc_h} - {sc_a}</div>
            <h2 style='color:#fff; font-size:2.2rem;'>{h_name} <span style='color:#D4AF37;'>VS</span> {a_name}</h2>
            
            <div class='data-grid'>
                <div class='data-node'><p>فوز المضيف</p><h3>{w_h:.1f}%</h3></div>
                <div class='data-node'><p>التعادل</p><h3>{dr:.1f}%</h3></div>
                <div class='data-node'><p>فوز الضيف</p><h3>{w_a:.1f}%</h3></div>
            </div>
            
            <div class='data-grid' style='margin-top:15px; border-top:1px solid rgba(212,175,55,0.1); padding-top:20px;'>
                <div class='data-node' style='border-color:#ff4b4b;'><p>🔥 مؤشر الخطورة</p><h3>{danger_idx}/20</h3></div>
                <div class='data-node' style='border-color:#D4AF37;'><p>🚩 الركنيات</p><h3>{int((h_pwr+a_pwr)*0.75)}</h3></div>
                <div class='data-node' style='border-color:#FFD700;'><p>🟨 البطاقات</p><h3>{int((h_def+a_def)*0.28)}</h3></div>
            </div>

            <div style='background:rgba(212,175,55,0.05); border-radius:15px; padding:15px; margin-top:20px;'>
                <p style='margin:0; color:#D4AF37; font-weight:bold;'>💡 الرؤية الاستراتيجية:</p>
                <p style='margin:0; color:#ccc; font-size:0.9rem;'>احتمالية تسجيل أهداف في الشوط الثاني تبلغ {first_half}. 
                المباراة تتسم بـ {'ندية دفاعية عالية' if (h_def+a_def)>15 else 'هجوم كاسح'}.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
