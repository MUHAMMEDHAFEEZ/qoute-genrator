#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ملف تكوين متقدم لمولد اقتباسات المشاهير العرب المسلمين
Advanced configuration for Arabic Muslim Celebrities Quote Generator
"""

import json
from main import ArabicQuoteGenerator

class QuoteGeneratorAPI:
    """واجهة برمجية متقدمة لمولد الاقتباسات"""
    
    def __init__(self):
        self.generator = ArabicQuoteGenerator()
        self.config = {
            "default_format": "markdown",
            "include_timestamp": True,
            "include_personality_info": False,
            "output_encoding": "utf-8"
        }
    
    def get_quote_json(self):
        """إرجاع اقتباس بتنسيق JSON"""
        personality, quote = self.generator.get_random_quote()
        
        result = {
            "personality": personality,
            "quote": quote,
            "format": "json",
            "language": "arabic"
        }
        
        if self.config["include_timestamp"]:
            from datetime import datetime
            result["timestamp"] = datetime.now().isoformat()
        
        return json.dumps(result, ensure_ascii=False, indent=2)
    
    def get_quote_html(self):
        """إرجاع اقتباس بتنسيق HTML"""
        personality, quote = self.generator.get_random_quote()
        
        html_template = """
        <div class="arabic-quote" dir="rtl">
            <blockquote>
                <p class="quote-text">"{quote}"</p>
                <footer class="quote-author">— <strong>{personality}</strong></footer>
            </blockquote>
        </div>
        """
        
        return html_template.format(quote=quote, personality=personality).strip()
    
    def get_quote_for_readme(self, style="github"):
        """إرجاع اقتباس مُنسق للاستخدام في README"""
        personality, quote = self.generator.get_random_quote()
        
        if style == "github":
            return f"""
<!-- Quote of the Day -->
<div align="center">
    <h3>🌟 اقتباس اليوم</h3>
    <blockquote>
        <p><em>"{quote}"</em></p>
        <footer><strong>— {personality}</strong></footer>
    </blockquote>
</div>
""".strip()
        
        elif style == "simple":
            return f"> {quote}\n>\n> — **{personality}**"
        
        else:
            return self.generator.generate_markdown_quote()
    
    def batch_generate_quotes(self, count=5):
        """توليد مجموعة من الاقتباسات"""
        quotes = []
        
        for _ in range(count):
            personality, quote = self.generator.get_random_quote()
            quotes.append({
                "personality": personality,
                "quote": quote
            })
        
        return quotes
    
    def export_all_quotes(self, filename="all_quotes.json"):
        """تصدير جميع الاقتباسات إلى ملف JSON"""
        all_quotes = {}
        
        for personality in self.generator.get_all_personalities():
            quotes_list = []
            # الحصول على جميع اقتباسات هذه الشخصية
            for quote in self.generator.quotes[personality]:
                quotes_list.append(quote)
            
            all_quotes[personality] = quotes_list
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(all_quotes, f, ensure_ascii=False, indent=2)
        
        return f"تم تصدير جميع الاقتباسات إلى {filename}"

def create_github_action_quote():
    """إنشاء اقتباس لاستخدامه في GitHub Actions"""
    api = QuoteGeneratorAPI()
    quote_data = api.get_quote_json()
    
    # حفظ في ملف للاستخدام في GitHub Actions
    with open("quote_data.json", "w", encoding="utf-8") as f:
        f.write(quote_data)
    
    # إنشاء اقتباس للـ README
    readme_quote = api.get_quote_for_readme("github")
    
    with open("readme_quote.md", "w", encoding="utf-8") as f:
        f.write(readme_quote)
    
    print("✅ تم إنشاء ملفات GitHub Actions:")
    print("   - quote_data.json")
    print("   - readme_quote.md")

def demo_advanced_features():
    """عرض الميزات المتقدمة"""
    print("🚀 الميزات المتقدمة لمولد الاقتباسات")
    print("=" * 50)
    
    api = QuoteGeneratorAPI()
    
    # JSON format
    print("\n📄 تنسيق JSON:")
    print(api.get_quote_json())
    
    # HTML format
    print("\n🌐 تنسيق HTML:")
    print(api.get_quote_html())
    
    # README format
    print("\n📋 تنسيق README:")
    print(api.get_quote_for_readme("github"))
    
    # Batch generation
    print("\n📦 مجموعة اقتباسات:")
    batch_quotes = api.batch_generate_quotes(3)
    for i, quote_data in enumerate(batch_quotes, 1):
        print(f"   {i}. {quote_data['personality']}: '{quote_data['quote']}'")
    
    # Export all quotes
    print(f"\n💾 {api.export_all_quotes()}")

if __name__ == "__main__":
    demo_advanced_features()
    print("\n" + "="*50)
    create_github_action_quote()
