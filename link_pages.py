import os
import re

dir_path = r'c:\Users\Kishore R\Downloads\resort'

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = re.sub(r'(<a[^>]*href=")[^"]*("[^>]*>\s*residences\s*</a>)', r'\g<1>index.html\g<2>', content, flags=re.IGNORECASE)
        content = re.sub(r'(<a[^>]*href=")[^"]*("[^>]*>\s*experiences\s*</a>)', r'\g<1>Experiences.html\g<2>', content, flags=re.IGNORECASE)
        content = re.sub(r'(<a[^>]*href=")[^"]*("[^>]*>\s*wellness\s*</a>)', r'\g<1>Wellness.html\g<2>', content, flags=re.IGNORECASE)
        content = re.sub(r'(<a[^>]*href=")[^"]*("[^>]*>\s*gastronomy\s*</a>)', r'\g<1>Gastronomy.html\g<2>', content, flags=re.IGNORECASE)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
print('Done linking pages!')
