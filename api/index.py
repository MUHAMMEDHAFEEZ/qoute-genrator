from flask import Flask, jsonify, Response
import random
from datetime import datetime

app = Flask(__name__)

# بيانات الاقتباسات
quotes_data = [
    {"text": "العلم ما نفع، ليس العلم ما حُفظ", "author": "الإمام الشافعي"},
    {"text": "الجهل هو العدو الأكبر للعقل البشري", "author": "ابن سينا"},
    {"text": "التاريخ هو علم الاجتماع الإنساني", "author": "ابن خلدون"},
    {"text": "لا تطلب الرزق من باب واحد، فإن أُغلق انفتح غيره", "author": "الجاحظ"},
    {"text": "على قدر أهل العزم تأتي العزائم", "author": "المتنبي"},
    {"text": "من لم يطلب العلم في صغره، تاه في كبره", "author": "ابن سينا"},
    {"text": "الشك هو الطريق إلى اليقين", "author": "ابن الهيثم"},
    {"text": "العدالة هي أساس الملك", "author": "الفارابي"}
]

@app.route('/')
def home():
    return {
        'name': 'Arabic Quote Generator API',
        'status': 'active',
        'version': '1.0',
        'endpoints': {
            'quote': '/api/quote',
            'image': '/api/quote/image',
            'health': '/health'
        }
    }

@app.route('/api/quote')
def get_quote():
    try:
        quote = random.choice(quotes_data)
        return jsonify({
            'quote': quote['text'],
            'author': quote['author'],
            'timestamp': datetime.now().isoformat(),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({'error': 'حدث خطأ', 'status': 'error'}), 500

@app.route('/api/quote/image')
def get_quote_image():
    try:
        quote = random.choice(quotes_data)
        
        # تنظيف النص
        clean_text = quote['text'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        clean_author = quote['author'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        # تقسيم النص إذا كان طويل
        if len(clean_text) > 40:
            words = clean_text.split()
            line1 = ' '.join(words[:len(words)//2])
            line2 = ' '.join(words[len(words)//2:])
            lines = [line1, line2]
        else:
            lines = [clean_text]
        
        height = 180 + (len(lines) - 1) * 25
        
        svg = f'''<svg width="500" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="100%" height="100%" fill="url(#bg)" rx="15"/>
    <rect x="10" y="10" width="480" height="{height-20}" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1" rx="10"/>
    '''
        
        y_pos = 80
        for line in lines:
            svg += f'''
    <text x="250" y="{y_pos}" font-family="Arial, sans-serif" font-size="18" fill="white" text-anchor="middle" font-weight="normal">{line}</text>'''
            y_pos += 25
        
        svg += f'''
    <text x="250" y="{y_pos + 30}" font-family="Arial, sans-serif" font-size="16" fill="#FFD700" text-anchor="middle" font-weight="bold">— {clean_author}</text>
    
    <text x="20" y="{height-15}" font-family="Arial, sans-serif" font-size="10" fill="rgba(255,255,255,0.5)">{datetime.now().strftime('%Y-%m-%d')}</text>
</svg>'''
        
        return Response(svg, mimetype='image/svg+xml', headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        })
    except Exception as e:
        error_svg = '''<svg width="500" height="150" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="#ff4757"/>
    <text x="250" y="80" font-family="Arial" font-size="16" fill="white" text-anchor="middle">خطأ في تحميل الاقتباس</text>
</svg>'''
        return Response(error_svg, mimetype='image/svg+xml')

@app.route('/health')
def health():
    return {
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'quotes_count': len(quotes_data)
    }

# هذا مهم لـ Vercel
def handler(request):
    return app(request.environ, request.start_response)
