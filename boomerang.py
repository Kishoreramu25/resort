import os
import re

dir_path = r'c:\Users\Kishore R\Downloads\resort'

boomerang_script = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const videos = document.querySelectorAll('video');
        videos.forEach(video => {
            // Ensure normal looping is disabled
            video.removeAttribute('loop');
            
            let isReversing = false;
            
            setInterval(() => {
                if (isNaN(video.duration)) return;

                // If playing forward and we reach the end
                if (!isReversing && video.currentTime >= video.duration - 0.1) {
                    isReversing = true;
                    video.pause();
                } 
                // If reversing and we reach the beginning (or 1 second mark if set)
                else if (isReversing && video.currentTime <= 0.1) {
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

        # If we haven't already added this script
        if 'isReversing' not in content:
            content = content.replace('</body>', boomerang_script)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Boomerang video effect applied.")
