import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات احترافية للواجهة المظلمة (Dark Mode)
st.set_page_config(page_title="Arabic Pro | Match Science", layout="centered")

# 2. كود CSS المطور لتصميم يشبه Replit مع لمسة ذهبية
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp { background-color: #0b0e14; font-family: 'Cairo', sans-serif; direction: RTL; text-align: right; }
    
    /* العناوين والوصف */
    .title-text { color: #D4AF37; font-size: 35px; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .subtitle-text { color: #8a8d97; font-size: 16px; text-align: center; margin-bottom: 30px; }
    
    /* حاويات الإدخال (شكل احترافي) */
    .stNumberInput, .stTextInput { background-color: #161b22 !important; border-radius: 12px !important; }
    .stNumberInput input { 
        color: #FFD700 !important; font-size: 22px !important; font-weight: bold !important;
        background-color: transparent !important; border: 1px solid #30363d !important; text-align: center !important;
    }
    
    /* تسميات الحقول (Label) بجانب الأرقام */
    label { color: #58a6ff !important; font-weight: 700 !important; font-size: 1.1rem !important; }
    
    /* زر التحليل (مثل الأزرار في الصورة) */
    .stButton>button { 
        background: linear-gradient(90deg, #D4AF37 0%, #FFD700 100%); color: black;
        font-weight: 900; border-radius: 12px; width: 100%; height: 60px; font-size: 1.5rem;
        border: none; box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.3); margin-top: 20px;
    }
    
    /* إخفاء شريط التمرير (Slider) نهائياً */
    .stSlider { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. واجهة المستخدم (Header)
st.markdown('<p class="title-text">Science | Arabic Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">أدخل قوة الهجوم والدفاع لتوليد توقعات دقيقة للمباريات بناءً على النمذجة الرياضية المتطورة.</p>', unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

# 4. معلمات المباراة (Match Parameters) - إدخال رقمي فقط
with st.container():
    st.markdown("### 📈 معلمات المباراة (Match Parameters)")
    
    # قسم الفريق المضيف
    st.markdown("---")
    st.markdown("<h4 style='color:#58a6ff;'>🔵 ملف الفريق المضيف (HOME)</h4>", unsafe_allow_html=True)
    h_name = st.text_input("اسم الفريق المضيف", "الأهلي")
    
    c1, c2 = st.columns(2)
    with c1: h_atk = st.number_input("تقييم الهجوم (Home)", 0.0, 10.0, 1.5, step=0.1)
    with c2: h_def = st.number_input("تقييم الدفاع (Home)", 0.0, 10.0, 1.2, step=0.1)

    # قسم الفريق الضيف
    st.markdown("<h4 style='color:#bc8cff;'>🟣 ملف الفريق الضيف (AWAY)</h4>", unsafe_allow_html=True)
    a_name = st.text_input("اسم الفريق الضيف", "الزمالك")
    
    c3, c4 = st.columns(2)
    with c3: a_atk = st.number_input("تقييم الهجوم (Away)", 0.0, 10.0, 1.4, step=0.1)
    with c4: a_def = st.number_input("تقييم الدفاع (Away)", 0.0, 10.0, 1.1, step=0.1)

# 5. زر التحليل الرياضي
if st.button("توليد التوقعات الرياضية 🚀"):
    # معادلة التحليل المتقدمة
    home_score = round(h_atk / a_def, 1) if a_def != 0 else h_atk
    away_score = round(a_atk / h_def, 1) if h_def != 0 else a_atk
    
    win_prob = round((home_score / (home_score + away_score)) * 100, 1)
    
    st.markdown("---")
    res1, res2, res3 = st.columns(3)
    res1.metric(f"فوز {h_name}", f"{win_prob}%")
    res2.metric("النتيجة المتوقعة", f"{int(home_score)}-{int(away_score)}")
    res3.metric(f"فوز {a_name}", f"{100-win_p}%")
    
    st.session_state.history.insert(0, {
        "المباراة": f"{h_name} vs {a_name}",
        "التوقع": f"{int(home_score)}-{int(away_score)}",
        "النسبة": f"{win_prob}%"
    })

# 6. سجل النتائج الاحترافي
if st.session_state.history:
    st.write("### 📜 سجل التحليلات")
    st.table(pd.DataFrame(st.session_state.history))

st.sidebar.markdown("<h2 style='color:#D4AF37;'>Arabic Pro AI</h2>", unsafe_allow_html=True)
if st.sidebar.button("🗑️ تفريغ السجل"):
    st.session_state.history = []
    st.rerun()
                                     
