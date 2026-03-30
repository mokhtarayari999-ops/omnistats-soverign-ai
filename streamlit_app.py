import streamlit as st
import requests
import numpy as np
import time

# --- 🔑 إعدادات المحرك السيادي ---
API_KEY = "757497fe293f4e39a291cc5c575c6dc3" 

st.set_page_config(page_title="OmniStats Sovereign AI", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    .stApp { background: radial-gradient(circle at center, #111 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .sovereign-panel { background: rgba(255, 255, 255, 0.01); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 40px; padding: 40px; backdrop-filter: blur(25px); }
    .glow-title { font-family: 'Orbitron', sans-serif; font-size: 3rem; text-align: center; color: #D4AF37; text-shadow: 0 0 25px #D4AF37; }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #F2D388, #D4AF37); color: #000 !important; font-weight: 900; border-radius: 100px; height: 65px; border: none; width: 100%; transition: 0.5s; }
    </style>
    """, unsafe_allow_html=True)

# دالة جلب البيانات مع تصحيح الرابط الجذري
def get_league_standings(league_code):
    # تم فصل الرابط لضمان عدم التصاق أي أحرف زائدة
    domain = "https://api.football-data.org"
    endpoint = f"/v4/competitions/{league_code}/standings"
    url = domain + endpoint
    
    headers = {'X-Auth-Token': API_KEY}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['standings'][0]['table'], "OK"
        else:
            return None, f"Status: {response.status_code}"
    except Exception as e:
        return None, str(e)

st.markdown("<p class='glow-title'>OMNISTATS</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='sovereign-panel'>", unsafe_allow_html=True)
    
    league_choice = st.selectbox("🌍 اختر الدوري المباشر:", ["PL", "SA", "PD", "BL1"], 
                                 format_func=lambda x: {"PL":"الدوري الإنجليزي", "SA":"الدوري الإيطالي", "PD":"الدوري الإسباني", "BL1":"الدوري الألماني"}[x])
    
    table, status = get_league_standings(league_choice)
    
    if table:
        st.success("✅ تم الاتصال بنجاح!")
        teams = [t['team']['name'] for t in table]
        c1, c2 = st.columns(2)
        with c1: h_team = st.selectbox("صاحب الأرض:", teams, index=0)
        with c2: a_team = st.selectbox("الضيف المتحدي:", teams, index=1)
        
        if st.button("إطلاق المحاكاة السيادية ⚡"):
            st.balloons()
            st.write(f"المحرك يحلل الآن مواجهة: **{h_team}** ضد **{a_team}**")
    else:
        st.error(f"⚠️ حالة المحرك: {status}")
        st.info("نصيحة الشريك: تأكد من تحديث الكود في GitHub وضغط Commit changes")

    st.markdown("</div>", unsafe_allow_html=True)
    
