from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Фейковые статьи
ARTICLES = {
    1: {"title": "Как защититься от SSRF", "content": "Никогда не используете такие имена, как backend, для вашего внутреннего сервиса и не располагайте их на предсказуемых портах. И уж точно не кладите туда флаги"},
    2: {"title": "Новости криптографии", "content": "Ничего нового"}
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/article/<int:id>")
def article(id):
    article = ARTICLES.get(id)
    if not article:
        return "Статья не найдена", 404
    return render_template("article.html", article=article, id=id)

@app.route("/share")
def share():
    url = request.args.get("url", "")
    try:
        # Для внутренних URL используем имя сервиса
        if "localhost" in url or "127.0.0.1" in url:
            url = url.replace("localhost", "blog").replace("127.0.0.1", "blog")
        
        response = requests.get(url, timeout=3)
        
        # Извлекаем чистый текст из HTML (для статей)
        if "article" in url:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            text = ' '.join(soup.stripped_strings)
            return render_template("share.html", preview=text[:500])  # Первые 500 символов
        
        return render_template("share.html", preview=response.text[:500])
    
    except Exception as e:
        return render_template("share.html", preview=f"Ошибка: {str(e)}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
