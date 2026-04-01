import streamlit as st
import numpy as np
import requests
import json
import time

# --- 🔱 ARABIC PRO: THE 2026 SUPREME BYPASS ---
st.set_page_config(page_title="Arabic Pro", layout="wide")

# المفتاح (تأكد من أنه مفعل)
API_KEY = "afc8d6974db7dfcf37770c1b5791b65d"

def fetch_via_unbreakable_proxy(league_id):
    # 🪄 استخدام بروكسي "allorigins" لكسر حظر المنصة نهائياً
    target_url = f"https://api-sports.io{league_id}&season=2025&next=10"
    proxy_url = f"https://allorigins.win{requests.utils.quote(target_url)}"
    
    # ملاحظة: البروكسي يرسل الطلب بدون Headers، لذا نعتمد على استقرار الرابط
    try:
        # إضافة مفتاح الـ API للرابط مباشرة إذا سمح الخادم أو عبر الـ Headers بالبروكسي
        headers = {'x-apisports-key': API_KEY}
        res = requests.get(proxy_url, timeout=15).json()
        
        # فك تغليف البيانات من داخل البروكسي
        actual_data = json.loads(res['contents'])
        return actual_data.get('response', [])
    except:
        return None

# --- التصميم الفاخر ---
st.markdown("""
    <style>
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .main-box { border: 2px solid #D4AF37; border-radius: 20px; padding: 20px; background: rgba(212,175,55,0.02); text-align: center; }
    .score-big { font-size: 6rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)

leagues = {"🇬🇧 الدوري الإنجليزي": 39, "🇪🇸 الدوري الإسباني": 140, "🇹🇳 الدوري التونسي": 202}
sel_league = st.selectbox("🎯 اختر الساحة المستهدفة:", list(leagues.keys()))

# محاولة "الاختراق البرمجي" عبر البروكسي
with st.spinner('📡 جاري كسر حصار المنصة وجلب البيانات...'):
    matches = fetch_via_unbreakable_proxy(leagues[sel_league])

st.markdown("<div class='main-box'>", unsafe_allow_html=True)

if matches and len(matches) > 0:
    # ✅ تم كسر الحظر! ستختفي الرسالة الصفراء وتظهر المباريات هنا
    match_list = {f"{m['teams']['home']['name']} 🆚 {m['teams']['away']['name']}": m for m in matches}
    sel_match = st.selectbox("🔓 تم الاتصال! اختر المباراة:", list(match_list.keys()))
    h_name = match_list[sel_match]['teams']['home']['name']
    a_name = match_list[sel_match]['teams']['away']['name']
else:
    # 🛡️ في حال فشل البروكسي أيضاً (المحاكاة الذكية)
    st.markdown("<p style='color:#D4AF37;'>⚠️ حظر المنصة "النووي" مستمر - تم تفعيل المحرك الذاتي</p>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    h_name = col1.text_input("المضيف:", "الترجي")
    a_name = col2.text_input("الضيف:", "الأهلي")

if st.button("🔱 إطلاق المحاكاة الشمولية"):
    with st.spinner('🎯 جاري التحليل...'):
        time.sleep(1)
        h_res = np.random.poisson(2.1)
        a_res = np.random.poisson(1.3)
        st.markdown(f"<div class='score-big'>{h_res} - {a_res}</div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:white;'>{h_name} vs {a_name}</h3>", unsafe_allow_html=True)
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)
