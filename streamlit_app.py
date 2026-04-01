import streamlit as st
import numpy as np
import time

# --- 🏗️ الهندسة المعمارية السيادية الفائقة ---
st.set_page_config(page_title="ARABIC PRO | SUPREME", layout="wide", initial_sidebar_state="collapsed")

# --- 🎨 CSS الكوانتي (إصدار السيادة 2026 - محمي تماماً) ---
st.markdown("""
<style>
    @import url('https://googleapis.com');
    .stApp { background: #000; color: #D4AF37; font-family: 'Cairo', sans-serif; }
    .result-frame { background: rgba(255,255,255,0.02); border: 2px solid #D4AF37; border-radius: 30px; padding: 25px; text-align: center; margin-top: 20px; }
    .score-quantum { font-size: 6.5rem; font-weight: 900; color: #D4AF37; text-shadow: 0 0 40px #D4AF37; line-height: 1; }
    .info-node { background: #0c0c0c; border: 1px solid rgba(212,175,55,0.3); border-radius: 15px; padding: 15px; flex: 1; min-width: 100px; }
    .odds-badge { background: #D4AF37; color: #000; border-radius: 8px; padding: 4px 8px; font-weight: 900; margin-top: 5px; display: inline-block; font-size: 0.9rem; }
    .stButton>button { background: linear-gradient(45deg, #D4AF37, #8A6D3B) !important; color: #000 !important; font-weight: 900 !important; border-radius: 50px !important; height: 3.8rem !important; font-size: 1.6rem !important; border: none !important; width: 100% !important; transition: 0.3s; box-shadow: 0 5px 20px rgba(212,175,55,0.4) !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#D4AF37; letter-spacing:3px;'>ARABIC PRO 🏆</h1>", unsafe_allow_html=True)

# واجهة المدخلات
c1, c2 = st.columns(2)
with c1:
    h_n = st.text_input("🏠 المضيف:", "نادي بارادو")
    h_atk = st.number_input("قوة الهجوم (1-10):", 1.0, 10.0, 7.1)
    h_def = st.number_input("صلابة الدفاع (1-10):", 1.0, 10.0, 6.9)
with c2:
    a_n = st.text_input("🚀 الضيف:", "شباب بلوزداد")
    a_atk = st.number_input("قوة الهجوم (1-10) :", 1.0, 10.0, 8.0)
    a_def = st.number_input("صلابة الدفاع (1-10) :", 1.0, 10.0, 8.6)

if st.button("🔱 إطلاق المحرك الاستخباري الشامل"):
    with st.status("📡 جاري استنفار كافة الحواسيب الإحصائية...", expanded=True) as status:
        time.sleep(1)
        st.write("🎲 محاكاة 1,000,000 سيناريو احتمالي...")
        time.sleep(0.5)
        st.write("📊 تحليل رادار الاستحواذ وتوقيت الأهداف...")
        status.update(label="✅ تم استخراج التقرير السيادي الكامل!", state="complete")
        
        # محرك المحاكاة
        h_idx = max(0.2, (h_atk*(11-a_def))/25); a_idx = max(0.2, (a_atk*(11-h_def))/25)
        h_s = np.random.poisson(h_idx, 1000000); a_s = np.random.poisson(a_idx, 1000000)
        
        w_h, dr, w_a = (h_s>a_s).mean()*100, (h_s==a_s).mean()*100, (h_s<a_s).mean()*100
        odd_h, odd_dr, odd_a = round(100/w_h, 2), round(100/dr, 2), round(100/w_a, 2)
        
        # المعطيات الإضافية
        pos_h = int((h_atk / (h_atk + a_atk)) * 100)
        pressure = int((h_atk + a_atk) * 0.95)
        timing = "الشوط الثاني" if (h_atk + a_atk) > 14 else "الشوط الأول"
        penalty = "عالية (🔥)" if (h_atk + a_atk) > 15 else "متوسطة (⚖️)"

        # ✅ بناء الواجهة النهائية الشاملة (تجميع كل الإبداع)
        out = "<div class='result-frame'>"
        out += f"<div class='score-quantum'>{int(np.mean(h_s))} - {int(np.mean(a_s))}</div>"
        out += f"<h2 style='color:#fff;'>{h_n} VS {a_n}</h2>"
        
        # 1. رادار الهيمنة
        out += f"<div style='margin:15px 0; background:rgba(212,175,55,0.05); border-radius:15px; padding:10px; border:1px solid #D4AF37;'>"
        out += f"<p style='margin:0; font-size:0.8rem; color:#888;'>رادار الهيمنة المتوقعة (Possession)</p>"
        out += f"<div style='display:flex; justify-content:between; align-items:center; padding:5px; font-weight:bold;'>"
        out += f"<span style='flex:1; text-align:left;'>{pos_h}%</span>"
        out += f"<div style='flex:2; height:8px; background:#222; border-radius:5px; margin:0 10px;'><div style='width:{pos_h}%; height:100%; background:#D4AF37; border-radius:5px;'></div></div>"
        out += f"<span style='flex:1; text-align:right;'>{100-pos_h}%</span></div></div>"

        # 2. شبكة المراهنات (الأرقام الذهبية)
        out += "<div style='display:flex; justify-content:center; gap:8px; flex-wrap:wrap;'>"
        out += f"<div class='info-node'><p>فوز المضيف</p><h3>{w_h:.1f}%</h3><div class='odds-badge'>{odd_h}</div></div>"
        out += f"<div class='info-node'><p>التعادل</p><h3>{dr:.1f}%</h3><div class='odds-badge'>{odd_dr}</div></div>"
        out += f"<div class='info-node'><p>فوز الضيف</p><h3>{w_a:.1f}%</h3><div class='odds-badge'>{odd_a}</div></div>"
        out += "</div>"

        # 3. الأحداث الجانبية (ركنيات، بطاقات، جزاء)
        out += "<div style='display:flex; justify-content:center; gap:8px; flex-wrap:wrap; margin-top:10px;'>"
        out += f"<div class='info-node' style='border-color:#D4AF37;'><p>🚩 ركنيات</p><h3>{int((h_atk+a_atk)*0.75)}</h3></div>"
        out += f"<div class='info-node' style='border-color:#FFD700;'><p>🟨 بطاقات</p><h3>{int((h_def+a_def)*0.28)}</h3></div>"
        out += f"<div class='info-node' style='border-color:#ff4b4b;'><p>⚽ ضربة جزاء</p><h3>{penalty}</h3></div>"
        out += "</div>"

        # 4. الرؤية الاستراتيجية وتغطية المخاطر
        out += f"<div style='background:rgba(212,175,55,0.05); border-radius:15px; padding:15px; margin-top:20px; border:1px dashed #D4AF37; text-align:right;'>"
        out += f"<p style='color:#D4AF37; margin:0;'>💡 <b>التقرير السيادي:</b></p>"
        out += f"<p style='color:#ccc; margin:0; font-size:0.85rem;'>مؤشر التسونامي: <b>{pressure}/20</b>. الحسم المتوقع في: <b>{timing}</b>.</p>"
        out += f"<p style='color:#D4AF37; margin:5px 0 0 0; font-size:0.85rem;'>🛡️ تغطية المخاطر ({h_n} أو تعادل): <b>{w_h+dr:.1f}%</b></p></div>"
        
        out += "</div>"
        st.markdown(out, unsafe_allow_html=True)
        st.balloons()
    
