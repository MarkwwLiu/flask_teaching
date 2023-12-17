# 使用 Flask-WTF 實現文章添加功能

在這個文章中，我們將介紹如何使用 Flask-WTF 擴展來實現一個簡單的文章添加功能。

我們將使用 Flask 框架搭配 FlaskForm 和 WTForms，以及 HTML 模板，建立一個包含文章列表和添加文章的簡單 Web 應用程式。

## 準備工作

首先，確保你已經安裝了 Flask 和 Flask-WTF。

你可以使用以下命令安裝這兩個擴展：

```bash
pip install Flask Flask-WTF
```

接下來，我們將擴展你提供的程式碼，以實現添加文章的功能。

```python
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
```

## 創建 HTML 模板

在 `templates` 目錄下，我們創建三個模板文件，分別是 `home.html`、`article.html` 和 `add_article.html`。

```html
<!-- home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Article List</h1>
    <ul>
        {% for article in articles %}
            <li><a href="{{ url_for('article', index=loop.index-1) }}">{{ article.title }}</a></li>
        {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_article') }}">Add Article</a></p>
</body>
</html>
```

```html
<!-- article.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ article.title }}</title>
</head>
<body>
    <h1>{{ article.title }}</h1>
    <p>{{ article.content }}</p>
    <p><a href="{{ url_for('home') }}">Back to Home</a></p>
</body>
</html>
```

```html
<!-- add_article.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Article</title>
</head>
<body>
    <h1>Add Article</h1>
    <form method="post">
        {{ form.hidden_tag() }}
        <label for="title">Title:</label>
        {{ form.title() }}
        <br>
        <label for="content">Content:</label>
        {{ form.content() }}
        <br>
        {{ form.submit() }}
    </form>
    <p><a href="{{ url_for('home') }}">Back to Home</a></p>
</body>
</html>
```

## 運行應用程式

確保你的目錄結構如下：

```
.
├── main.py
└── templates


    ├── add_article.html
    ├── article.html
    └── home.html
```

然後運行 Flask 應用程式：

```bash
python main.py
```

打開瀏覽器，訪問 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)，你將看到文章列表。

點擊 "Add Article" 連結，進入添加文章的頁面，填寫表單後點擊提交，即可添加新的文章。

添加完成後，返回主頁，你可以看到新增的文章列表。

這是一個簡單的 Flask 應用程式示例，展示了如何使用 Flask-WTF 擴展實現表單功能。

希望這篇文章能幫助你更深入理解 Flask 的應用。

#### 關於我的連結
- GitHub: https://github.com/MarkwwLiu
- Facebook: https://www.facebook.com/TestMrMark
- Linkedin: https://www.linkedin.com/in/%E7%B4%8B%E7%91%8B-%E5%8A%89-03356584/
- CakeResume: https://www.cakeresume.com/me/ak790718

##### link: https://github.com/MarkwwLiu/flask_teaching/blob/main/flask_sample_WFT/flask_sample_WFT.md
