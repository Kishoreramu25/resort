import os
import shutil
import re

dir_path = r'c:\Users\Kishore R\Downloads\resort'

# 1. Create missing resort pages
resort1_path = os.path.join(dir_path, 'resort1.html')
resort2_path = os.path.join(dir_path, 'resort2.html')
resort3_path = os.path.join(dir_path, 'resort3.html')
index_path = os.path.join(dir_path, 'index.html')

# Copy index.html to resort1.html if it doesn't exist (or overwrite to ensure correct base)
print("Creating resort1.html...")
shutil.copy(index_path, resort1_path)
with open(resort1_path, 'r', encoding='utf-8') as f:
    r1_content = f.read()
r1_content = r1_content.replace('<title>Residences | The Chennai Sanctuary</title>', '<title>Resort 1 | The Chennai Sanctuary</title>')
# Keep the active residences top navbar highlighting clean or update it if needed, but the main update script below will do all nav highlight rewrites.
with open(resort1_path, 'w', encoding='utf-8') as f:
    f.write(r1_content)

# Copy resort2.html to resort3.html if it doesn't exist
print("Creating resort3.html...")
shutil.copy(resort2_path, resort3_path)
with open(resort3_path, 'r', encoding='utf-8') as f:
    r3_content = f.read()
r3_content = r3_content.replace('<title>Resort 2 | The Chennai Sanctuary</title>', '<title>Resort 3 | The Chennai Sanctuary</title>')
r3_content = r3_content.replace('welcome to resort 2.', 'welcome to resort 3.')
r3_content = r3_content.replace('A Visual Journey of Resort 2', 'A Visual Journey of Resort 3')
# replace images of Resort 3 so it has slightly different feel if possible, or just keep same beautiful layout
with open(resort3_path, 'w', encoding='utf-8') as f:
    f.write(r3_content)

# 2. Template Definition for Unified Navigation
nav_template = """<!-- TopNavBar -->
<style>
.su-nav-link {
    position: relative;
    padding-bottom: 4px;
}
.su-nav-link::before {
    content: "";
    position: absolute;
    left: 0;
    bottom: -4px;
    width: 100%;
    border-bottom: 2px solid #023625;
    transform: scaleX(0);
    transition: all 0.5s ease;
    transform-origin: center;
}
.su-nav-link:hover::before, .su-nav-link.active::before {
    transform: scaleX(1);
}
.su-btn {
    transition: all 0.3s ease;
    border-radius: 50rem;
}
.su-btn:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}
.su-icon-wrapper {
    transition: all 0.3s ease;
}
.offcanvas-toggle:hover .su-icon-wrapper {
    color: #023625;
}
</style>

<header class="fixed top-0 left-0 w-full z-50 bg-[#fff9ef]/95 backdrop-blur-md border-b border-[#023625]/10 shadow-sm transition-all duration-500">
    <div class="max-w-[1440px] mx-auto px-6 md:px-16 flex justify-between items-center py-4">
        <a href="index.html" class="text-xl md:text-2xl font-light tracking-tighter text-emerald-900 font-headline-xl text-decoration-none">
            The Chennai Sanctuary
        </a>
        <nav class="hidden lg:flex items-center space-x-10">
            <a href="resort1.html" class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide {RESORT1_ACTIVE_TOP}">resort 1</a>
            <a href="resort2.html" class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide {RESORT2_ACTIVE_TOP}">resort 2</a>
            <a href="resort3.html" class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide {RESORT3_ACTIVE_TOP}">resort 3</a>
            <a href="index.html" class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide {INDEX_ACTIVE_TOP}">residences</a>
            <a href="Experiences.html" class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide {EXPERIENCES_ACTIVE_TOP}">experiences</a>
            <a href="Wellness.html" class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide {WELLNESS_ACTIVE_TOP}">wellness</a>
            <a href="Gastronomy.html" class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide {GASTRONOMY_ACTIVE_TOP}">gastronomy</a>
        </nav>
        <div class="flex items-center gap-4 md:gap-6">
            <a href="#booking-form" class="su-btn hidden md:inline-block bg-primary text-on-primary px-8 py-3 font-label-caps uppercase tracking-widest text-sm text-decoration-none">
                Book Now
            </a>
            <button class="offcanvas-toggle bg-transparent border-0 p-2 cursor-pointer flex items-center justify-center">
                <span class="su-icon-wrapper text-emerald-900">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
                    </svg>
                </span>
            </button>
        </div>
    </div>
</header>

<!-- Offcanvas Sidebar -->
<div id="offcanvas" class="fixed top-0 right-0 h-full w-full sm:w-[400px] bg-[#fff9ef] shadow-2xl z-[60] translate-x-full transition-transform duration-500 ease-[cubic-bezier(0.77,0,0.175,1)] overflow-y-auto">
    <div class="p-8 md:p-12 flex flex-col h-full">
        <div class="flex justify-between items-center mb-10">
            <div class="text-2xl font-light tracking-tighter text-emerald-900 font-headline-xl">The Chennai Sanctuary</div>
            <button id="close-offcanvas" class="w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-sm hover:rotate-90 transition-transform duration-400 cursor-pointer border-0">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 16 16"><path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/></svg>
            </button>
        </div>
        
        <!-- Navigation Links -->
        <div class="mb-10">
            <!-- Primary Destinations -->
            <div class="mb-8">
                <span class="block font-label-caps text-[10px] text-amber-600 font-bold uppercase tracking-widest mb-3">Destinations</span>
                <ul class="flex flex-col gap-5 list-none p-0 m-0">
                    <li><a href="resort1.html" class="{RESORT1_OFFCANVAS_CLASS}">Resort 1</a></li>
                    <li><a href="resort2.html" class="{RESORT2_OFFCANVAS_CLASS}">Resort 2</a></li>
                    <li><a href="resort3.html" class="{RESORT3_OFFCANVAS_CLASS}">Resort 3</a></li>
                </ul>
            </div>
            
            <!-- Divider -->
            <div class="h-px bg-emerald-900/10 my-6"></div>
            
            <!-- Secondary Retreat Lifestyle -->
            <div>
                <span class="block font-label-caps text-[10px] text-emerald-900/50 font-bold uppercase tracking-widest mb-3">Retreat Lifestyle</span>
                <ul class="flex flex-col gap-4 list-none p-0 m-0">
                    <li><a href="index.html" class="{INDEX_OFFCANVAS_CLASS}">Residences</a></li>
                    <li><a href="Experiences.html" class="{EXPERIENCES_OFFCANVAS_CLASS}">Experiences</a></li>
                    <li><a href="Wellness.html" class="{WELLNESS_OFFCANVAS_CLASS}">Wellness</a></li>
                    <li><a href="Gastronomy.html" class="{GASTRONOMY_OFFCANVAS_CLASS}">Gastronomy</a></li>
                </ul>
            </div>
        </div>

        <div class="mb-auto border-b border-emerald-900/10 pb-10">
            <p class="font-body-md text-lg text-stone-600 leading-relaxed">A sanctuary for the soul in the heart of the tropics. Experience true quiet luxury and ancestral wisdom.</p>
        </div>
        
        <div class="mt-8 flex gap-4">
            <a href="#" class="w-12 h-12 rounded-full bg-white flex items-center justify-center text-stone-600 hover:bg-primary hover:text-white transition-colors duration-300 shadow-sm"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" viewBox="0 0 16 16"><path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/></svg></a>
            <a href="#" class="w-12 h-12 rounded-full bg-white flex items-center justify-center text-stone-600 hover:bg-primary hover:text-white transition-colors duration-300 shadow-sm"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" viewBox="0 0 16 16"><path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/></svg></a>
        </div>
    </div>
</div>
<!-- Offcanvas Overlay -->
<div id="offcanvas-overlay" class="fixed inset-0 bg-black/40 z-[55] opacity-0 pointer-events-none transition-opacity duration-500"></div>
"""

# HTML files to process
html_files = [
    'index.html',
    'Experiences.html',
    'Wellness.html',
    'Gastronomy.html',
    'resort1.html',
    'resort2.html',
    'resort3.html'
]

# Style definitions for active vs inactive
PRIMARY_ACTIVE = "font-headline-md text-3xl text-amber-600 font-semibold transition-colors"
PRIMARY_INACTIVE = "font-headline-md text-3xl text-emerald-900 hover:text-amber-600 transition-colors"

SECONDARY_ACTIVE = "font-body-md text-base text-amber-600 font-semibold transition-colors"
SECONDARY_INACTIVE = "font-body-md text-base text-on-surface-variant hover:text-primary transition-colors"

for filename in html_files:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine which file is currently active and set class replacements
    current_nav = nav_template
    
    # Top Navbar replacements
    current_nav = current_nav.replace('{RESORT1_ACTIVE_TOP}', 'active text-amber-600' if filename == 'resort1.html' else '')
    current_nav = current_nav.replace('{RESORT2_ACTIVE_TOP}', 'active text-amber-600' if filename == 'resort2.html' else '')
    current_nav = current_nav.replace('{RESORT3_ACTIVE_TOP}', 'active text-amber-600' if filename == 'resort3.html' else '')
    current_nav = current_nav.replace('{INDEX_ACTIVE_TOP}', 'active text-amber-600' if filename == 'index.html' else '')
    current_nav = current_nav.replace('{EXPERIENCES_ACTIVE_TOP}', 'active text-amber-600' if filename == 'Experiences.html' else '')
    current_nav = current_nav.replace('{WELLNESS_ACTIVE_TOP}', 'active text-amber-600' if filename == 'Wellness.html' else '')
    current_nav = current_nav.replace('{GASTRONOMY_ACTIVE_TOP}', 'active text-amber-600' if filename == 'Gastronomy.html' else '')

    # Offcanvas primary replacements
    current_nav = current_nav.replace('{RESORT1_OFFCANVAS_CLASS}', PRIMARY_ACTIVE if filename == 'resort1.html' else PRIMARY_INACTIVE)
    current_nav = current_nav.replace('{RESORT2_OFFCANVAS_CLASS}', PRIMARY_ACTIVE if filename == 'resort2.html' else PRIMARY_INACTIVE)
    current_nav = current_nav.replace('{RESORT3_OFFCANVAS_CLASS}', PRIMARY_ACTIVE if filename == 'resort3.html' else PRIMARY_INACTIVE)

    # Offcanvas secondary replacements
    current_nav = current_nav.replace('{INDEX_OFFCANVAS_CLASS}', SECONDARY_ACTIVE if filename == 'index.html' else SECONDARY_INACTIVE)
    current_nav = current_nav.replace('{EXPERIENCES_OFFCANVAS_CLASS}', SECONDARY_ACTIVE if filename == 'Experiences.html' else SECONDARY_INACTIVE)
    current_nav = current_nav.replace('{WELLNESS_OFFCANVAS_CLASS}', SECONDARY_ACTIVE if filename == 'Wellness.html' else SECONDARY_INACTIVE)
    current_nav = current_nav.replace('{GASTRONOMY_OFFCANVAS_CLASS}', SECONDARY_ACTIVE if filename == 'Gastronomy.html' else SECONDARY_INACTIVE)

    # Replace existing navigation block using a broad regex pattern
    pattern = r'<!-- TopNavBar -->[\s\S]*?<!-- Offcanvas Overlay -->\n<div id="offcanvas-overlay" class="fixed inset-0 bg-black/40 z-\[55\] opacity-0 pointer-events-none transition-opacity duration-500"></div>'
    
    if re.search(pattern, content):
        content = re.sub(pattern, current_nav, content)
        print(f"Navigation updated successfully in {filename}")
    else:
        # Fallback if pattern mismatches slightly
        print(f"Warning: Standard pattern not matched in {filename}, attempting fallback...")
        fallback_pattern = r'<!-- Top.*?Nav.*?-->\s*<(nav|header)[\s\S]*?</\1>[\s\S]*?<!-- Offcanvas Overlay -->\n<div id="offcanvas-overlay" class="fixed inset-0 bg-black/40 z-\[55\] opacity-0 pointer-events-none transition-opacity duration-500"></div>'
        if re.search(fallback_pattern, content):
            content = re.sub(fallback_pattern, current_nav, content)
            print(f"Navigation updated via fallback in {filename}")
        else:
            print(f"Error: Navigation section NOT found in {filename}!")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("All navigation updates completed successfully.")
