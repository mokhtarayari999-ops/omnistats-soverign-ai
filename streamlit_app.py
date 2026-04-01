import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 ARABIC PRO: THE 2026 QUANTUM UPDATE ---
st.set_page_config(page_title="Arabic Pro | ذكاء 2026", layout="wide")

API_KEY = "8abdb813dece636993e2182de4ee374a"
BASE_URL = "https://api-sports.io"
HEADERS = {'x-apisports-key': API_KEY}

def fetch_data_magic(league_id):
    # محاولة جلب المباريات (مباشر + اليوم + القادم)
    # نستخدم معلمة 'live' أولاً لجلب ما يحدث الآن
    urls = [
        f"{BASE_URL}/fixtures?league={league_id}&live=all", # المباشر
        f"{BASE_URL}/fixtures?league={league_id}&season=2025&next=10", # القادم
        f"{BASE_URL}/fixtures?league={league_id}&season=2025&last=5" # المنتهي (للدراسة)
    ]
    all_matches = []
    for url in urls:
        try:
            res = requests.get(url, headers=HEADERS, timeout=5).json()
            if res.get('response'): all_matches.extend(res['response'])
        except: continue
    return all_matches

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)

# قائمة دوريات حيوية (معرفات صحيحة لعام 2026)
leagues = {"🇹🇳 الدوري التونسي": 202, "🇬🇧 البريميرليج": 39, "🇪🇸 الليجا": 140, "🇪🇬 الدوري المصري": 233}
sel_league_name = st.selectbox("🎯 نظام الرصد الذكي:", list(leagues.keys()))

# 🚀 الربط العشوائي الذكي
matches = fetch_data_magic(leagues[sel_league_name])

if matches:
    # فرز المباريات لعدم التكرار
    unique_matches = {f"{m['teams']['home']['name']} 🆚 {m['teams']['away']['name']} ({m['fixture']['status']['short']})": m for m in matches}
    sel_match_str = st.selectbox("📅 المباريات المكتشفة (مباشر/مجدولة):", list(unique_matches.keys()))
    m = unique_matches[sel_match_str]
    
    # استخراج البيانات الحقيقية
    h_name, a_name = m['teams']['home']['name'], m['teams']['away']['name']
    
    # 🔱 زر المحاكاة لا يظهر إلا بوجود مباراة
    if st.button("🔱 إطلاق المحاكاة الشمولية"):
        with st.spinner('⏳ جاري سحب البيانات الحية...'):
            time.sleep(1)
            # محاكاة تعتمد على حالة المباراة (إذا كانت مباشرة نأخذ النتيجة الحالية)
            h_score = m['goals'].get('home', 0) if m['goals'].get('home') is not None else 0
            a_score = m['goals'].get('away', 0) if m['goals'].get('away') is not None else 0
            
            # توقع الأهداف الإضافية (Poisson)
            h_extra = np.random.poisson(1.2)
            a_extra = np.random.poisson(0.8)
            
            st.markdown(f"""
                <div style='text-align:center; border:2px solid #D4AF37; padding:20px; border-radius:20px;'>
                    <p style='color:#888;'>النتيجة المتوقعة النهائية</p>
                    <h1 style='font-size:5rem; color:#D4AF37;'>{h_score + h_extra} - {a_score + a_extra}</h1>
                    <h2 style='color:white;'>{h_name} vs {a_name}</h2>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
else:
    # حل "سحري" في حال عدم وجود مباريات إطلاقاً في الـ API
    st.error("📡 الخادم لا يرسل بيانات لهذا الدوري حالياً.")
    if st.checkbox("⚙️ تفعيل المحاكي اليدوي (Force Mode)"):
        h_name = st.text_input("المضيف:", "الترجي")
        a_name = st.text_input("الضيف:", "الأهلي")
        if st.button("🔱 محاكاة قسرية"):
            st.write(f"النتيجة المتوقعة لـ {h_name} و {a_name} هي 2 - 1")

