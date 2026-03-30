import streamlit as st
import requests
import numpy as np

# --- 🔑 NUCLEAR CONFIG ---
API_KEY = "757497fe293f4e39a291cc5c575c6dc3" 

st.set_page_config(page_title="OmniStats Sovereign", layout="wide", page_icon="🔱")

# التنسيق الفاخر
st.markdown("""
    <style>
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .glass-panel { background: rgba(255, 255, 255, 0.05); border: 1px solid #D4AF37; border-radius: 20px; padding: 25px; }
    </style>
    """, unsafe_allow_html=True)

# دالة جلب البيانات (مجزأة لضمان الصحة 100%)
def fetch_data(league_code):
    # بناء الرابط بقطع منفصلة لمنع الالتصاق
    part1 = "https://api.football-data.org"
    part2 = "/v4/competitions/"
    part3 = "/standings"
    full_url = part1 + part2 + league_code + part3
    
    headers = {'X-Auth-Token': API_KEY}
    try:
        response = requests.get(full_url, headers=headers, timeout=10)
        return response
    except Exception as e:
        return str(e)

st.title("🔱 OMNISTATS CORE")

with st.container():
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    
    league = st.selectbox("🌍 اختر الدوري:", ["PL", "SA", "PD", "BL1"], 
                          format_func=lambda x: {"PL":"إنجلترا", "SA":"إيطاليا", "PD":"إسبانيا", "BL1":"ألمانيا"}[x])
    
    res = fetch_data(league)
    
    # فحص النتيجة الحقيقية
    if isinstance(res, requests.Response):
        if res.status_code == 200:
            st.success("✅ المحرك متصل بالبيانات الحقيقية!")
            data = res.json()['standings'][0]['table']
            teams = [t['team']['name'] for t in data]
            st.selectbox("الفريق المتاح:", teams)
        else:
            st.error(f"⚠️ خطأ من المصدر برقم: {res.status_code}")
            if res.status_code == 403:
                st.info("تنبيه: المفتاح الذي تستخدمه مرفوض أو غير مفعل.")
    else:
        st.error(f"❌ فشل الاتصال التقني: {res}")
        
    st.markdown("</div>", unsafe_allow_html=True)
        
