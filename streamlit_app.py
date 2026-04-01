import streamlit as st
import numpy as np
import time

# --- 🏗️ الهندسة المعمارية السيادية ---
st.set_page_config(page_title="ARABIC PRO | BET INTEL", layout="wide", initial_sidebar_state="collapsed")

# --- 🎨 CSS النيون الاحترافي (نسخة المراهنات العالمية) ---
st.markdown("""
<style>
    @import url('https://googleapis.com');
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .result-frame { background: rgba(255,255,255,0.02); border: 2px solid #D4AF37; border-radius: 30px; padding: 30px; text-align: center; margin-top: 20px; }
    .main-score { font-size: 6rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; }
    .info-node { background: #0c0c0c; border: 1px solid rgba(212,175,55,0.3); border-radius: 15px; padding: 15px; flex: 1; min-width: 100px; }
    .odds-badge { background: #D4AF37; color: #000; border-radius: 10px; padding: 5px 10px; font-weight: 900; margin-top: 5px; display: inline-block; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)

# واجهة المدخلات
c1, c2 = st.columns(2)
with c1:
    h_n = st.text_input("🏠 المضيف:", "نادي بارادو")
    h_atk = st.number_input("قوة الهجوم:", 1.0, 10.0, 7.1)
    h_def = st.number_input("الصلابة الدفاعية:", 1.0, 10.0, 6.9)
with c2:
    a_n = st.text_input("🚀 الضيف:", "شباب بلوزداد")
    a_atk = st.number_input("قوة الهجوم :", 1.0, 10.0, 8.0)
    a_def = st.number_input("الصلابة الدفاعية :", 1.0, 10.0, 8.6)

if st.button("🔱 إطلاق المحرك الاستخباري"):
    with st.spinner('🎯 جاري استخراج الاحتمالات العميقة...'):
        time.sleep(1.5)
        h_idx = max(0.2, (h_atk*(11-a_def))/25); a_idx = max(0.2, (a_atk*(11-h_def))/25)
        h_s = np.random.poisson(h_idx, 500000); a_s = np.random.poisson(a_idx, 500000)
        
        # الحسابات
        w_h, dr, w_a = (h_s>a_s).mean()*100, (h_s==a_s).mean()*100, (h_s<a_s).mean()*100
        
        # 🎲 إضافة "الأرقام العادلة" (Odds) كما في شركات المراهنة
        odd_h = round(100/w_h, 2) if w_h > 0 else 10
        odd_dr = round(100/dr, 2) if dr > 0 else 10
        odd_a = round(100/w_a, 2) if w_a > 0 else 10

        out = "<div class='result-frame'>"
        out += f"<div class='main-score'>{int(np.mean(h_s))} - {int(np.mean(a_s))}</div>"
        out += f"<h2 style='color:#fff;'>{h_n} VS {a_n}</h2>"
        
        out += "<div style='display:flex; justify-content:center; gap:10px; flex-wrap:wrap; margin-top:20px;'>"
        out += f"<div class='info-node'><p>فوز المضيف</p><h3>{w_h:.1f}%</h3><div class='odds-badge'>{odd_h}</div></div>"
        out += f"<div class='info-node'><p>التعادل</p><h3>{dr:.1f}%</h3><div class='odds-badge'>{odd_dr}</div></div>"
        out += f"<div class='info-node'><p>فوز الضيف</p><h3>{w_a:.1f}%</h3><div class='odds-badge'>{odd_a}</div></div>"
        out += "</div>"

        # إضافة احتمالية "الفرصة المزدوجة"
        out += f"<p style='margin-top:20px; color:#D4AF37;'>💡 تغطية المخاطر (الفرصة المزدوجة): <b>{h_n} أو تعادل: {w_h+dr:.1f}%</b></p>"
        out += "</div>"
        st.markdown(out, unsafe_allow_html=True)
        st.balloons()
    
