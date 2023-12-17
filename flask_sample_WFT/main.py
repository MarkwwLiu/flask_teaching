# main.py
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test123'  # 需要設定一個秘密金鑰，用於安全性

class ArticleForm(FlaskForm):
    title = StringField('Title')
    content = StringField('Content')
    submit = SubmitField('Submit')

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

@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    form = ArticleForm()

    if form.validate_on_submit():
        new_article = Article(title=form.title.data, content=form.content.data)
        articles.append(new_article)
        return redirect(url_for('home'))

    return render_template('add_article.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
