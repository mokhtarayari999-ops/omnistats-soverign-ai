import streamlit as st
import numpy as np
import time

# --- 🔱 AURASTATS ARABIC PRO: THE FINAL MASTERPIECE v800.0 ---
st.set_page_config(page_title="AuraStats Arabic Pro", layout="wide", page_icon="🔱")

# --- CSS الهوية الإمبراطورية الفائقة (وضوح تام للموبايل) ---
st.markdown("""
    <style>
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .main-panel { border: 2px solid #D4AF37; border-radius: 45px; padding: 25px; background: rgba(212,175,55,0.02); text-align: center; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #F2D388 50%, #D4AF37 100%); color: black !important; font-weight: 900; border-radius: 100px; height: 75px; font-size: 1.6rem; border: none; box-shadow: 0 0 40px rgba(212,175,55,0.4); }
    .stat-badge { background: #111; border: 1px solid #D4AF37; border-radius: 25px; padding: 20px; margin: 10px; min-width: 140px; }
    .score-display { font-size: 7.5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 50px #D4AF37; margin: 0; line-height: 1; }
    .player-card { margin-top: 20px; padding: 25px; border: 2px solid #D4AF37; border-radius: 30px; background: rgba(212,175,55,0.15); box-shadow: inset 0 0 30px rgba(212,175,55,0.2); }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37; font-size:3.8rem; margin-bottom:0;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888; letter-spacing: 2px;'>SOVEREIGN ANALYTICS ENGINE</p>", unsafe_allow_html=True)

# 🧠 مصفوفة البيانات العربية الكبرى
all_arabic_leagues = {
    "🇩🇿 الدوري الجزائري": ["مولودية الجزائر vs شباب بلوزداد", "اتحاد العاصمة vs شبيبة القبائل", "وفاق سطيف vs قسنطينة"],
    "🇹🇳 الدوري التونسي الممتاز": ["الترجي الرياضي vs النادي الإفريقي", "النجم الساحلي vs النادي الصفاقسي", "الملعب التونسي vs الاتحاد المنستيري"],
    "🇪🇬 الدوري المصري الممتاز": ["الأهلي vs الزمالك", "بيراميدز vs فيوتشر", "المصري vs الاتحاد"],
    "🇸🇦 دوري روشن السعودي": ["الهلال vs النصر", "الاتحاد vs الأهلي السعودي", "الشباب vs الاتفاق"],
    "🇲🇦 الدوري المغربي (البطولة)": ["الوداد vs الرجاء", "الجيش الملكي vs نهضة بركان"],
    "🌍 أبطال أفريقيا / آسيا": ["الأهلي vs صن داونز", "الهلال vs العين", "الترجي vs الوداد"]
}

# قاعدة بيانات النجوم (MOTM)
players_db = {
    "مولودية الجزائر": ["أندي ديلور", "زكريا نايدجي", "يوسف بلايلي"],
    "شباب بلوزداد": ["إسلام سليماني", "عبد الرؤوف بن غيث"],
    "الأهلي": ["حسين الشحات", "إمام عاشور", "وسام أبو علي"],
    "الزمالك": ["زيزو", "عبد الله السعيد"],
    "الترجي الرياضي": ["يوسف بلايلي", "يان ساس", "ياسين مرياح"],
    "النادي الإفريقي": ["بلال آيت مالك", "كينغسلي إيدو"]
}

sel_league = st.selectbox("🎯 اختر المسرح القتالي:", list(all_arabic_leagues.keys()))
sel_match = st.selectbox("المواجهات المرصودة:", all_arabic_leagues[sel_league])

h_name, a_name = sel_match.split(" vs ")

st.markdown("<div class='main-panel'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
h_xg = col1.slider(f"قوة {h_name} (xG):", 0.1, 5.0, 1.85)
a_xg = col2.slider(f"قوة {a_name} (xG):", 0.1, 5.0, 1.48)

if st.button("🔱 إطلاق المحاكاة الإمبراطورية المطلقة"):
    with st.spinner('🎯 يتم الآن تحليل 100,000 سيناريو وحساب المتغيرات...'):
        time.sleep(1.5)
        h_sim = np.random.poisson(h_xg, 100000)
        a_sim = np.random.poisson(a_xg, 100000)
        
        score_h, score_a = int(np.mean(h_sim)), int(np.mean(a_sim))
        corners = int((h_xg + a_xg) * 3.8)
        win_p = (h_sim > a_sim).mean() * 100
        cards = int(((h_xg + a_xg) / 2) * 2.5) + np.random.randint(1, 4)
        possession = int(50 + (h_xg - a_xg) * 10)
        penalties = "نعم" if (h_xg + a_xg) > 3.5 else "لا"

        all_stars = players_db.get(h_name, ["نجم المباراة"]) + players_db.get(a_name, ["نجم المباراة"])
        man_of_match = np.random.choice(all_stars)

        st.markdown(f"""
            <div style='margin-top:10px;'>
                <p style='color:#D4AF37; margin:0; font-size:1.3rem;'>النتيجة الأكثر توقعاً</p>
                <h1 class='score-display'>{score_h} - {score_a}</h1>
                <h3 style='color:white; font-size:2rem;'>{h_name} vs {a_name}</h3>
                <hr style='border:1px solid #D4AF37; opacity:0.3; margin:30px 0;'>
                <div style='display:flex; justify-content:center; flex-wrap:wrap;'>
                    <div class='stat-badge'><p style='color:#D4AF37; margin:0;'>🚩 ركنيات</p><h2 style='color:white; margin:0;'>{corners}</h2></div>
                    <div class='stat-badge'><p style='color:#D4AF37; margin:0;'>🟨 بطاقات</p><h2 style='color:white; margin:0;'>{cards}</h2></div>
                    <div class='stat-badge'><p style='color:#D4AF37; margin:0;'>⚽ استحواذ</p><h2 style='color:white; margin:0;'>{possession}%</h2></div>
                    <div class='stat-badge'><p style='color:#D4AF37; margin:0;'>🧤 ركلة جزاء</p><h2 style='color:white; margin:0;'>{penalties}</h2></div>
                </div>
                <div class='player-card'>
                    <p style='color:#D4AF37; margin:0; font-size:1.2rem; font-weight:bold;'>⭐ رجل المباراة المتوقع</p>
                    <h2 style='color:white; margin:10px 0; font-size:2.5rem;'>{man_of_match}</h2>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#333; margin-top:50px;'>AURASTATS AI | v800.0 ULTIMATE IMMORTAL</p>", unsafe_allow_html=True)
