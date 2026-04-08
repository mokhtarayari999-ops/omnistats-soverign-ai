import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات الصفحة
st.set_page_config(page_title="ARABIC PRO AI", layout="centered")

# 2. تصميم الواجهة الذهبية والسوداء بوضوح فائق (High Contrast)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* الخلفية سوداء فحمية */
    .stApp { background-color: #000000; font-family: 'Cairo', sans-serif; direction: RTL; text-align: right; }
    
    /* جعل العناوين ذهبية صارخة */
    h1, h2, h3 { color: #FFD700 !important; font-weight: 900 !important; text-align: center; }
    
    /* نصوص الإدخال باللون الأبيض الناصع */
    label, p { color: #FFFFFF !important; font-size: 1.3rem !important; font-weight: bold !important; }
    
    /* تنسيق صناديق إدخال الأرقام (بديل الـ Slider) */
    .stNumberInput div div input { 
        background-color: #1a1a1a !important; 
        color: #FFD700 !important; 
        border: 2px solid #FFD700 !important;
        font-size: 1.6rem !important;
        height: 60px !important;
        text-align: center !important;
    }
    
    /* زر التحليل العميق */
    .stButton>button { 
        background-color: #FFD700; color: black; font-weight: 900; 
        border-radius: 20px; width: 100%; height: 3.5em; font-size: 1.3rem;
        border: 2px solid white; margin-top: 15px;
    }
    
    /* تصحيح لون النتائج الباهتة (البطاقات الذهبية) */
    div[data-testid="stMetric"] { 
        background-color: #111111 !important; 
        border: 2px solid #FFD700 !important; 
        padding: 20px !important; 
        border-radius: 15px !important;
        text-align: center !important;
    }
    
    /* جعل الأرقام والنسب المئوية ذهبية واضحة جداً وغير باهتة */
    div[data-testid="stMetricValue"] { 
        color: #FFD700 !important; 
        font-size: 3rem !important; 
        font-weight: 900 !important;
        opacity: 1 !important; /* ضمان عدم وجود بهتان */
    }
    
    /* جعل تسميات النتائج بيضاء واضحة */
    div[data-testid="stMetricLabel"] { 
        color: #FFFFFF !important; 
        font-size: 1.2rem !important; 
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 ARABIC PRO AI")
st.write("---")

if "history" not in st.session_state:
    st.session_state.history = []

# 3. المدخلات الرقمية يدوياً (تم استبدال الـ Slider بـ Number Input)
st.markdown("### 📝 إدخال البيانات بالارقام")
col1, col2 = st.columns(2)

with col1:
    h_name = st.text_input("الفريق المضيف", "الأهلي")
    h_atk = st.number_input("قوة الهجوم (المضيف)", 0, 100, 75)
    h_def = st.number_input("قوة الدفاع (المضيف)", 0, 100, 70)

with col2:
    a_name = st.text_input("الفريق الضيف", "الزمالك")
    a_atk = st.number_input("قوة الهجوم (الضيف)", 0, 100, 70)
    a_def = st.number_input("قوة الدفاع (الضيف)", 0, 100, 75)

st.write("---")

# 4. زر التنفيذ وعرض النتائج الواضحة
if st.button("✨ تنفيذ التحليل العميق"):
    total_h = (h_atk + h_def) / 2
    total_a = (a_atk + a_def) / 2
    win_p = round((total_h / (total_h + total_a)) * 100, 1)
    
    # عرض النتائج في بطاقات واضحة وغير باهتة
    c1, c2, c3 = st.columns(3)
    c1.metric(f"فوز {h_name}", f"{win_p}%")
    c2.metric("النتيجة", f"{int(h_atk/30)}-{int(a_atk/30)}")
    c3.metric(f"فوز {a_name}", f"{100-win_p}%")
    
    st.session_state.history.append({
        "المباراة": f"{h_name} vs {a_name}",
        "التوقع": f"{int(h_atk/30)}-{int(a_atk/30)}",
        "الوقت": datetime.now().strftime("%H:%M")
    })

# 5. السجل
if st.session_state.history:
    st.write("### 📜 سجل التحليلات")
    st.table(pd.DataFrame(st.session_state.history))

st.sidebar.button("🗑️ مسح السجل", on_click=lambda: st.session_state.clear())
    
