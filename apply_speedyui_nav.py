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

<header class="fixed top-0 left-0 w-full z-50 bg-stone-50/90 backdrop-blur-md border-b border-stone-200/20 shadow-sm transition-all duration-500">
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
<div id="offcanvas" class="fixed top-0 right-0 h-full w-full sm:w-[400px] bg-[#fff9ef] shadow-2xl z-[60] translate-x-full transition-transform duration-500 ease-[cubic-bezier(0.77,0,0.175,1)] overflow-y-auto">
    <div class="p-8 md:p-12 flex flex-col h-full">
        <div class="flex justify-between items-center mb-10">
            <div class="text-2xl font-light tracking-tighter text-emerald-900 font-headline-xl">The Chennai Sanctuary</div>
            <button id="close-offcanvas" class="w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-sm hover:rotate-90 transition-transform duration-400 cursor-pointer border-0">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 16 16"><path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/></svg>
            </button>
        </div>
        <div class="lg:hidden mb-10 border-b border-emerald-900/10 pb-6">
            <ul class="flex flex-col gap-4 list-none p-0 m-0">
                <li><a href="index.html" class="font-headline-md text-2xl text-emerald-900 hover:text-amber-600 transition-colors {INDEX_ACTIVE}">Residences</a></li>
                <li><a href="Experiences.html" class="font-headline-md text-2xl text-emerald-900 hover:text-amber-600 transition-colors {EXPERIENCES_ACTIVE}">Experiences</a></li>
                <li><a href="Wellness.html" class="font-headline-md text-2xl text-emerald-900 hover:text-amber-600 transition-colors {WELLNESS_ACTIVE}">Wellness</a></li>
                <li><a href="Gastronomy.html" class="font-headline-md text-2xl text-emerald-900 hover:text-amber-600 transition-colors {GASTRONOMY_ACTIVE}">Gastronomy</a></li>
            </ul>
        </div>
        <div class="mb-10 border-b border-emerald-900/10 pb-10">
            <p class="font-body-md text-lg text-stone-600 leading-relaxed">A sanctuary for the soul in the heart of the tropics. Experience true quiet luxury and ancestral wisdom.</p>
        </div>
        <div class="mb-auto">
            <h2 class="font-headline-md text-2xl mb-6 text-emerald-900">Get In Touch</h2>
            <div class="flex gap-4 mb-6 group cursor-pointer">
                <span class="text-primary mt-1 group-hover:scale-110 transition-transform"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 16 16"><path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414.05 3.555ZM0 4.697v7.104l5.803-3.558L0 4.697ZM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586l-1.239-.757Zm3.436-.586L16 11.801V4.697l-5.803 3.546Z"/></svg></span>
                <div>
                    <span class="block text-sm text-stone-500 mb-1">Email</span>
                    <span class="font-semibold text-emerald-900">sanctuary@chennai.com</span>
                </div>
            </div>
            <div class="flex gap-4 mb-6 group cursor-pointer">
                <span class="text-primary mt-1 group-hover:scale-110 transition-transform"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.885.511a1.745 1.745 0 0 1 2.61.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/></svg></span>
                <div>
                    <span class="block text-sm text-stone-500 mb-1">Phone</span>
                    <span class="font-semibold text-emerald-900">+91 44 1234 5678</span>
                </div>
            </div>
            <div class="flex gap-4 mb-6 group cursor-pointer">
                <span class="text-primary mt-1 group-hover:scale-110 transition-transform"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg></span>
                <div>
                    <span class="block text-sm text-stone-500 mb-1">Location</span>
                    <span class="font-semibold text-emerald-900">East Coast Road, Chennai, India</span>
                </div>
            </div>
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

script_template = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const toggles = document.querySelectorAll('.offcanvas-toggle');
        const closeBtn = document.getElementById('close-offcanvas');
        const offcanvas = document.getElementById('offcanvas');
        const overlay = document.getElementById('offcanvas-overlay');

        if(offcanvas && overlay) {
            function openOffcanvas() {
                offcanvas.classList.remove('translate-x-full');
                overlay.classList.remove('opacity-0', 'pointer-events-none');
            }

            function closeOffcanvas() {
                offcanvas.classList.add('translate-x-full');
                overlay.classList.add('opacity-0', 'pointer-events-none');
            }

            toggles.forEach(toggle => {
                const newToggle = toggle.cloneNode(true);
                toggle.parentNode.replaceChild(newToggle, toggle);
                newToggle.addEventListener('click', openOffcanvas);
            });
            
            closeBtn.addEventListener('click', closeOffcanvas);
            overlay.addEventListener('click', closeOffcanvas);
        }
    });
</script>
"""

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        current_nav = nav_template.replace('{INDEX_ACTIVE}', 'active' if filename == 'index.html' else '')
        current_nav = current_nav.replace('{EXPERIENCES_ACTIVE}', 'active' if filename == 'Experiences.html' else '')
        current_nav = current_nav.replace('{WELLNESS_ACTIVE}', 'active' if filename == 'Wellness.html' else '')
        current_nav = current_nav.replace('{GASTRONOMY_ACTIVE}', 'active' if filename == 'Gastronomy.html' else '')

        # Replace existing TopNavBar section
        pattern = r'<!-- Top.*?Nav.*?-->\s*<(nav|header)[\s\S]*?</\1>'
        content = re.sub(pattern, current_nav, content)

        if 'openOffcanvas' not in content:
            content = content.replace('</body>', script_template + '\n</body>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Navigation bar successfully updated.")
