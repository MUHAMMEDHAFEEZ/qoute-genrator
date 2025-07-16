from flask import Flask, jsonify, Response
import random

app = Flask(__name__)

# Simple quotes data
quotes = [
    {"text": "العلم ما نفع، ليس العلم ما حُفظ", "author": "الإمام الشافعي"},
    {"text": "الجهل هو العدو الأكبر للعقل البشري", "author": "ابن سينا"},
    {"text": "التاريخ هو علم الاجتماع الإنساني", "author": "ابن خلدون"}
]

@app.route('/')
def home():
    return {'message': 'Arabic Quote Generator API', 'status': 'working'}

@app.route('/api/quote')
def get_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

@app.route('/api/quote/image')
def get_quote_image():
    quote = random.choice(quotes)
    svg = f'''<svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
<rect width="100%" height="100%" fill="#4285f4"/>
<text x="200" y="100" font-family="Arial" font-size="14" fill="white" text-anchor="middle">{quote["text"][:50]}</text>
<text x="200" y="130" font-family="Arial" font-size="12" fill="#ffd700" text-anchor="middle">— {quote["author"]}</text>
</svg>'''
    return Response(svg, mimetype='image/svg+xml')

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(debug=True)
