import feedparser

ZENN_FEED_URL = "https://zenn.dev/hisao5232/feed"
OUTPUT_HTML = "zenn.html"


def fetch_zenn_articles():
    feed = feedparser.parse(ZENN_FEED_URL)
    return feed.entries


def generate_html(items):
    html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Zenn Articles</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<!-- 共通ヘッダー -->
<header>
    <div class="header-container">
        <div class="logo">go-pro-world.net</div>

        <div class="menu-btn" id="menu-btn">
            &#9776;
        </div>

        <nav class="navbar" id="navbar">
            <ul>
                <li><a href="/index.html">Home</a></li>
                <li><a href="/about.html">About</a></li>
                <li><a href="/zenn.html">Zenn</a></li>
                <li><a href="/github.html">GitHub</a></li>
                <li><a href="/contact.html">Contact</a></li>
            </ul>
        </nav>
    </div>
</header>

<h1 style="text-align:center; margin-top:30px;">📘 Zenn Articles</h1>
<div style="max-width:900px; margin:0 auto; padding:20px;">
"""

    # 記事一覧
    for item in items:
        title = item.title
        url = item.link
        date = item.published[:10]

        html += f"""
<div class="repo">
    <a href="{url}" target="_blank">{title}</a>
    <div class="desc">{date}</div>
</div>
"""

    html += """
</div>

<script src="script.js"></script>
</body>
</html>
"""
    return html


def main():
    print("Zenn 記事を取得中...")
    items = fetch_zenn_articles()
    html = generate_html(items)

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print("zenn.html を生成しました！")


if __name__ == "__main__":
    main()
