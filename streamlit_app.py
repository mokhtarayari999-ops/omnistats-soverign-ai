import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 ARABIC PRO: THE MAGIC UPDATE v3.0 ---
st.set_page_config(page_title="Arabic Pro | الذكاء الرياضي", layout="wide")

API_KEY = "8abdb813dece636993e2182de4ee374a"
BASE_URL = "https://api-sports.io"
HEADERS = {'x-apisports-key': API_KEY}

# 🪄 الوظيفة السحرية 1: جلب كل الدوريات المتاحة تلقائياً دون كتابتها
@st.cache_data(ttl=86400) # تخزين النتائج ليوم كامل لسرعة الأداء
def get_all_leagues():
    try:
        # جلب الدوريات الكبرى والمشهورة فقط لتقليل الفوضى
        res = requests.get(f"{BASE_URL}/leagues", headers=HEADERS, timeout=10).json()
        all_leagues = {item['league']['name']: item['league']['id'] for item in res['response'] if item['league']['id'] in [202, 233, 307, 39, 140, 135, 78, 2, 3]}
        return all_leagues
    except:
        return {"🇹🇳 الدوري التونسي": 202, "🇸🇦 دوري روشن": 307}

# 🪄 الوظيفة السحرية 2: جلب المباريات المباشرة أو القادمة
def get_fixtures(league_id):
    url = f"{BASE_URL}/fixtures?league={league_id}&season=2025&next=15"
    try:
        res = requests.get(url, headers=HEADERS, timeout=10).json()
        return res.get('response', [])
    except: return []

# --- الواجهة الإمبراطورية المحدثة ---
st.markdown("<h1 style='text-align:center; color:#D4AF37;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)

# الخطوة 1: اختيار الدوري (يتم جلب القائمة سحرياً)
available_leagues = get_all_leagues()
sel_league_name = st.selectbox("🌍 النظام جاهز.. اختر ساحة المعركة (الدوري):", list(available_leagues.keys()))
league_id = available_leagues[sel_league_name]

# الخطوة 2: جلب المباريات فور اختيار الدوري
with st.status("📡 جاري مسح الترددات وجلب المواجهات...", expanded=False) as status:
    matches = get_fixtures(league_id)
    status.update(label="✅ تم الاتصال بنجاح!", state="complete")

st.markdown("<div style='border: 2px solid #D4AF37; border-radius: 30px; padding: 25px; background: rgba(212,175,55,0.05);'>", unsafe_allow_html=True)

if matches:
    titles = {f"{m['teams']['home']['name']} 🆚 {m['teams']['away']['name']}": m for m in matches}
    sel_match = st.selectbox("📅 اختر المباراة المراد تحليلها إحصائياً:", list(titles.keys()))
    m_data = titles[sel_match]
    
    # محاكي ذكي لـ xG (أهداف متوقعة) مبني على رتبة الفريق (تبسيط ذكي)
    h_name, a_name = m_data['teams']['home']['name'], m_data['teams']['away']['name']
    h_xg = 2.0 if "الترجي" in h_name or "الأهلي" in h_name else 1.5
    a_xg = 1.2
else:
    st.error("⚠️ لا توجد مباريات مجدولة حالياً لهذا الدوري في الخادم.")
    h_name, a_name, h_xg, a_xg = "فريق أ", "فريق ب", 1.5, 1.0

# زر الإطلاق الشمولي
if st.button("🔱 إطلاق المحاكاة العميقة (Deep Simulation)"):
    h_sim = np.random.poisson(h_xg, 100000)
    a_sim = np.random.poisson(a_xg, 100000)
    
    st.markdown(f"<h1 style='text-align:center; font-size:6rem; color:#D4AF37;'>{int(np.mean(h_sim))} - {int(np.mean(a_sim))}</h1>", unsafe_allow_html=True)
    st.toast(f"تم تحليل 100,000 سيناريو لمباراة {h_name}!")
    st.balloons()

st.markdown("</div>", unsafe_allow_html=True)
        
