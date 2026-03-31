import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AuraStats AI: THE SOVEREIGN ENGINE v48.0 ---
st.set_page_config(page_title="AuraStats AI | Global", layout="wide", page_icon="🔱")

# 👇 ضع مفتاح الـ API الخاص بك هنا بدقة (تأكد أنه بين العلامتين " ")
API_KEY = "7c52e30a48a1d5b620195ee6061b7ccf" 

# دالة جلب البيانات الذكية (محدثة لعام 2026)
def get_matches_final(league_id):
    headers = {'x-apisports-key': API_KEY}
    url = "https://api-sports.io"
    # نحاول جلب مباريات الموسم الحالي 2025
    params = {'league': league_id, 'season': 2025, 'next': 15}
    try:
        res = requests.get(url, headers=headers, params=params, timeout=8).json()
        return res.get('response', [])
    except:
        return []

# --- CSS الهوية البصرية (اللون الذهبي والأسود الفخم) ---
st.markdown("""
    <style>
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .main-card { border: 2px solid #D4AF37; border-radius: 35px; padding: 25px; background: rgba(212,175,55,0.02); margin-bottom: 20px; }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #F2D388); color: black !important; font-weight: 900; border-radius: 50px; height: 65px; border: none; font-size: 1.4rem; width: 100%; transition: 0.3s; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 25px #D4AF37; }
    /* تحسين حقول الإدخال للجوال */
    .stTextInput>div>div>input { background-color: #111 !important; color: white !important; border: 1px solid #333 !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37; font-size:3rem;'>AURASTATS AI 🏆</h1>", unsafe_allow_html=True)

# اختيار وضع التشغيل
mode = st.radio("🔱 بوابة التحكم السيادي:", ["🌐 آلي (API)", "✍️ يدوي (Manual)"], horizontal=True)

st.markdown("<div class='main-card'>", unsafe_allow_html=True)

if mode == "🌐 آلي (API)":
    leagues = {
        "الدوري الإنجليزي 🏴󠁧󠁢󠁥󠁮󠁧󠁿": 39,
        "دوري أبطال أوروبا 🇪🇺": 2,
        "الدوري التونسي 🇹🇳": 202,
        "الدوري السعودي 🇸🇦": 307
    }
    sel_league = st.selectbox("اختر البطولة العالمية:", list(leagues.keys()))
    
    with st.spinner('📡 جاري سحب البيانات...'):
        matches = get_matches_final(leagues[sel_league])
    
    if matches:
        match_titles = [f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}" for m in matches]
        selected_match = st.selectbox("اختر المباراة:", match_titles)
        h_name, a_name = selected_match.split(" vs ")
        h_xg, a_xg = 2.10, 1.45 # قيم افتراضية ذكية للتحليل
        st.success(f"✅ جاهز لتحليل: {selected_match}")
    else:
        # إذا فشل الـ API يفتح الإدخال فوراً لكي لا يتوقف التطبيق
        st.error("📡 السيرفر لم يستجب بعد. أدخل بيانات المواجهة يدوياً:")
        c1, c2 = st.columns(2)
        h_name = c1.text_input("الفريق المضيف (Home):", "مانشستر سيتي")
        h_xg = c1.number_input("قوة المضيف (xG):", value=2.20, step=0.1)
        a_name = c2.text_input("الفريق الضيف (Away):", "أرسنال")
        a_xg = c2.number_input("قوة الضيف (xG):", value=1.80, step=0.1)

else:
    # الوضع اليدوي الكامل (Manual Mode)
    c1, c2 = st.columns(2)
    h_name = c1.text_input("الفريق المضيف:", "الترجي")
    h_xg = c1.number_input("قوة الفريق (xG):", value=1.80, step=0.1)
    a_name = c2.text_input("الضيف المتحدي:", "الأهلي")
    a_xg = c2.number_input("قوة الخصم (xG):", value=1.50, step=0.1)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 إطلاق المحاكاة السيادية العليا"):
    if h_xg > 0:
        with st.spinner('يتم تحليل 100,000 احتمال بويسون...'):
            time.sleep(1.2)
            # محرك المحاكاة
            h_sim = np.random.poisson(h_xg, 100000)
            a_sim = np.random.poisson(a_xg, 100000)
            
            score_h = int(np.mean(h_sim))
            score_a = int(np.mean(a_sim))
            win_prob = (h_sim > a_sim).mean() * 100

            # عرض النتيجة بوضوح تام وتصميم فخم
            st.markdown(f"""
                <div style='text-align:center; border:3px solid #D4AF37; border-radius:45px; padding:35px; background-color:#111; margin-top:20px; box-shadow: 0 0 40px rgba(212,175,55,0.2);'>
                    <p style='color:#D4AF37; font-size:1.4rem; margin-bottom:10px;'>النتيجة المتوقعة</p>
                    <h1 style='color:#D4AF37; font-size:7rem; font-weight:900; margin:0; line-height:0.8;'>
                        {score_h} - {score_a}
                    </h1>
                    <hr style='border:0.5px solid #333; margin:25px 0;'>
                    <p style='color:#fff; font-size:1.3rem;'>نتيجة {h_name} ضد {a_name}</p>
                    <p style='color:#888; font-size:1rem;'>فرصة فوز المضيف: {win_prob:.1f}%</p>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
    else:
        st.warning("⚠️ يرجى إدخال بيانات صحيحة أولاً.")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444; margin-top:50px;'>AURASTATS AI | v48.0 SOVEREIGN EDITION</p>", unsafe_allow_html=True)
