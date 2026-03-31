import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AURASTATS EMPIRE: THE FINAL WIPE v240.0 ---
st.set_page_config(page_title="AuraStats Empire", layout="wide", page_icon="🔱")

# 👇 ضع مفتاحك من موقع football-data.org هنا بدقة
API_KEY = "757497fe293f4e39a291cc5c575c6dc3" 

def fetch_empire_data_ultimate(league_code):
    headers = { 'X-Auth-Token': API_KEY }
    
    # 🛠️ الإصلاح الجوهري: استخدام روابط كاملة وثابتة تماماً لمنع أي تداخل
    league_urls = {
        "PL": "https://football-data.org",
        "PD": "https://football-data.org",
        "BL1": "https://football-data.org",
        "SA": "https://football-data.org",
        "FL1": "https://football-data.org",
        "CL": "https://football-data.org"
    }
    
    url = league_urls.get(league_code)
    
    try:
        # طلب المباريات القادمة (Scheduled)
        params = {'status': 'SCHEDULED'}
        response = requests.get(url, headers=headers, params=params, timeout=15, verify=False)
        
        if response.status_code == 200:
            return response.json().get('matches', [])
        elif response.status_code == 429:
            st.warning("⚠️ السيرفر مضغوط! انتظر دقيقة واحدة وأعد المحاولة.")
            return None
        else:
            # رسالة خطأ واضحة لمساعدة القائد مختار في التشخيص
            st.error(f"❌ تنبيه من السيرفر العالمي: كود {response.status_code}")
            return None
    except Exception as e:
        st.error(f"❌ فشل الاتصال: تأكد من تشغيل الإنترنت ومسح ذاكرة التطبيق.")
        return None

# --- واجهة القائد مختار ---
st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS EMPIRE 🏆</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#888;'>مركز التحكم السيادي | النسخة v240.0</p>", unsafe_allow_html=True)

leagues = {
    "🇪🇸 الدوري الإسباني": "PD",
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي": "PL",
    "🇩🇪 الدوري الألماني": "BL1",
    "🇮🇹 الدوري الإيطالي": "SA",
    "🇫🇷 الدوري الفرنسي": "FL1",
    "🇪🇺 دوري أبطال أوروبا": "CL"
}

sel_league = st.selectbox("🎯 اختر المسرح القتالي:", list(leagues.keys()))

if st.button("📡 فرض الاتصال السيادي المباشر"):
    # 🧹 تنظيف الذاكرة المؤقتة لضمان قراءة الكود الجديد
    st.cache_data.clear()
    with st.spinner('🎯 جاري فرض السيادة الرقمية على السيرفر...'):
        time.sleep(1)
        matches = fetch_empire_data_ultimate(leagues[sel_league])
        
        if matches:
            st.success(f"✅ نجح الاختراق! تم رصد {len(matches)} مباريات عالمية.")
            for m in matches:
                h_name = m['homeTeam']['name']
                a_name = m['awayTeam']['name']
                match_time = m['utcDate'].replace("T", " ").replace("Z", "")
                
                with st.expander(f"🏟️ {h_name} vs {a_name} | 🕒 {match_time}"):
                    col1, col2 = st.columns(2)
                    h_xg = col1.slider(f"قوة {h_name}:", 0.5, 4.5, 2.0, key=f"h_{m['id']}")
                    a_xg = col2.slider(f"قوة {a_name}:", 0.5, 4.5, 1.5, key=f"a_{m['id']}")
                    
                    if st.button(f"🚀 إطلاق المحاكاة لـ {h_name}", key=f"btn_{m['id']}"):
                        h_sim = np.random.poisson(h_xg, 100000)
                        a_sim = np.random.poisson(a_xg, 100000)
                        st.markdown(f"<h1 style='text-align:center; color:#D4AF37;'>{int(np.mean(h_sim))} - {int(np.mean(a_sim))}</h1>", unsafe_allow_html=True)
                        st.balloons()
        
