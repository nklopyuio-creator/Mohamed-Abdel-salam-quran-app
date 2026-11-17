import streamlit as st
import streamlit.components.v1 as components

# إعدادات عامة للسيرفر مستقرة وآمنة
st.set_page_config(page_title="المصحف الإلكتروني المتكامل", page_icon="📖", layout="centered")

# دالة قراءة ملفات الواجهة الخارجية الثلاثة وحقنها برمجياً
def get_custom_interface():
    with open("index.html", "r", encoding="utf-8") as html_file:
        html_code = html_file.read()
    with open("style.css", "r", encoding="utf-8") as css_file:
        css_code = css_file.read()
    with open("script.js", "r", encoding="utf-8") as js_file:
        js_code = js_file.read()
        
    # دمج التنسيقات والأزرار والحركات في قالب مستقل تماماً
    full_interface = html_code.replace('<link rel="stylesheet" href="style.css">', f'<style>{css_code}</style>')
    full_interface = full_interface.replace('<script src="script.js"></script>', f'<script>{js_code}</script>')
    return full_interface

# عرض الواجهة الاحترافية للمستخدم دون الحاجة لاتصالات إنترنت من السيرفر
try:
    ui_content = get_custom_interface()
    components.html(ui_content, height=950, scrolling=True)
except Exception as e:
    st.error(f"يرجى التأكد من وجود ملفات index.html و style.css و script.js بجانب هذا الملف. الخطأ: {e}")
  
