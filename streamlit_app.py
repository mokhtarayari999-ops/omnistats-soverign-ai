import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعداد الصفحة والواجهة الاحترافية (Black & Gold)
st.set_page_config(page_title="Arabic Pro | الإصدار الذهبي", layout="wide")

# تنسيق CSS مخصص للوضوح العالي وإزالة الـ Cursor
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp { 
        background-color: #000000; 
        font-family: 'Cairo', sans-serif; 
        direction: RTL; 
        text-align: right; 
    }
    
    /* العناوين بالذهبي المشع */
    h1, h2, h3 { 
        color: #D4AF37 !important; 
        font-weight: 900 !important;
        text-align: center;
    }
    
    /* النصوص والملصقات باللون الأبيض الناصع */
    label, p, span { 
        color: #FFFFFF !important; 
        font-size: 1.2rem !important;
        font-weight: bold !important;
    }
    
    /* تنسيق صناديق الإدخال الرقمي (بدون شريط تمرير) */
    .stNumberInput input { 
        background-color: #1a1a1a !important; 
        color: #D4AF37 !important; 
        border: 2px solid #D4AF37 !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        text-align: center !important;
        border-radius: 10px !important;
    }

    /* تنسيق الأزرار */
    .stButton>button { 
        background-color: #D4AF37; 
        color: black; 
        font-weight: 900; 
        font-size: 1.3rem;
        border-radius: 15px; 
        width: 100%;
        height: 3.5em;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي كما في صورتك
st.title("🏆 ARABIC PRO")
st.markdown("### نظام التوقيع والتحليل اليدوي")

# سجل النتائج في الذاكرة
if "history" not in st.session_state:
    st.session_state.history = []

# 2. منطقة الإدخال الرقمي المباشر
st.write("---")
st.markdown("### 📝 إدخال بيانات المباراة يدوياً بالارقام")

col_h, col_a = st.columns(2)

with col_h:
    st.markdown("### 🏠 الفريق المضيف")
    h_name = st.text_input("اسم الفريق المضيف", "الأهلي")
    # استبدال الـ Slider بـ Number Input (كتابة فقط)
    h_atk = st.number_input("قوة الهجوم (المضيف)", 0, 100, 75, key="h_atk")
    h_def = st.number_input("قوة الدفاع (المضيف)", 0, 100, 70, key="h_def")

with col_a:
    st.markdown("### ✈️ الفريق الضيف")
    a_name = st.text_input("اسم الفريق الضيف", "الزمالك")
    # استبدال الـ Slider بـ Number Input (كتابة فقط)
    a_atk = st.number_input("قوة الهجوم (الضيف)", 0, 100, 70, key="a_atk")
    a_def = st.number_input("قوة الدفاع (الضيف)", 0, 100, 75, key="a_def")

# 3. زر التحليل والنتائج
if st.button("✨ تشغيل التحليل الذهبي الآن"):
    # حساب احتمالات بسيطة بناءً على الأرقام المدخلة
    h_score = (h_atk + h_def) / 2
    a_score = (a_atk + a_def) / 2
    total = h_score + a_score
    win_p = round((h_score / total) * 100, 1)
    
    st.markdown("---")
    st.subheader("📊 التوقعات النهائية")
    c1, c2, c3 = st.columns(3)
    c1.metric(f"فوز {h_name}", f"{win_p}%")
    c2.metric("النتيجة المتوقعة", f"{int(h_atk/30)}-{int(a_atk/35)}")
    c3.metric(f"فوز {a_name}", f"{100-win_p}%")
    
    # إضافة للسجل
    st.session_state.history.append({
        "الوقت": datetime.now().strftime("%H:%M"),
        "المباراة": f"{h_name} vs {a_name}",
        "التوقع": f"{int(h_atk/30)}-{int(a_atk/35)}",
        "الأفضلية": h_name if win_p > 50 else a_name
    })

# 4. سجل النتائج الواضح
st.write("---")
st.subheader("📜 سجل نتائجك")
if st.session_state.history:
    st.table(pd.DataFrame(st.session_state.history))
else:
    st.info("لا توجد تحليلات مسجلة.")

st.sidebar.markdown("<h2 style='color:#D4AF37;'>ARABIC PRO</h2>", unsafe_allow_html=True)
if st.sidebar.button("🗑️ مسح السجل"):
    st.session_state.history = []
    st.rerun()
