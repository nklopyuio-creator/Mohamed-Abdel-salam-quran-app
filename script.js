// مصفوفة بأسماء سور القرآن الكريم الـ 114 مرتبة بالتسلسل
const quranSurahsFullList = [
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
];

function switchPage(pageId) {
    document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
    document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
    
    document.getElementById(`page-${pageId}`).classList.add('active');
    
    const navButtons = document.querySelectorAll('.nav-btn');
    if(pageId === 'home') navButtons[0].classList.add('active');
    if(pageId === 'listen') navButtons[1].classList.add('active');
    if(pageId === 'read') navButtons[2].classList.add('active');
    if(pageId === 'developer') navButtons[3].classList.add('active');
    
    if(pageId !== 'listen') {
        const player = document.getElementById("audioPlayer");
        if(player) player.pause();
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const audioSelect = document.getElementById("audioSurahSelect");
    const readSelect = document.getElementById("readSurahSelect");
    
    // توليد قائمة الـ 114 سورة كاملة داخل خيارات التحكم
    quranSurahsFullList.forEach((name, index) => {
        let optA = document.createElement("option");
        optA.value = index + 1;
        optA.textContent = `${index + 1}. سورة ${name}`;
        audioSelect.appendChild(optA);
        
        let optR = document.createElement("option");
        optR.value = index + 1;
        optR.textContent = `${index + 1}. سورة ${name}`;
        readSelect.appendChild(optR);
    });
});

function playAudio() {
    const server = document.getElementById("reciterSelect").value;
    const num = document.getElementById("audioSurahSelect").value;
    const player = document.getElementById("audioPlayer");
    const formatted = num.padStart(3, '0');
    player.src = `${server}${formatted}.mp3`;
    player.play();
}

// دالة جلب وعرض القرآن الكريم كاملاً متخطية حظر السيرفرات
function fetchSurahText() {
    const num = parseInt(document.getElementById("readSurahSelect").value);
    const display = document.getElementById("quranDisplay");
    
    display.innerHTML = "جاري فتح آيات كتاب الله الشريف من المصحف الرقمي المحلي...";
    
    // استخدام قاعدة بيانات مفتوحة ومستقرة ومخزنة سحابياً بصيغة JSON المباشرة لتفادي حظر المتصفحات
    fetch(`https://jsdelivr.net`)
        .then(res => {
            if (!res.ok) throw new Error("فشل تحميل قاعدة البيانات");
            return res.json();
        })
        .then(data => {
            // تصفية الآيات التابعة للسورة المختارة فقط من الملف الشامل
            const surahAyahs = data.quran.filter(item => item.surah === num);
            let fullText = "";
            
            // إضافة البسملة في بداية السور عدا سورة الفاتحة والتوبة
            if (num !== 1 && num !== 9) {
                fullText += "<b style='color:#15803D; font-size: 28px;'>بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</b><br><br>";
            }
            
            surahAyahs.forEach(ayah => {
                let txt = ayah.text;
                // تنظيف نص الآية الأولى من البسملة المدمجة لجمال العرض والتنسيق
                if (ayah.verse === 1 && num !== 1) {
                    txt = txt.replace("بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ", "");
                }
                fullText += `${txt} <span style='color:#D97706;'>﴿${ayah.verse}﴾</span> `;
            });
            
            display.innerHTML = fullText;
        })
        .catch(err => {
            display.innerHTML = "<b style='color:#DC2626;'>حدث خطأ أثناء تحميل المصحف. يرجى التحقق من اتصال الإنترنت وإعادة المحاولة.</b>";
            console.error(err);
        });
          }
