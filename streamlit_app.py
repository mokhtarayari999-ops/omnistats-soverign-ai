import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AURASTATS EMPIRE: ABSOLUTE MASTERY v100.0 ---
st.set_page_config(page_title="AuraStats Empire", layout="wide")

# 👇 ضع مفتاحك هنا (تأكد من نسخه بدقة وبدون مسافات)
API_KEY = "8abdb813dece636993e2182de4ee374a" 

def fetch_live_empire(league_id):
    # 🕵️ محاكاة هوية متصفح حقيقي لتجاوز الحظر
    headers = {
        'x-apisports-key': API_KEY,
        'x-rapidapi-host': "v3.football.api-sports.io",
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
    }
    url = "https://api-sports.io"
    
    # طلب مباريات موسم 2025/2026 الحالية
    params = {'league': league_id, 'season': 2025, 'next': 12}
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        # التأكد من نجاح الطلب قبل فك التشفير
        if response.status_code == 200:
            res_json = response.json()
            if res_json.get('response'):
                return res_json['response']
            elif res_json.get('errors'):
                st.error(f"❌ تنبيه من السيرفر: {res_json['errors']}")
        else:
            st.error(f"❌ السيرفر رد بكود: {response.status_code}")
        return None
    except Exception as e:
        st.error(f"❌ حدث خطأ تقني: {e}")
        return None

# --- تصميم الواجهة الفخمة ---
st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS EMPIRE 🏆</h1>", unsafe_allow_html=True)

leagues = {
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي": 39,
    "🇪🇸 الدوري الإسباني": 140,
    "🇹🇳 الدوري التونسي": 202,
    "🇪🇺 أبطال أوروبا": 2
}

sel_league = st.selectbox("🎯 اختر المسرح القتالي:", list(leagues.keys()))

if st.button("📡 فرض الاتصال وجلب البيانات الحية"):
    with st.spinner('🎯 جاري فك التشفير والعبور من الحماية...'):
        matches = fetch_live_empire(leagues[sel_league])
        
        if matches:
            st.success(f"✅ نجح الاختراق! وجدنا {len(matches)} مباريات.")
            for m in matches:
                h_name = m['teams']['home']['name']
                a_name = m['teams']['away']['name']
                
                with st.expander(f"🏟️ {h_name} vs {a_name}"):
                    # محرك المحاكاة الحصري
                    h_xg = st.slider(f"قوة {h_name}:", 0.5, 4.0, 2.1, key=f"h_{h_name}")
                    a_xg = st.slider(f"قوة {a_name}:", 0.5, 4.0, 1.4, key=f"a_{a_name}")
                    
                    if st.button(f"🚀 تحليل {h_name} ضد {a_name}", key=f"btn_{h_name}"):
                        h_sim = np.random.poisson(h_xg, 100000)
                        a_sim = np.random.poisson(a_xg, 100000)
                        st.markdown(f"<div style='text-align:center; border:2px solid gold; padding:20px; border-radius:40px; background:#111;'><h1>{int(np.mean(h_sim))} - {int(np.mean(a_sim))}</h1></div>", unsafe_allow_html=True)
                        st.balloons()
    
