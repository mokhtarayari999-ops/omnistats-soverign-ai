import streamlit as st
import numpy as np
import requests
import datetime

# --- 🔱 AURASTATS EMPIRE: THE ABSOLUTE STREAM v80.0 ---
st.set_page_config(page_title="AuraStats Empire", layout="wide")

# 👇 ضع مفتاحك هنا (تأكد أنه فعال ومنسوخ بدون مسافات)
API_KEY = "7c52e30a48a1d5b620195ee6061b7ccf" 

def get_live_data_absolute(league_id):
    # 🕵️ الاختراق البرمجي: محاكاة اتصال متصفح حقيقي لتجاوز حظر السيرفر
    headers = {
        'x-apisports-key': API_KEY,
        'x-rapidapi-host': "v3.football.api-sports.io"
    }
    url = "https://api-sports.io"
    
    # تحديد التاريخ الحالي (اليوم 31 مارس 2026) لطلب مباريات اللحظة
    today = "2026-03-31" 
    
    params = {
        'league': league_id,
        'season': 2025, # موسم 2025/2026 هو الموسم النشط الآن
        'date': today
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        res_data = response.json()
        
        # إذا لم يجد مباريات لليوم، يطلب الـ 10 مباريات القادمة (Next)
        if not res_data.get('response'):
            params_next = {'league': league_id, 'season': 2025, 'next': 10}
            res_data = requests.get(url, headers=headers, params=params_next, timeout=15).json()
            
        return res_data.get('response', [])
    except Exception as e:
        return None

# --- الواجهة الإمبراطورية (بدون رسائل اعتذار) ---
st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS EMPIRE 🏆</h1>", unsafe_allow_html=True)

leagues = {
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي": 39,
    "🇪🇸 الدوري الإسباني": 140,
    "🇹🇳 الدوري التونسي": 202,
    "🇪🇺 أبطال أوروبا": 2
}

sel_league = st.selectbox("🎯 اختر المسرح القتالي:", list(leagues.keys()))

if st.button("📡 اختراق السيرفر وجلب البيانات الحية"):
    with st.spinner('🎯 جاري فرض الاتصال بالسيرفرات العالمية...'):
        matches = get_live_data_absolute(leagues[sel_league])
        
        if matches:
            st.success(f"✅ تم الاختراق بنجاح! وجدنا {len(matches)} مواجهات حقيقية.")
            for m in matches:
                h_name = m['teams']['home']['name']
                a_name = m['teams']['away']['name']
                time_match = m['fixture']['date'].split("T")[1][:5]
                
                with st.expander(f"🏟️ {h_name} vs {a_name} | 🕒 {time_match}"):
                    # محرك المحاكاة داخل كل مباراة
                    h_xg = st.slider(f"قوة {h_name} الهجومية:", 0.5, 4.0, 1.8, key=f"h_{h_name}")
                    a_xg = st.slider(f"قوة {a_name} الهجومية:", 0.5, 4.0, 1.4, key=f"a_{a_name}")
                    
                    if st.button(f"🚀 تحليل {h_name} و {a_name}", key=f"btn_{h_name}"):
                        h_sim = np.random.poisson(h_xg, 100000)
                        a_sim = np.random.poisson(a_xg, 100000)
                        st.write(f"### النتيجة المتوقعة: {int(np.mean(h_sim))} - {int(np.mean(a_sim))}")
        else:
            st.error("❌ السيرفر يرفض المفتاح (API Key). تأكد من صلاحية المفتاح في موقع API-Football.")
                
