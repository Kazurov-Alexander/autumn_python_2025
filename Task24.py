# task24 todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов

from flask import Flask
from flask import render_template
# from flask import request
# from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    return render_template('index.html', title = 'МОЙ МОЗГ', user = user)

# Страница "О компании"
@app.route('/company')
def page_company():
    return "<html><body><h2>О компании</h2><p>Мы создаём умные решения для умных людей.</p></body></html>"

# Страница "Контакты"
@app.route('/contacts')
def page_contacts():
    return "<html><body><h2>Контакты</h2><p>Email: info@example.com<br>Телефон: +123456789</p></body></html>"

# Страница "Список постов"
@app.route('/posts')
def page_posts():
    posts = [
        {
            'id': 1,
            'title': 'Банан',
            'content': 'Полезный и вкусный фрукт.',
            'image_url': 'https://foodcity.ru/storage/products/October2018/Zrk47quyPHLitYsACVRY.jpg'
        },
        {
            'id': 2,
            'title': 'Яблоко',
            'content': 'Символ здоровья и знаний, а ещё его украл Адам, к счастью сейчас яблоко можно купить)',
            'image_url': 'https://cdn.smt.bz/uploads/media/photo/1554916/%D0%AF%D0%B1%D0%BB%D0%BE%D0%BA%D0%BE.webp'
        },
        {
            'id': 3,
            'title': 'Виноград',
            'content': 'Идеален для перекуса и вина, содержит много фруктозы (кстати, грузинское вино самое вкусное!).',
            'image_url': 'https://frutsnab.ru/wa-data/public/shop/products/32/00/32/images/72/72.970.jpg'
        }
    ]

    html = "<html><body><h2>Список постов</h2><ul>"
    for post in posts:
        html += f"""
        <li>
            <h3>{post['title']}</h3>
            <p>{post['content']}</p>
            <img src="{post['image_url']}" alt="{post['title']}" width="200">
        </li>
        """
    html += "</ul></body></html>"
    return html



#@app.route("/")
#def hello_world():
#    #return "<p>Hello, World!</p>"
#    name = request.args.get("prompt", "Задай вопрос!")
#    clid = request.args.get("clid", "ID")
#    return ( f"Hello, {escape(name)}! Hello, {escape(clid)}!" )

@app.route("/about")
def page_about():
    return "<html><body><h2>О себе</h2><p>Немного о себе.</p></body></html>"

#@app.route("/page")
#def page():
