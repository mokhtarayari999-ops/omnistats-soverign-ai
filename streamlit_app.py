import streamlit as st
import pandas as pd
import random
import time

# إعداد الصفحة وتصميم الهوية (أسود وذهبي)
st.set_page_config(page_title="نظام المحاكاة الشمولية 2026", layout="centered")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .main { background-color: #000000; }
    h1, h2, h3, p, label, .stMarkdown { 
        color: #D4AF37 !important; 
        text-align: right; 
        font-family: 'Cairo', sans-serif; 
    }
    .stNumberInput input { background-color: #1a1a1a; color: white; border: 1px solid #D4AF37; }
    .stTextInput input { background-color: #1a1a1a; color: white; border: 1px solid #D4AF37; text-align: right; }
    .stButton>button { 
        width: 100%; border-radius: 10px; height: 3.5em;
        background: linear-gradient(45deg, #D4AF37, #8A6E2F); 
        color: black; font-weight: bold; border: none; font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'history_log' not in st.session_state:
    st.session_state.history_log = []

st.title("🔱 نظام المحاكاة الشمولية العظمى")
st.subheader("إصدار 2026 - مشروع Arabic Pro")

# --- المدخلات ---
st.markdown("### 🏟️ الفريق المضيف")
home_t = st.text_input("اسم الفريق", value="الترجي", key="h1")
h_att = st.number_input("قوة الهجوم (1-10)", 0.0, 10.0, 8.20, key="h2")
h_def = st.number_input("صلابة الدفاع (1-10)", 0.0, 10.0, 8.00, key="h3")

st.markdown("---")
st.markdown("### ✈️ الفريق الضيف")
away_t = st.text_input("اسم الفريق ", value="الأهلي", key="a1")
a_att = st.number_input("قوة الهجوم (1-10) ", 0.0, 10.0, 7.50, key="a2")
a_def = st.number_input("صلابة الدفاع (1-10) ", 0.0, 10.0, 8.50, key="a3")

if st.button("إطلاق المحاكاة العظمى 🚀"):
    with st.spinner('جاري تحليل البيانات...'):
        time.sleep(1.5)
        h_score = max(0, int((h_att - a_def/2) * random.uniform(0.6, 1.4)))
        a_score = max(0, int((a_att - h_def/2) * random.uniform(0.6, 1.4)))
        res = f"{h_score} - {a_score}"
        st.session_state.history_log.insert(0, {"المضيف": home_t, "النتيجة": res, "الضيف": away_t})
    
    st.markdown(f"<h1 style='text-align: center; color: white;'>{home_t} {res} {away_t}</h1>", unsafe_allow_html=True)
    st.balloons()

if st.session_state.history_log:
    st.markdown("### 📋 السجل")
    st.table(pd.DataFrame(st.session_state.history_log))
