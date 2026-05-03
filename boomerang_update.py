import os
import re

dir_path = r'c:\Users\Kishore R\Downloads\resort'

new_script = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const videos = document.querySelectorAll('video');
        videos.forEach(video => {
            // Ensure normal looping is disabled
            video.removeAttribute('loop');
            
            // Extract the start time from the src hash (e.g. #t=2)
            let startTime = 0.1;
            if (video.src && video.src.includes('#t=')) {
                const match = video.src.match(/#t=([0-9.]+)/);
                if (match) {
                    startTime = parseFloat(match[1]);
                }
            }
            
            let isReversing = false;
            
            setInterval(() => {
                if (isNaN(video.duration)) return;

                // If playing forward and we reach the end
                if (!isReversing && video.currentTime >= video.duration - 0.1) {
                    isReversing = true;
                    video.pause();
                } 
                // If reversing and we reach the dynamic start time
                else if (isReversing && video.currentTime <= startTime) {
                    isReversing = false;
                    video.play();
                }
                
                // Manually step back to simulate reverse playback cross-browser
                if (isReversing) {
                    video.currentTime -= 0.05;
                }
            }, 50);
        });
    });
</script>
</body>
"""

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace the existing script
        content = re.sub(r'<script>\s*document\.addEventListener\("DOMContentLoaded", function\(\) \{\s*const videos = document\.querySelectorAll[\s\S]*?</script>\s*</body>', new_script, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated boomerang script in all HTML files.")
