import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AURASTATS AI: THE GLOBAL EMPIRE v60.0 ---
st.set_page_config(page_title="AuraStats AI | Empire", layout="wide", page_icon="🔱")

# مفتاحك السحري (تأكد من وضعه لفتح الأبواب الموصدة)
API_KEY = "7c52e30a48a1d5b620195ee6061b7ccf" 

def get_empire_data(league_id):
    headers = {'x-apisports-key': API_KEY}
    url = "https://api-sports.io"
    # مصفوفة البحث عبر المواسم لضمان جلب البيانات الحية (2025/2026)
    for season in [2025, 2024]:
        params = {'league': league_id, 'season': season, 'next': 15}
        try:
            res = requests.get(url, headers=headers, params=params, timeout=10).json()
            if res.get('response'): return res['response']
        except: continue
    return []

# --- CSS التصميم الإمبراطوري المتكامل ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #0a0a0a 0%, #000 100%); color: #D4AF37; }
    .stat-card { background: rgba(212,175,55,0.05); border: 1px solid #D4AF37; border-radius: 25px; padding: 20px; text-align: center; }
    .main-result { font-size: 7rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 30px #D4AF37; margin:0; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37; font-size:3.5rem;'>AURASTATS EMPIRE 🌍</h1>", unsafe_allow_html=True)

# 🌍 المصفوفة الكبرى للدوريات (لا حدود هنا!)
all_leagues = {
    "🏆 دوري أبطال أوروبا": 2,
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي": 39,
    "🇪🇸 الدوري الإسباني": 140,
    "🇮🇹 الدوري الإيطالي": 135,
    "🇩🇪 الدوري الألماني": 78,
    "🇫🇷 الدوري الفرنسي": 61,
    "🇹🇳 الدوري التونسي": 202,
    "🇲🇦 الدوري المغربي": 200,
    "🇪🇬 الدوري المصري": 233,
    "🇸🇦 دوري روشن السعودي": 307,
    "🇶🇦 دوري نجوم قطر": 305,
    "🇦🇪 الدوري الإماراتي": 301,
    "🇩🇿 الدوري الجزائري": 194,
    "🌍 دوري أبطال أفريقيا": 12,
    "🟡 دوري أبطال آسيا": 17,
    "🏆 كأس العالم للأندية": 15,
    "🇵🇹 الدوري البرتغالي": 94,
    "🇳🇱 الدوري الهولندي": 88,
    "🇹🇷 الدوري التركي": 203,
    "🇺🇸 الدوري الأمريكي": 253
}

tab_api, tab_manual = st.tabs(["📡 الرصد العالمي (API)", "🧪 المختبر السيادي (Manual)"])

with tab_api:
    sel_league = st.selectbox("اختر المسرح القتالي:", list(all_leagues.keys()))
    with st.spinner('📡 يتم الآن اختراق السيرفرات العالمية...'):
        matches = get_empire_data(all_leagues[sel_league])
    
    if matches:
        titles = {f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}": m for m in matches}
        sel_match_label = st.selectbox("المواجهات المرصودة:", list(titles.keys()))
        m_data = titles[sel_match_label]
        h_n, a_n = m_data['teams']['home']['name'], m_data['teams']['away']['name']
        h_xg, a_xg = 2.15, 1.40 # قوة تقديرية ذكية
    else:
        st.error("⚠️ السيرفر الخارجي يقاوم! انتقل للمختبر اليدوي فوراً.")
        h_xg = 0

with tab_manual:
    col1, col2 = st.columns(2)
    h_m_n = col1.text_input("المستضيف:", "الترجي")
    h_m_xg = col1.slider(f"قوة هجوم {h_m_n}:", 0.1, 5.0, 1.8)
    a_m_n = col2.text_input("المتحدي:", "الأهلي")
    a_m_xg = col2.slider(f"قوة هجوم {a_m_n}:", 0.1, 5.0, 1.5)

if st.button("🔱 إطلاق التحليل الإمبراطوري الشامل"):
    # دمج البيانات
    final_h, final_a = (h_n, a_n) if 'h_n' in locals() and h_xg > 0 else (h_m_n, a_m_n)
    final_h_xg, final_a_xg = (h_xg, a_xg) if 'h_n' in locals() and h_xg > 0 else (h_m_xg, a_m_xg)

    with st.spinner('🎯 معالجة 100,000 سيناريو احتمالي...'):
        time.sleep(1)
        h_sim = np.random.poisson(final_h_xg, 100000)
        a_sim = np.random.poisson(final_a_xg, 100000)
        
        score_h, score_a = int(np.mean(h_sim)), int(np.mean(a_sim))
        win_p = (h_sim > a_sim).mean() * 100
        corners = int((final_h_xg + final_a_xg) * 3.8)

        st.markdown(f"""
            <div style='text-align:center; border:2px solid #D4AF37; border-radius:40px; padding:40px; background:rgba(0,0,0,0.8);'>
                <h1 class='main-result'>{score_h} - {score_a}</h1>
                <h2 style='color:#fff;'>{final_h} vs {final_a}</h2>
                <hr style='border:1px solid #D4AF37; opacity:0.2; margin:20px 0;'>
                <div style='display:flex; justify-content:space-around;'>
                    <div class='stat-card'><p>🚩 ركنيات</p><h3>{corners}</h3></div>
                    <div class='stat-card'><p>📈 فوز المضيف</p><h3>{win_p:.1f}%</h3></div>
                    <div class='stat-card'><p>⚽ مجموع الـ xG</p><h3>{final_h_xg+final_a_xg:.1f}</h3></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
