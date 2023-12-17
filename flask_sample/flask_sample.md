# 使用 Flask 創建簡單的文章網站

Flask 是一個輕量級的 Python Web 框架，它可以讓你輕鬆建立 Web 應用程式。

在這個文章中，我們將使用 Flask 創建一個簡單的文章網站，展示如何使用模板引擎渲染網頁，以及如何處理動態路由。

## 準備工作

首先，確保你已經安裝了 Flask。你可以使用以下命令安裝 Flask：

```bash
pip install Flask
```

接著，我們創建一個簡單的文章類型和一個文章列表。每個文章都有標題和內容。

```python
# main.py
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
```

## 創建模板

在 `templates` 目錄下，我們創建兩個模板文件，分別是 `home.html` 和 `article.html`。

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

這兩個模板使用了 Flask 提供的 Jinja2 模板引擎，可以動態生成 HTML 內容。

## 運行應用程式

確保你的目錄結構如下：

```
.
└── flask_sample
    ├── main.py
    └── templates
        ├── article.html
        └── home.html
```

然後運行 Flask 應用程式：

```bash
python main.py
```

打開瀏覽器，訪問 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)，你將看到文章列表。點擊文章標題，可以查看單篇文章的內容。

這是一個簡單的 Flask 應用程式示例，你可以根據這個基礎擴展和改進，以滿足更多功能需求。

希望這篇文章能幫助你入門使用 Flask 構建 Web 應用程式。

### [返回首頁](../README.md)

#### 關於我的連結
- GitHub: https://github.com/MarkwwLiu
- Facebook: https://www.facebook.com/TestMrMark
- Linkedin: https://www.linkedin.com/in/%E7%B4%8B%E7%91%8B-%E5%8A%89-03356584/
- CakeResume: https://www.cakeresume.com/me/ak790718

##### link: https://github.com/MarkwwLiu/flask_teaching/blob/main/flask_sample/flask_sample.md
