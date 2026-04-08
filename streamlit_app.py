import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعداد الصفحة وتوسيع العرض للهاتف
st.set_page_config(page_title="ARABIC PRO AI", layout="wide")

# 2. كود الـ CSS "الخارق" للواجهة الذهبية والسوداء الفاخرة
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* الخلفية سوداء فخمة */
    .stApp { background-color: #000000; font-family: 'Cairo', sans-serif; direction: RTL; text-align: right; }
    
    /* العنوان الرئيسي الذهبي */
    .main-title { color: #FFD700; font-size: 3rem; font-weight: 900; text-align: center; text-shadow: 2px 2px 10px #D4AF37; margin-bottom: 20px; }
    
    /* النصوص والملصقات بالأبيض الناصع */
    label, p { color: #FFFFFF !important; font-size: 1.3rem !important; font-weight: bold !important; text-align: right; }
    
    /* صناديق الأرقام الذهبية (بديلة المنزلقات الحمراء) */
    .stNumberInput div div input { 
        background-color: #111111 !important; 
        color: #FFD700 !important; 
        border: 2px solid #FFD700 !important;
        font-size: 1.8rem !important;
        height: 65px !important;
        text-align: center !important;
        border-radius: 15px !important;
    }
    
    /* زر التحليل العميق الذهبي الكبير */
    .stButton>button { 
        background-color: #FFD700 !important; color: black !important; font-weight: 900 !important; 
        border-radius: 20px !important; width: 100% !important; height: 4em !important; 
        font-size: 1.4rem !important; border: 2px solid white !important; margin-top: 20px;
    }
    
    /* تنسيق سجل النتائج ليكون واضحاً وغير باهت */
    .stDataFrame, .stTable { background-color: #111111 !important; border: 1px solid #FFD700 !important; border-radius: 10px; }
    
    /* إخفاء أي منزلقات (Sliders) قديمة */
    .stSlider { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. محتوى التطبيق
st.markdown('<div class="main-title">🏆 ARABIC PRO</div>', unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

# 4. منطقة الإدخال الرقمي المباشر (بدون أشرطة حمراء)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏠 الفريق المضيف")
    h_name = st.text_input("اسم الفريق", "الأهلي", key="hn")
    h_atk = st.number_input("🚀 قوة الهجوم", 0, 100, 80, key="ha")
    h_def = st.number_input("🛡️ قوة الدفاع", 0, 100, 75, key="hd")

with col2:
    st.markdown("### ✈️ الفريق الضيف")
    a_name = st.text_input("اسم الفريق ", "الزمالك", key="an")
    a_atk = st.number_input("🚀 قوة الهجوم ", 0, 100, 70, key="aa")
    a_def = st.number_input("🛡️ قوة الدفاع ", 0, 100, 80, key="ad")

st.write("---")

# 5. زر التحليل والنتائج الواضحة جداً
if st.button("✨ تنفيذ التحليل الذهبي العميق"):
    with st.spinner('جاري التحليل السيادي...'):
        win_p = round(((h_atk + h_def) / (h_atk + h_def + a_atk + a_def)) * 100, 1)
        score = f"{int(h_atk/30)} - {int(a_atk/35)}"
        
        st.markdown(f"### 📊 النتيجة المتوقعة: <span style='color:#FFD700;'>{score}</span>", unsafe_allow_html=True)
        st.markdown(f"### 📈 نسبة فوز {h_name}: <span style='color:#FFD700;'>{win_p}%</span>", unsafe_allow_html=True)
        
        # حفظ في السجل
        st.session_state.history.insert(0, {
            "الوقت": datetime.now().strftime("%H:%M"),
            "المباراة": f"{h_name} vs {away_name if 'away_name' in locals() else a_name}",
            "التوقع": score,
            "النسبة": f"{win_p}%"
        })

# 6. سجل النتائج الاحترافي
st.write("---")
st.markdown("## 📜 سجل نتائج التحليلات")
if st.session_state.history:
    st.table(pd.DataFrame(st.session_state.history))
else:
    st.info("السجل فارغ حالياً، ابدأ بإدخال بيانات أول مباراة.")

# القائمة الجانبية
st.sidebar.markdown("<h2 style='color:#FFD700;'>ARABIC PRO</h2>", unsafe_allow_html=True)
if st.sidebar.button("🗑️ مسح السجل"):
    st.session_state.history = []
    st.rerun()
                
