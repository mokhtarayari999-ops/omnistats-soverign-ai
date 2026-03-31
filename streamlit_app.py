import streamlit as st
import numpy as np
import time

# --- 🔱 AURASTATS ARABIC PRO: THE FULL MATRIX v750.0 ---
st.set_page_config(page_title="AuraStats Arabic Pro", layout="wide", page_icon="🔱")

# --- CSS الهوية الإمبراطورية الفخمة ---
st.markdown("""
    <style>
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .main-panel { border: 2px solid #D4AF37; border-radius: 40px; padding: 25px; background: rgba(212,175,55,0.02); text-align: center; }
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #F2D388 50%, #D4AF37 100%); color: black !important; font-weight: 900; border-radius: 100px; height: 65px; border: none; font-size: 1.4rem; box-shadow: 0 0 30px rgba(212,175,55,0.4); }
    .stat-badge { background: #111; border: 1px solid #D4AF37; border-radius: 20px; padding: 15px; margin: 10px; min-width: 120px; }
    .score-display { font-size: 6.5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 40px #D4AF37; margin: 0; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37; font-size:3.5rem;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)

# 🧠 قاعدة بيانات النجوم (رجل المباراة لكل دوري)
players_db = {
    "الأهلي": ["حسين الشحات", "إمام عاشور", "وسام أبو علي"],
    "الزمالك": ["زيزو", "عبد الله السعيد", "شيكابالا"],
    "الترجي الرياضي": ["ياسين مرياح", "يوسف بلايلي", "يان ساس"],
    "النادي الإفريقي": ["كينغسلي إيدو", "بلال آيت مالك", "غيث الزعلوني"],
    "الهلال": ["ميتروفيتش", "سالم الدوسري", "مالكوم"],
    "النصر": ["كريستيانو رونالدو", "ساديو ماني", "تاليسكا"],
    "الوداد": ["مباي نيانغ", "محمد مفيد", "جمال حركاس"],
    "الرجاء": ["يسري بوزوق", "آدم النفاتي", "صابر بوغرين"],
    "مولودية الجزائر": ["يوسف بلايلي", "أندي ديلور", "زكريا نايدجي"],
    "السد": ["أكرم عفيف", "حسن الهيدوس"],
    "العين": ["سفيان رحيمي", "لابا كودجو"]
}

# 🌍 المصفوفة العربية الكبرى
all_arabic_leagues = {
    "🇹🇳 الدوري التونسي الممتاز": ["الترجي الرياضي vs النادي الإفريقي", "النجم الساحلي vs النادي الصفاقسي", "الملعب التونسي vs الاتحاد المنستيري"],
    "🇪🇬 الدوري المصري الممتاز": ["الأهلي vs الزمالك", "بيراميدز vs فيوتشر", "المصري vs الاتحاد السكندري"],
    "🇸🇦 دوري روشن السعودي": ["الهلال vs النصر", "الاتحاد vs الأهلي السعودي", "الشباب vs الاتفاق"],
    "🇲🇦 الدوري المغربي (البطولة)": ["الوداد vs الرجاء", "الجيش الملكي vs نهضة بركان", "الفتح الرباطي vs اتحاد طنجة"],
    "🇩🇿 الدوري الجزائري": ["مولودية الجزائر vs شباب بلوزداد", "اتحاد العاصمة vs شبيبة القبائل"],
    "🇶🇦 دوري نجوم قطر": ["السد vs الدحيل", "الريان vs الغرافة"],
    "🇦🇪 الدوري الإماراتي": ["العين vs شباب الأهلي", "الوصل vs الشارقة"],
    "🌍 أبطال أفريقيا / آسيا": ["الأهلي vs صن داونز", "الهلال vs العين", "الترجي vs الوداد"]
}

sel_league = st.selectbox("🎯 اختر البطولة العربية الحية:", list(all_arabic_leagues.keys()))
current_matches = all_arabic_leagues[sel_league]
sel_match = st.selectbox("المواجهات المرصودة:", current_matches)

h_name, a_name = sel_match.split(" vs ")

st.markdown("<div class='main-panel'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
h_xg = col1.slider(f"قوة {h_name} (xG):", 0.5, 5.0, 2.23)
a_xg = col2.slider(f"قوة {a_name} (xG):", 0.5, 5.0, 1.85)

if st.button("🚀 إطلاق المحاكاة الشمولية القصوى 🔱"):
    with st.spinner('🎯 تحليل السجلات التاريخية وسلوك اللاعبين...'):
        time.sleep(1.5)
        h_sim = np.random.poisson(h_xg, 100000)
        a_sim = np.random.poisson(a_xg, 100000)
        
        score_h, score_a = int(np.mean(h_sim)), int(np.mean(a_sim))
        corners = int((h_xg + a_xg) * 3.8)
        win_p = (h_sim > a_sim).mean() * 100
        
        # خوارزمية البطاقات (تفاعلية)
        cards = int(((h_xg + a_xg) / 2) * 2.5) + np.random.randint(1, 4)
        
        # اختيار رجل المباراة من قاعدة البيانات المدمجة
        all_stars = players_db.get(h_name, ["نجم المباراة"]) + players_db.get(a_name, ["نجم المباراة"])
        man_of_match = np.random.choice(all_stars)

        st.markdown(f"""
            <div style='margin-top:10px;'>
                <p style='color:#D4AF37; margin:0;'>النتيجة الأكثر توقعاً</p>
                <h1 class='score-display'>{score_h} - {score_a}</h1>
                <h3 style='color:white;'>{h_name} vs {a_name}</h3>
                <hr style='border:1px solid #D4AF37; opacity:0.2; margin:20px 0;'>
                <div style='display:flex; justify-content:center; flex-wrap:wrap;'>
                    <div class='stat-badge'><p style='color:#D4AF37; margin:0;'>🚩 ركنيات</p><h2 style='color:white; margin:0;'>{corners}</h2></div>
                    <div class='stat-badge'><p style='color:#D4AF37; margin:0;'>🟨 بطاقات</p><h2 style='color:white; margin:0;'>{cards}</h2></div>
                    <div class='stat-badge'><p style='color:#D4AF37; margin:0;'>📈 فوز {h_name}</p><h2 style='color:white; margin:0;'>{win_p:.1f}%</h2></div>
                </div>
                <div style='margin-top:20px; padding:20px; border:1px solid #D4AF37; border-radius:25px; background:rgba(212,175,55,0.1); box-shadow: inset 0 0 20px rgba(212,175,55,0.1);'>
                    <p style='color:#D4AF37; margin:0;'>⭐ رجل المباراة المتوقع</p>
                    <h2 style='color:white; margin:10px 0;'>{man_of_match}</h2>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#333; margin-top:50px;'>AURASTATS AI | THE ARABIC EMPIRE v750.0</p>", unsafe_allow_html=True)
