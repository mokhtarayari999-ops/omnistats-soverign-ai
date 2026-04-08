import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
import time

# 1. إعدادات الهوية البصرية الفخمة
st.set_page_config(page_title="Arabic Pro 2026", layout="centered")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .main { background-color: #000000; }
    h1, h2, h3, p, label { color: #D4AF37 !important; text-align: right; font-family: 'Cairo', sans-serif; }
    .stNumberInput input { background-color: #1a1a1a; color: white; border: 1px solid #D4AF37; text-align: center; }
    .stTextInput input { background-color: #1a1a1a; color: white; border: 1px solid #D4AF37; text-align: right; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em;
        background: linear-gradient(45deg, #D4AF37, #8A6E2F); 
        color: black; font-weight: bold; border: none; font-size: 18px;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; justify-content: center; }
    </style>
    """, unsafe_allow_html=True)

if 'history_log' not in st.session_state:
    st.session_state.history_log = []

st.title("🔱 نظام المحاكاة الشمولية العظمى")
st.subheader("مشروع Arabic Pro - إصدار 2026")

# 2. تنظيم المدخلات في أعمدة احترافية
col_home, col_away = st.columns(2)

with col_home:
    st.markdown("### 🏟️ المضيف")
    h_name = st.text_input("اسم الفريق", value="الترجي", key="h_n")
    h_att = st.number_input("الهجوم (1-10)", 0.0, 10.0, 8.2, key="h_a")
    h_def = st.number_input("الدفاع (1-10)", 0.0, 10.0, 8.0, key="h_d")

with col_away:
    st.markdown("### ✈️ الضيف")
    a_name = st.text_input("اسم الفريق ", value="الأهلي", key="a_n")
    a_att = st.number_input("الهجوم (1-10) ", 0.0, 10.0, 7.5, key="a_a")
    a_def = st.number_input("الدفاع (1-10) ", 0.0, 10.0, 8.5, key="a_d")

st.divider()

# 3. محرك المحاكاة والتحليل البصري
if st.button("إطلاق المحاكاة العظمى 🚀"):
    with st.spinner('جاري تحليل القوى...'):
        time.sleep(1.2)
        h_score = max(0, int((h_att - a_def/2) * random.uniform(0.7, 1.3)))
        a_score = max(0, int((a_att - h_def/2) * random.uniform(0.7, 1.3)))
        res = f"{h_score} - {a_score}"
        st.session_state.history_log.insert(0, {"المضيف": h_name, "النتيجة": res, "الضيف": a_name})

    st.markdown(f"<h1 style='text-align: center; font-size: 50px; color: white;'>{h_name} {res} {a_name}</h1>", unsafe_allow_html=True)
    st.balloons()

    # --- رادار القوى الاحترافي ---
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=[h_att, h_def, (h_att+h_def)/2], theta=['الهجوم','الدفاع','التوازن'], fill='toself', name=h_name, line_color='#D4AF37'))
    fig.add_trace(go.Scatterpolar(r=[a_att, a_def, (a_att+a_def)/2], theta=['الهجوم','الدفاع','التوازن'], fill='toself', name=a_name, line_color='#FFFFFF'))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#D4AF37")
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# 4. سجل العمليات
st.subheader("📋 سجل العمليات التاريخي")
if st.session_state.history_log:
    st.table(pd.DataFrame(st.session_state.history_log))
    if st.button("🗑️ مسح السجل"):
        st.session_state.history_log = []
        st.rerun()
else:
    st.info("السجل فارغ حالياً.. ابدأ أول محاكاة.")
    
