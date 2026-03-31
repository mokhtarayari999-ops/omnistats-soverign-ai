import streamlit as st
import numpy as np
import requests

# --- 🔱 AURASTATS EMPIRE: THE PENETRATOR v90.0 ---
st.set_page_config(page_title="AuraStats Empire", layout="wide")

# 👇 ضع مفتاحك هنا بدقة متناهية
API_KEY = "8abdb813dece636993e2182de4ee374a" 

def force_get_data(league_id):
    # التعديل الجوهري: إضافة الـ Host والـ User-Agent لخداع السيرفر والظهور كمتصفح حقيقي
    headers = {
        'x-apisports-key': API_KEY,
        'User-Agent': 'Mozilla/5.0'
    }
    # الرابط المباشر للنتائج المجدولة (Fixtures)
    url = f"https://api-sports.io{league_id}&season=2025&next=10"
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        res_json = response.json()
        
        # تشخيص الأخطاء الحقيقية القادمة من API-Football
        if res_json.get('errors'):
            error_msg = str(res_json['errors'])
            if "token" in error_msg.lower():
                st.error(f"❌ السيرفر يرفض المفتاح: المفتاح غير مفعل بعد (يحتاج ساعة للتفعيل) أو أنه خاطئ.")
            else:
                st.error(f"❌ خطأ من السيرفر: {error_msg}")
            return None
            
        return res_json.get('response', [])
    except Exception as e:
        st.error(f"❌ فشل الاتصال بالإنترنت أو بالسيرفر: {e}")
        return None

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS EMPIRE 🏆</h1>", unsafe_allow_html=True)

leagues = {"🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي": 39, "🇪🇸 الدوري الإسباني": 140, "🇹🇳 الدوري التونسي": 202}
sel_league = st.selectbox("🎯 اختر الدوري:", list(leagues.keys()))

if st.button("📡 فرض الاتصال وجلب البيانات الحية"):
    with st.spinner('🎯 جاري فك التشفير...'):
        matches = force_get_data(leagues[sel_league])
        if matches:
            st.success(f"✅ نجح الاختراق! وجدنا {len(matches)} مباريات.")
            for m in matches:
                st.write(f"🏟️ {m['teams']['home']['name']} vs {m['teams']['away']['name']}")
                
