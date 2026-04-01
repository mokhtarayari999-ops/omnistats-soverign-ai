import streamlit as st
import numpy as np
import time

# --- 🏗️ الهندسة المعمارية السيادية الفائقة ---
st.set_page_config(page_title="ARABIC PRO | FORTRESS", layout="wide", initial_sidebar_state="collapsed")

# 🧠 الحصن المعلوماتي: قاعدة بيانات مدمجة (محدثة لعام 2026) لضمان عدم الانقطاع
# تم اختيار الأرقام بناءً على "موازين القوى العالمية" الحالية
INTEL_DATABASE = {
    "إدخال يدوي (Manual)": {"atk": 7.0, "def": 7.0},
    "نادي بارادو (DZ)": {"atk": 7.1, "def": 6.9},
    "شباب بلوزداد (DZ)": {"atk": 8.0, "def": 8.6},
    "مولودية الجزائر (DZ)": {"atk": 8.2, "def": 7.8},
    "اتحاد العاصمة (DZ)": {"atk": 7.5, "def": 8.1},
    "وفاق سطيف (DZ)": {"atk": 7.3, "def": 7.2},
    "الترجي التونسي (TN)": {"atk": 8.4, "def": 8.3},
    "النادي الإفريقي (TN)": {"atk": 7.6, "def": 7.9},
    "النادي الأهلي (EG)": {"atk": 8.7, "def": 8.5},
    "نادي الزمالك (EG)": {"atk": 8.1, "def": 7.8},
    "مانشستر سيتي (EN)": {"atk": 9.8, "def": 9.0},
    "ريال مدريد (ES)": {"atk": 9.5, "def": 9.2},
    "برشلونة (ES)": {"atk": 8.9, "def": 8.1},
    "ليفربول (EN)": {"atk": 9.2, "def": 8.5},
    "بايرن ميونخ (DE)": {"atk": 9.3, "def": 8.4},
    "باريس سان جيرمان (FR)": {"atk": 9.0, "def": 8.0},
    "الهلال السعودي (SA)": {"atk": 8.9, "def": 8.3},
    "النصر السعودي (SA)": {"atk": 8.8, "def": 7.8},
    "الاتحاد السعودي (SA)": {"atk": 8.3, "def": 8.0}
}

# --- 🎨 الـ CSS الاحترافي (الذهب الأسود) ---
st.markdown("""
<style>
    @import url('https://googleapis.com');
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .result-card { background: rgba(255,255,255,0.02); border: 2px solid #D4AF37; border-radius: 30px; padding: 30px; text-align: center; margin-top: 20px; }
    .score-quantum { font-size: 6rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; line-height: 1; }
    .info-node { background: #0c0c0c; border: 1px solid rgba(212,175,55,0.3); border-radius: 15px; padding: 15px; flex: 1; min-width: 100px; }
    .odds-badge { background: #D4AF37; color: #000; border-radius: 8px; padding: 4px 8px; font-weight: 900; margin-top: 5px; display: inline-block; font-size: 0.9rem; }
    .stButton>button { background: linear-gradient(45deg, #D4AF37, #8A6D3B) !important; color: #000 !important; font-weight: 900 !important; border-radius: 50px !important; height: 3.8rem !important; font-size: 1.6rem !important; border: none !important; width: 100% !important; transition: 0.3s; box-shadow: 0 5px 20px rgba(212,175,55,0.4) !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37; letter-spacing:3px;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)

# --- واجهة اختيار الفرق "الذكية" ---
col_sel1, col_sel2 = st.columns(2)

with col_sel1:
    pick_h = st.selectbox("🎯 اختر المضيف (سيتم جلب بياناته):", list(INTEL_DATABASE.keys()), index=1)
    # تعبئة الخانات تلقائياً بمجرد الاختيار
    h_atk = st.number_input("قوة الهجوم:", 1.0, 10.0, INTEL_DATABASE[pick_h]["atk"], key="h_atk")
    h_def = st.number_input("صلابة الدفاع:", 1.0, 10.0, INTEL_DATABASE[pick_h]["def"], key="h_def")

with col_sel2:
    pick_a = st.selectbox("🎯 اختر الضيف (سيتم جلب بياناته):", list(INTEL_DATABASE.keys()), index=2)
    a_atk = st.number_input("قوة الهجوم :", 1.0, 10.0, INTEL_DATABASE[pick_a]["atk"], key="a_atk")
    a_def = st.number_input("صلابة الدفاع :", 1.0, 10.0, INTEL_DATABASE[pick_a]["def"], key="a_def")

if st.button("🔱 إطلاق المحرك الاستخباري الشامل"):
    with st.status("📡 جاري استحضار البيانات السيادية...", expanded=True) as status:
        time.sleep(1)
        st.write("🎲 معالجة 1,000,000 سيناريو احتمالي...")
        status.update(label="✅ التقرير جاهز!", state="complete")
        
        # محرك المحاكاة المليوني
        h_idx = max(0.2, (h_atk*(11-a_def))/25); a_idx = max(0.2, (a_atk*(11-h_def))/25)
        h_s = np.random.poisson(h_idx, 1000000); a_s = np.random.poisson(a_idx, 1000000)
        
        w_h, dr, w_a = (h_s>a_s).mean()*100, (h_s==a_s).mean()*100, (h_s<a_s).mean()*100
        odd_h, odd_dr, odd_a = round(100/w_h, 2), round(100/dr, 2), round(100/w_a, 2)
        
        # المعطيات الجانبية
        corn, cards = int((h_atk+a_atk)*0.75), int((h_def+a_def)*0.28)
        penalty = "عالية (🔥)" if (h_atk + a_atk) > 15 else "متوسطة (⚖️)"

        # ✅ العرض الإمبراطوري الشامل
        out = "<div class='result-card'>"
        out += f"<div class='score-quantum'>{int(np.mean(h_s))} - {int(np.mean(a_s))}</div>"
        out += f"<h2 style='color:#fff;'>{pick_h} <span style='color:#D4AF37;'>VS</span> {pick_a}</h2>"
        
        # شبكة المراهنات
        out += "<div style='display:flex; justify-content:center; gap:8px; flex-wrap:wrap; margin-top:20px;'>"
        out += f"<div class='info-node'><p>فوز المضيف</p><h3>{w_h:.1f}%</h3><div class='odds-badge'>{odd_h}</div></div>"
        out += f"<div class='info-node'><p>التعادل</p><h3>{dr:.1f}%</h3><div class='odds-badge'>{odd_dr}</div></div>"
        out += f"<div class='info-node'><p>فوز الضيف</p><h3>{w_a:.1f}%</h3><div class='odds-badge'>{odd_a}</div></div>"
        out += "</div>"

        # الأحداث الجانبية
        out += "<div style='display:flex; justify-content:center; gap:8px; flex-wrap:wrap; margin-top:10px;'>"
        out += f"<div class='info-node' style='border-color:#D4AF37;'><p>🚩 ركنيات</p><h3>{corn}</h3></div>"
        out += f"<div class='info-node' style='border-color:#FFD700;'><p>🟨 بطاقات</p><h3>{cards}</h3></div>"
        out += f"<div class='info-node' style='border-color:#ff4b4b;'><p>⚽ ضربة جزاء</p><h3>{penalty}</h3></div>"
        out += "</div>"
        
        out += "</div>"
        st.markdown(out, unsafe_allow_html=True)
        st.balloons()
