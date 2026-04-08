import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعداد الصفحة والسمة الذهبية بوضوح عالٍ
st.set_page_config(page_title="Arabic Pro | إدخال رقمي دقيق", layout="wide")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp { 
        background-color: #000000; 
        font-family: 'Cairo', sans-serif; 
        direction: RTL; 
        text-align: right; 
    }
    
    h1, h2, h3 { 
        color: #FFD700 !important; 
        text-shadow: 2px 2px 4px #000000;
    }
    
    p, span, label { 
        color: #FFFFFF !important; 
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }
    
    /* تنسيق صناديق إدخال الأرقام لتكون واضحة بالذهبي */
    .stNumberInput input { 
        background-color: #1a1a1a !important; 
        color: #FFD700 !important; 
        border: 2px solid #FFD700 !important;
        font-size: 1.3rem !important;
        text-align: center !important;
    }

    .stButton>button { 
        background-color: #FFD700; color: black; font-weight: bold; 
        border-radius: 10px; width: 100%; height: 3.5em; font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 ARABIC PRO: التحليل الرقمي الدقيق")

if "match_history" not in st.session_state:
    st.session_state.match_history = []

# 2. منطقة الإدخال بالارقام بدلاً من الشريط
st.subheader("🔢 أدخل القيم الرقمية للمباراة")
col_h, col_a = st.columns(2)

with col_h:
    st.markdown("### 🏠 الفريق المضيف")
    h_name = st.text_input("اسم الفريق المضيف", "الأهلي")
    # استبدال Slider بـ Number Input
    h_atk = st.number_input("🚀 قوة الهجوم (0-100)", min_value=0, max_value=100, value=75, step=1)
    h_def = st.number_input("🛡️ قوة الدفاع (0-100)", min_value=0, max_value=100, value=70, step=1)

with col_a:
    st.markdown("### ✈️ الفريق الضيف")
    a_name = st.text_input("اسم الفريق الضيف", "الزمالك")
    # استبدال Slider بـ Number Input
    a_atk = st.number_input("🚀 قوة الهجوم (0-100) ", min_value=0, max_value=100, value=70, step=1)
    a_def = st.number_input("🛡️ قوة الدفاع (0-100) ", min_value=0, max_value=100, value=75, step=1)

st.write("---")

# 3. الزر ومنطق الحساب
if st.button("🔥 تنفيذ التحليل الرقمي"):
    h_total = (h_atk + h_def) / 2 + 5
    a_total = (a_atk + a_def) / 2
    win_p = round((h_total / (h_total + a_total)) * 100, 1)
    
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.metric(f"فوز {h_name}", f"{win_p}%")
    c2.metric("النتيجة المتوقعة", f"{int(h_atk/30)}-{int(a_atk/30)}")
    c3.metric(f"فوز {a_name}", f"{100-win_p}%")
    
    st.session_state.match_history.append({
        "التاريخ": datetime.now().strftime("%H:%M"),
        "المباراة": f"{h_name} vs {a_name}",
        "التوقع": f"{int(h_atk/30)}-{int(a_atk/30)}",
        "الأفضلية": h_name if win_p > 50 else a_name
    })

# 4. سجل النتائج
st.subheader("📜 سجل التحليلات")
if st.session_state.match_history:
    st.table(pd.DataFrame(st.session_state.match_history))

st.sidebar.markdown("<h2 style='color:#FFD700;'>ARABIC PRO</h2>", unsafe_allow_html=True)
if st.sidebar.button("🗑️ مسح السجل"):
    st.session_state.match_history = []
    st.rerun()
    
