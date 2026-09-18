"""Inline styles.css and assets/*.jpg (base64) into a single self-contained index.html."""
import base64, re
html = open('index.src.html', encoding='utf8').read()
css = open('styles.css', encoding='utf8').read()
html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>\n' + css + '\n</style>')

def embed(m):
    path = m.group(1)
    data = base64.b64encode(open(path, 'rb').read()).decode()
    return 'src="data:image/jpeg;base64,' + data + '"'

html = re.sub(r'src="(assets/[^"]+\.jpg)"', embed, html)
open('index.html', 'w', encoding='utf8').write(html)
print(len(html) // 1024, 'KB')
