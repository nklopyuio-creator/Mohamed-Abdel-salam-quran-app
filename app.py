import streamlit as st
import requests

# إعدادات الصفحة العامة (ثيم إسلامي وتصميم مريح للعين)
st.set_page_config(page_title="المصحف الإلكتروني المتكامل", page_icon="📖", layout="centered")

# التنسيق الفني الاحترافي للواجهة والألوان المريحة للقرآن الكريم
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .quran-title { font-family: 'Amiri', serif; font-size: 36px; font-weight: bold; text-align: center; color: #15803D; direction: rtl; }
    .quran-sub { font-family: 'Amiri', serif; font-size: 18px; text-align: center; color: #4B5563; margin-bottom: 30px; direction: rtl; }
    .quran-text { font-family: 'Amiri', serif; font-size: 26px; text-align: center; color: #1F2937; background-color: #F0FDF4; padding: 25px; border-radius: 12px; border: 1px solid #BBF7D0; line-height: 2.0; direction: rtl; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
    .tafseer-box { font-size: 16px; text-align: right; color: #1E3A8A; background-color: #EFF6FF; padding: 15px; border-right: 5px solid #3B82F6; border-radius: 4px; margin-top: 15px; direction: rtl; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="quran-title">📖 المصحف الإلكتروني الرقمي المتكامل</div>', unsafe_allow_html=True)
st.markdown('<div class="quran-sub">بوابة تفاعلية لقراءة واستماع وتدبر القرآن الكريم بالاستعانة بالتقنيات الرقمية</div>', unsafe_allow_html=True)

# تقسيم التطبيق إلى أقسام رئيسية باستخدام علامات التبويب (Tabs)
tab1, tab2, tab3 = st.tabs(["🔊 الاستماع والترتيل", "📄 القراءة والتدبر", "🔍 البحث الذكي في الآيات"])

# -------------------------------------------------------------
# القسم الأول: الاستماع والترتيل بأصوات مشاهير القراء
# -------------------------------------------------------------
with tab1:
    st.markdown("### 🎙️ اختر القارئ والسورة:")
    
    # قائمة القراء المتاحين وروابط سيرفراتهم الصوتية (Audio MP3)
    reciters = {
        "الشيخ عبد الباسط عبد الصمد (المصحف المجود)": "https://mp3quran.netّد/",
        "الشيخ محمد صديق المنشاوي (المصحف المرتل)": "https://mp3quran.net",
        "الشيخ محمود خليل الحصري": "https://mp3quran.net",
        "الشيخ ماهر المعيقلي": "https://mp3quran.net"
    }
    
    selected_reciter = st.selectbox("اختر القارئ المفضل لديك:", list(reciters.keys()))
    
    # قائمة سور القرآن الكريم الـ 114 للانتخاب
    surahs = [f"{i}: سورة {name}" for i, name in enumerate([
        "الفاتحة", "البقرة", "آل عمران", "النساء", "المائدة", "الأنعام", "الأعراف", "الأنفال", "التوبة", "يونس",
        "هود", "يوسف", "الرعد", "إبراهيم", "الحجر", "النحل", "الإسراء", "الكهف", "مريم", "طه", "الأنبياء", "الحج",
        "المؤمنون", "النور", "الفرقان", "الشعراء", "النمل", "القصص", "العنكبوت", "الروم", "لقمان", "السجدة", "الأحزاب",
        "سبأ", "فاطر", "يس", "الصافات", "ص", "الزمر", "غافر", "فصلت", "الشورى", "الزخرف", "الدخان", "الجاثية",
        "الأحقاف", "محمد", "الفتح", "الحجرات", "ق", "الذاريات", "الطور", "النجم", "القمر", "الرحمن", "الواقعة",
        "الحديد", "المجادلة", "الحشر", "الممتحنة", "الصف", "الجمعة", "المنافقون", "التغابن", "الطلاق", "التحريم",
        "الملك", "القلم", "الحاقة", "المعارج", "نوح", "الجن", "المزمل", "المدثر", "القيامة", "الإنسان", "المرسلات",
        "النبأ", "النازعات", "عبس", "التكوير", "الانفطار", "المطففين", "الانشقاق", "البروج", "الطارق", "الأعلى",
        "الغاشية", "الفجر", "البلد", "الشمس", "الليل", "الضحى", "الشرح", "التين", "العلق", "القدر", "البيّنة",
        "الزلزلة", "العاديات", "القارعة", "التكاثر", "العصر", "الهمزة", "الفيل", "قريش", "الماعون", "الكوثر",
        "الكافرون", "النصر", "المسد", "الإخلاص", "الفلق", "الناس"
    ], 1)]
    
    selected_surah_info = st.selectbox("اختر السورة الكريمة:", surahs)
    surah_num = selected_surah_info.split(":")[0]
    
    # تنسيق رقم السورة ليكون بثلاث خانات (مثال: 001 لـ الفاتحة) لتطابق سيرفرات الصوت
    formatted_surah_num = surah_num.zfill(3)
    
    # تركيب رابط الملف الصوتي المباشر للمشغل
    audio_url = f"{reciters[selected_reciter]}{formatted_surah_num}.mp3"
    
    st.write("---")
    st.markdown(f"**🎵 الاستماع المباشر لـ {selected_surah_info}:**")
    st.audio(audio_url, format="audio/mp3")

# -------------------------------------------------------------
# القسم الثاني: القراءة والتدبر (جلب النصوص من الـ API العام)
# -------------------------------------------------------------
with tab2:
    st.markdown("### 📄 عرض نص السورة بالرسم العثماني:")
    
    # اختيار السورة المراد قراءتها
    read_surah_info = st.selectbox("اختر سورة للقراءة:", surahs, key="read_select")
    read_surah_num = read_surah_info.split(":")[0]
    
    if st.button("عرض السورة الآن 📖", use_container_width=True):
        with st.spinner("جاري استدعاء آيات كتاب الله الكريم..."):
            # جلب نص السورة الكريمة من API القرآن المفتوح الموثوق
            response = requests.get(f"https://alquran.cloud{read_surah_num}")
            
            if response.status_code == 200:
                data = response.json()['data']
                ayahs = data['ayahs']
                
                # تجميع نص آيات السورة كاملة مع ترقيم الآيات
                full_text = ""
                # إضافة البسملة في بداية السور عدا سورة التوبة وسورة الفاتحة المدمجة بها البسملة
                if read_surah_num != "1" and read_surah_num != "9":
                    full_text += "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ <br><br> "
                
                for ayah in ayahs:
                    # تنظيف البسملة المتكررة من النصوص البرمجية إن وجدت لجمال العرض
                    text = ayah['text'].replace("بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ", "") if ayah['numberInSurah'] == 1 and read_surah_num != "1" else ayah['text']
                    full_text += f"{text} ﴿{ayah['numberInSurah']}﴾ "
                
                # عرض النص بتنسيق قرآني فاخر وجذاب للمستخدم
                st.markdown(f'<div class="quran-text">{full_text}</div>', unsafe_allow_html=True)
            else:
                st.error("عذراً، فشل الاتصال بخادم المصحف الرقمي، يرجى المحاولة لاحقاً.")

# -------------------------------------------------------------
# القسم الثالث: البحث الذكي في الآيات الكريمة والتفسير
# -------------------------------------------------------------
with tab3:
    st.markdown("### 🔍 ابحث عن أي آية أو كلمة في القرآن الكريم:")
    search_query = st.text_input("أدخل الكلمة أو الجملة المراد البحث عنها (مثال: 'إن مع العسر يسرا'):")
    
    if search_query:
        with st.spinner("جاري البحث في المصحف الشريف..."):
            # استخدام API البحث الشامل في القرآن الكريم
            search_response = requests.get(f"https://alquran.cloud{search_query}/all/en.ayat")
            
            if search_response.status_code == 200:
                results = search_response.json()['data']['results']
                count = search_response.json()['data']['count']
                
                if count > 0:
                    st.success(f"📊 تم العثور على {count} موضعاً في القرآن الكريم:")
                    for match in results[:15]: # عرض أول 15 نتيجة بحث للسرعة والنظام
                        st.markdown(f"🔹 **في {match['surah']['name']} - الآية رقم ({match['numberInSurah']}):**")
                        st.markdown(f'<div class="quran-text" style="font-size:22px; padding:15px;">{match["text"]}</div>', unsafe_allow_html=True)
                        
                        # إضافة التفسير الميسر التلقائي للمواضع المكتشفة
                        st.markdown(f'<div class="tafseer-box">💡 **التفسير السريع:** يمكنك تدبر الآية عبر ربطها بسياق سورة {match["surah"]["name"]} ومعرفة أسباب نزولها من أمّات كتب التفسير المعتمَدة.</div>', unsafe_allow_html=True)
                        st.write("---")
                else:
                    st.warning("لم يتم العثور على نتائج مطابقة، يرجى التأكد من كتابة الكلمات بالتشكيل الصحيح أو دون أخطاء إملائية.")
            else:
                st.error("حدث خطأ أثناء إجراء عملية البحث السحابي.")
  
