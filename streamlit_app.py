import streamlit as st
import requests
import numpy as np
import time

# --- 🔑 تأكد من أن هذا هو مفتاحك الصحيح بدقة ---
API_KEY = "757497fe293f4e39a291cc5c575c6dc3" 

st.set_page_config(page_title="OmniStats Sovereign AI", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    .stApp { background: radial-gradient(circle at center, #111 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .sovereign-panel { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 30px; padding: 35px; backdrop-filter: blur(20px); }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #F2D388, #D4AF37); color: #000 !important; font-weight: 900; border-radius: 100px; height: 60px; border: none; }
    </style>
    """, unsafe_allow_html=True)

def get_data_with_debug(league_code):
    url = f"https://api.football-data.org{league_code}/standings"
    headers = {'X-Auth-Token': API_KEY}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['standings'][0]['table'], "OK"
        elif response.status_code == 403:
            return None, "المفتاح مرفوض (403) - تأكد من تفعيله من الإيميل"
        elif response.status_code == 429:
            return None, "طلبات كثيرة (429) - انتظر دقيقة وأعد المحاولة"
        else:
            return None, f"خطأ غير معروف: {response.status_code}"
    except Exception as e:
        return None, f"فشل الاتصال بالإنترنت: {str(e)}"

st.markdown("<h1 style='text-align:center; color:#D4AF37;'>🔱 OMNISTATS CORE</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='sovereign-panel'>", unsafe_allow_html=True)
    
    league_choice = st.selectbox("🌍 اختر الدوري المباشر:", ["PL", "SA", "PD", "BL1", "CL"], 
                                 format_func=lambda x: {"PL":"الدوري الإنجليزي", "SA":"الدوري الإيطالي", "PD":"الدوري الإسباني", "BL1":"الدوري الألماني", "CL":"دوري أبطال أوروبا"}[x])
    
    table, status = get_data_with_debug(league_choice)
    
    if table:
        st.success("✅ تم الاتصال بنجاح بالخوادم العالمية!")
        teams = [t['team']['name'] for t in table]
        c1, c2 = st.columns(2)
        with c1: h_team = st.selectbox("صاحب الأرض:", teams, index=0)
        with c2: a_team = st.selectbox("الضيف المتحدي:", teams, index=1)
        
        if st.button("إطلاق المحاكاة السيادية ⚡"):
            st.balloons()
            st.write(f"المحرك يحلل الآن مواجهة: **{h_team}** ضد **{a_team}**")
    else:
        st.error(f"⚠️ حالة المحرك: {status}")
        st.info("نصيحة: تأكد من نسخ المفتاح كاملاً وبدون مسافات إضافية في ملف app.py")

    st.markdown("</div>", unsafe_allow_html=True)
            
