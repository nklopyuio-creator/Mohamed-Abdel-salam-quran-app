import streamlit as st
import streamlit.components.v1 as components
import os

# إعدادات عامة للسيرفر مستقرة وآمنة لضمان التوافق مع الهواتف
st.set_page_config(page_title="المصحف الإلكتروني المتكامل", page_icon="📖", layout="centered")

def get_custom_interface():
    # التأكد من المسارات وقراءة الملفات بترميز تدعمه كافة المتصفحات
    html_path = "index.html"
    css_path = "style.css"
    js_path = "script.js"
    
    if os.path.exists(html_path) and os.path.exists(css_path) and os.path.exists(js_path):
        with open(html_path, "r", encoding="utf-8") as html_file:
            html_code = html_file.read()
        with open(css_path, "r", encoding="utf-8") as css_file:
            css_code = css_file.read()
        with open(js_path, "r", encoding="utf-8") as js_file:
            js_code = js_file.read()
            
        # دمج الأكواد بشكل مباشر وآمن يمنع تعارض الحماية
        full_interface = html_code.replace('<link rel="stylesheet" href="style.css">', f'<style>{css_code}</style>')
        full_interface = full_interface.replace('<script src="script.js"></script>', f'<script>{js_code}</script>')
        return full_interface
    else:
        return "<h3>خطأ: لم يتم العثور على ملفات الواجهة الأساسية داخل المستودع.</h3>"

# تشغيل واجهة المصحف الشريف وكرت المطور محمد عبدالسلام شاهين
try:
    ui_content = get_custom_interface()
    # استخدام ارتفاع ديناميكي مريح وتفعيل التمرير الداخلي لمنع التداخل
    components.html(ui_content, height=1000, scrolling=True)
except Exception as e:
    st.error(f"حدث خطأ أثناء تحميل مكونات الواجهة: {e}")
  
