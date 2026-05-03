import os
import re

dir_path = r'c:\Users\Kishore R\Downloads\resort'

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
            <a href="index.html" class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide {INDEX_ACTIVE}">residences</a>
            <a href="Experiences.html" class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide {EXPERIENCES_ACTIVE}">experiences</a>
            <a href="Wellness.html" class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide {WELLNESS_ACTIVE}">wellness</a>
            <a href="Gastronomy.html" class="su-nav-link font-headline-md text-emerald-900 hover:text-primary lowercase tracking-wide {GASTRONOMY_ACTIVE}">gastronomy</a>
        </nav>
        <div class="flex items-center gap-4 md:gap-6">
            <a href="#" class="su-btn hidden md:inline-block bg-primary text-on-primary px-8 py-3 font-label-caps uppercase tracking-widest text-sm">
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
<div id="offcanvas" class="fixed top-0 right-0 h-full w-[300px] sm:w-[400px] bg-[#fff9ef] shadow-2xl z-[60] translate-x-full transition-transform duration-500 ease-[cubic-bezier(0.77,0,0.175,1)] overflow-y-auto">
    <div class="p-8 md:p-12 flex flex-col h-full">
        <div class="flex justify-between items-center mb-10">
            <div class="text-2xl font-light tracking-tighter text-emerald-900 font-headline-xl">The Chennai Sanctuary</div>
            <button id="close-offcanvas" class="min-w-[48px] shrink-0 w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-sm hover:rotate-90 transition-transform duration-400 cursor-pointer border-0">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 16 16"><path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/></svg>
            </button>
        </div>
        
        <!-- Navigation Links -->
        <div class="mb-10">
            <ul class="flex flex-col gap-6 list-none p-0 m-0">
                <li><a href="index.html" class="font-headline-md text-2xl text-emerald-900 hover:text-amber-600 transition-colors {INDEX_ACTIVE}">Residences</a></li>
                <li><a href="Experiences.html" class="font-headline-md text-2xl text-emerald-900 hover:text-amber-600 transition-colors {EXPERIENCES_ACTIVE}">Experiences</a></li>
                <li><a href="Wellness.html" class="font-headline-md text-2xl text-emerald-900 hover:text-amber-600 transition-colors {WELLNESS_ACTIVE}">Wellness</a></li>
                <li><a href="Gastronomy.html" class="font-headline-md text-2xl text-emerald-900 hover:text-amber-600 transition-colors {GASTRONOMY_ACTIVE}">Gastronomy</a></li>
            </ul>
        </div>
    </div>
</div>
<!-- Offcanvas Overlay -->
<div id="offcanvas-overlay" class="fixed inset-0 bg-black/40 z-[55] opacity-0 pointer-events-none transition-opacity duration-500"></div>
"""

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        current_nav = nav_template.replace('{INDEX_ACTIVE}', 'active text-amber-600' if filename == 'index.html' else '')
        current_nav = current_nav.replace('{EXPERIENCES_ACTIVE}', 'active text-amber-600' if filename == 'Experiences.html' else '')
        current_nav = current_nav.replace('{WELLNESS_ACTIVE}', 'active text-amber-600' if filename == 'Wellness.html' else '')
        current_nav = current_nav.replace('{GASTRONOMY_ACTIVE}', 'active text-amber-600' if filename == 'Gastronomy.html' else '')

        # Replace existing TopNavBar section
        pattern = r'<!-- TopNavBar -->[\s\S]*?<!-- Offcanvas Overlay -->\n<div id="offcanvas-overlay" class="fixed inset-0 bg-black/40 z-\[55\] opacity-0 pointer-events-none transition-opacity duration-500"></div>'
        
        if re.search(pattern, content):
            content = re.sub(pattern, current_nav, content)
        else:
            # Fallback
            print(f"Pattern not found in {filename}, falling back...")
            fallback_pattern = r'<!-- Top.*?Nav.*?-->\s*<(nav|header)[\s\S]*?</\1>'
            content = re.sub(fallback_pattern, current_nav, content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Nav successfully cleaned up: removed extra content and adjusted mobile width.")
