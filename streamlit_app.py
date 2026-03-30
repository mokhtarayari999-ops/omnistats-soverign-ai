import streamlit as st
import requests
import numpy as np
import plotly.graph_objects as go
import time

# --- 🔑 إعدادات المحرك السيادي ---
# تأكد أن هذا المفتاح صحيح وفعال من إيميلك
API_KEY = "757497fe293f4e39a291cc5c575c6dc3" 

# 1. التكوين البصري الفاخر (Ultra-Luxury Branding)
st.set_page_config(page_title="OmniStats Sovereign AI", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    
    /* الخلفية والتصميم العام */
    .stApp { background: radial-gradient(circle at center, #111 0%, #000 100%); color: #D4AF37; font-family: 'Cairo', sans-serif; }
    
    /* بطاقة التحليل الزجاجية */
    .sovereign-panel {
        background: rgba(255, 255, 255, 0.01);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 40px;
        padding: 40px;
        backdrop-filter: blur(20px);
        box-shadow: 0 0 80px rgba(212, 175, 55, 0.1);
    }
    
    /* العناوين الذهبية المشعة */
    .glow-title { font-family: 'Orbitron', sans-serif; font-size: 3.5rem; text-align: center; color: #D4AF37; text-shadow: 0 0 25px #D4AF37; margin-bottom: 5px; }
    
    /* تخصيص الأزرار */
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37, #F2D388, #D4AF37);
        color: #000 !important; font-weight: 900; border-radius: 100px;
        height: 70px; border: none; font-size: 1.4rem; transition: 0.5s; width: 100%;
        text-transform: uppercase; letter-spacing: 2px;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 15px 40px rgba(212, 175, 55, 0.5); }
    </style>
    """, unsafe_allow_html=True)

# 2. محرك البيانات المحدث (Corrected Data Engine)
def get_league_standings(league_code):
    # تم تصحيح الرابط هنا: حذف .orgpl ووضع .org/v4
    url = f"https://api.football-data.org{league_code}/standings"
    headers = {'X-Auth-Token': API_KEY}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['standings']['table'], "SUCCESS"
        elif response.status_code == 403:
            return None, "خطأ 403: المفتاح غير مفعل أو ممنوع"
        elif response.status_code == 429:
            return None, "خطأ 429: تم الوصول للحد الأقصى للطلبات المجانية اليوم"
        else:
            return None, f"خطأ برمز: {response.status_code}"
    except Exception as e:
        return None, f"فشل الاتصال: {str(e)}"

# 3. خوارزمية محاكاة مونت كارلو (Sim Engine)
def simulate_match(h_avg, a_avg):
    sims = 15000 # زيادة الدقة لـ 15 ألف سيناريو
    h_goals = np.random.poisson(h_avg, sims)
    a_goals = np.random.poisson(a_avg, sims)
    h_win = (h_goals > a_goals).mean() * 100
    draw = (h_goals == a_goals).mean() * 100
    a_win = (a_goals > h_goals).mean() * 100
    return round(h_win, 1), round(draw, 1), round(a_win, 1)

# 4. بناء لوحة التحكم
st.markdown("<p class='glow-title'>OMNISTATS</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666; letter-spacing:10px;'>SOVEREIGN ELITE v9.0</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='sovereign-panel'>", unsafe_allow_html=True)
    
    # قائمة الاختيار
    league_choice = st.selectbox("🌍 اختر الدوري المباشر:", ["PL", "SA", "PD", "BL1", "CL"], 
                                 format_func=lambda x: {"PL":"الدوري الإنجليزي الممتاز", "SA":"الدوري الإيطالي", "PD":"الدوري الإسباني", "BL1":"الدوري الألماني", "CL":"دوري أبطال أوروبا"}[x])
    
    table, status = get_league_standings(league_choice)
    
    if table:
        st.success(f"✅ تم الاتصال بنجاح. المحرك السيادي جاهز.")
        teams = [t['team']['name'] for t in table]
        
        col_h, vs, col_a = st.columns([2, 0.5, 2])
        
        with col_h:
            h_team = st.selectbox("الفريق المضيف:", teams, index=0)
            h_data = next(t for t in table if t['team']['name'] == h_team)
            h_avg = h_data['goalsFor'] / h_data['playedGames']
            st.metric("معدل التهديف الحقيقي", round(h_avg, 2))
            
        with vs:
            st.markdown("<h1 style='text-align:center; margin-top:50px; opacity:0.2;'>VS</h1>", unsafe_allow_html=True)
            
        with col_a:
            a_team = st.selectbox("الفريق الضيف:", teams, index=1)
            a_data = next(t for t in table if t['team']['name'] == a_team)
            a_avg = a_data['goalsFor'] / a_data['playedGames']
            st.metric("معدل التهديف الحقيقي", round(a_avg, 2))

        if st.button("إطلاق المحاكاة السيادية 🧠⚡"):
            with st.spinner('يتم الآن معالجة آلاف السيناريوهات عبر محرك مونت كارلو...'):
                time.sleep(1.5)
                h_p, d_p, a_p = simulate_match(h_avg, a_avg)
                
                st.markdown("<br><hr style='opacity:0.2'><br>", unsafe_allow_html=True)
                r1, r2, r3 = st.columns(3)
                r1.markdown(f"<div style='text-align:center;'><p>فوز {h_team}</p><h1 style='color:#D4AF37;'>{h_p}%</h1></div>", unsafe_allow_html=True)
                r2.markdown(f"<div style='text-align:center;'><p>التعادل</p><h1 style='color:white;'>{d_p}%</h1></div>", unsafe_allow_html=True)
                r3.markdown(f"<div style='text-align:center;'><p>فوز {a_team}</p><h1 style='color:#D4AF37;'>{a_p}%</h1></div>", unsafe_allow_html=True)
                
                st.balloons()
    else:
        st.error(f"⚠️ حالة المحرك: {status}")
        st.info("تلميح شريكك التقني: إذا كان الخطأ 403، فالمفتاح لم يتم تفعيله بعد من خوادم الموقع.")

    st.markdown("</div>", unsafe_allow_html=True)

# 5. التوقيع
st.markdown("<p style='text-align:center; color:#222; margin-top:60px; font-family:Orbitron;'>OMNISTATS | THE SOVEREIGN BUILD | v9.0 FINAL</p>", unsafe_allow_html=True)
            
