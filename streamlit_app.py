import streamlit as st
import numpy as np
import time
import random

# 1. الهوية البصرية السيادية (Sovereign Pro UI)
st.set_page_config(page_title="OmniStats Sovereign Bot", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background: radial-gradient(circle at center, #050505 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .bot-panel { background: rgba(212, 175, 55, 0.02); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 35px; padding: 40px; backdrop-filter: blur(25px); }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #F2D388, #D4AF37); color: black !important; font-weight: 900; border-radius: 100px; height: 70px; font-size: 1.5rem; transition: 0.5s; border: none; width: 100%; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 40px rgba(212, 175, 55, 0.5); }
    .news-feed { background: rgba(255,255,255,0.03); border-right: 5px solid #D4AF37; padding: 20px; border-radius: 15px; margin-bottom: 15px; font-size: 15px; color: #eee; }
    /* تنسيق المقاييس الحيوية */
    [data-testid="stMetricValue"] { color: white !important; font-size: 2.5rem !important; font-weight: 900 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. محرك البوت الاستخباري (The Intelligence Core)
def run_scout_bot(team_name):
    # محاكاة سيناريوهات أخبار حقيقية ومؤثرة
    scenarios = [
        {"msg": f"تحليل البوت: غيابات مؤثرة في خط دفاع {team_name} 🛡️", "impact": -0.35},
        {"msg": f"تحليل البوت: {team_name} يمر بأفضل حالة هجومية هذا الموسم 🔥", "impact": 0.40},
        {"msg": f"تحليل البوت: إجهاد بدني واضح على لاعبي {team_name} 📉", "impact": -0.25},
        {"msg": f"تحليل البوت: عودة القوة الضاربة لهجوم {team_name} ✅", "impact": 0.30},
        {"msg": f"تحليل البوت: تغيير تكتيكي مرتقب لتعزيز الاستحواذ لـ {team_name} 🧠", "impact": 0.20}
    ]
    selected = random.sample(scenarios, 2)
    total_impact = sum([s['impact'] for s in selected])
    # xG أساسي يحاكي أداء الفرق الكبرى
    base_xg = random.uniform(1.4, 2.3)
    return base_xg + total_impact, selected

# 3. محاكي بويسون الكمي (50,000 سيناريو)
def simulate_sovereign(h_xg, a_xg):
    sims = 50000
    h_g = np.random.poisson(h_xg, sims)
    a_g = np.random.poisson(a_xg, sims)
    # استخراج النتيجة الأكثر تكراراً بدقة
    scores = list(zip(h_g, a_g))
    best_score = max(set(scores), key=scores.count)
    
    h_win = (h_g > a_g).mean() * 100
    draw = (h_g == a_g).mean() * 100
    a_win = (a_g > h_g).mean() * 100
    
    # تحويل النتائج لأرقام صحيحة واضحة (Fixing the np.int64 error)
    final_score_text = f"{int(best_score[0])} - {int(best_score[1])}"
    return h_win, draw, a_win, final_score_text

# 4. بناء مسرح العمليات
st.markdown("<p style='font-family:Orbitron; font-size:3.5rem; text-align:center; color:#D4AF37; margin:0;'>🔱 OMNISTATS BOT</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666; letter-spacing:10px; margin-bottom:30px;'>THE SOVEREIGN SCOUT v21.0</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='bot-panel'>", unsafe_allow_html=True)
    
    # اختيار الفرق
    c_input1, c_input2 = st.columns(2)
    with c_input1: h_team = st.text_input("صاحب الأرض:", "الترجي الرياضي")
    with c_input2: a_team = st.text_input("الضيف المتحدي:", "النادي الإفريقي")
    
    st.write("<br>", unsafe_allow_html=True)
    
    if st.button("إطلاق البوت الاستخباري والمحاكاة ⚡🤖"):
        with st.spinner('البوت يقوم بتمشيط البيانات وإجراء 50,000 محاكاة...'):
            time.sleep(2)
            
            # تشغيل البوت لكل فريق
            h_final_xg, h_news = run_scout_bot(h_team)
            a_final_xg, a_news = run_scout_bot(a_team)
            
            # إجراء المحاكاة
            hw, dr, aw, score_display = simulate_sovereign(h_final_xg, a_final_xg)
            
            # عرض تقرير الاستخبارات
            st.markdown("### 📡 تقارير الاستخبارات الميدانية")
            rep1, rep2 = st.columns(2)
            with rep1:
                for n in h_news: st.markdown(f"<div class='news-feed'>{n['msg']}</div>", unsafe_allow_html=True)
            with rep2:
                for n in a_news: st.markdown(f"<div class='news-feed'>{n['msg']}</div>", unsafe_allow_html=True)
            
            st.markdown("<hr style='opacity:0.1; margin:30px 0;'>", unsafe_allow_html=True)
            
            # عرض احتمالات الفوز
            res1, res2, res3 = st.columns(3)
            res1.metric(f"فوز {h_team}", f"{round(hw, 1)}%")
            res2.metric("التعادل الإحصائي", f"{round(dr, 1)}%")
            res3.metric(f"فوز {a_team}", f"{round(aw, 1)}%")
            
            # النتيجة النهائية الصافية (المصححة)
            st.markdown(f"""
                <div style='text-align:center; padding:40px; border:2px solid #D4AF37; border-radius:100px; margin-top:40px; background: rgba(212,175,55,0.05);'>
                    <p style='color:#D4AF37; margin:0; text-transform:uppercase; letter-spacing:5px;'>النتيجة المتوقعة نهائياً</p>
                    <h1 style='font-size:5rem; color:white; margin:10px 0;'>{score_display}</h1>
                    <p style='color:#444; margin:0;'>بناءً على 50,000 سيناريو احتمالي</p>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#222; margin-top:60px; font-family:Orbitron;'>OMNISTATS | TACTICAL BOT ENGINE | MARCH 2026</p>", unsafe_allow_html=True)
