import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات الصفحة لتناسب شاشة الهاتف
st.set_page_config(page_title="ARABIC PRO", layout="centered")

# 2. تصميم ذهبي وأسود بوضوح عالٍ جداً للهاتف
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp { background-color: #000000; font-family: 'Cairo', sans-serif; direction: RTL; text-align: right; }
    
    /* عناوين ذهبية كبيرة */
    h1 { color: #FFD700 !important; font-size: 2.2rem !important; text-align: center; font-weight: 900 !important; }
    h3 { color: #FFD700 !important; font-size: 1.5rem !important; }
    
    /* نصوص بيضاء واضحة جداً */
    label, p { color: #FFFFFF !important; font-size: 1.2rem !important; font-weight: bold !important; }
    
    /* صناديق الأرقام: كبيرة ومريحة للمس بالهاتف */
    .stNumberInput div div input { 
        background-color: #111111 !important; 
        color: #FFD700 !important; 
        border: 2px solid #FFD700 !important;
        font-size: 1.8rem !important;
        height: 70px !important;
        text-align: center !important;
        border-radius: 15px !important;
    }
    
    /* زر التحليل: كبير وسهل الضغط */
    .stButton>button { 
        background-color: #FFD700; color: black; font-weight: 900; 
        border-radius: 20px; width: 100%; height: 4em; font-size: 1.4rem;
        margin-top: 20px; border: 2px solid #ffffff;
    }
    
    /* إخفاء المنزلقات تماماً */
    .stSlider { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 ARABIC PRO")
st.write("---")

# سجل النتائج
if "history" not in st.session_state:
    st.session_state.history = []

# 3. إدخال البيانات بالارقام فقط (مناسب للمس)
st.markdown("### 🏠 الفريق المضيف")
h_name = st.text_input("اسم الفريق الأول", "المضيف")
h_atk = st.number_input("🚀 قوة الهجوم (رقم)", 0, 100, 50, key="h_atk")
h_def = st.number_input("🛡️ قوة الدفاع (رقم)", 0, 100, 50, key="h_def")

st.write("---")

st.markdown("### ✈️ الفريق الضيف")
a_name = st.text_input("اسم الفريق الثاني", "الضيف")
a_atk = st.number_input("🚀 قوة الهجوم (رقم) ", 0, 100, 50, key="a_atk")
a_def = st.number_input("🛡️ قوة الدفاع (رقم) ", 0, 100, 50, key="a_def")

# 4. تنفيذ التحليل
if st.button("🔥 ابدأ التحليل الذهبي"):
    total_h = (h_atk + h_def) / 2
    total_a = (a_atk + a_def) / 2
    win_p = round((total_h / (total_h + total_a)) * 100, 1)
    
    st.success(f"النتيجة المتوقعة لـ {h_name}: {int(h_atk/30)}")
    st.success(f"النتيجة المتوقعة لـ {a_name}: {int(a_atk/35)}")
    
    # إضافة للسجل
    st.session_state.history.append({
        "المباراة": f"{h_name} x {a_name}",
        "النتيجة": f"{int(h_atk/30)}-{int(a_atk/35)}",
        "الوقت": datetime.now().strftime("%H:%M")
    })

# 5. عرض سجل النتائج
if st.session_state.history:
    st.write("### 📜 السجل")
    st.table(pd.DataFrame(st.session_state.history))

if st.sidebar.button("🗑️ مسح السجل"):
    st.session_state.history = []
    st.rerun()
    
