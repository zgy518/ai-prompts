import markdown
import os

# Read markdown
with open('产品-200个AI提示词合集.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert to HTML
md_html = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

# CSS for Chinese typography
css = """
<style>
  @page { size: A4; margin: 2cm; }
  body {
    font-family: "Microsoft YaHei", "SimHei", sans-serif;
    font-size: 12pt; line-height: 1.8; color: #222;
    max-width: 800px; margin: 0 auto; padding: 20px;
  }
  h1 { font-size: 22pt; color: #1a1a2e; border-bottom: 3px solid #1a1a2e; padding-bottom: 8px; margin-top: 30px; }
  h2 { font-size: 16pt; color: #16213e; border-bottom: 2px solid #00cc66; padding-bottom: 5px; margin-top: 25px; }
  h3 { font-size: 13pt; color: #333; margin-top: 20px; }
  strong { color: #1a1a2e; }
  code {
    background: #f4f4f4; padding: 2px 6px; border-radius: 3px;
    font-size: 10pt; font-family: "Consolas", "Courier New", monospace;
  }
  pre {
    background: #f8f8f8; padding: 12px; border-left: 4px solid #00cc66;
    font-size: 9pt; line-height: 1.5; overflow-x: auto;
    white-space: pre-wrap; word-wrap: break-word;
  }
  blockquote {
    border-left: 4px solid #00cc66; padding: 10px 15px;
    background: #f0fff8; margin: 15px 0;
  }
  table { border-collapse: collapse; width: 100%; margin: 15px 0; }
  th, td { border: 1px solid #ddd; padding: 8px 12px; text-align: left; }
  th { background: #1a1a2e; color: white; }
  hr { border: none; border-top: 1px solid #eee; margin: 25px 0; }
  ul, ol { padding-left: 25px; }
  li { margin: 4px 0; }
</style>
"""

full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
{css}
</head>
<body>
{md_html}
</body>
</html>"""

# Save HTML
html_path = '200个AI提示词-从入门到精通.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"HTML file created: {html_path}")

# Try PDF conversion with weasyprint
try:
    from weasyprint import HTML
    pdf_path = '200个AI提示词-从入门到精通.pdf'
    HTML(filename=html_path).write_pdf(pdf_path)
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"PDF generated: {pdf_path} ({size_kb:.0f} KB)")
except ImportError:
    print("WeasyPrint not available, HTML only")
except Exception as e:
    print(f"PDF failed: {e}")
    print("Using HTML file instead - you can Print to PDF from browser or use online converter")
