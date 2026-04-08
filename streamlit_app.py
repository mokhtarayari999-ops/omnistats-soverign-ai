import streamlit as st
import pandas as pd
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="ARABIC PRO", layout="centered")

# تنسيق الواجهة بالأسود والذهبي مع نصوص واضحة جداً
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp { background-color: #000000; font-family: 'Cairo', sans-serif; direction: RTL; text-align: right; }
    
    /* الذهبي للعناوين */
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; font-weight: 900 !important; }
    
    /* الأبيض الواضح للنصوص */
    label, p, span { color: #FFFFFF !important; font-size: 1.3rem !important; font-weight: 700 !important; }
    
    /* صناديق إدخال الأرقام - بديل الخط الأحمر */
    .stNumberInput input { 
        background-color: #1a1a1a !important; 
        color: #D4AF37 !important; 
        border: 2px solid #D4AF37 !important;
        font-size: 1.5rem !important;
        text-align: center !important;
    }
    
    /* زر التحليل */
    .stButton>button { 
        background-color: #D4AF37; color: black; font-weight: 900; 
        border-radius: 10px; width: 100%; height: 3em; font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# العنوان كما في الصورة
st.title("🏆 ARABIC PRO")
st.markdown("### نظام التوقيع والتحليل اليدوي")
st.write("---")

if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("## 📝 إدخال بيانات المباراة يدوياً")

# تقسيم الفريقين
col_h, col_a = st.columns(2)

with col_h:
    st.markdown("### 🏠 الفريق المضيف")
    home_name = st.text_input("اسم الفريق المضيف", "الأهلي")
    # هنا التغيير الجذري: نستخدم number_input بدل slider
    h_atk = st.number_input("قوة الهجوم (المضيف)", 0, 100, 75)
    h_def = st.number_input("قوة الدفاع (المضيف)", 0, 100, 70)

with col_a:
    st.markdown("### ✈️ الفريق الضيف")
    away_name = st.text_input("اسم الفريق الضيف", "الزمالك")
    a_atk = st.number_input("قوة الهجوم (الضيف)", 0, 100, 70)
    a_def = st.number_input("قوة الدفاع (الضيف)", 0, 100, 75)

st.write("---")

if st.button("✨ تشغيل التحليل الذهبي"):
    # حسابات التوقع
    total_h = (h_atk + h_def) / 2
    total_a = (a_atk + a_def) / 2
    win_p = round((total_h / (total_h + total_a)) * 100, 1)
    
    st.subheader("📊 النتيجة المتوقعة")
    c1, c2, c3 = st.columns(3)
    c1.metric(f"فوز {home_name}", f"{win_p}%")
    c2.metric("النتيجة", f"{int(h_atk/30)}-{int(a_atk/30)}")
    c3.metric(f"فوز {away_name}", f"{100-win_p}%")
    
    # إضافة للسجل
    st.session_state.history.append({
        "المباراة": f"{home_name} vs {away_name}",
        "التوقع": f"{int(h_atk/30)}-{int(a_atk/30)}",
        "الوقت": datetime.now().strftime("%H:%M")
    })

# سجل النتائج
st.write("---")
st.subheader("📜 سجل النتائج")
if st.session_state.history:
    st.table(pd.DataFrame(st.session_state.history))

st.sidebar.title("إعدادات")
if st.sidebar.button("مسح السجل"):
    st.session_state.history = []
    st.rerun()
    
