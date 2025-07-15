import random
import json
import os
from datetime import datetime

class ArabicQuoteGenerator:
    def __init__(self):
        self.quotes = {
            "ابن سينا": [
                "الطب مهنة تُحفظ بها الحياة، وعلم يُستكشف به أسرار الوجود",
                "الجهل هو العدو الأكبر للعقل البشري",
                "من لم يطلب العلم في صغره، تاه في كبره"
            ],
            "الإمام الشافعي": [
                "العلم ما نفع، ليس العلم ما حُفظ",
                "من تكلم فيما لا يعنيه، سمع ما لا يرضيه",
                "الناس في غفلة والموت يقظان"
            ],
            "ابن خلدون": [
                "التاريخ هو علم الاجتماع الإنساني",
                "العصبية هي الرباط الذي يجمع الأفراد في مجتمع واحد",
                "إن الدولة لها أعمار طبيعية كما للأشخاص"
            ],
            "الجاحظ": [
                "لا تطلب الرزق من باب واحد، فإن أُغلق انفتح غيره",
                "الكتاب خير جليس في الزمان، وأفضل صاحب وصديق",
                "من جهل شيئاً عاداه"
            ],
            "أبو نواس": [
                "دع الأيام تفعل ما تشاء، وطب نفساً إذا حكم القضاء",
                "ولا تجزع لحادثة الليالي، فما لحوادث الدنيا بقاء",
                "إذا ما كنت ذا رأي فكن ذا عزيمة، فإن فساد الرأي أن تترددا"
            ],
            "المتنبي": [
                "على قدر أهل العزم تأتي العزائم، وتأتي على قدر الكرام المكارم",
                "وما انتفاع أخي الدنيا بناظره، إذا استوت عنده الأنوار والظلم",
                "الرأي قبل شجاعة الشجعان، هو أول وهي المحل الثاني"
            ],
            "ابن رشد": [
                "الجهل يؤدي إلى الخوف، والخوف يؤدي إلى الكراهية، والكراهية تؤدي إلى العنف",
                "الفلسفة صديقة الشريعة ورضيعتها",
                "التعلم هو الطريق الوحيد للحرية الحقيقية"
            ],
            "ابن الهيثم": [
                "الشك هو الطريق إلى اليقين",
                "الحقيقة تُطلب لذاتها، وليس لغرض آخر",
                "من لم يشك لم ينظر، ومن لم ينظر لم يُبصر"
            ],
            "الفارابي": [
                "الأمة الفاضلة هي التي تجتمع على طلب السعادة",
                "العدالة هي أساس الملك",
                "العقل هو أشرف ما في الإنسان"
            ],
            "الغزالي": [
                "العلم ليس بكثرة النقل، وإنما بنور يقذفه الله في القلب",
                "من صدق الله صدقه الله",
                "القلب إذا أقبل على الله أقبل الله عليه"
            ]
        }
    
    def get_random_quote(self):
        """إرجاع اقتباس عشوائي من مشهور عربي مسلم"""
        personality = random.choice(list(self.quotes.keys()))
        quote = random.choice(self.quotes[personality])
        return personality, quote
    
    def get_quote_by_personality(self, personality):
        """إرجاع اقتباس عشوائي من شخصية محددة"""
        if personality in self.quotes:
            quote = random.choice(self.quotes[personality])
            return personality, quote
        else:
            return None, "الشخصية غير موجودة"
    
    def get_all_personalities(self):
        """إرجاع قائمة بجميع الشخصيات المتاحة"""
        return list(self.quotes.keys())
    
    def generate_markdown_quote(self):
        """توليد اقتباس بتنسيق Markdown"""
        personality, quote = self.get_random_quote()
        return f"> {quote}\n>\n> — **{personality}**"
    
    def save_quote_to_file(self, filename="daily_quote.md"):
        """حفظ اقتباس يومي في ملف"""
        quote_md = self.generate_markdown_quote()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        content = f"# اقتباس اليوم\n\n{quote_md}\n\n*تم التحديث في: {timestamp}*\n"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return content

def main():
    generator = ArabicQuoteGenerator()
    
    print("🌟 مولد اقتباسات المشاهير العرب المسلمين 🌟")
    print("=" * 50)
    
    while True:
        print("\nاختر من القائمة:")
        print("1. اقتباس عشوائي")
        print("2. اقتباس من شخصية محددة")
        print("3. عرض جميع الشخصيات")
        print("4. توليد اقتباس بتنسيق Markdown")
        print("5. حفظ اقتباس يومي")
        print("6. خروج")
        
        choice = input("\nأدخل اختيارك (1-6): ").strip()
        
        if choice == "1":
            personality, quote = generator.get_random_quote()
            print(f"\n📜 اقتباس من {personality}:")
            print(f"'{quote}'")
        
        elif choice == "2":
            personalities = generator.get_all_personalities()
            print("\nالشخصيات المتاحة:")
            for i, p in enumerate(personalities, 1):
                print(f"{i}. {p}")
            
            try:
                p_choice = int(input("\nاختر رقم الشخصية: ")) - 1
                if 0 <= p_choice < len(personalities):
                    selected_personality = personalities[p_choice]
                    personality, quote = generator.get_quote_by_personality(selected_personality)
                    print(f"\n📜 اقتباس من {personality}:")
                    print(f"'{quote}'")
                else:
                    print("❌ رقم غير صحيح!")
            except ValueError:
                print("❌ يرجى إدخال رقم صحيح!")
        
        elif choice == "3":
            personalities = generator.get_all_personalities()
            print("\n👥 الشخصيات المتاحة:")
            for i, p in enumerate(personalities, 1):
                print(f"{i}. {p}")
        
        elif choice == "4":
            markdown_quote = generator.generate_markdown_quote()
            print("\n📝 اقتباس بتنسيق Markdown:")
            print(markdown_quote)
        
        elif choice == "5":
            filename = input("أدخل اسم الملف (اتركه فارغاً للاسم الافتراضي): ").strip()
            if not filename:
                filename = "daily_quote.md"
            
            content = generator.save_quote_to_file(filename)
            print(f"\n✅ تم حفظ الاقتباس في الملف: {filename}")
            print("\nمحتوى الملف:")
            print(content)
        
        elif choice == "6":
            print("\n👋 شكراً لاستخدام مولد الاقتباسات!")
            break
        
        else:
            print("❌ اختيار غير صحيح! يرجى المحاولة مرة أخرى.")

if __name__ == "__main__":
    main()