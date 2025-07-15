#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arabic Quote Generator API
مولد اقتباسات المشاهير العرب المسلمين - API
"""

from flask import Flask, jsonify, request, render_template_string, Response
from flask_cors import CORS
import random
import json
from datetime import datetime
from main import ArabicQuoteGenerator
import base64
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import requests

app = Flask(__name__)
CORS(app)  # للسماح بالوصول من مواقع أخرى

# إنشاء مولد الاقتباسات
generator = ArabicQuoteGenerator()

@app.route('/')
def home():
    """الصفحة الرئيسية للAPI"""
    return render_template_string("""
    <!DOCTYPE html>
    <html dir="rtl" lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API مولد اقتباسات المشاهير العرب المسلمين</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                   background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                   color: white; margin: 0; padding: 20px; }
            .container { max-width: 800px; margin: 0 auto; background: rgba(255,255,255,0.1);
                        padding: 30px; border-radius: 15px; backdrop-filter: blur(10px); }
            h1 { text-align: center; color: #FFD700; margin-bottom: 30px; }
            .endpoint { background: rgba(255,255,255,0.2); padding: 15px; margin: 10px 0;
                       border-radius: 8px; border-left: 4px solid #FFD700; }
            .code { background: #2d3748; color: #e2e8f0; padding: 10px; border-radius: 5px;
                   font-family: 'Courier New', monospace; margin: 10px 0; overflow-x: auto; }
            .demo-quote { background: rgba(255,255,255,0.2); padding: 20px; margin: 20px 0;
                         border-radius: 10px; text-align: center; }
            .quote-text { font-size: 1.2em; font-style: italic; margin-bottom: 10px; }
            .quote-author { font-weight: bold; color: #FFD700; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌟 API مولد اقتباسات المشاهير العرب المسلمين</h1>
            
            <div class="demo-quote" id="liveQuote">
                <div class="quote-text">جاري تحميل الاقتباس...</div>
                <div class="quote-author"></div>
            </div>
            
            <h2>📡 نقاط النهاية المتاحة (API Endpoints)</h2>
            
            <div class="endpoint">
                <h3>🎲 اقتباس عشوائي</h3>
                <div class="code">GET /api/quote</div>
                <p>يرجع اقتباساً عشوائياً بتنسيق JSON</p>
            </div>
            
            <div class="endpoint">
                <h3>🖼️ صورة اقتباس للـ README</h3>
                <div class="code">GET /api/quote/image</div>
                <p>يرجع صورة SVG يمكن استخدامها مباشرة في README</p>
                <div class="code">![Quote](YOUR_API_URL/api/quote/image)</div>
            </div>
            
            <div class="endpoint">
                <h3>📝 اقتباس بتنسيق نص</h3>
                <div class="code">GET /api/quote/text</div>
                <p>يرجع اقتباساً كنص خام</p>
            </div>
            
            <div class="endpoint">
                <h3>🎯 اقتباس من شخصية محددة</h3>
                <div class="code">GET /api/quote?personality=ابن_سينا</div>
                <p>يرجع اقتباساً من شخصية محددة</p>
            </div>
            
            <div class="endpoint">
                <h3>👥 قائمة الشخصيات</h3>
                <div class="code">GET /api/personalities</div>
                <p>يرجع قائمة بجميع الشخصيات المتاحة</p>
            </div>
            
            <h2>💡 أمثلة للاستخدام في README</h2>
            
            <div class="endpoint">
                <h3>استخدام كصورة:</h3>
                <div class="code">![اقتباس يومي](YOUR_API_URL/api/quote/image)</div>
            </div>
            
            <div class="endpoint">
                <h3>استخدام مع JavaScript:</h3>
                <div class="code">fetch('YOUR_API_URL/api/quote')
  .then(response => response.json())
  .then(data => console.log(data));</div>
            </div>
            
            <script>
                // تحديث الاقتباس كل 10 ثوانٍ
                function loadQuote() {
                    fetch('/api/quote')
                        .then(response => response.json())
                        .then(data => {
                            document.querySelector('.quote-text').textContent = '"' + data.quote + '"';
                            document.querySelector('.quote-author').textContent = '— ' + data.personality;
                        })
                        .catch(error => console.error('Error:', error));
                }
                
                loadQuote();
                setInterval(loadQuote, 10000);
            </script>
        </div>
    </body>
    </html>
    """)

@app.route('/api/quote')
def api_quote():
    """API للحصول على اقتباس عشوائي أو من شخصية محددة"""
    personality_param = request.args.get('personality', '').replace('_', ' ')
    
    if personality_param:
        personality, quote = generator.get_quote_by_personality(personality_param)
        if not personality:
            return jsonify({
                'error': 'الشخصية غير موجودة',
                'available_personalities': generator.get_all_personalities()
            }), 404
    else:
        personality, quote = generator.get_random_quote()
    
    return jsonify({
        'personality': personality,
        'quote': quote,
        'timestamp': datetime.now().isoformat(),
        'language': 'ar'
    })

@app.route('/api/quote/text')
def api_quote_text():
    """API للحصول على اقتباس كنص خام"""
    personality, quote = generator.get_random_quote()
    return f'"{quote}" — {personality}', 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/api/quote/image')
def api_quote_image():
    """API للحصول على صورة SVG للاقتباس"""
    personality_param = request.args.get('personality', '').replace('_', ' ')
    
    if personality_param:
        personality, quote = generator.get_quote_by_personality(personality_param)
        if not personality:
            personality, quote = generator.get_random_quote()
    else:
        personality, quote = generator.get_random_quote()
    
    # إنشاء SVG
    svg_content = create_quote_svg(quote, personality)
    
    return Response(svg_content, mimetype='image/svg+xml')

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

@app.route('/api/personalities')
def api_personalities():
    """API للحصول على قائمة الشخصيات"""
    personalities = generator.get_all_personalities()
    return jsonify({
        'personalities': personalities,
        'count': len(personalities)
    })

@app.route('/api/stats')
def api_stats():
    """إحصائيات حول المجموعة"""
    personalities = generator.get_all_personalities()
    total_quotes = sum(len(generator.quotes[p]) for p in personalities)
    
    return jsonify({
        'total_personalities': len(personalities),
        'total_quotes': total_quotes,
        'personalities': personalities,
        'version': '1.0.0'
    })

@app.route('/health')
def health_check():
    """فحص صحة الخدمة"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Arabic Quote Generator API'
    })

if __name__ == '__main__':
    print("🌟 تشغيل API مولد اقتباسات المشاهير العرب المسلمين")
    print("📡 الخدمة متاحة على: http://localhost:5000")
    print("🖼️ لاستخدام الصورة في README: http://localhost:5000/api/quote/image")
    app.run(debug=True, host='0.0.0.0', port=5000)
