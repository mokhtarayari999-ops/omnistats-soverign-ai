import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.stats import poisson
import time

# 1. إعدادات المنصة الاحترافية (Pro Analysis UI)
st.set_page_config(page_title="OmniStats Pro | Sovereign Intelligence", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    
    /* لوحة التحكم الاحترافية */
    .pro-panel {
        background: rgba(20, 20, 20, 0.9);
        border: 1px solid #D4AF37;
        border-radius: 15px;
        padding: 40px;
        box-shadow: 0 0 50px rgba(212, 175, 55, 0.1);
    }
    
    .glow-header { font-family: 'Orbitron', sans-serif; font-size: 2.8rem; text-align: center; color: #D4AF37; margin: 0; }
    
    /* زر التحليل العميق */
    .stButton>button {
        background: #D4AF37;
        color: #000 !important; font-weight: 900; border-radius: 5px;
        height: 70px; border: none; font-size: 1.5rem; transition: 0.3s;
        width: 100%; text-transform: uppercase;
    }
    .stButton>button:hover { background: #F2D388; box-shadow: 0 0 30px #D4AF37; }
    
    .input-box { background: #111; border-radius: 10px; padding: 20px; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

# 2. الخوارزمية السيادية (The Sovereign Mathematical Engine)
def calculate_probabilities(home_exp_goals, away_exp_goals):
    # مصفوفة احتمالات الأهداف (من 0 إلى 8 لكل فريق)
    home_probs = [poisson.pmf(i, home_exp_goals) for i in range(9)]
    away_probs = [poisson.pmf(i, away_exp_goals) for i in range(9)]
    
    # حساب مصفوفة الاحتمالات المتقاطعة
    m = np.outer(home_probs, away_probs)
    
    win_h = np.sum(np.tril(m, -1)) * 100
    draw = np.sum(np.diag(m)) * 100
    win_a = np.sum(np.triu(m, 1)) * 100
    
    # استخراج النتائج الـ 3 الأكثر احتمالية
    flat_m = m.flatten()
    top_3_indices = np.argsort(flat_m)[-3:][::-1]
    top_scores = []
    for idx in top_3_indices:
        h, a = divmod(idx, 9)
        top_scores.append((f"{h} - {a}", round(flat_m[idx] * 100, 1)))
        
    return win_h, draw, win_a, top_scores

# 3. واجهة المستخدم (The Pro Dashboard)
st.markdown("<p class='glow-header'>OMNISTATS PRO</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; letter-spacing:5px;'>ADVANCED ANALYTICS ENGINE</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='pro-panel'>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns(2, gap="large")
    
    with col_l:
        st.markdown("<div class='input-box'>", unsafe_allow_html=True)
        h_name = st.text_input("الفريق المضيف (HOME):", "النادي الإفريقي")
        h_att = st.number_input(f"قوة الهجوم لـ {h_name} (xG):", 0.1, 5.0, 1.8, step=0.1)
        h_def = st.number_input(f"صلابة الدفاع لـ {h_name} (0=ضعيف، 5=حديد):", 0.0, 5.0, 1.2, step=0.1)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_r:
        st.markdown("<div class='input-box'>", unsafe_allow_html=True)
        a_name = st.text_input("الفريق الضيف (AWAY):", "النادي البنزرتي")
        a_att = st.number_input(f"قوة الهجوم لـ {a_name} (xG):", 0.1, 5.0, 1.2, step=0.1)
        a_def = st.number_input(f"صلابة الدفاع لـ {a_name} (0=ضعيف، 5=حديد):", 0.0, 5.0, 1.5, step=0.1)
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)
    
    if st.button("تفعيل المحاكاة السيادية الاحترافية ⚡"):
        with st.spinner('جارِ تحليل المعطيات وحساب احتمالات بويسون...'):
            time.sleep(1.5)
            # تعديل معدل الأهداف بناءً على قوة دفاع الخصم
            h_final_xg = h_att * (1 - (a_def * 0.1))
            a_final_xg = a_att * (1 - (h_def * 0.1))
            
            wh, d, wa, scores = calculate_probabilities(h_final_xg, a_final_xg)
            
            # عرض النتائج الاستراتيجية
            st.markdown("<hr style='border-color:#333;'>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            c1.metric(f"فوز {h_name}", f"{round(wh, 1)}%")
            c2.metric("احتمال التعادل", f"{round(d, 1)}%")
            c3.metric(f"فوز {a_name}", f"{round(wa, 1)}%")
            
            st.markdown("### 🎯 النتائج الأكثر توقعاً (Exact Score)")
            s1, s2, s3 = st.columns(3)
            s1.info(f"النتيجة: **{scores[0][0]}** (احتمال: {scores[0][1]}%)")
            s2.info(f"النتيجة: **{scores[1][0]}** (احتمال: {scores[1][1]}%)")
            s3.info(f"النتيجة: **{scores[2][0]}** (احتمال: {scores[2][1]}%)")
            
            # مقارنة بصرية احترافية
            fig = go.Figure(data=[
                go.Bar(name=h_name, x=['الهجوم', 'الدفاع'], y=[h_att, h_def], marker_color='#D4AF37'),
                go.Bar(name=a_name, x=['الهجوم', 'الدفاع'], y=[a_att, a_def], marker_color='#fff')
            ])
            fig.update_layout(barmode='group', template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
            
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#222; margin-top:50px;'>OMNISTATS | PROFESSIONAL SOVEREIGN ENGINE | v18.0</p>", unsafe_allow_html=True)
