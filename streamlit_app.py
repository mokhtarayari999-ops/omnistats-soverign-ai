import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AuraStats AI: The Sovereign Resurrection v45.0 ---
st.set_page_config(page_title="AuraStats AI", layout="wide")

# 👇 تأكد من وضع مفتاحك هنا بدقة
API_KEY = "7c52e30a48a1d5b620195ee6061b7ccf" 

def get_matches_final(league_id):
    headers = {'x-apisports-key': API_KEY}
    url = "https://api-sports.io"
    # جلب مباريات موسم 2025 (العام الحالي 2026)
    params = {'league': league_id, 'season': 2025, 'next': 10}
    try:
        res = requests.get(url, headers=headers, params=params, timeout=10).json()
        return res.get('response', [])
    except: return []

# التصميم الفخم
st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS AI 🏆</h1>", unsafe_allow_html=True)

mode = st.radio("بوابة التحكم:", ["🌐 آلي (API)", "✍️ يدوي"], horizontal=True)

with st.container():
    if mode == "🌐 آلي (API)":
        leagues = {"الدوري الإنجليزي 🏴󠁧󠁢󠁥󠁮󠁧󠁿": 39, "دوري أبطال أوروبا 🇪🇺": 2, "الدوري التونسي 🇹🇳": 202}
        sel_league = st.selectbox("اختر البطولة:", list(leagues.keys()))
        matches = get_matches_final(leagues[sel_league])
        
        if matches:
            match_titles = [f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}" for m in matches]
            selected_match = st.selectbox("اختر المباراة:", match_titles)
            h_name = selected_match.split(" vs ")[0]
            a_name = selected_match.split(" vs ")[1]
            h_xg, a_xg = 2.10, 1.45 # قيم افتراضية ذكية للـ API
            st.success(f"✅ تم الاتصال بـ {selected_match}")
        else:
            st.warning("📡 السيرفر يستعد.. جرب 'اليدوي' مؤقتاً أو انتظر دقيقة")
            h_name, a_name, h_xg, a_xg = "المضيف", "الضيف", 1.8, 1.5
    else:
        c1, c2 = st.columns(2)
        h_name = c1.text_input("الفريق المضيف:", "الترجي")
        h_xg = c1.number_input("xG المضيف:", value=1.8)
        a_name = c2.text_input("الضيف المتحدي:", "الأهلي")
        a_xg = c2.number_input("xG الضيف:", value=1.5)

    if st.button("🚀 إطلاق المحاكاة السيادية"):
        with st.spinner('AuraStats يحلل 100,000 احتمال...'):
            time.sleep(1.5)
            # محرك المحاكاة (بويسون)
            h_sim = np.random.poisson(h_xg, 100000)
            a_sim = np.random.poisson(a_xg, 100000)
            
            # حساب النتيجة الأكثر تكراراً
            res_list = list(zip(h_sim, a_sim))
            score = max(set(res_list), key=res_list.count)
            win_prob = (h_sim > a_sim).mean() * 100
            corners = int((h_xg + a_xg) * 3.2)

            # عرض النتائج بشكل "سيادي"
            st.markdown(f"""
                <div style='text-align:center; border:3px solid #D4AF37; border-radius:50px; padding:30px; background:rgba(212,175,55,0.05);'>
                    <h3 style='color:#D4AF37;'>النتيجة المتوقعة</h3>
                    <h1 style='font-size:5rem; color:white;'>{score[0]} - {score[1]}</h1>
                    <hr style='border:1px solid #D4AF37;'>
                    <div style='display:flex; justify-content:space-around; color:#D4AF37;'>
                        <div><b>🚩 ركنيات</b><br>{corners}</div>
                        <div><b>📊 فوز {h_name}</b><br>{win_prob:.1f}%</div>
                        <div><b>⚽ الهداف</b><br>مهاجم {h_name}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
