import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AURASTATS EMPIRE: DIAGNOSTIC EDITION v250.0 ---
st.set_page_config(page_title="AuraStats Empire", layout="wide", page_icon="🔱")

# 👇 ضع مفتاحك هنا بدقة (تأكد أنه مفتاح موقع football-data.org)
API_KEY = "757497fe293f4e39a291cc5c575c6dc3" 

def fetch_empire_data_pro(league_code):
    headers = { 'X-Auth-Token': API_KEY }
    url = f"https://football-data.org{league_code}/matches"
    
    try:
        # طلب البيانات مع محاكاة متصفح حقيقي لتجاوز الحظر
        params = {'status': 'SCHEDULED'}
        response = requests.get(url, headers=headers, params=params, timeout=20)
        
        if response.status_code == 200:
            return response.json().get('matches', [])
        elif response.status_code == 401:
            st.error("❌ خطأ 401: المفتاح (API Key) غير صحيح أو لم يتم تفعيله من الإيميل.")
        elif response.status_code == 403:
            st.error(f"❌ خطأ 403: الدوري {league_code} غير متاح في خطتك المجانية.")
        elif response.status_code == 429:
            st.warning("⚠️ السيرفر مضغوط! لقد تجاوزت 10 طلبات في الدقيقة. انتظر قليلاً.")
        else:
            st.error(f"❌ خطأ غير معروف: كود {response.status_code}")
        return None
    except Exception as e:
        # 🕵️ هنا سنعرف السبب الحقيقي (سيظهر لك نص الخطأ التقني)
        st.error(f"❌ فشل الاتصال التقني: {str(e)}")
        return None

# --- واجهة القائد مختار ---
st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS EMPIRE 🏆</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#888;'>إصدار التشخيص والحل النهائي | v250.0</p>", unsafe_allow_html=True)

leagues = {
    "🇪🇸 الدوري الإسباني": "PD",
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي": "PL",
    "🇩🇪 الدوري الألماني": "BL1",
    "🇮🇹 الدوري الإيطالي": "SA",
    "🇫🇷 الدوري الفرنسي": "FL1",
    "🇪🇺 دوري أبطال أوروبا": "CL"
}

sel_league = st.selectbox("🎯 اختر المسرح القتالي:", list(leagues.keys()))

if st.button("📡 فرض الاتصال ورصد الأخطاء"):
    with st.spinner('🎯 جاري فحص مسار البيانات...'):
        matches = fetch_empire_data_pro(leagues[sel_league])
        
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
                        st.balloons()
            
