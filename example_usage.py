#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مثال على استخدام مولد اقتباسات المشاهير العرب المسلمين
Example usage of Arabic Muslim Celebrities Quote Generator
"""

from main import ArabicQuoteGenerator

def demo_basic_usage():
    """عرض الاستخدام الأساسي للمولد"""
    print("🌟 مثال على الاستخدام الأساسي")
    print("=" * 40)
    
    # إنشاء مولد الاقتباسات
    generator = ArabicQuoteGenerator()
    
    # اقتباس عشوائي
    personality, quote = generator.get_random_quote()
    print(f"\n📜 اقتباس عشوائي:")
    print(f"   الشخصية: {personality}")
    print(f"   الاقتباس: '{quote}'")
    
    # اقتباس بتنسيق Markdown
    markdown_quote = generator.generate_markdown_quote()
    print(f"\n📝 تنسيق Markdown:")
    print(markdown_quote)

def demo_specific_personality():
    """عرض اقتباسات من شخصيات محددة"""
    print("\n\n🎯 اقتباسات من شخصيات محددة")
    print("=" * 40)
    
    generator = ArabicQuoteGenerator()
    
    # اختبار شخصيات مختلفة
    test_personalities = ["ابن سينا", "المتنبي", "الغزالي"]
    
    for personality in test_personalities:
        person, quote = generator.get_quote_by_personality(personality)
        if person:
            print(f"\n📚 {person}:")
            print(f"   '{quote}'")

def demo_all_personalities():
    """عرض جميع الشخصيات المتاحة"""
    print("\n\n👥 جميع الشخصيات المتاحة")
    print("=" * 40)
    
    generator = ArabicQuoteGenerator()
    personalities = generator.get_all_personalities()
    
    for i, personality in enumerate(personalities, 1):
        print(f"{i:2d}. {personality}")

def demo_save_quote():
    """عرض حفظ اقتباس في ملف"""
    print("\n\n💾 حفظ اقتباس في ملف")
    print("=" * 40)
    
    generator = ArabicQuoteGenerator()
    
    # حفظ اقتباس يومي
    filename = "example_quote.md"
    content = generator.save_quote_to_file(filename)
    
    print(f"✅ تم حفظ الاقتباس في: {filename}")
    print("\nمحتوى الملف:")
    print("-" * 30)
    print(content)

def demo_multiple_quotes():
    """عرض عدة اقتباسات متتالية"""
    print("\n\n🎲 عدة اقتباسات عشوائية")
    print("=" * 40)
    
    generator = ArabicQuoteGenerator()
    
    for i in range(3):
        personality, quote = generator.get_random_quote()
        print(f"\n{i+1}. {personality}:")
        print(f"   '{quote}'")

if __name__ == "__main__":
    print("🌟 مرحباً بك في عرض مولد اقتباسات المشاهير العرب المسلمين")
    print("=" * 60)
    
    # تشغيل جميع الأمثلة
    demo_basic_usage()
    demo_specific_personality()
    demo_all_personalities()
    demo_save_quote()
    demo_multiple_quotes()
    
    print("\n\n🎉 انتهى العرض! يمكنك الآن استخدام المولد في مشاريعك")
    print("💡 لاستخدام المولد التفاعلي، شغل: python main.py")
