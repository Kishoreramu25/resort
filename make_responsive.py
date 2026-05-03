import os
import re

dir_path = r'c:\Users\Kishore R\Downloads\resort'

replacements = [
    # Padding and margins
    (r'\bpx-16\b', 'px-6 md:px-16'),
    (r'\bpy-20\b', 'py-12 md:py-20'),
    (r'\bpy-\[120px\]\b', 'py-[80px] md:py-[120px]'),
    (r'\bpx-margin-edge\b', 'px-6 md:px-margin-edge'),
    (r'\bmt-\[120px\]\b', 'mt-[80px] md:mt-[120px]'),
    (r'\bpy-6\b', 'py-4 md:py-6'),
    
    # Typography sizing (only replace the text- classes, not font- classes)
    (r'\btext-display-lg\b', 'text-[48px] md:text-[84px] leading-tight md:leading-none'),
    (r'\btext-headline-xl\b', 'text-[40px] md:text-[60px] leading-tight'),
    (r'\btext-headline-lg\b', 'text-[32px] md:text-[48px] leading-tight'),
    (r'\btext-headline-md\b', 'text-[24px] md:text-[32px] leading-snug'),
    (r'\btext-2xl\b', 'text-xl md:text-2xl'),
    
    # Grids
    (r'\bgrid-cols-2\b', 'grid-cols-1 sm:grid-cols-2'),
    (r'\bgrid-cols-4\b', 'grid-cols-1 sm:grid-cols-2 md:grid-cols-4'),
    
    # Gaps
    (r'\bgap-16\b', 'gap-10 md:gap-16'),
    (r'\bgap-12\b', 'gap-8 md:gap-12'),
    
    # Flex directions (be careful, maybe just let flex wrap)
    # Book Now buttons might be too large
    (r'\bpx-8 py-3\b', 'px-5 py-2 md:px-8 md:py-3'),
]

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for old, new in replacements:
            # We use word boundaries except when there are brackets.
            # So let's just do a string replace for some if regex is tricky, but regex is fine.
            content = re.sub(old, new, content)
            
        # Fix the bottom fixed bar for mobile so items stack or wrap nicely
        content = content.replace('flex gap-8 md:gap-12 items-center mb-4 md:mb-0', 'flex gap-4 md:gap-12 items-center mb-4 md:mb-0 w-full justify-between md:justify-start')
        content = content.replace('<button class="bg-tertiary-fixed text-on-tertiary-fixed font-label-caps text-label-caps px-12 py-4 uppercase tracking-[0.2em] hover:bg-white transition-all shadow-lg">', '<button class="bg-tertiary-fixed text-on-tertiary-fixed font-label-caps text-label-caps w-full md:w-auto px-6 md:px-12 py-3 md:py-4 uppercase tracking-[0.2em] hover:bg-white transition-all shadow-lg">')
        
        # In index.html: <div class="flex gap-12"> (Total Privacy / Bespoke Service)
        content = content.replace('<div class="flex gap-8 md:gap-12">', '<div class="flex flex-col sm:flex-row gap-8 md:gap-12">')
        content = content.replace('<div class="flex gap-12">', '<div class="flex flex-col sm:flex-row gap-8 md:gap-12">')

        # Mobile menu hidden class fix on header links:
        # It's already <nav class="hidden md:flex items-center space-x-12">, which hides it on mobile. We leave that.

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Responsiveness updates applied to all HTML files.")
