import streamlit as st
import numpy as np
import requests
import time
from datetime import datetime

# --- 🛰️ النواة المركزية المركزية ---
st.set_page_config(page_title="ARABIC PRO | النظام الشامل", layout="wide", initial_sidebar_state="collapsed")

# مفتاح الـ API (للمحافظة على خيار الربط الآلي)
API_KEY = "8abdb813dece636993e2182de4ee374a"
HEADERS = {'x-apisports-key': API_KEY}

# --- 🎨 CSS التصميم الإمبراطوري المتكامل (الذهب والزجاج) ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .main-header { text-align: center; padding: 25px; border-bottom: 2px solid #D4AF37; background: rgba(212,175,55,0.02); margin-bottom: 20px; }
    .glass-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(212,175,55,0.3); border-radius: 25px; padding: 30px; text-align: center; box-shadow: 0 15px 35px rgba(0,0,0,0.5); }
    .score-quantum { font-size: 5.5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; line-height: 1; margin: 15px 0; }
    .stat-node { background: #0a0a0a; border: 1px solid #D4AF37; border-radius: 15px; padding: 12px; margin: 5px; flex: 1; min-width: 100px; }
    .stat-node p { font-size: 0.8rem; color: #888; margin: 0; }
    .stat-node h3 { font-size: 1.2rem; color: #fff; margin: 5px 0 0 0; }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #8A6D3B) !important; color: #000 !important; font-weight: 900 !important; border-radius: 15px !important; padding: 15px !important; width: 100% !important; font-size: 1.3rem !important; border: none !important; box-shadow: 0 8px 20px rgba(212,175,55,0.3) !important; }
    input { background: #0a0a0a !important; border: 1px solid #D4AF37 !important; color: #fff !important; font-size: 1.1rem !important; border-radius: 10px !important; text-align: center !important; }
    label { color: #D4AF37 !important; font-weight: bold !important; font-size: 0.9rem !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-header'><h1>ARABIC PRO 🏆</h1><p style='color:#666;'>نظام المحاكاة الشمولية العظمى - إصدار 2026</p></div>", unsafe_allow_html=True)

# --- 🛠️ نظام الإدخال المزدوج (آلي + يدوي) ---
leagues = {"🌍 إدخال يدوي (شامل)": 0, "🇬🇧 الدوري الإنجليزي": 39, "🇪🇸 الدوري الإسباني": 140, "🇹🇳 الدوري التونسي": 202, "🇪🇬 الدوري المصري": 233}
sel_league = st.selectbox("🎯 اختر وضع الرصد أو البطولة:", list(leagues.keys()))

matches = None
if leagues[sel_league] != 0:
    try:
        url = f"https://api-sports.io{leagues[sel_league]}&season=2025&next=10"
        res = requests.get(url, headers=HEADERS, timeout=5).json()
        matches = res.get('response', [])
    except: st.warning("📡 تعذر جلب البيانات الآلية حالياً. تم التحويل للوضع اليدوي.")

# --- واجهة موازين القوى (الشمولية المطلقة) ---
c1, c2 = st.columns(2)
with c1:
    h_name = st.text_input("🏟️ اسم المضيف:", "الترجي") if not matches else st.selectbox("اختر المضيف:", [m['teams']['home']['name'] for m in matches])
    h_pwr = st.number_input("قوة الهجوم (1-10):", 1.0, 10.0, 8.2, key="h_pwr")
    h_def = st.number_input("صلابة الدفاع (1-10):", 1.0, 10.0, 8.0, key="h_def")

with c2:
    a_name = st.text_input("✈️ اسم الضيف:", "الأهلي") if not matches else st.selectbox("اختر الضيف:", [m['teams']['away']['name'] for m in matches])
    a_pwr = st.number_input("قوة الهجوم (1-10) :", 1.0, 10.0, 7.5, key="a_pwr")
    a_def = st.number_input("صلابة الدفاع (1-10) :", 1.0, 10.0, 8.5, key="a_def")

# --- محرك المحاكاة المليونية ---
if st.button("🔱 إطـلاق المحاكاة الشمولية العميقة"):
    with st.spinner('⏳ جاري تحليل موازين القوى...'):
        time.sleep(2)
        # معادلة المحاكاة (الهجوم ضد الدفاع)
        h_idx = max(0.2, (h_pwr * (11 - a_def)) / 25)
        a_idx = max(0.2, (a_pwr * (11 - h_def)) / 25)
        
        h_sim = np.random.poisson(h_idx, 1000000)
        a_sim = np.random.poisson(a_idx, 1000000)
        
        score_h, score_a = int(np.round(np.mean(h_sim))), int(np.round(np.mean(a_sim)))
        win_h = (h_sim > a_sim).mean() * 100
        draw = (h_sim == a_sim).mean() * 100
        win_a = (h_sim < a_sim).mean() * 100
        btts = ((h_sim > 0) & (a_sim > 0)).mean() * 100

        st.markdown(f"""
            <div class='glass-card'>
                <p style='color: #888; font-size: 0.9rem; margin:0;'>النتيجة المتوقعة النهائية</p>
                <div class='score-quantum'>{score_h} - {score_a}</div>
                <h2 style='color: white; font-size: 1.8rem;'>{h_name} <span style='color:#D4AF37;'>❌</span> {a_name}</h2>
                <hr style='border: 1px solid rgba(212,175,55,0.1); margin: 20px 0;'>
                <div style='display: flex; justify-content: space-around; flex-wrap: wrap;'>
                    <div class='stat-node'><p>فوز {h_name}</p><h3>{win_h:.1f}%</h3></div>
                    <div class='stat-node'><p>احتمال التعادل</p><h3>{draw:.1f}%</h3></div>
                    <div class='stat-node'><p>فوز {a_name}</p><h3>{win_a:.1f}%</h3></div>
                </div>
                <div style='display: flex; justify-content: space-around; flex-wrap: wrap; margin-top:15px;'>
                    <div class='stat-node'><p>كلاهما يسجل</p><h3>{btts:.1f}%</h3></div>
                    <div class='stat-node'><p>الركنيات</p><h3>{int((h_idx+a_idx)*4)}</h3></div>
                    <div class='stat-node'><p>البطاقات</p><h3>{int((h_def+a_def)*0.2)}</h3></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.markdown("<p style='text-align: center; color: #333; margin-top: 50px; font-size: 0.8rem;'>ARABIC PRO | SUPREME JOINT PROJECT v29.0</p>", unsafe_allow_html=True)
        
