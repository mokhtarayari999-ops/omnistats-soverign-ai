import streamlit as st
import numpy as np
import time

# --- 🏗️ الهندسة المعمارية للنظام ---
st.set_page_config(page_title="ARABIC PRO", layout="wide", initial_sidebar_state="collapsed")

# --- 🎨 الـ CSS السيادي (محمي ومصقول 100%) ---
st.markdown("""
<style>
    @import url('https://googleapis.com');
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .header-master { text-align: center; padding: 25px; border-bottom: 2px solid #D4AF37; margin-bottom: 30px; }
    .title-master { font-size: 2.5rem; font-weight: 900; letter-spacing: 3px; color: #D4AF37; margin: 0; }
    .result-frame { background: rgba(255,255,255,0.02); border: 2px solid #D4AF37; border-radius: 30px; padding: 30px; text-align: center; margin-top: 20px; }
    .score-quantum { font-size: 6.5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; line-height: 1; margin: 15px 0; }
    .info-grid { display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; margin-top: 25px; }
    .info-node { background: #0c0c0c; border: 1px solid rgba(212,175,55,0.3); border-radius: 15px; padding: 15px; min-width: 100px; flex: 1; }
    .info-node p { font-size: 0.8rem; color: #777; margin: 0; }
    .info-node h3 { font-size: 1.3rem; color: #fff; margin: 5px 0 0 0; }
    .stNumberInput input, .stTextInput input { background: #050505 !important; border: 1px solid #D4AF37 !important; color: #fff !important; text-align: center !important; border-radius: 12px !important; }
    .stButton>button { background: linear-gradient(45deg, #D4AF37, #8A6D3B) !important; color: #000 !important; font-weight: 900 !important; border-radius: 50px !important; height: 3.5rem !important; font-size: 1.5rem !important; border: none !important; width: 100% !important; transition: 0.3s; }
    .stButton>button:hover { transform: scale(1.01); box-shadow: 0 0 30px rgba(212,175,55,0.4) !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='header-master'><h1 class='title-master'>ARABIC PRO 🏆</h1></div>", unsafe_allow_html=True)

# --- واجهة إدخال المعطيات ---
c1, c2 = st.columns(2)
with c1:
    h_n = st.text_input("🏠 الفريق المضيف:", "نادي بارادو")
    h_atk = st.number_input("قوة الهجوم (1-10):", 1.0, 10.0, 7.1)
    h_def = st.number_input("صلابة الدفاع (1-10):", 1.0, 10.0, 6.9)

with c2:
    a_n = st.text_input("🚀 الفريق الضيف:", "شباب بلوزداد")
    a_atk = st.number_input("قوة الهجوم (1-10) :", 1.0, 10.0, 8.0)
    a_def = st.number_input("صلابة الدفاع (1-10) :", 1.0, 10.0, 8.6)

# --- محرك المحاكاة والتحليل ---
if st.button("🔱 إطلاق التحليل السيادي الشامل"):
    with st.spinner('🎯 جاري معالجة 500,000 سيناريو...'):
        time.sleep(1)
        
        # الحسابات الرياضية العميقة
        h_idx = max(0.2, (h_atk * (11 - a_def)) / 25)
        a_idx = max(0.2, (a_atk * (11 - h_def)) / 25)
        h_s = np.random.poisson(h_idx, 500000)
        a_s = np.random.poisson(a_idx, 500000)
        
        res_h, res_a = int(np.round(np.mean(h_s))), int(np.round(np.mean(a_s)))
        win_h, dr, win_a = (h_s > a_s).mean()*100, (h_s == a_s).mean()*100, (h_s < a_s).mean()*100
        corn, cards = int((h_atk+a_atk)*0.75), int((h_def+a_def)*0.28)

        # 🧩 الإضافة الموعودة: رادار توزيع الأهداف
        # إذا كان إجمالي القوة الهجومية عالياً، يرجح الشوط الثاني (أهداف متأخرة)
        total_pwr = h_atk + a_atk
        goal_timing = "الشوط الثاني (بعد الدقيقة 60)" if total_pwr > 14 else "الشوط الأول (بداية حذرة)"

        # ✅ الحقن المعماري (نظام القطعة الواحدة)
        out = "<div class='result-frame'>"
        out += f"<p style='color:#888; letter-spacing:2px;'>توقعات المحرك السيادي</p>"
        out += f"<div class='score-quantum'>{res_h} - {res_a}</div>"
        out += f"<h2 style='color:#fff;'>{h_n} <span style='color:#D4AF37;'>VS</span> {a_n}</h2>"
        out += "<div class='info-grid'>"
        out += f"<div class='info-node'><p>فوز المضيف</p><h3>{win_h:.1f}%</h3></div>"
        out += f"<div class='info-node'><p>تعادل</p><h3>{dr:.1f}%</h3></div>"
        out += f"<div class='info-node'><p>فوز الضيف</p><h3>{win_a:.1f}%</h3></div>"
        out += "</div><div class='info-grid' style='margin-top:15px;'>"
        out += f"<div class='info-node' style='border-color:#D4AF37;'><p>🚩 ركنيات</p><h3>{corn}</h3></div>"
        out += f"<div class='info-node' style='border-color:#FFD700;'><p>🟨 بطاقات</p><h3>{cards}</h3></div>"
        out += "</div>"
        
        # 🛡️ الجزء المضاف الجديد
        out += "<div style='background:rgba(212,175,55,0.05); border-radius:15px; padding:15px; margin-top:20px; border:1px dashed #D4AF37;'>"
        out += f"<p style='color:#D4AF37; margin:0; font-weight:bold;'>💡 رادار توزيع الأهداف:</p>"
        out += f"<p style='color:#ccc; margin:0; font-size:0.9rem;'>يُتوقع تركيز الأهداف في: <b>{goal_timing}</b></p></div>"
        
        out += "</div>"
        
        st.markdown(out, unsafe_allow_html=True)
        st.balloons()
    
