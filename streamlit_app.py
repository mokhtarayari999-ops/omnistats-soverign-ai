import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعداد الصفحة والسمة الذهبية بوضوح عالٍ
st.set_page_config(page_title="Arabic Pro | الواجهة الواضحة", layout="wide")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* الخلفية سوداء فحمية لزيادة تباين الألوان */
    .stApp { 
        background-color: #000000; 
        font-family: 'Cairo', sans-serif; 
        direction: RTL; 
        text-align: right; 
    }
    
    /* جعل العناوين باللون الذهبي المشع */
    h1, h2, h3 { 
        color: #FFD700 !important; 
        font-weight: 800 !important;
        text-shadow: 2px 2px 4px #000000;
    }
    
    /* جعل النصوص العادية باللون الأبيض الناصع والخط سميك */
    p, span, label, .stMarkdown { 
        color: #FFFFFF !important; 
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }
    
    /* تحسين وضوح صناديق الإدخال */
    input { 
        background-color: #1a1a1a !important; 
        color: #FFD700 !important; 
        border: 2px solid #FFD700 !important;
        font-size: 1.2rem !important;
    }

    /* تنسيق الأرقام والنتائج لتكون واضحة جداً */
    [data-testid="stMetricValue"] { 
        color: #FFD700 !important; 
        font-size: 2.5rem !important; 
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 ARABIC PRO: التحليل الرياضي الشامل")

# 2. سجل النتائج
if "match_history" not in st.session_state:
    st.session_state.match_history = []

# 3. إدخال البيانات يدوياً (قوة الهجوم والدفاع)
st.subheader("📊 أدخل بيانات المباراة بدقة")
col_h, col_a = st.columns(2)

with col_h:
    st.markdown("### 🏠 الفريق المضيف")
    h_name = st.text_input("اسم فريق الأرض", "النصر")
    h_atk = st.slider("🚀 قوة الهجوم يدوياً", 0, 100, 80)
    h_def = st.slider("🛡️ قوة الدفاع يدوياً", 0, 100, 70)

with col_a:
    st.markdown("### ✈️ الفريق الضيف")
    a_name = st.text_input("اسم فريق الخصم", "الهلال")
    a_atk = st.slider("🚀 قوة الهجوم يدوياً ", 0, 100, 85)
    a_def = st.slider("🛡️ قوة الدفاع يدوياً ", 0, 100, 75)

st.divider()

# 4. زر التحليل وتوليد النتيجة
if st.button("🔥 ابدأ التحليل الذهبي الآن"):
    # حسابات بسيطة للتوقع
    h_chance = (h_atk + h_def) / 2 + 5 # ميزة الأرض
    a_chance = (a_atk + a_def) / 2
    
    total = h_chance + a_chance
    win_p = round((h_chance / total) * 100, 1)
    loss_p = round(100 - win_p, 1)
    
    # عرض النتائج بخط كبير وواضح
    c1, c2, c3 = st.columns(3)
    c1.metric(f"فوز {h_name}", f"{win_p}%")
    c2.metric("النتيجة المتوقعة", f"{int(h_atk/30)}-{int(a_atk/30)}")
    c3.metric(f"فوز {a_name}", f"{loss_p}%")
    
    # حفظ في السجل
    st.session_state.match_history.append({
        "التوقيت": datetime.now().strftime("%H:%M"),
        "المباراة": f"{h_name} vs {a_name}",
        "التوقع": f"{int(h_atk/30)}-{int(a_atk/30)}",
        "الأقرب للفوز": h_name if win_p > loss_p else a_name
    })

# 5. سجل النتائج الواضح
st.write("---")
st.subheader("📜 سجل نتائجك السابقة")
if st.session_state.match_history:
    df = pd.DataFrame(st.session_state.match_history)
    st.table(df) # جدول أبيض واضح على خلفية سوداء
else:
    st.info("لا توجد تحليلات سابقة بعد.")

st.sidebar.markdown("<h2 style='color:#FFD700;'>ARABIC PRO AI</h2>", unsafe_allow_html=True)
if st.sidebar.button("🗑️ مسح السجل بالكامل"):
    st.session_state.match_history = []
    st.rerun()
