import streamlit as st
import numpy as np
import requests

# --- 🔱 AURASTATS EMPIRE: THE FINAL KEY v95.0 ---
st.set_page_config(page_title="AuraStats Empire", layout="wide")

# 👇 ضع مفتاحك هنا (تأكد من وجود العلامات " " حوله)
API_KEY = "8abdb813dece636993e2182de4ee374a" 

def force_get_data(league_id):
    headers = {
        'x-apisports-key': API_KEY,
        'Content-Type': 'application/json'
    }
    # 🛠️ الإصلاح الجوهري: فصل الرابط عن المتغيرات تماماً
    url = "https://api-sports.io"
    query_params = {
        'league': league_id,
        'season': 2025,
        'next': 10
    }
    
    try:
        # إرسال الطلب مع params لضمان عدم التصاق الروابط
        response = requests.get(url, headers=headers, params=query_params, timeout=15)
        res_json = response.json()
        
        if res_json.get('errors'):
            st.error(f"❌ تنبيه من السيرفر: {res_json['errors']}")
            return None
            
        return res_json.get('response', [])
    except Exception as e:
        st.error(f"❌ حدث خطأ غير متوقع: {e}")
        return None

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS EMPIRE 🏆</h1>", unsafe_allow_html=True)

leagues = {
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي": 39,
    "🇪🇸 الدوري الإسباني": 140,
    "🇹🇳 الدوري التونسي": 202,
    "🇸🇦 دوري روشن": 307
}

sel_league = st.selectbox("🎯 اختر الدوري المراد اختراقه:", list(leagues.keys()))

if st.button("📡 فرض الاتصال وجلب البيانات الحية"):
    with st.spinner('🎯 جاري تنظيف الرابط وفك التشفير...'):
        matches = force_get_data(leagues[sel_league])
        if matches:
            st.success(f"✅ نجح الاختراق! تم العثور على {len(matches)} مباريات.")
            for m in matches:
                st.info(f"🏟️ {m['teams']['home']['name']} vs {m['teams']['away']['name']}")
