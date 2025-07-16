#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arabic Quote Generator API for Vercel
مولد اقتباسات المشاهير العرب المسلمين - API
"""

from flask import Flask, jsonify, request, Response
import random
from datetime import datetime

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

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
    max_chars = 45
    if len(quote) > max_chars:
        words = quote.split()
        current_line = ""
        for word in words:
            test_line = current_line + " " + word if current_line else word
            if len(test_line) <= max_chars:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
    else:
        lines = [quote]
    
    # حساب الأبعاد
    line_height = 35
    padding = 40
    width = 600
    height = padding * 2 + len(lines) * line_height + 120
    
    # تنظيف النصوص
    clean_lines = []
    for line in lines:
        clean_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
        clean_lines.append(clean_line)
    
    clean_personality = personality.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="100%" height="100%" fill="url(#bg)" rx="15"/>
    <rect x="10" y="10" width="{width-20}" height="{height-20}" 
          fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1" rx="10"/>
    '''
    
    # إضافة أسطر النص
    y_pos = 80
    for line in clean_lines:
        font_size = 22 if len(clean_lines) <= 2 else 18
        svg_content += f'''
    <text x="{width//2}" y="{y_pos}" 
          font-family="Arial, sans-serif" 
          font-size="{font_size}" 
          fill="white" 
          text-anchor="middle" 
          font-weight="normal">{line}</text>'''
        y_pos += line_height
    
    # إضافة اسم المؤلف
    svg_content += f'''
    <text x="{width//2}" y="{y_pos + 30}" 
          font-family="Arial, sans-serif" 
          font-size="16" 
          fill="#FFD700" 
          text-anchor="middle" 
          font-weight="bold">— {clean_personality}</text>
    
    <text x="20" y="{height-15}" 
          font-family="Arial, sans-serif" 
          font-size="11" 
          fill="rgba(255,255,255,0.5)">{datetime.now().strftime('%Y-%m-%d')}</text>
    </svg>'''
    
    return svg_content

@app.route('/')
def home():
    """الصفحة الرئيسية"""
    return {
        'name': 'Arabic Quote Generator API',
        'status': 'active',
        'endpoints': {
            'quote': '/api/quote',
            'image': '/api/quote/image',
            'personalities': '/api/personalities',
            'health': '/health'
        }
    }

@app.route('/api/quote')
def api_quote():
    """API للحصول على اقتباس"""
    try:
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
            'language': 'ar',
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': 'حدث خطأ في الخادم',
            'details': str(e),
            'status': 'error'
        }), 500

@app.route('/api/quote/image')
def api_quote_image():
    """API للحصول على صورة SVG للاقتباس"""
    try:
        personality_param = request.args.get('personality', '')
        if personality_param:
            personality_param = personality_param.replace('_', ' ')
            personality, quote = get_quote_by_personality(personality_param)
            if not personality:
                personality, quote = get_random_quote()
        else:
            personality, quote = get_random_quote()
        
        svg_content = create_quote_svg(quote, personality)
        
        return Response(
            svg_content, 
            mimetype='image/svg+xml',
            headers={
                'Cache-Control': 'no-cache',
                'Access-Control-Allow-Origin': '*'
            }
        )
    except:
        # خطأ بسيط
        error_svg = '''<svg width="600" height="200" xmlns="http://www.w3.org/2000/svg">
<rect width="100%" height="100%" fill="#ff4757"/>
<text x="300" y="110" font-family="Arial" font-size="16" fill="white" text-anchor="middle">Service Error</text>
</svg>'''
        return Response(
            error_svg, 
            mimetype='image/svg+xml',
            headers={'Access-Control-Allow-Origin': '*'}
        )

@app.route('/api/personalities')
def api_personalities():
    """API للحصول على قائمة الشخصيات"""
    try:
        return jsonify({
            'personalities': list(quotes_data.keys()),
            'count': len(quotes_data),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': 'حدث خطأ في الخادم',
            'details': str(e),
            'status': 'error'
        }), 500

@app.route('/health')
def health_check():
    """فحص صحة الخدمة"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Arabic Quote Generator API',
        'version': '2.0'
    })

@app.route('/api/info')
def api_info():
    """معلومات الـ API"""
    return jsonify({
        'name': 'Arabic Quote Generator API',
        'version': '2.0',
        'description': 'مولد اقتباسات المشاهير العرب المسلمين',
        'endpoints': {
            '/api/quote': 'اقتباس عشوائي JSON',
            '/api/quote/image': 'صورة اقتباس SVG',
            '/api/personalities': 'قائمة الشخصيات',
            '/health': 'فحص صحة الخدمة'
        },
        'personalities_count': len(quotes_data),
        'total_quotes': sum(len(quotes) for quotes in quotes_data.values())
    })

@app.errorhandler(404)
def not_found(error):
    """معالج الصفحات غير الموجودة"""
    return jsonify({
        'error': 'الصفحة غير موجودة',
        'available_endpoints': ['/api/quote', '/api/quote/image', '/api/personalities', '/health'],
        'status': 'error'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """معالج أخطاء الخادم"""
    return jsonify({
        'error': 'خطأ في الخادم',
        'status': 'error'
    }), 500

@app.route('/test')
def test():
    """Simple test endpoint"""
    return {'status': 'working', 'message': 'API is running'}

# For Vercel serverless deployment
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
