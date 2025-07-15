# 🌟 API مولد اقتباسات المشاهير العرب المسلمين

![اقتباس ملهم](http://localhost:5000/api/quote/image)

[![Deploy to Vercel](https://img.shields.io/badge/Deploy%20to-Vercel-000000?style=flat&logo=vercel)](https://vercel.com/new/clone?repository-url=https://github.com/your-username/arabic-quote-api)
[![Deploy to Railway](https://img.shields.io/badge/Deploy%20to-Railway-0B0D0E?style=flat&logo=railway)](https://railway.app/new/template)
[![Deploy to Heroku](https://img.shields.io/badge/Deploy%20to-Heroku-430098?style=flat&logo=heroku)](https://heroku.com/deploy)

## 🚀 استخدام فوري - أضف هذا السطر إلى README الخاص بك:

```markdown
![اقتباس يومي](https://your-api-url.vercel.app/api/quote/image)
```

**النتيجة:** صورة جميلة بخلفية متدرجة تعرض اقتباساً ملهماً من التراث العربي الإسلامي تتغير كل مرة يتم تحديث الصفحة!

## 📱 مثال حي

إليك كيف يبدو في README:

![مثال الاستخدام](http://localhost:5000/api/quote/image)

## 🎯 نقاط النهاية المتاحة

| Endpoint | الوصف | مثال |
|----------|--------|-------|
| `/api/quote/image` | 🖼️ صورة SVG للاقتباس | `![Quote](url/api/quote/image)` |
| `/api/quote` | 📄 اقتباس JSON | للاستخدام مع JavaScript |
| `/api/quote/text` | 📝 نص خام | للحصول على نص فقط |
| `/api/quote?personality=ابن_سينا` | 🎯 من شخصية محددة | اقتباس مخصص |
| `/api/personalities` | 👥 قائمة الشخصيات | جميع الأسماء المتاحة |

## 🌟 مميزات خاصة

- ✨ **صور SVG جميلة** مع خلفيات متدرجة
- 🎲 **10 شخصيات تاريخية** مع 30+ اقتباس
- 🔄 **تحديث تلقائي** في كل طلب
- 🌐 **دعم كامل للعربية** مع اتجاه RTL
- ⚡ **سريع وخفيف** - استجابة فورية
- 🆓 **مجاني تماماً** للاستخدام

## 🚀 نشر سريع (5 دقائق)

### Vercel (الأسهل):
1. Fork هذا المشروع على GitHub
2. اذهب إلى [vercel.com](https://vercel.com)
3. انقر "New Project" واختر المشروع
4. انقر "Deploy" - انتهى! 🎉

### Railway:
```bash
npm install -g @railway/cli
railway login
railway new --template arabic-quote-api
```

## 📖 أمثلة للاستخدام

### في README عادي:
```markdown
![Quote](https://your-app.vercel.app/api/quote/image)
```

### مع GitHub Actions للتحديث اليومي:
```yaml
- name: Update Quote
  run: |
    curl "https://your-app.vercel.app/api/quote/image" > quote.svg
    git add quote.svg && git commit -m "Update daily quote"
```

### مع JavaScript:
```javascript
fetch('https://your-app.vercel.app/api/quote')
  .then(r => r.json())
  .then(data => console.log(`${data.personality}: ${data.quote}`));
```

### مع Python:
```python
import requests
response = requests.get('https://your-app.vercel.app/api/quote')
quote_data = response.json()
print(f"{quote_data['personality']}: {quote_data['quote']}")
```

## 👥 الشخصيات المتاحة

| الشخصية | التخصص | القرن |
|---------|---------|-------|
| ابن سينا | طب وفلسفة | 11م |
| الإمام الشافعي | فقه وأصول | 8-9م |
| ابن خلدون | تاريخ واجتماع | 14-15م |
| الجاحظ | أدب وفكر | 8-9م |
| أبو نواس | شعر وأدب | 8-9م |
| المتنبي | شعر | 10م |
| ابن رشد | فلسفة وطب | 12م |
| ابن الهيثم | علوم وبصريات | 10-11م |
| الفارابي | فلسفة وموسيقى | 9-10م |
| الغزالي | فقه وفلسفة | 11-12م |

## 🔧 تشغيل محلي

```bash
git clone https://github.com/your-username/arabic-quote-api
cd arabic-quote-api
pip install -r requirements.txt
python app.py
```

الخدمة ستعمل على: `http://localhost:5000`

## 📊 إحصائيات المشروع

- 🎭 **10 شخصيات** تاريخية مؤثرة
- 📜 **30+ اقتباس** ملهم ومتنوع
- 🌍 **9+ قرون** من التراث الإسلامي
- ⚡ **استجابة < 100ms** في المتوسط
- 🎨 **تصميم جميل** للصور

## 🤝 المساهمة

نرحب بالمساهمات! يمكنك:
- إضافة شخصيات جديدة
- تحسين تصميم الصور
- إضافة اقتباسات جديدة
- تطوير ميزات إضافية

## 📄 الترخيص

MIT License - استخدمه في أي مشروع بحرية كاملة!

## 🔗 روابط سريعة

- 📚 [دليل النشر الكامل](DEPLOYMENT.md)
- 🧪 [اختبار الـ API](test_api.py)
- 💡 [أمثلة متقدمة](advanced_usage.py)
- 🎮 [النسخة التفاعلية](main.py)

---

**⭐ إذا أعجبك المشروع، لا تنس النجمة على GitHub!**

> العلم ما نفع، ليس العلم ما حُفظ
>
> — **الإمام الشافعي**
