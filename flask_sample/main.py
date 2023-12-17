from flask import Flask, render_template

app = Flask(__name__)

# 假設有一個簡單的文章類型
class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content

# 創建一個文章列表
articles = [
    Article("Flask 簡介", "Flask 是一個輕量級的 Python Web 框架。"),
    Article("如何使用 Flask", "使用 Flask 可以輕鬆建立 Web 應用程式。"),
]
@app.route('/')
def home():
    return render_template('home.html', articles=articles)

@app.route('/article/<int:index>')
def article(index):
    # 檢查索引是否有效
    if 0 <= index < len(articles):
        return render_template('article.html', article=articles[index])
    else:
        return 'Article not found'

if __name__ == '__main__':
    app.run(debug=True)
