import requests

USERNAME = "hisao5232"
OUTPUT_HTML = "github.html"

API_URL = f"https://api.github.com/users/{USERNAME}/repos"


def fetch_repos():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


def generate_html(repos):
    html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GitHub Repositories</title>
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

<h1 style="text-align:center; margin-top:30px;">🐙 GitHub Repositories</h1>
<div style="max-width:900px; margin:0 auto; padding:20px;">
"""

    # ===== リポジトリ一覧 =====
    for repo in repos:
        name = repo.get("name")
        desc = repo.get("description") or "（説明なし）"
        url = repo.get("html_url")

        html += f"""
<div class="repo">
    <a href="{url}" target="_blank">{name}</a>
    <div class="desc">{desc}</div>
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
    print("GitHub リポジトリ一覧を取得中...")
    repos = fetch_repos()
    html = generate_html(repos)

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print("github.html を生成しました！")


if __name__ == "__main__":
    main()
