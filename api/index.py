from http.server import BaseHTTPRequestHandler
import json
import random
from urllib.parse import urlparse, parse_qs

# بيانات الاقتباسات
quotes = [
    {"text": "العلم ما نفع، ليس العلم ما حُفظ", "author": "الإمام الشافعي"},
    {"text": "الجهل هو العدو الأكبر للعقل البشري", "author": "ابن سينا"},
    {"text": "التاريخ هو علم الاجتماع الإنساني", "author": "ابن خلدون"},
    {"text": "لا تطلب الرزق من باب واحد، فإن أُغلق انفتح غيره", "author": "الجاحظ"},
    {"text": "على قدر أهل العزم تأتي العزائم", "author": "المتنبي"}
]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            url = urlparse(self.path)
            path = url.path
            
            # CORS headers
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            
            if path == '/' or path == '':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {
                    'name': 'Arabic Quote Generator API',
                    'status': 'active',
                    'endpoints': {
                        'quote': '/api/quote',
                        'image': '/api/quote/image',
                        'health': '/health'
                    }
                }
                self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
                
            elif path == '/health':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'healthy', 'message': 'API is working'}
                self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
                
            elif path == '/api/quote':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                quote = random.choice(quotes)
                response = {
                    'quote': quote['text'],
                    'author': quote['author'],
                    'status': 'success'
                }
                self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
                
            elif path == '/api/quote/image':
                self.send_response(200)
                self.send_header('Content-type', 'image/svg+xml')
                self.end_headers()
                
                quote = random.choice(quotes)
                clean_text = quote['text'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                clean_author = quote['author'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                
                svg = f'''<svg width="500" height="200" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#bg)" rx="15"/>
    <text x="250" y="100" font-family="Arial" font-size="16" fill="white" text-anchor="middle">{clean_text[:60]}</text>
    <text x="250" y="130" font-family="Arial" font-size="14" fill="#FFD700" text-anchor="middle">— {clean_author}</text>
</svg>'''
                self.wfile.write(svg.encode('utf-8'))
                
            else:
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'error': 'Not found', 'status': 'error'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'error': 'Internal server error', 'details': str(e)}
            self.wfile.write(json.dumps(response).encode('utf-8'))
