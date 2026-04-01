import streamlit as st
import numpy as np
import requests
import json

# --- 🔱 ARABIC PRO: THE UNBREAKABLE BYPASS ---
st.set_page_config(page_title="Arabic Pro", layout="wide")

# تأكد من أن مفتاحك فعال
API_KEY = "afc8d6974db7dfcf37770c1b5791b65d"

def fetch_impossible(league_id):
    # استخدام بروكسي وسيط لكسر حظر المنصة
    target = f"https://api-sports.io{league_id}&season=2025&next=10"
    proxy_url = f"https://allorigins.win{requests.utils.quote(target)}"
    
    try:
        # إرسال الطلب عبر النفق الوسيط
        res = requests.get(proxy_url, timeout=15).json()
        # فك تغليف البيانات المستلمة من البروكسي
        actual_data = json.loads(res['contents'])
        return actual_data.get('response', [])
    except:
        return None

# --- واجهة 2026 الفاخرة ---
st.markdown("<h1 style='text-align:center; color:#D4AF37;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)

leagues = {"🇬🇧 الدوري الإنجليزي": 39, "🇪🇸 الدوري الإسباني": 140, "🇹🇳 الدوري التونسي": 202}
sel_league = st.selectbox("🎯 اختر الساحة المستهدفة:", list(leagues.keys()))

# محاولة الربط "العابرة للحظر"
matches = fetch_impossible(leagues[sel_league])

st.markdown("<div style='border:2px solid #D4AF37; padding:20px; border-radius:20px; text-align:center;'>", unsafe_allow_html=True)

if matches:
    # في حال نجح البروكسي في كسر الحظر
    match_titles = {f"{m['teams']['home']['name']} 🆚 {m['teams']['away']['name']}": m for m in matches}
    sel_match = st.selectbox("✅ تم كسر الحظر! اختر المواجهة:", list(match_titles.keys()))
    h_name = match_titles[sel_match]['teams']['home']['name']
    a_name = match_titles[sel_match]['teams']['away']['name']
else:
    # استمرار وضع الحماية (المحاكاة الذكية)
    st.markdown("<p style='color:#D4AF37;'>⚠️ نظام حماية المنصة مستمر - تم تفعيل المعالج الذاتي</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    h_name = c1.text_input("المضيف:", "مانشستر سيتي")
    a_name = c2.text_input("الضيف:", "ريال مدريد")

if st.button("🔱 إطلاق المحاكاة"):
    h_res, a_res = np.random.poisson(2.1), np.random.poisson(1.3)
    st.markdown(f"<h1 style='font-size:5rem; color:#D4AF37;'>{h_res} - {a_res}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:white;'>{h_name} vs {a_name}</p>", unsafe_allow_html=True)
    st.balloons()

st.markdown("</div>", unsafe_allow_html=True)
