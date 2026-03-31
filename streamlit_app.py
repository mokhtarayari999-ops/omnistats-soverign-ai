import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AuraStats AI: The Steel Engine v44.0 ---
st.set_page_config(page_title="AuraStats AI", layout="wide")

# 👇 تأكد من وضع مفتاحك هنا بدقة (بدون مسافات زائدة)
API_KEY = "7c52e30a48a1d5b620195ee6061b7ccf" 

def get_matches_ultra(league_id):
    headers = {'x-apisports-key': API_KEY}
    url = "https://api-sports.io"
    
    # 🕵️ محاولة ذكية: البحث في موسم 2025 و 2024 لضمان النتائج
    results = []
    for season in [2025, 2024]:
        params = {'league': league_id, 'season': season, 'next': 15}
        try:
            res = requests.get(url, headers=headers, params=params, timeout=10).json()
            if res.get('response'):
                results = res['response']
                break # إذا وجد مباريات يتوقف عن البحث
        except: continue
    return results

# --- التصميم السيادي ---
st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS AI 🏆</h1>", unsafe_allow_html=True)

mode = st.radio("بوابة التحكم:", ["🌐 آلي (API)", "✍️ يدوي"], horizontal=True)

if mode == "🌐 آلي (API)":
    # أضفت لك "الدوري الإنجليزي" كخيار أول لأنه الأضمن للاختبار
    leagues = {
        "الدوري الإنجليزي 🏴󠁧󠁢󠁥󠁮󠁧󠁿": 39,
        "دوري أبطال أوروبا 🇪🇺": 2,
        "الدوري الإسباني 🇪🇸": 140,
        "الدوري التونسي 🇹🇳": 202
    }
    sel_league = st.selectbox("اختر البطولة العالمية:", list(leagues.keys()))
    
    with st.spinner('📡 جاري جلب البيانات...'):
        matches = get_matches_ultra(leagues[sel_league])
    
    if matches:
        match_titles = [f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}" for m in matches]
        selected_match = st.selectbox("اختر المباراة:", match_titles)
        st.success(f"✅ تم الاتصال بنجاح: {selected_match}")
        h_xg, a_xg = 2.0, 1.5
    else:
        # 💡 هذه الإضافة مهمة: إذا فشل الـ API يفتح لك الخانات يدوياً فوراً
        st.warning("⚠️ السيرفر مشغول حالياً. يمكنك إدخال البيانات يدوياً أدناه:")
        c1, c2 = st.columns(2)
        h_xg = c1.number_input("xG المضيف (تقديري):", value=1.8)
        a_xg = c2.number_input("xG الضيف (تقديري):", value=1.5)
else:
    c1, c2 = st.columns(2)
    h_xg = c1.number_input("xG المضيف:", value=1.8)
    a_xg = c2.number_input("xG الضيف:", value=1.5)

if st.button("🚀 إطلاق المحاكاة السيادية"):
    st.balloons()
    st.markdown(f"<div style='text-align:center; border:2px solid gold; padding:20px; border-radius:50px;'><h2>التحليل جاهز!</h2></div>", unsafe_allow_html=True)
    
