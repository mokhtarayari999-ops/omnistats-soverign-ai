import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AURASTATS EMPIRE: THE ABSOLUTE FIX v135.0 ---
st.set_page_config(page_title="AuraStats Empire", layout="wide", page_icon="🔱")

# 👇 ضع مفتاحك من موقع football-data.org هنا
API_KEY = "757497fe293f4e39a291cc5c575c6dc3" 

def fetch_empire_data(league_code):
    headers = { 'X-Auth-Token': API_KEY }
    
    # 🛠️ الإصلاح الجوهري: إضافة "/" قبل معرف الدوري لضمان عدم الالتصاق
    url = f"https://football-data.org{league_code}/matches"
    
    try:
        # طلب المباريات المجدولة القادمة
        params = {'status': 'SCHEDULED'}
        response = requests.get(url, headers=headers, params=params, timeout=15)
        
        if response.status_code == 200:
            return response.json().get('matches', [])
        elif response.status_code == 403:
            st.error("❌ عذراً القائد مختار: هذا الدوري غير متاح في خطتك المجانية.")
            return None
        elif response.status_code == 429:
            st.warning("⚠️ السيرفر يطلب الهدوء! انتظر دقيقة وأعد المحاولة.")
            return None
        else:
            st.error(f"❌ تنبيه من السيرفر: كود {response.status_code}")
            return None
    except Exception as e:
        st.error(f"❌ فشل الاتصال التقني: تأكد من صحة الرابط.")
        return None

# --- تصميم واجهة الإمبراطور مختار ---
st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS EMPIRE 🏆</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#888;'>مركز التحكم السيادي | القائد مختار</p>", unsafe_allow_html=True)

# معرفات الدوريات المتاحة في خطة Football-data.org المجانية
leagues = {
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي": "PL",
    "🇪🇸 الدوري الإسباني": "PD",
    "🇩🇪 الدوري الألماني": "BL1",
    "🇮🇹 الدوري الإيطالي": "SA",
    "🇫🇷 الدوري الفرنسي": "FL1",
    "🇪🇺 دوري أبطال أوروبا": "CL"
}

sel_league = st.selectbox("🎯 اختر البطولة المراد تحليلها:", list(leagues.keys()))

if st.button("📡 فرض الاتصال وجلب المباريات الحية"):
    with st.spinner('🎯 جاري تنظيف الرابط وفك التشفير...'):
        time.sleep(1)
        matches = fetch_empire_data(leagues[sel_league])
        
        if matches:
            st.success(f"✅ نجح الاختراق! تم رصد {len(matches)} مباريات عالمية.")
            for m in matches:
                h_name = m['homeTeam']['name']
                a_name = m['awayTeam']['name']
                match_time = m['utcDate'].replace("T", " ").replace("Z", "")
                
                with st.expander(f"🏟️ {h_name} vs {a_name} | 🕒 {match_time}"):
                    # محرك المحاكاة السيادي
                    col1, col2 = st.columns(2)
                    h_xg = col1.slider(f"قوة {h_name}:", 0.5, 4.5, 2.0, key=f"h_{m['id']}")
                    a_xg = col2.slider(f"قوة {a_name}:", 0.5, 4.5, 1.5, key=f"a_{m['id']}")
                    
                    if st.button(f"🚀 إطلاق المحاكاة لـ {h_name}", key=f"btn_{m['id']}"):
                        h_sim = np.random.poisson(h_xg, 100000)
                        a_sim = np.random.poisson(a_xg, 100000)
                        res_h, res_a = int(np.mean(h_sim)), int(np.mean(a_sim))
                        
                        st.markdown(f"<div style='text-align:center; border:2px solid #D4AF37; padding:15px; border-radius:30px; background:#111;'><h1 style='color:#D4AF37;'>{res_h} - {res_a}</h1><p style='color:white;'>النتيجة المتوقعة</p></div>", unsafe_allow_html=True)
                        st.balloons()
