import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AURASTATS EMPIRE: THE FINAL BREACH v180.0 ---
st.set_page_config(page_title="AuraStats Empire", layout="wide")

# 👇 ضع مفتاحك هنا (تأكد أنه من football-data.org)
API_KEY = "757497fe293f4e39a291cc5c575c6dc3" 

def fetch_empire_data_absolute(league_code):
    # 🕵️ التكتيك الجديد: استخدام هيدرز "نظيفة" جداً وتجنب الـ Params المعقدة
    headers = { 
        'X-Auth-Token': API_KEY,
        'Accept': 'application/json'
    }
    
    # الروابط المباشرة والنهائية (بدون أي دمج متغيرات)
    url = f"https://football-data.org{league_code}/matches?status=SCHEDULED"
    
    try:
        # فرض الطلب بدون فحص أمان (تجاوز الـ SSL) ومع مهلة طويلة
        response = requests.get(url, headers=headers, timeout=25, verify=False)
        
        # 🛠️ الفحص الجوهري: إذا لم يكن الرد JSON، سنعرف السبب فوراً
        if "application/json" in response.headers.get("Content-Type", ""):
            res_data = response.json()
            return res_data.get('matches', [])
        else:
            # إذا أرسل السيرفر صفحة خطأ نصية (وهو سبب المشكلة عندك)
            st.error("⚠️ السيرفر يحجب الطلب حالياً (حماية أمنية). جرب اختيار دوري آخر أو انتظر 5 دقائق.")
            return None
    except Exception as e:
        st.error(f"❌ خطأ في العبور: {e}")
        return None

# --- واجهة القائد مختار ---
st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS EMPIRE 🏆</h1>", unsafe_allow_html=True)

leagues = {
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي": "PL",
    "🇪🇸 الدوري الإسباني": "PD",
    "🇩🇪 الدوري الألماني": "BL1",
    "🇮🇹 الدوري الإيطالي": "SA",
    "🇪🇺 أبطال أوروبا": "CL"
}

sel_league = st.selectbox("🎯 اختر المسرح القتالي:", list(leagues.keys()))

if st.button("📡 فرض الاتصال السيادي المطلق"):
    with st.spinner('🎯 جاري كسر الحظر والعبور للسيرفر العالمي...'):
        matches = fetch_empire_data_absolute(leagues[sel_league])
        
        if matches:
            st.success(f"✅ نجح الاختراق! تم رصد {len(matches)} مباريات.")
            for m in matches:
                h_name, a_name = m['homeTeam']['name'], m['awayTeam']['name']
                with st.expander(f"🏟️ {h_name} vs {a_name}"):
                    h_xg = st.slider(f"قوة {h_name}:", 0.5, 4.5, 2.0, key=f"h_{m['id']}")
                    a_xg = st.slider(f"قوة {a_name}:", 0.5, 4.5, 1.5, key=f"a_{m['id']}")
                    if st.button(f"🚀 محاكاة {h_name}", key=f"btn_{m['id']}"):
                        h_sim = np.random.poisson(h_xg, 100000)
                        a_sim = np.random.poisson(a_xg, 100000)
                        st.markdown(f"<h1 style='text-align:center; color:#D4AF37;'>{int(np.mean(h_sim))} - {int(np.mean(a_sim))}</h1>", unsafe_allow_html=True)
