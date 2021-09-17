from flask import Flask, render_template, jsonify

books = [
    {
     'id': 0,
     'title': 'اشتري الآن وادفع لاحقًا تخفيض',
     'discount': '20%',
     'code': "661509a0eca952249cab64dc5770b635",
     'dec': 'هي خدمة الالكتروني تسهل للعملاء الشراء من موقع نايس عباية بدفع لاحقا بعد 14 يوم من عملية الشراء او بالتقسيط الميسر حسب رغبة العميل بدون اي تكاليف اضافية للعميل عبر منصة شركة تابي'
    },{
     'id': 0,
     'title': 'اشتري الآن وادفع لاحقًا تخفيض',
     'discount': '30%',
     'code': "AB4F63F9AC65152575886860DDE480A1",
     'dec': 'هي خدمة الالكتروني تسهل للعملاء الشراء من موقع نايس عباية بدفع لاحقا بعد 14 يوم من عملية الشراء او بالتقسيط الميسر حسب رغبة العميل بدون اي تكاليف اضافية للعميل عبر منصة شركة تابي'
    },
    {
     'id': 0,
     'title': 'اشتري الآن وادفع لاحقًا تخفيض',
     'discount': '15%',
     'code': "e221d66c9b7d63c038de8332fd9c9aba",
     'dec': 'هي خدمة الالكتروني تسهل للعملاء الشراء من موقع نايس عباية بدفع لاحقا بعد 14 يوم من عملية الشراء او بالتقسيط الميسر حسب رغبة العميل بدون اي تكاليف اضافية للعميل عبر منصة شركة تابي'
    },
    {
     'id': 0,
     'title': 'اشتري الآن وادفع لاحقًا تخفيض',
     'discount': '10%',
     'code': "998ab57f3c26d6d33e138d84e0300c6a",
     'dec': 'هي خدمة الالكتروني تسهل للعملاء الشراء من موقع نايس عباية بدفع لاحقا بعد 14 يوم من عملية الشراء او بالتقسيط الميسر حسب رغبة العميل بدون اي تكاليف اضافية للعميل عبر منصة شركة تابي'
    },
    {
     'id': 0,
     'title': 'اشتري الآن وادفع لاحقًا تخفيض',
     'discount': '5%',
     'code': "0be6a9ebe61f379d4fbc9e1479b0757b",
     'dec': 'هي خدمة الالكتروني تسهل للعملاء الشراء من موقع نايس عباية بدفع لاحقا بعد 14 يوم من عملية الشراء او بالتقسيط الميسر حسب رغبة العميل بدون اي تكاليف اضافية للعميل عبر منصة شركة تابي'
    },
    {
     'id': 0,
     'title': 'اشتري الآن وادفع لاحقًا تخفيض',
     'discount': '7%',
     'code': "1949975a53c477d6590efdf6d2cd2272",
     'dec': 'هي خدمة الالكتروني تسهل للعملاء الشراء من موقع نايس عباية بدفع لاحقا بعد 14 يوم من عملية الشراء او بالتقسيط الميسر حسب رغبة العميل بدون اي تكاليف اضافية للعميل عبر منصة شركة تابي'
    },
]


app = Flask(__name__)

def get_book(code):
    for b in books:
        if b.get("code")==code:
            return  b

@app.route("/")
def index():
    return jsonify(books)

@app.route('/discount/<id>', methods=['GET'])
def index2():
    return jsonify(get_book(id))

if __name__ == "__main__":
    app.run()