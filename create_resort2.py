import os

def create_resort2():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Image replacements
    replacements = {
        'menuu2.jpeg': 'RESORT -2/2146f984-1213-47ce-b3bf-17ae438c6f16.jpg',
        'menuuu.jpeg': 'RESORT -2/4a67a22f-56d2-4d7b-9d90-bd40363da533.jpg',
        'menu3.jpeg': 'RESORT -2/656ca488-5305-4a91-991a-abb8122691aa.jpg',
        'img1.jpeg': 'RESORT -2/788c4c20-d73d-441e-a9cd-0cfe4cc6e141.jpg',
        'img2.jpeg': 'RESORT -2/a9bf0073-8b8a-407f-b0bb-845a29483148.jpg',
        'img3.jpeg': 'RESORT -2/ce847465-c3b7-4f3a-81fd-6cfe150d6ddf.jpg',
        'img4.jpeg': 'RESORT -2/dd8b6cbf-ede9-487d-9c39-145248796e0f.jpg'
    }
    
    for old_img, new_img in replacements.items():
        content = content.replace(f'"{old_img}"', f'"{new_img}"')
        
    # Update title and text
    content = content.replace('<title>Residences | The Chennai Sanctuary</title>', '<title>Resort 2 | The Chennai Sanctuary</title>')
    content = content.replace('redefining the art of private living.', 'welcome to resort 2.')
    
    # Update active class for nav
    # Top nav
    content = content.replace('class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide active text-amber-600">residences', 'class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide ">residences')
    content = content.replace('class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide ">resort 2', 'class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide active text-amber-600">resort 2')
    
    # Offcanvas nav
    content = content.replace('class="font-headline-md text-2xl text-emerald-900 hover:text-amber-600 transition-colors active text-amber-600">Residences', 'class="font-headline-md text-2xl text-emerald-900 hover:text-amber-600 transition-colors ">Residences')
    content = content.replace('class="font-headline-md text-2xl text-emerald-900 hover:text-amber-600 transition-colors ">Resort 2', 'class="font-headline-md text-2xl text-emerald-900 hover:text-amber-600 transition-colors active text-amber-600">Resort 2')

    with open('resort2.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    create_resort2()
