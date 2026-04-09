import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="ARABIC PRO", layout="centered")

# 2. CSS خارق لإصلاح التداخل وإخفاء الـ Sliders نهائياً
st.markdown("""
    <style>
    .stApp { background-color: #000000; direction: RTL; text-align: right; }
    h1, h3 { color: #FFD700 !important; text-align: center !important; font-family: 'Arial'; }
    label { color: #FFFFFF !important; font-size: 1.2rem !important; font-weight: bold !important; }
    
    /* إخفاء أي Slider (الخطوط الحمراء) نهائياً */
    .stSlider { display: none !important; }
    
    /* تنسيق صناديق الأرقام لتكون ذهبية وواضحة */
    input[type=number] {
        background-color: #1a1a1a !important;
        color: #FFD700 !important;
        border: 2px solid #FFD700 !important;
        font-size: 1.5rem !important;
        text-align: center !important;
        border-radius: 10px !important;
    }
    
    /* زر التحليل العميق */
    .stButton>button {
        background-color: #FFD700 !important; color: black !important;
        font-weight: 900 !important; font-size: 1.3rem !important;
        border-radius: 15px !important; height: 3.5em !important; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. محتوى التطبيق (تم حذف الكلمة العمودية المسببة للتعليق)
st.title("🏆 ARABIC PRO")
st.write("---")

if "history" not in st.session_state:
    st.session_state.history = []

# مدخلات الفريق (أرقام فقط - لا توجد خطوط حمراء هنا)
st.markdown("### 🏟️ بيانات المباراة")
h_name = st.text_input("اسم فريق المضيف", "الزمالك")
col1, col2 = st.columns(2)
with col1: h_atk = st.number_input("🚀 قوة الهجوم", 0, 100, 70)
with col2: h_def = st.number_input("🛡️ قوة الدفاع", 0, 100, 70)

st.write("---")

if st.button("✨ تنفيذ التحليل العميق"):
    # حساب سريع
    prob = round((h_atk / (h_atk + 50)) * 100, 1)
    st.markdown(f"<h2 style='color:#FFD700; text-align:center;'>النتيجة المتوقعة: {int(h_atk/30)} - 0</h2>", unsafe_allow_html=True)
    
    st.session_state.history.insert(0, {"المباراة": h_name, "التوقع": f"{int(h_atk/30)}-0"})

# سجل النتائج
st.subheader("📜 سجل نتائج التحليلات")
if st.session_state.history:
    st.table(pd.DataFrame(st.session_state.history))
