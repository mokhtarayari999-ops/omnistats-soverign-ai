import streamlit as st
import requests
import numpy as np
import time

# --- 🔑 NUCLEAR CONFIG ---
API_KEY = "757497fe293f4e39a291cc5c575c6dc3" 

st.set_page_config(page_title="OmniStats Quantum Elite", layout="wide", page_icon="🔱")

# التنسيق الفاخر
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    .stApp { background: radial-gradient(circle at center, #111 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .glass-panel { background: rgba(255, 255, 255, 0.01); border: 1px solid rgba(212, 175, 55, 0.3); border-radius: 35px; padding: 40px; backdrop-filter: blur(30px); }
    .glow-header { font-family: 'Orbitron', sans-serif; font-size: 3rem; text-align: center; color: #D4AF37; text-shadow: 0 0 20px #D4AF37; }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #F2D388, #D4AF37); color: #000 !important; font-weight: 900; border-radius: 100px; height: 60px; border: none; }
    </style>
    """, unsafe_allow_html=True)

# دالة جلب البيانات (تم تصحيح الرابط جذرياً هنا)
def fetch_live_data(league_code):
    # تأكد أن الرابط ينتهي بـ .org/v4 وليس .orgpl/v4
    url = f"https://api.football-data.org{league_code}/standings"
    headers = {'X-Auth-Token': API_KEY}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.json()['standings'][0]['table'], "OK"
        else:
            return None, f"خطأ {response.status_code}"
    except Exception as e:
        return None, "خطأ في الرابط أو الاتصال"

st.markdown("<p class='glow-header'>OMNISTATS</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    
    league = st.selectbox("🌍 اختر الدوري المباشر:", ["PL", "SA", "PD", "BL1"], 
                          format_func=lambda x: {"PL":"الدوري الإنجليزي", "SA":"الدوري الإيطالي", "PD":"الدوري الإسباني", "BL1":"الدوري الألماني"}[x])
    
    table, status = fetch_live_data(league)
    
    if table:
        st.success("✅ تم الاتصال بنجاح. المحرك جاهز.")
        teams = [t['team']['name'] for t in table]
        col1, col2 = st.columns(2)
        with col1: h_team = st.selectbox("صاحب الأرض:", teams, index=0)
        with col2: a_team = st.selectbox("الضيف المتحدي:", teams, index=1)
        
        if st.button("إطلاق المحاكاة الكمية ⚡"):
            st.balloons()
            st.info(f"المحرك يحلل الآن مواجهة: **{h_team}** ضد **{a_team}**")
    else:
        st.error(f"⚠️ حالة المحرك: {status}")
        st.info("تأكد من حذف أي أحرف زائدة (مثل pl) في نهاية الرابط داخل الكود.")

    st.markdown("</div>", unsafe_allow_html=True)
                                
