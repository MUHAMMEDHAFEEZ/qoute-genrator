#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arabic Quote Generator API for Vercel
مولد اقتباسات المشاهير العرب المسلمين - API
"""

from flask import Flask, jsonify, request, Response
import random
import json
from datetime import datetime

app = Flask(__name__)

# اقتباسات المشاهير العرب المسلمين
quotes_data = {
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

def get_random_quote():
    """إرجاع اقتباس عشوائي"""
    personality = random.choice(list(quotes_data.keys()))
    quote = random.choice(quotes_data[personality])
    return personality, quote

def get_quote_by_personality(personality):
    """إرجاع اقتباس من شخصية محددة"""
    if personality in quotes_data:
        quote = random.choice(quotes_data[personality])
        return personality, quote
    else:
        return None, "الشخصية غير موجودة"

def create_quote_svg(quote, personality):
    """إنشاء صورة SVG للاقتباس"""
    
    # تقسيم النص لعدة أسطر إذا كان طويلاً
    lines = []
    if len(quote) > 60:
        words = quote.split()
        current_line = ""
        for word in words:
            if len(current_line + " " + word) <= 60:
                current_line += " " + word if current_line else word
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
    else:
        lines = [quote]
    
    # حساب الأبعاد
    line_height = 30
    padding = 40
    width = 600
    height = padding * 2 + len(lines) * line_height + 80  # 80 للمؤلف
    
    svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <!-- خلفية -->
    <rect width="100%" height="100%" fill="url(#bg)" rx="15"/>
    
    <!-- إطار -->
    <rect x="10" y="10" width="{width-20}" height="{height-20}" 
          fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2" rx="10"/>
    
    <!-- رمز الاقتباس -->
    <text x="30" y="50" font-family="Arial, sans-serif" font-size="40" fill="#FFD700">"</text>
    '''
    
    # إضافة أسطر النص
    y_pos = 80
    for line in lines:
        svg += f'''
    <text x="{width//2}" y="{y_pos}" font-family="Arial, sans-serif" font-size="18" 
          fill="white" text-anchor="middle" direction="rtl">{line}</text>'''
        y_pos += line_height
    
    # إضافة اسم المؤلف
    svg += f'''
    <text x="{width//2}" y="{y_pos + 30}" font-family="Arial, sans-serif" font-size="16" 
          fill="#FFD700" text-anchor="middle" font-weight="bold">— {personality}</text>
    
    <!-- رمز الاقتباس الختامي -->
    <text x="{width-50}" y="{height-30}" font-family="Arial, sans-serif" font-size="40" fill="#FFD700">"</text>
    
    <!-- تاريخ التحديث -->
    <text x="20" y="{height-10}" font-family="Arial, sans-serif" font-size="10" 
          fill="rgba(255,255,255,0.7)">{datetime.now().strftime('%Y-%m-%d')}</text>
          
    </svg>'''
    
    return svg

@app.route('/')
def home():
    """الصفحة الرئيسية"""
    return '''
    <!DOCTYPE html>
    <html dir="rtl" lang="ar">
    <head>
        <meta charset="UTF-8">
        <title>API مولد اقتباسات المشاهير العرب</title>
        <style>
            body { font-family: Arial; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                   color: white; padding: 20px; text-align: center; }
            .container { max-width: 800px; margin: 0 auto; }
            h1 { color: #FFD700; }
            .endpoint { background: rgba(255,255,255,0.1); padding: 15px; margin: 10px;
                       border-radius: 8px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌟 API مولد اقتباسات المشاهير العرب المسلمين</h1>
            <div class="endpoint">
                <h3>🖼️ صورة الاقتباس</h3>
                <p>/api/quote/image</p>
            </div>
            <div class="endpoint">
                <h3>📄 اقتباس JSON</h3>
                <p>/api/quote</p>
            </div>
            <div class="endpoint">
                <h3>👥 قائمة الشخصيات</h3>
                <p>/api/personalities</p>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/api/quote')
def api_quote():
    """API للحصول على اقتباس"""
    personality_param = request.args.get('personality', '').replace('_', ' ')
    
    if personality_param:
        personality, quote = get_quote_by_personality(personality_param)
        if not personality:
            return jsonify({
                'error': 'الشخصية غير موجودة',
                'available_personalities': list(quotes_data.keys())
            }), 404
    else:
        personality, quote = get_random_quote()
    
    return jsonify({
        'personality': personality,
        'quote': quote,
        'timestamp': datetime.now().isoformat(),
        'language': 'ar'
    })

@app.route('/api/quote/image')
def api_quote_image():
    """API للحصول على صورة SVG للاقتباس"""
    personality_param = request.args.get('personality', '').replace('_', ' ')
    
    if personality_param:
        personality, quote = get_quote_by_personality(personality_param)
        if not personality:
            personality, quote = get_random_quote()
    else:
        personality, quote = get_random_quote()
    
    # إنشاء SVG
    svg_content = create_quote_svg(quote, personality)
    
    return Response(svg_content, mimetype='image/svg+xml')

@app.route('/api/personalities')
def api_personalities():
    """API للحصول على قائمة الشخصيات"""
    return jsonify({
        'personalities': list(quotes_data.keys()),
        'count': len(quotes_data)
    })

@app.route('/health')
def health_check():
    """فحص صحة الخدمة"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Arabic Quote Generator API'
    })

# Vercel serverless function handler
def handler(request):
    """Handler for Vercel"""
    return app(request.environ, lambda *args: None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
