import os
import re

dir_path = r'c:\Users\Kishore R\Downloads\resort'

replacements = {
    'Gastronomy.html': [
        (
            '<div class="md:col-span-7 relative">',
            '<div class="md:col-span-7 relative order-last md:order-none">'
        )
    ],
    'Experiences.html': [
        (
            '<div class="grid grid-cols-12 gap-gutter items-center mb-24">',
            '<div class="grid grid-cols-1 md:grid-cols-12 gap-gutter items-center mb-24">'
        ),
        (
            '<div class="w-full md:w-1/2">',
            # Wait, there are two w-full md:w-1/2 in Experiences.html. The first one contains the image, the second contains the text.
            # I should use regex to replace only the first one, or use a more specific target.
        )
    ],
    'Wellness.html': [
        (
            '<section class="px-6 md:px-16 mb-[80px] md:mb-[120px] grid grid-cols-12 gap-gutter items-center">',
            '<section class="px-6 md:px-16 mb-[80px] md:mb-[120px] grid grid-cols-1 md:grid-cols-12 gap-gutter items-center">'
        ),
        (
            '<div class="col-start-2 col-span-5">',
            '<div class="md:col-start-2 md:col-span-5">'
        ),
        (
            '<div class="col-start-8 col-span-4',
            '<div class="md:col-start-8 md:col-span-4'
        )
    ]
}

# Let's do string replacements explicitly to be safe.
def process_experiences(content):
    content = content.replace(
        '<div class="grid grid-cols-12 gap-gutter items-center mb-24">', 
        '<div class="grid grid-cols-1 md:grid-cols-12 gap-gutter items-center mb-24">'
    )
    # The image container in Private Moments section
    target = '<div class="w-full md:w-1/2">\n<div class="aspect-square md:aspect-[4/5]'
    replacement = '<div class="w-full md:w-1/2 order-last md:order-none">\n<div class="aspect-square md:aspect-[4/5]'
    
    # In case the exact indentation is different, we can use regex
    content = re.sub(
        r'<div class="w-full md:w-1/2">\s*<div class="aspect-square md:aspect-\[4/5\]',
        r'<div class="w-full md:w-1/2 order-last md:order-none">\n<div class="aspect-square md:aspect-[4/5]',
        content
    )
    return content

def process_gastronomy(content):
    content = content.replace(
        '<div class="md:col-span-7 relative">',
        '<div class="md:col-span-7 relative order-last md:order-none">'
    )
    return content

def process_wellness(content):
    # Depending on previous script, mb-section-padding might have been replaced with mb-[80px] md:mb-[120px] or similar.
    # Let's just find `grid grid-cols-12 gap-gutter` and replace it
    content = re.sub(
        r'grid grid-cols-12 gap-gutter items-center',
        r'grid grid-cols-1 md:grid-cols-12 gap-gutter items-center',
        content
    )
    content = content.replace(
        '<div class="col-start-2 col-span-5">',
        '<div class="md:col-start-2 md:col-span-5">'
    )
    content = content.replace(
        '<div class="col-start-8 col-span-4',
        '<div class="md:col-start-8 md:col-span-4'
    )
    return content

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if filename == 'Experiences.html':
            content = process_experiences(content)
        elif filename == 'Gastronomy.html':
            content = process_gastronomy(content)
        elif filename == 'Wellness.html':
            content = process_wellness(content)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Mobile layout ordering fixed.")
