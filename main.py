import feedparser
import time
import re

URL="https://v2.velog.io/rss/@myoungjinseo"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = "## 📝 Latest Blog Post\n\n"
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    feed_date = feed['published_parsed']
    formatted_date = time.strftime('%Y/%m/%d', feed_date)
    title = feed['title']
    link = feed['link']
    markdown_text += f"- **{formatted_date}** — [{title}]({link})\n"

updated_readme = re.sub(
    r"(<!-- BLOG-POST-START -->)(.*?)(<!-- BLOG-POST-END -->)",
    f"\\1\n{markdown_text}\n\\3",
    readme_contents,
    flags=re.DOTALL
)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_readme)
f.close()
