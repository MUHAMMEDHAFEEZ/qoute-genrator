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
    if len(quote) > 50:
        words = quote.split()
        current_line = ""
        for word in words:
            if len(current_line + " " + word) <= 50:
                current_line += " " + word if current_line else word
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
    else:
        lines = [quote]
    
    # حساب الأبعاد
    line_height = 35
    padding = 50
    width = 600
    height = padding * 2 + len(lines) * line_height + 100
    
    svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
        </linearGradient>
        <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="rgba(0,0,0,0.3)"/>
        </filter>
    </defs>
    
    <!-- خلفية -->
    <rect width="100%" height="100%" fill="url(#bg)" rx="20" filter="url(#shadow)"/>
    
    <!-- إطار -->
    <rect x="15" y="15" width="{width-30}" height="{height-30}" 
          fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="2" rx="15"/>
    
    <!-- رمز الاقتباس الافتتاحي -->
    <text x="40" y="60" font-family="Georgia, serif" font-size="50" fill="#FFD700" opacity="0.8">❝</text>
    '''
    
    # إضافة أسطر النص
    y_pos = 90
    for i, line in enumerate(lines):
        font_size = 20 if len(lines) <= 2 else 18
        svg += f'''
    <text x="{width//2}" y="{y_pos}" font-family="Arial, sans-serif" font-size="{font_size}" 
          fill="white" text-anchor="middle" font-weight="400">{line}</text>'''
        y_pos += line_height
    
    # إضافة اسم المؤلف
    svg += f'''
    <text x="{width//2}" y="{y_pos + 40}" font-family="Arial, sans-serif" font-size="18" 
          fill="#FFD700" text-anchor="middle" font-weight="bold">— {personality}</text>
    
    <!-- رمز الاقتباس الختامي -->
    <text x="{width-60}" y="{height-40}" font-family="Georgia, serif" font-size="50" fill="#FFD700" opacity="0.8">❞</text>
    
    <!-- تاريخ التحديث -->
    <text x="25" y="{height-15}" font-family="Arial, sans-serif" font-size="12" 
          fill="rgba(255,255,255,0.6)">{datetime.now().strftime('%Y-%m-%d')}</text>
          
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
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API مولد اقتباسات المشاهير العرب</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white; padding: 20px; text-align: center; margin: 0;
                min-height: 100vh; display: flex; align-items: center; justify-content: center;
            }
            .container { 
                max-width: 900px; margin: 0 auto; 
                background: rgba(255,255,255,0.15); padding: 40px; 
                border-radius: 20px; backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
            }
            h1 { color: #FFD700; margin-bottom: 30px; font-size: 2.5em; }
            .endpoint { 
                background: rgba(255,255,255,0.2); padding: 20px; margin: 15px 0;
                border-radius: 15px; border-left: 5px solid #FFD700;
                text-align: right;
            }
            .endpoint h3 { color: #FFD700; margin-bottom: 10px; }
            .endpoint p { font-family: 'Courier New', monospace; background: rgba(0,0,0,0.2); 
                         padding: 10px; border-radius: 8px; }
            .demo { margin: 30px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌟 API مولد اقتباسات المشاهير العرب المسلمين</h1>
            
            <div class="demo">
                <h2>🖼️ معاينة مباشرة:</h2>
                <img src="/api/quote/image" alt="اقتباس ملهم" style="max-width: 100%; border-radius: 15px; margin: 20px 0;">
            </div>
            
            <div class="endpoint">
                <h3>🖼️ صورة الاقتباس</h3>
                <p>GET /api/quote/image</p>
            </div>
            <div class="endpoint">
                <h3>📄 اقتباس JSON</h3>
                <p>GET /api/quote</p>
            </div>
            <div class="endpoint">
                <h3>👥 قائمة الشخصيات</h3>
                <p>GET /api/personalities</p>
            </div>
            <div class="endpoint">
                <h3>🎯 اقتباس محدد</h3>
                <p>GET /api/quote?personality=ابن_سينا</p>
            </div>
            
            <div style="margin-top: 40px; font-size: 0.9em; opacity: 0.8;">
                <p>🚀 جاهز للاستخدام في GitHub README ومواقع الويب</p>
                <p>💡 استخدم: &lt;img src="YOUR_URL/api/quote/image" /&gt;</p>
            </div>
        </div>
    </body>
    </html>
    '''

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
        personality_param = request.args.get('personality', '').replace('_', ' ')
        
        if personality_param:
            personality, quote = get_quote_by_personality(personality_param)
            if not personality:
                personality, quote = get_random_quote()
        else:
            personality, quote = get_random_quote()
        
        # إنشاء SVG
        svg_content = create_quote_svg(quote, personality)
        
        response = Response(svg_content, mimetype='image/svg+xml')
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        response.headers['Access-Control-Allow-Origin'] = '*'
        
        return response
    except Exception as e:
        # إرجاع SVG خطأ
        error_svg = f'''<svg width="600" height="200" xmlns="http://www.w3.org/2000/svg">
            <rect width="100%" height="100%" fill="#ff6b6b"/>
            <text x="300" y="100" font-family="Arial" font-size="18" fill="white" text-anchor="middle">
                خطأ في تحميل الاقتباس
            </text>
            <text x="300" y="130" font-family="Arial" font-size="14" fill="white" text-anchor="middle">
                {str(e)[:50]}
            </text>
        </svg>'''
        return Response(error_svg, mimetype='image/svg+xml')

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

# For Vercel deployment
if __name__ != '__main__':
    # This is running on Vercel
    app.debug = False

# Vercel serverless function handler
def handler(event, context):
    """Handler for Vercel serverless functions"""
    from werkzeug.wrappers import Request, Response as WerkzeugResponse
    from werkzeug.serving import WSGIRequestHandler
    import io
    
    # Create a WSGI environ from the event
    environ = {
        'REQUEST_METHOD': event.get('httpMethod', 'GET'),
        'PATH_INFO': event.get('path', '/'),
        'QUERY_STRING': event.get('queryStringParameters', ''),
        'CONTENT_TYPE': event.get('headers', {}).get('content-type', ''),
        'CONTENT_LENGTH': str(len(event.get('body', ''))),
        'HTTP_HOST': event.get('headers', {}).get('host', 'localhost'),
        'SERVER_NAME': 'localhost',
        'SERVER_PORT': '80',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': io.StringIO(event.get('body', '')),
        'wsgi.errors': io.StringIO(),
        'wsgi.multithread': False,
        'wsgi.multiprocess': True,
        'wsgi.run_once': False
    }
    
    # Add headers to environ
    for key, value in event.get('headers', {}).items():
        environ[f'HTTP_{key.upper().replace("-", "_")}'] = value
    
    response = {'statusCode': 200, 'headers': {}, 'body': ''}
    
    def start_response(status, headers):
        response['statusCode'] = int(status.split()[0])
        for header, value in headers:
            response['headers'][header] = value
    
    result = app(environ, start_response)
    response['body'] = ''.join(result)
    
    return response

# Alternative simpler handler for Vercel
app.wsgi_app = app.wsgi_app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
