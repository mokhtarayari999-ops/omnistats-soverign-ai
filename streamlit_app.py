import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AURASTATS EMPIRE: THE LAST STAND v300.0 ---
st.set_page_config(page_title="AuraStats Empire", layout="wide")

# 👇 ضع مفتاحك الجديد (API Token) هنا - تأكد من تفعيله من الإيميل!
API_KEY = "757497fe293f4e39a291cc5c575c6dc3" 

def fetch_absolute_empire(league_code):
    # 🕵️ السر العظيم: محاكاة متصفح Chrome حقيقي لتجاوز أي حظر
    headers = { 
        'X-Auth-Token': API_KEY,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    url = f"https://football-data.org{league_code}/matches"
    
    try:
        # طلب المباريات المجدولة القادمة
        params = {'status': 'SCHEDULED'}
        response = requests.get(url, headers=headers, params=params, timeout=25)
        
        if response.status_code == 200:
            return response.json().get('matches', [])
        elif response.status_code == 429:
            st.warning("⚠️ السيرفر مضغوط! انتظر 60 ثانية بالضبط.")
            return None
        else:
            # تشخيص دقيق للخطأ
            st.error(f"❌ تنبيه السيرفر: كود {response.status_code}. (تأكد من تفعيل المفتاح)")
            return None
    except Exception as e:
        st.error(f"❌ فشل العبور التقني: {e}")
        return None

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS EMPIRE 🏆</h1>", unsafe_allow_html=True)

leagues = {
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي": "PL",
    "🇪🇸 الدوري الإسباني": "PD",
    "🇩🇪 الدوري الألماني": "BL1",
    "🇮🇹 الدوري الإيطالي": "SA",
    "🇫🇷 الدوري الفرنسي": "FL1",
    "🇪🇺 دوري أبطال أوروبا": "CL"
}

sel_league = st.selectbox("🎯 اختر المسرح القتالي:", list(leagues.keys()))

if st.button("📡 فرض الاتصال السيادي المطلق"):
    with st.spinner('🎯 جاري كسر الحواجز وجلب البيانات الحية...'):
        time.sleep(1)
        matches = fetch_absolute_empire(leagues[sel_league])
        
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
