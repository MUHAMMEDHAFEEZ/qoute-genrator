# 🌟 مولد اقتباسات المشاهير العرب المسلمين - API

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Arabic](https://img.shields.io/badge/Language-Arabic-orange.svg)](https://github.com)
[![API](https://img.shields.io/badge/API-Live-brightgreen.svg)](https://qoute-genrator-gf24bzusj-hafeezqoutegenertors-projects.vercel.app)

**API قابل للاستخدام مباشرة** لعرض اقتباسات من مشاهير العرب والمسلمين في ملفات README ومواقع الويب.

## 🚀 الاستخدام السريع في README

أضف هذا السطر في ملف README الخاص بك:

```markdown
![اقتباس يومي](https://qoute-genrator-gf24bzusj-hafeezqoutegenertors-projects.vercel.app/api/quote/image)
```

أو للحصول على اقتباس نصي:

```markdown
<!-- QUOTE:START -->
انتظر التحديث التلقائي...
<!-- QUOTE:END -->
```

## 📡 نقاط النهاية المتاحة (API Endpoints)

### 🖼️ صورة الاقتباس (الأكثر استخداماً)

```http
GET /api/quote/image
```

**مثال للاستخدام:**

```markdown
![Quote](https://qoute-genrator-gf24bzusj-hafeezqoutegenertors-projects.vercel.app/api/quote/image)
```

### 🎲 اقتباس عشوائي JSON

```http
GET /api/quote
```

**Response:**

```json
{
  "personality": "ابن سينا",
  "quote": "الطب مهنة تُحفظ بها الحياة، وعلم يُستكشف به أسرار الوجود",
  "timestamp": "2025-07-16T12:00:00",
  "language": "ar"
}
```

### 🎯 اقتباس من شخصية محددة

```http
GET /api/quote?personality=ابن_سينا
```

### 📝 اقتباس نصي خام

```http
GET /api/quote/text
```

### 👥 قائمة الشخصيات

```http
GET /api/personalities
```

## 🌐 منصات الاستضافة المدعومة

- **Vercel** (مُوصى به) - `vercel.json` متضمن
- **Railway** - `railway.toml` متضمن  
- **Heroku** - `Procfile` و `runtime.txt` متضمن
- **Docker** - `Dockerfile` متضمن
- **أي خدمة تدعم Python/Flask**

## 📋 الميزات

- ✨ **مجموعة متنوعة**: اقتباسات من 10 شخصيات تاريخية مشهورة
- 🎲 **عشوائي وذكي**: اختيار عشوائي أو من شخصية محددة
- 📝 **تنسيق Markdown**: إخراج مُنسق للاستخدام في GitHub
- 💾 **حفظ تلقائي**: إمكانية حفظ الاقتباسات في ملفات
- 🌐 **دعم العربية**: واجهة وتطبيق باللغة العربية بالكامل
- 🎨 **سهل الاستخدام**: واجهة تفاعلية بسيطة

## 👥 الشخصيات المتاحة

| الشخصية | المجال | الفترة الزمنية |
|---------|--------|--------------|
| **ابن سينا** | طب وفلسفة | 980-1037م |
| **الإمام الشافعي** | فقه وأصول | 767-820م |
| **ابن خلدون** | تاريخ واجتماع | 1332-1406م |
| **الجاحظ** | أدب وفكر | 776-868م |
| **أبو نواس** | شعر وأدب | 756-814م |
| **المتنبي** | شعر | 915-965م |
| **ابن رشد** | فلسفة وطب | 1126-1198م |
| **ابن الهيثم** | علوم وبصريات | 965-1040م |
| **الفارابي** | فلسفة وموسيقى | 872-950م |
| **الغزالي** | فقه وفلسفة | 1058-1111م |

## 🚀 التثبيت والتشغيل

### المتطلبات

- Python 3.6 أو أحدث
- لا توجد مكتبات خارجية مطلوبة

### التثبيت

```bash
# استنساخ المشروع
git clone https://github.com/your-username/quote-generator.git
cd quote-generator

# تشغيل المشروع
python main.py
```

### الاستخدام السريع

```python
from main import ArabicQuoteGenerator

# إنشاء مولد الاقتباسات
generator = ArabicQuoteGenerator()

# الحصول على اقتباس عشوائي
personality, quote = generator.get_random_quote()
print(f"{personality}: {quote}")

# توليد اقتباس بتنسيق Markdown
markdown_quote = generator.generate_markdown_quote()
print(markdown_quote)
```

## 📖 أمثلة على الاستخدام

### اقتباس عشوائي

```python
generator = ArabicQuoteGenerator()
personality, quote = generator.get_random_quote()
# المتنبي: "على قدر أهل العزم تأتي العزائم"
```

### اقتباس من شخصية محددة

```python
personality, quote = generator.get_quote_by_personality("ابن سينا")
# ابن سينا: "الطب مهنة تُحفظ بها الحياة"
```

### تنسيق Markdown للـ README

```markdown
> العلم ما نفع، ليس العلم ما حُفظ
>
> — **الإمام الشافعي**
```

## 🎯 الاستخدام في مشاريع GitHub

يمكنك استخدام هذا المولد لإضافة اقتباسات ملهمة إلى ملفات README الخاصة بك:

```python
# إنشاء اقتباس يومي
generator = ArabicQuoteGenerator()
quote_content = generator.save_quote_to_file("daily_quote.md")
```

أو إضافة اقتباس مباشر في README:

> الجهل يؤدي إلى الخوف، والخوف يؤدي إلى الكراهية، والكراهية تؤدي إلى العنف
>
> — **ابن رشد**

## 📁 هيكل المشروع

```text
quote-generator/
│
├── main.py              # الملف الرئيسي للتطبيق
├── requirements.txt     # متطلبات المشروع
├── README.md           # هذا الملف
└── daily_quote.md      # ملف الاقتباس اليومي (يتم إنشاؤه تلقائياً)
```

## 🔧 التطوير والمساهمة

### إضافة شخصيات جديدة

```python
# في main.py، أضف إلى قاموس self.quotes
"اسم الشخصية": [
    "اقتباس 1",
    "اقتباس 2",
    "اقتباس 3"
]
```

### تشغيل الاختبارات

```bash
python -m pytest tests/  # إذا كنت تريد إضافة اختبارات
```

## 🌟 أمثلة من الاقتباسات

### في العلم والمعرفة

> من تكلم فيما لا يعنيه، سمع ما لا يرضيه
>
> — **الإمام الشافعي**

### في الحكمة والفلسفة

> الشك هو الطريق إلى اليقين
>
> — **ابن الهيثم**

### في الأدب والشعر

> دع الأيام تفعل ما تشاء، وطب نفساً إذا حكم القضاء
>
> — **أبو نواس**

## 🤝 المساهمة

نرحب بمساهماتكم! يمكنكم:

1. **إضافة شخصيات جديدة**: أضيفوا مزيداً من المشاهير العرب والمسلمين
2. **تحسين الاقتباسات**: أضيفوا اقتباسات جديدة للشخصيات الموجودة
3. **تطوير الميزات**: أضيفوا ميزات جديدة مثل البحث أو التصنيف
4. **تحسين التوثيق**: ساعدوا في تحسين هذا الملف

### خطوات المساهمة

1. Fork المشروع
2. إنشاء branch جديد (`git checkout -b feature/amazing-feature`)
3. Commit التغييرات (`git commit -m 'Add amazing feature'`)
4. Push إلى Branch (`git push origin feature/amazing-feature`)
5. فتح Pull Request

## 📄 الترخيص

هذا المشروع مرخص تحت رخصة MIT - راجع ملف [LICENSE](LICENSE) للتفاصيل.

## 📞 التواصل

- **GitHub**: [your-username](https://github.com/your-username)
- **Email**: [your.email@example.com](mailto:your.email@example.com)

## 🙏 شكر وتقدير

- شكر خاص لجميع العلماء والمفكرين العرب والمسلمين الذين أثروا الحضارة الإنسانية
- مساهمات المجتمع في تطوير هذا المشروع

---

**⭐ إذا أعجبك هذا المشروع، لا تنس وضع نجمة!**

> الكتاب خير جليس في الزمان، وأفضل صاحب وصديق
>
> — **الجاحظ**