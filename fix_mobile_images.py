import os

dir_path = r'c:\Users\Kishore R\Downloads\resort'

replacements = [
    # index.html & others aspect ratios
    ('aspect-[4/5]', 'aspect-square md:aspect-[4/5]'),
    ('aspect-[16/9]', 'aspect-[4/3] md:aspect-[16/9]'),
    ('aspect-[9/16] md:aspect-auto', 'aspect-square md:aspect-auto'),
    ('aspect-[21/9]', 'aspect-square md:aspect-[21/9]'),
    
    # Experiences.html fixed heights
    ('h-[600px]', 'h-[400px] md:h-[600px]'),
    ('h-[300px]', 'h-[200px] md:h-[300px]'),
    ('gap-8 h-[800px]', 'gap-8 auto-rows-[350px] md:auto-rows-auto md:h-[800px]'),
    
    # Wellness.html & Gastronomy fixed heights and grid items
    ('gap-8 h-[1000px]', 'gap-8 auto-rows-[350px] md:auto-rows-auto md:h-[1000px]'),
    ('col-span-8 relative', 'col-span-12 md:col-span-8 relative'),
    ('col-span-4 flex flex-col', 'col-span-12 md:col-span-4 flex flex-col'),
]

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for old, new in replacements:
            content = content.replace(old, new)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Image responsiveness script executed successfully.")
