import os
import re

dir_path = r'c:\Users\Kishore R\Downloads\resort'
images = ['img.jpeg', 'img1.jpeg', 'img2.jpeg', 'img3.jpeg', 'img4.jpeg', 'img5.jpeg', 'img6.jpeg']
img_idx = 0

def repl(match):
    global img_idx
    res = f'{match.group(1)}{images[img_idx % len(images)]}{match.group(3)}'
    img_idx += 1
    return res

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = re.sub(r'(<img[^>]*\bsrc=")([^"]+)(")', repl, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Images replaced.")
