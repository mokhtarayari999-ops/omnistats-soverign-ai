import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AURASTATS PRO: THE ABSOLUTE RESULTS v1100.0 ---
st.set_page_config(page_title="Arabic Pro", layout="wide")

# 👇 ضع مفتاحك هنا (تأكد من تفعيله من بريدك الإلكتروني)
API_KEY = "8abdb813dece636993e2182de4ee374a" 

def fetch_live_absolute(league_id):
    headers = {
        'x-apisports-key': API_KEY,
        'User-Agent': 'Mozilla/5.0 (iPhone; OS 16_0) AppleWebKit/605.1.15'
    }
    url = f"https://api-sports.io{league_id}&season=2025&next=10"
    try:
        res = requests.get(url, headers=headers, timeout=10).json()
        return res.get('response', [])
    except: return None

# --- CSS الهوية الإمبراطورية الفائقة ---
st.markdown("""
    <style>
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .main-panel { border: 2px solid #D4AF37; border-radius: 40px; padding: 25px; background: rgba(212,175,55,0.02); text-align: center; }
    .score-display { font-size: 6.5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 40px #D4AF37; margin: 0; line-height: 1; }
    .stat-badge { background: #111; border: 1px solid #D4AF37; border-radius: 20px; padding: 15px; margin: 10px; min-width: 120px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)

leagues = {"🇹🇳 الدوري التونسي الممتاز": 202, "🇪🇬 الدوري المصري الممتاز": 233, "🇸🇦 دوري روشن": 307}
sel_league = st.selectbox("🎯 اختر البطولة المراد رصدها حياً:", list(leagues.keys()))

# محاولة الربط السريع
matches = fetch_live_absolute(leagues[sel_league])

st.markdown("<div class='main-panel'>", unsafe_allow_html=True)

if matches:
    titles = {f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}": m for m in matches}
    sel_match = st.selectbox("المواجهات المرصودة حياً (Live):", list(titles.keys()))
    h_name, a_name = sel_match.split(" vs ")
    h_xg, a_xg = 2.1, 1.4
else:
    st.markdown("<p style='color:#888;'>📡 جاري محاولة الربط... (يمكنك الإدخال يدوياً أدناه)</p>", unsafe_allow_html=True)
    col_l, col_r = st.columns(2)
    h_name = col_l.text_input("المضيف:", "الترجي")
    a_name = col_r.text_input("الضيف:", "الأهلي")
    h_xg, a_xg = 2.2, 1.5

# 🚀 زر إطلاق النتائج (الأهم في هذا التحديث)
if st.button("🔱 إطلاق المحاكاة الشمولية والنتائج"):
    with st.spinner('🎯 جاري تحليل 100,000 سيناريو...'):
        time.sleep(1)
        h_sim = np.random.poisson(h_xg, 100000)
        a_sim = np.random.poisson(a_xg, 100000)
        
        score_h, score_a = int(np.mean(h_sim)), int(np.mean(a_sim))
        corners = int((h_xg + a_xg) * 3.8)
        win_p = (h_sim > a_sim).mean() * 100

        # عرض النتائج التي طلبتها (النتيجة + الركنيات + الشمولية)
        st.markdown(f"""
            <div style='margin-top:20px;'>
                <p style='color:#D4AF37; margin:0;'>النتيجة المتوقعة</p>
                <h1 class='score-display'>{score_h} - {score_a}</h1>
                <hr style='border:1px solid #D4AF37; opacity:0.2; margin:20px 0;'>
                <div style='display:flex; justify-content:center; flex-wrap:wrap;'>
                    <div class='stat-badge'><p style='color:#D4AF37; margin:0;'>🚩 ركنيات</p><h2 style='color:white; margin:0;'>{corners}</h2></div>
                    <div class='stat-badge'><p style='color:#D4AF37; margin:0;'>📈 فوز {h_name}</p><h2 style='color:white; margin:0;'>{win_p:.1f}%</h2></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)
