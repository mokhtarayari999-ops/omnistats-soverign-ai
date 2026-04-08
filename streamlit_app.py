import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
import time

# 1. إعداد الصفحة وتصميم الهوية (إصدار 2026 الخارق)
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
    .stNumberInput input { background-color: #1a1a1a; color: white; border: 1px solid #D4AF37; text-align: center; }
    .stTextInput input { background-color: #1a1a1a; color: white; border: 1px solid #D4AF37; text-align: right; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em;
        background: linear-gradient(45deg, #D4AF37, #8A6E2F); 
        color: black; font-weight: bold; border: none; font-size: 18px;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.3);
    }
    .stTable { border: 1px solid #D4AF37; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# تهيئة سجل البيانات
if 'history_log' not in st.session_state:
    st.session_state.history_log = []

st.title("🔱 نظام المحاكاة الشمولية العظمى")
st.subheader("إصدار 2026 - مشروع Arabic Pro")

# --- منطقة إدخال بيانات الفريقين ---
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### 🏟️ المضيف")
    home_t = st.text_input("اسم الفريق", value="الترجي", key="h_name")
    h_att = st.number_input("قوة الهجوم (1-10)", 0.0, 10.0, 8.20, key="h_att")
    h_def = st.number_input("صلابة الدفاع (1-10)", 0.0, 10.0, 8.00, key="h_def")

with col_b:
    st.markdown("### ✈️ الضيف")
    away_t = st.text_input("اسم الفريق ", value="الأهلي", key="a_name")
    a_att = st.number_input("قوة الهجوم (1-10) ", 0.0, 10.0, 7.50, key="a_att")
    a_def = st.number_input("صلابة الدفاع (1-10) ", 0.0, 10.0, 8.50, key="a_att_def")

st.divider()

# --- زر المحاكاة والتحليل ---
if st.button("إطلاق المحاكاة العظمى 🚀"):
    with st.spinner('جاري تحليل القوى الاستراتيجية...'):
        time.sleep(1.5)
        
        # محرك النتائج الذكي
        h_score = max(0, int((h_att - a_def/2) * random.uniform(0.6, 1.4)))
        a_score = max(0, int((a_att - h_def/2) * random.uniform(0.6, 1.4)))
        result_str = f"{h_score} - {a_score}"
        
        # حفظ في السجل
        st.session_state.history_log.insert(0, {
            "المضيف": home_t,
            "النتيجة": result_str,
            "الضيف": away_t
        })

    # عرض النتيجة الكبيرة
    st.markdown(f"<h1 style='text-align: center; font-size: 60px; color: white;'>{home_t} {result_str} {away_t}</h1>", unsafe_allow_html=True)
    st.balloons()

    # --- رادار القوى المتقابلة (الإضافة الجديدة) ---
    st.markdown("### 📊 رادار القوى المتقابلة")
    fig = go.Figure()
    
    # بيانات المضيف (ذهبي)
    fig.add_trace(go.Scatterpolar(
        r=[h_att, h_def, (h_att+h_def)/2],
        theta=['الهجوم', 'الدفاع', 'التوازن'],
        fill='toself', name=home_t, line_color='#D4AF37'
    ))
    
    # بيانات الضيف (أبيض/فضي)
    fig.add_trace(go.Scatterpolar(
        r=[a_att, a_def, (a_att+a_def)/2],
        theta=['الهجوم', 'الدفاع', 'التوازن'],
        fill='toself', name=away_t, line_color='#FFFFFF'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10], color="#D4AF37")),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#D4AF37", size=14)
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# --- سجل العمليات ---
st.subheader("📋 سجل العمليات التاريخي")
if st.session_state.history_log:
    st.table(pd.DataFrame(st.session_state.history_log))
    if st.button("🗑️ تفريغ السجل"):
        st.session_state.history_log = []
        st.rerun()
else:
    st.info("السجل فارغ حالياً.. ابدأ أول محاكاة.")
    
