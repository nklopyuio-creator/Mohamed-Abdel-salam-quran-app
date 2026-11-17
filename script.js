const quranSurahsList = [
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

// وظيفة التنقل المتعدد بين الصفحات وإخفاء الباقي
function switchPage(pageId) {
    // 1. إخفاء كافة الصفحات وإزالة الحالة النشطة
    document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
    document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
    
    // 2. إظهار الصفحة المطلوبة وتنشيط زر التوجيه الخاص بها
    document.getElementById(`page-${pageId}`).classList.add('active');
    
    // ربط تنشيط الأزرار العلوية حسب اسم الصفحة المفتوحة
    const buttons = document.querySelectorAll('.nav-btn');
    if(pageId === 'home') buttons[0].classList.add('active');
    if(pageId === 'listen') buttons[1].classList.add('active');
    if(pageId === 'read') buttons[2].classList.add('active');
    
    // إيقاف الصوت تلقائياً عند مغادرة صفحة الاستماع حفاظاً على راحة المستخدم
    if(pageId !== 'listen') {
        const player = document.getElementById("audioPlayer");
        if(player) player.pause();
    }
}

// تهيئة القوائم عند التحميل
document.addEventListener("DOMContentLoaded", () => {
    const audioSelect = document.getElementById("audioSurahSelect");
    const readSelect = document.getElementById("readSurahSelect");
    
    quranSurahsList.forEach((name, index) => {
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

function fetchSurahText() {
    const num = document.getElementById("readSurahSelect").value;
    const display = document.getElementById("quranDisplay");
    
    display.innerHTML = "جاري فتح آيات كتاب الله الكريم...";
    
    fetch(`https://alquran.cloud{num}`)
        .then(res => res.json())
        .then(data => {
            const ayahs = data.data.ayahs;
            let fullText = "";
            
            if (num !== "1" && num !== "9") {
                fullText += "<b style='color:#15803D;'>بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</b><br><br>";
            }
            
            ayahs.forEach(ayah => {
                let txt = ayah.text;
                if (ayah.numberInSurah === 1 && num !== "1") {
                    txt = txt.replace("بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ", "");
                }
                fullText += `${txt} <span style='color:#D97706;'>﴿${ayah.numberInSurah}﴾</span> `;
            });
            display.innerHTML = fullText;
        })
        .catch(err => {
            display.innerHTML = "فشل جلب الآيات الكريمة، تأكد من اتصالك بالإنترنت.";
        });
}
