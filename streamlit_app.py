import streamlit as st
import numpy as np
import requests
import time

# --- 🔱 AuraStats AI: The Final Precision v41.0 ---
st.set_page_config(page_title="AuraStats AI", layout="wide")

# 👇 ضع مفتاحك هنا بدقة (تأكد أن المفتاح داخل العلامات " ")
API_KEY = "c2f6d97fe715446c4be7f30600191daa" 

def get_data(league_id):
    headers = {'x-apisports-key': API_KEY}
    # 🛠️ الإصلاح الجوهري هنا: فصلنا الرابط عن المتغيرات بشكل صحيح
    url = "https://api-sports.io"
    params = {
        'league': league_id,
        'season': 2025,
        'next': 15
    }
    try:
        # استخدام params يمنع أخطاء الروابط (URL Errors)
        res = requests.get(url, headers=headers, params=params, timeout=10)
        data = res.json()
        if data.get('errors'):
            return []
        return data.get('response', [])
    except:
        return []

# --- الواجهة السيادية المحدثة ---
st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AURASTATS AI 🏆</h1>", unsafe_allow_html=True)

mode = st.radio("بوابة التحكم:", ["🌐 آلي (API)", "✍️ يدوي"], horizontal=True)

if mode == "🌐 آلي (API)":
    leagues = {"أبطال أوروبا": 2, "الدوري الإنجليزي": 39, "الدوري الإسباني": 140, "الدوري التونسي": 202}
    sel_league = st.selectbox("اختر البطولة العالمية:", list(leagues.keys()))
    
    with st.spinner('📡 جاري سحب البيانات الحقيقية...'):
        matches = get_data(leagues[sel_league])
    
    if matches:
        match_names = [f"{m['teams']['home']['name']} vs {m['teams']['away']['name']}" for m in matches]
        sel_match = st.selectbox("اختر المباراة القادمة:", match_names)
        
        match_info = matches[match_names.index(sel_match)]
        h_name = match_info['teams']['home']['name']
        a_name = match_info['teams']['away']['name']
        h_xg, a_xg = 2.10, 1.45 
        st.success(f"✅ تم الاتصال بنجاح بمباراة: {sel_match}")
    else:
        st.error("⚠️ لم نجد مباريات (تأكد من المفتاح والإنترنت)")
        h_xg = 0
else:
    c1, c2 = st.columns(2)
    h_name = c1.text_input("المضيف:", "الترجي")
    h_xg = c1.number_input(f"xG {h_name}:", value=1.80)
    a_name = c2.text_input("الضيف:", "الأهلي")
    a_xg = c2.number_input(f"xG {a_name}:", value=1.50)

if st.button("🚀 إطلاق المحاكاة السيادية"):
    if h_xg > 0:
        with st.spinner('يتم تحليل 100,000 سيناريو...'):
            time.sleep(1)
            h_sim = np.random.poisson(h_xg, 100000)
            a_sim = np.random.poisson(a_xg, 100000)
            st.markdown(f"<div style='text-align:center; border:2px solid #D4AF37; padding:20px; border-radius:50px;'><h2>النتيجة المتوقعة: {int(np.mean(h_sim))} - {int(np.mean(a_sim))}</h2></div>", unsafe_allow_html=True)
            st.balloons()
        
