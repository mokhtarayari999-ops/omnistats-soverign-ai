import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AuraStats AI: The Speed Engine v46.0 ---
st.set_page_config(page_title="AuraStats AI", layout="wide")

API_KEY = "7c52e30a48a1d5b620195ee6061b7ccf"

def get_matches_fast(league_id):
    headers = {'x-apisports-key': API_KEY}
    url = "https://api-sports.io"
    params = {'league': league_id, 'season': 2025, 'next': 10}
    try:
        # وضعنا مهلة 5 ثوانٍ فقط لكي لا ننتظر طويلاً
        res = requests.get(url, headers=headers, params=params, timeout=5).json()
        return res.get('response', [])
    except: return []

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS AI 🏆</h1>", unsafe_allow_html=True)

mode = st.radio("بوابة التحكم:", ["🌐 آلي (API)", "✍️ يدوي"], horizontal=True)

if mode == "🌐 آلي (API)":
    leagues = {"الدوري الإنجليزي 🏴󠁧󠁢󠁥󠁮󠁧󠁿": 39, "دوري أبطال أوروبا 🇪🇺": 2, "الدوري التونسي 🇹🇳": 202}
    sel_league = st.selectbox("اختر البطولة:", list(leagues.keys()))
    
    # محاولة جلب البيانات
    matches = get_matches_fast(leagues[sel_league])
    
    if matches:
        match_titles = [f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}" for m in matches]
        selected_match = st.selectbox("اختر المباراة:", match_titles)
        h_name, a_name = selected_match.split(" vs ")
        h_xg, a_xg = 2.1, 1.4
        st.success(f"✅ تم سحب مباريات {sel_league}")
    else:
        # 💡 الحل الجذري: إذا فشل الـ API لا ننتظر، نفتح الإدخال فوراً!
        st.error("📡 السيرفر لم يستجب. أدخل بيانات المواجهة يدوياً أدناه:")
        c1, c2 = st.columns(2)
        h_name = c1.text_input("المضيف (تقديري):", "مانشستر سيتي")
        h_xg = c1.number_input("قوة المضيف (xG):", value=2.2)
        a_name = c2.text_input("الضيف (تقديري):", "أرسنال")
        a_xg = c2.number_input("قوة الضيف (xG):", value=1.9)
else:
    # الوضع اليدوي الكامل
    c1, c2 = st.columns(2)
    h_name = c1.text_input("الفريق المضيف:", "الترجي")
    h_xg = c1.number_input("xG المضيف:", value=1.8)
    a_name = c2.text_input("الضيف:", "الأهلي")
    a_xg = c2.number_input("xG الضيف:", value=1.5)

if st.button("🚀 إطلاق المحاكاة السيادية"):
    with st.spinner('AuraStats يحلل السيناريوهات...'):
        time.sleep(1)
        h_sim = np.random.poisson(h_xg, 100000)
        a_sim = np.random.poisson(a_xg, 100000)
        score_h, score_a = int(np.mean(h_sim)), int(np.mean(a_sim))
        
        st.markdown(f"""
            <div style='text-align:center; border:2px solid #D4AF37; border-radius:30px; padding:20px; background:rgba(212,175,55,0.05);'>
                <h1 style='color:white;'>{score_h} - {score_a}</h1>
                <p style='color:#D4AF37;'>نتيجة {h_name} ضد {a_name}</p>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
