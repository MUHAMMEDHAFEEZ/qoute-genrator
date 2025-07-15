"""
مثال سريع لاستخدام API مولد الاقتباسات العربية
Quick example for using Arabic Quote Generator API
"""

import requests
import json

# رابط الـ API (غيّره برابطك بعد النشر)
API_URL = "http://localhost:5000"

def test_api():
    """اختبار جميع نقاط النهاية للـ API"""
    
    print("🧪 اختبار API مولد الاقتباسات العربية")
    print("="*50)
    
    # 1. اختبار الصحة
    try:
        response = requests.get(f"{API_URL}/health")
        print("✅ فحص الصحة:", response.status_code)
        print("📊 البيانات:", response.json())
    except Exception as e:
        print("❌ خطأ في فحص الصحة:", e)
        return
    
    print("\n" + "-"*30)
    
    # 2. اقتباس عشوائي
    try:
        response = requests.get(f"{API_URL}/api/quote")
        if response.status_code == 200:
            data = response.json()
            print("🎲 اقتباس عشوائي:")
            print(f"   الشخصية: {data['personality']}")
            print(f"   الاقتباس: '{data['quote']}'")
            print(f"   الوقت: {data['timestamp']}")
        else:
            print("❌ خطأ في الاقتباس العشوائي:", response.status_code)
    except Exception as e:
        print("❌ خطأ:", e)
    
    print("\n" + "-"*30)
    
    # 3. قائمة الشخصيات
    try:
        response = requests.get(f"{API_URL}/api/personalities")
        if response.status_code == 200:
            data = response.json()
            print("👥 الشخصيات المتاحة:")
            for i, personality in enumerate(data['personalities'], 1):
                print(f"   {i:2d}. {personality}")
            print(f"📊 المجموع: {data['count']} شخصيات")
        else:
            print("❌ خطأ في قائمة الشخصيات:", response.status_code)
    except Exception as e:
        print("❌ خطأ:", e)
    
    print("\n" + "-"*30)
    
    # 4. اقتباس من شخصية محددة
    try:
        response = requests.get(f"{API_URL}/api/quote", 
                               params={'personality': 'ابن_سينا'})
        if response.status_code == 200:
            data = response.json()
            print("🎯 اقتباس من ابن سينا:")
            print(f"   '{data['quote']}'")
        else:
            print("❌ خطأ في الاقتباس المحدد:", response.status_code)
    except Exception as e:
        print("❌ خطأ:", e)
    
    print("\n" + "-"*30)
    
    # 5. اقتباس نصي
    try:
        response = requests.get(f"{API_URL}/api/quote/text")
        if response.status_code == 200:
            print("📝 اقتباس نصي:")
            print(f"   {response.text}")
        else:
            print("❌ خطأ في الاقتباس النصي:", response.status_code)
    except Exception as e:
        print("❌ خطأ:", e)
    
    print("\n" + "-"*30)
    
    # 6. رابط صورة الاقتباس
    print("🖼️ رابط صورة الاقتباس:")
    print(f"   {API_URL}/api/quote/image")
    print("\nلاستخدامه في README:")
    print(f"   ![Quote]({API_URL}/api/quote/image)")

def generate_readme_example():
    """توليد مثال README مع الاقتباس"""
    
    print("\n\n📝 مثال README مع الاقتباس:")
    print("="*50)
    
    readme_template = f"""# مشروعي الرائع

وصف المشروع هنا...

## اقتباس اليوم

![اقتباس ملهم]({API_URL}/api/quote/image)

## المزيد من المحتوى

باقي محتويات README...
"""
    
    print(readme_template)
    
    # حفظ في ملف
    with open("README_example.md", "w", encoding="utf-8") as f:
        f.write(readme_template)
    
    print("✅ تم حفظ المثال في: README_example.md")

if __name__ == "__main__":
    test_api()
    generate_readme_example()
    
    print("\n🎉 انتهى الاختبار!")
    print("💡 نصيحة: استبدل API_URL برابط الاستضافة الخاص بك")
    print("🌐 مثال: https://your-app.vercel.app")
