import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعداد الصفحة
st.set_page_config(page_title="ARABIC PRO AI", layout="centered")

# 2. كود الـ CSS الخارق للوضوح الكامل (بدون باهت وبدون Sliders)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* خلفية سوداء نقية */
    .stApp { background-color: #000000; font-family: 'Cairo', sans-serif; direction: RTL; text-align: right; }
    
    /* عنوان ذهبي ضخم وواضح */
    h1 { color: #FFD700 !important; text-align: center !important; font-size: 2.5rem !important; font-weight: 900 !important; text-shadow: 2px 2px 5px #000; margin-bottom: 30px; }
    
    /* نصوص بيضاء صارخة */
    label, p { color: #FFFFFF !important; font-size: 1.3rem !important; font-weight: bold !important; opacity: 1 !important; }
    
    /* صناديق الأرقام الذهبية (بديل الخطوط الحمراء) */
    div[data-baseweb="input"] { background-color: #111111 !important; border: 2px solid #FFD700 !important; border-radius: 15px !important; }
    input { color: #FFD700 !important; font-size: 1.5rem !important; font-weight: bold !important; text-align: center !important; }
    
    /* إخفاء أي Slider قديم بقوة */
    .stSlider { display: none !important; visibility: hidden !important; }
    
    /* زر التحليل الذهبي الفاخر */
    .stButton>button { 
        background-color: #FFD700 !important; color: #000000 !important; font-weight: 900 !important; 
        font-size: 1.5rem !important; border-radius: 20px !important; width: 100% !important; 
        height: 4em !important; border: 2px solid #ffffff !important; box-shadow: 0 4px 15px rgba(255,215,0,0.4);
    }

    /* نتائج واضحة جداً وغير باهتة */
    div[data-testid="stMetricValue"] { color: #FFD700 !important; font-size: 2.5rem !important; font-weight: 900 !important; opacity: 1 !important; }
    div[data-testid="stMetricLabel"] { color: #FFFFFF !important; font-size: 1.1rem !important; opacity: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. واجهة التطبيق
st.title("🏆 ARABIC PRO")

if "history" not in st.session_state:
    st.session_state.history = []

# منطقة الإدخال الرقمي المباشر
st.markdown("### 📝 بيانات المباراة")
h_name = st.text_input("اسم الفريق المضيف", "الزمالك")

col1, col2, col3 = st.columns(3)
with col1: h_atk = st.number_input("🚀 هجوم", 0, 100, 70, key="atk_h")
with col2: h_mid = st.number_input("⚙️ وسط", 0, 100, 60, key="mid_h")
with col3: h_def = st.number_input("🛡️ دفاع", 0, 100, 70, key="def_h")

st.write("---")

# 4. تنفيذ التحليل وعرض النتائج
if st.button("🔥 تنفيذ التحليل العميق"):
    # معادلة بسيطة للتوقع
    power = (h_atk + h_mid + h_def) / 3
    win_p = round(power, 1)
    predicted_score = f"{int(h_atk/30)} - 0"
    
    st.markdown("---")
    res1, res2 = st.columns(2)
    res1.metric("احتمالية الفوز", f"{win_p}%")
    res2.metric("النتيجة المتوقعة", predicted_score)
    
    # حفظ في السجل
    st.session_state.history.insert(0, {
        "المباراة": h_name,
        "التوقع": predicted_score,
        "الوقت": datetime.now().strftime("%H:%M")
    })

# 5. سجل النتائج
st.write("---")
st.subheader("📜 سجل نتائج التحليلات")
if st.session_state.history:
    st.table(pd.DataFrame(st.session_state.history))
else:
    st.info("قم بإجراء أول تحليل لرؤية النتائج هنا.")

st.sidebar.markdown("<h2 style='color:#FFD700;'>إعدادات</h2>", unsafe_allow_html=True)
if st.sidebar.button("🗑️ مسح السجل"):
    st.session_state.history = []
    st.rerun()
